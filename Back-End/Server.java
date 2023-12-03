import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        try (ServerSocket servidor = new ServerSocket(12345)) {
            System.out.println("Servidor iniciado. Aguardando conexões...");

            while (true) {
                try{
                    Socket cliente = servidor.accept();
                    System.out.println("Cliente conectado: " + cliente);

                    BufferedReader receptor = new BufferedReader(new InputStreamReader(cliente.getInputStream()));
                    PrintWriter transmissor = new PrintWriter(cliente.getOutputStream(), true);

                    System.out.println("Atribuindo nova Thread para esse cliente");
                    Thread t = new Validacao(cliente, receptor, transmissor);
                    t.start();
                }
                catch (Exception erro) {
                    System.err.println(erro.getMessage());
                }   

            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}
