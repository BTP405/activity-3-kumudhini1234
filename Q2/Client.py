import socket
import pickle

def send_task(worker_host, worker_port, task):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the worker node
        client_socket.connect((worker_host, worker_port))
        print(f"Connected to worker node {worker_host}:{worker_port}")

        # Pickle the task
        pickled_task = pickle.dumps(task)

        # Send the pickled task to the worker node
        client_socket.sendall(pickled_task)

        # Receive the result from the worker node
        result = client_socket.recv(4096)

        # Unpickle the result
        result = pickle.loads(result)

        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

# Define the calculate_sum function outside the main function
def calculate_sum(a, b):
    return a + b

def main():
    # Define worker node host and port
    worker_host = 'localhost'
    worker_port = 12345

    # Define the task 
    task = {'function': calculate_sum, 'args': (5, 10)}

    # Send the task to the worker node
    result = send_task(worker_host, worker_port, task)
    print("Result:", result)

if __name__ == "__main__":
    main()
