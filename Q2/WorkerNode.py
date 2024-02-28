import socket
import pickle

def execute_task(client_socket, address):
    try:
        # Receive the pickled task from the client
        pickled_task = client_socket.recv(4096)

        # Unpickle the task
        task = pickle.loads(pickled_task)

        # Extract function and arguments from the task
        function = task['function']
        args = task['args']

        # Execute the function with its arguments
        result = function(*args)

        # Pickle the result
        pickled_result = pickle.dumps(result)

        # Send the pickled result back to the client
        client_socket.sendall(pickled_result)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address
    server_socket.bind(('localhost', 12345))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Worker node is listening for incoming connections...")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        # Execute the task sent by the client
        execute_task(client_socket, client_address)

if __name__ == "__main__":
    main()
