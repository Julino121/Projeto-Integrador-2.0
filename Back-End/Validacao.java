import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.logging.*;

public class Validacao extends Thread {
    private Socket s;
    private BufferedReader receptor;
    private PrintWriter transmissor;
    private static final Logger logger = Logger.getLogger(Validacao.class.getName());

    public Validacao(Socket s, BufferedReader receptor, PrintWriter transmissor) {
        this.s = s;
        this.receptor = receptor;
        this.transmissor = transmissor;
    }

    @Override
    public void run() {
        try {
            String dados;

            System.out.println("Cliente utilizando o servidor: ");
            dados = receptor.readLine();
            logger.info("Recebidos dados a serem validados: " + dados);

            String[] parts = dados.split(":");
            boolean isValid = true;
            System.out.println("Starting validation");

            for (int i = 0; i < parts.length; i += 2) {
                String field = parts[i].trim();
                String value = parts[i + 1].trim();

                switch (field.toLowerCase()) {
                    case "name":
                        if (!isValidName(value)) {
                            isValid = false;
                            System.out.println("Validating " + field + ": " + value);
                            System.out.println("Validation result: " + isValid);
                        }
                        break;
                    case "cpf":
                        if (!isValidCPF(value)) {
                            isValid = false;
                            System.out.println("Validating " + field + ": " + value);
                            System.out.println("Validation result: " + isValid);
                        }
                        break;
                    case "email":
                        if (!isValidEmail(value)) {
                            isValid = false;
                            System.out.println("Validating " + field + ": " + value);
                            System.out.println("Validation result: " + isValid);
                        }
                        break;
                    default:
                        // Handle unknown field or other custom logic
                }
            }

            if (isValid) {
                System.out.println("Dados validados");
                String validado = "VALIDADO";
                transmissor.println(validado);
            } else {
                System.out.println("Dados Invalidos");
                String invalido = "INVALIDO";
                transmissor.println(invalido);
            }

        } catch (IOException e) {
            System.err.println(e.getMessage());
        } finally {
            try {
                s.close();
                transmissor.close();
                receptor.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static boolean isValidName(String name) {
        return name.matches("^[a-zA-Z]+( [a-zA-Z]+)*$");
    }

    private static boolean isValidCPF(String cpf) {
        String cleanedCPF = cpf.replaceAll("[^0-9]", "");

        // Check if CPF has 11 digits
        if (cleanedCPF.length() != 11) {
            return false;
        }

        // Calculate the first verification digit
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            sum += (cleanedCPF.charAt(i) - '0') * (10 - i);
        }
        int firstVerificationDigit = 11 - (sum % 11);
        if (firstVerificationDigit > 9) {
            firstVerificationDigit = 0;
        }

        // Calculate the second verification digit
        sum = 0;
        for (int i = 0; i < 10; i++) {
            sum += (cleanedCPF.charAt(i) - '0') * (11 - i);
        }
        int secondVerificationDigit = 11 - (sum % 11);
        if (secondVerificationDigit > 9) {
            secondVerificationDigit = 0;
        }

        // Check if verification digits match
        return (cleanedCPF.charAt(9) - '0') == firstVerificationDigit &&
               (cleanedCPF.charAt(10) - '0') == secondVerificationDigit;
    }

    private static boolean isValidEmail(String email) {
        return email.matches("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}");
    }
}