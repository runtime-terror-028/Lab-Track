import socket
import time

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(client_socket.recv(1024).decode())  # Print server status
    except ConnectionRefusedError:
        print("Server: Offline")
        return

    start_time = time.time()
    print("Connected to the server.")

    while True:
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            client_socket.send("login".encode())
            login(client_socket)
        elif choice == "2":
            client_socket.send("register".encode())
            register(client_socket)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    elapsed_time = int(time.time() - start_time)
    print(f"Connection to the server closed. Session duration: {elapsed_time} seconds.")

    client_socket.close()

def login(client_socket):
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    client_socket.send(username.encode())
    client_socket.send(password.encode())

    response = client_socket.recv(1024).decode()
    print(response)

def register(client_socket):
    username = input("Enter your desired username: ").strip()
    password = input("Enter your password: ").strip()

    client_socket.send(username.encode())
    client_socket.send(password.encode())

    response = client_socket.recv(1024).decode()
    print(response)

if __name__ == "__main__":
    main()
