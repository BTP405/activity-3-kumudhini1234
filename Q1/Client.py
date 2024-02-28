import socket
import pickle
import os

def send_file(server_host, server_port, file_path):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_host, server_port))
        print(f"Connected to server {server_host}:{server_port}")

        # Read file contents
        with open(file_path, 'rb') as file:
            data = file.read()

        # Create file dictionary to pickle
        file_data = {'file_name': os.path.basename(file_path), 'data': data}

        # Pickle and send file
        pickled_data = pickle.dumps(file_data)
        client_socket.sendall(pickled_data)

        print(f"File '{file_path}' sent to server")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

def main():
    # Define server host and port
    server_host = 'localhost'
    server_port = 12345

    # Prompt user for file path
    file_path = input("Enter the file path to send: ")

    # Send file to server
    send_file(server_host, server_port, file_path)

if __name__ == "__main__":
    main()
