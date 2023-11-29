import socket
import time

def main():
    host = "localhost"
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Send a message to the Java server
        message = "precipitacao_total1,1.1"
        client_socket.sendall(message.encode())

        # Shutdown the client socket
        client_socket.shutdown(socket.SHUT_WR)  
        print(f"Sent to Java server: {message}")

        # Receive a response from the Java server
        response = client_socket.recv(1024).decode()
        response = "Received from Java server: " + response

        if response == '':
            response = "Received from Java server: No response"

        return response

if __name__ == "__main__":
    print(main())

    #Lucas