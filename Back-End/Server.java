import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

    public static void main(String[] args) {
        int portNumber = 12345;

        try (ServerSocket serverSocket = new ServerSocket(portNumber)) {
            System.out.println("Java Socket Server is listening on port " + portNumber);

            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                     PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                    // Get message from Python client
                    String message = in.readLine();

                    // Parse JSON using Gson
                    Gson gson = new Gson();
                    FormData formData = gson.fromJson(message, FormData.class);

                    // Processar os dados conforme necessário (por exemplo, salvar no banco de dados)
                    // Aqui, estamos apenas imprimindo os dados recebidos
                    System.out.println("Dados do formulário recebidos:");
                    System.out.println("Personal Info: " + formData.getPersonalInfo());
                    System.out.println("Address: " + formData.getAddress());
                    System.out.println("Appointment: " + formData.getAppointment());

                    // Send a response back to the Python client
                    String response = "Java received your message PYTHON";
                    out.println(response);
                    System.out.println("Sent response to Python client");

                } catch (IOException e) {
                    System.err.println("Error handling client connection: " + e.getMessage());
                }
            }

        } catch (IOException e) {
            System.err.println("Could not listen on port " + portNumber);
            System.exit(-1);
        }
    }
}
