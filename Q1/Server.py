import socket
import pickle
import os

def receive_file(server_directory):
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the server address
        server_socket.bind(('localhost', 12345))

        # Listen for incoming connections
        server_socket.listen(1)
        print("Server is listening for incoming connections...")

        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            print(f"Connected to: {client_address}")

            # Receive pickled file data
            pickled_data = client_socket.recv(4096)
            if not pickled_data:
                break

            # Unpickle file data
            file_data = pickle.loads(pickled_data)

            # Extract file name and data
            file_name = file_data['file_name']
            file_content = file_data['data']

            # Construct file path
            file_path = os.path.join(server_directory, file_name)

            # Write received file to disk
            with open(file_path, 'wb') as file:
                file.write(file_content)

            print(f"File '{file_name}' received and saved to {server_directory}")

            # Send acknowledgment back to client
            client_socket.sendall(b"File received by the server!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        server_socket.close()

def main():
    # Specify directory where received file will be saved
    server_directory = input("Enter the directory to save the received file: ")

    # Receive file from client
    receive_file(server_directory)

if __name__ == "__main__":
    main()
