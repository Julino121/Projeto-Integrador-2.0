import net from 'net';

export function validationInServer(dadosValidar) {
    const host = "localhost";
    const port = 12345;

    return new Promise((resolve, reject) => {
        const socket = new net.Socket();

        socket.connect(port, host, () => {
            // Converta os dados para o formato esperado pelo servidor Java
            const dadosFormatados = Object.entries(dadosValidar)
                .map(([key, value]) => `${key}:${value}`)
                .join(':');

            // Envie uma mensagem para o servidor Java
            socket.write(dadosFormatados, 'utf-8', () => {
                // Desative a escrita no socket do cliente
                socket.end();
                console.log(`Dados enviados para validação: ${JSON.stringify(dadosValidar)}`);
            });
        });

        // Manipule os dados recebidos do servidor Java
        socket.on('data', (data) => {
            const response = data.toString('utf-8');
            
            // Verifique se uma resposta válida foi recebida
            const resultado = response !== null ? response : "Nenhuma resposta válida recebida do servidor Java.";

            // Resolva a promessa com o resultado
            resolve(resultado);

            // Feche a conexão com o servidor
            socket.end();
        });

        // Lidere os eventos de erro e fechamento da conexão
        socket.on('error', (err) => {
            console.error(`Erro na conexão com o servidor: ${err.message}`);
            reject(err); // Rejeite a promessa em caso de erro
        });

        socket.on('close', () => {
            console.log('Conexão fechada com o servidor');
        });
    });
}
