import socket
import pickle
import threading

def receive_messages():
    try:
        while True:
            # Receive pickled message from server
            pickled_message = client_socket.recv(4096)
            if not pickled_message:
                break

            # Unpickle message
            message = pickle.loads(pickled_message)

            # Display message to user
            print(message)
    except Exception as e:
        print(f"Error receiving messages: {e}")

def send_message():
    try:
        while True:
            # Get user input
            message = input("Enter your message: ")

            # Pickle message
            pickled_message = pickle.dumps(message)

            # Send pickled message to server
            client_socket.sendall(pickled_message)
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    global client_socket

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))

    # Start receiving messages in a separate thread
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    # Start sending messages in the main thread
    send_message()

if __name__ == "__main__":
    main()
