import socket
import sqlite3
import hashlib
import threading
import time

def create_user_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def start_server():
    start_server_input = input("Do you want to start the server? (yes/no): ").lower()
    
    if start_server_input == 'yes' or start_server_input == 'y':
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12345
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server is listening on {host}:{port}")

        # Create a thread for handling client connections
        thread = threading.Thread(target=handle_connections, args=(server_socket,))
        thread.start()

        start_time = time.time()

        # Wait for the admin to enter 'exit' to close the server
        while True:
            elapsed_time = int(time.time() - start_time)
            print(f"Server has been running for {elapsed_time} seconds.")
            
            close_input = input("Enter 'exit' to close the server: ").lower()
            if close_input == 'exit':
                server_socket.close()
                break

        # Wait for the handle_connections thread to finish
        thread.join()

        print("Server closed.")
    else:
        print("Server not started.")

def handle_connections(server_socket):
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        # Create a thread for handling each client separately
        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()

def handle_client(conn):
    conn.send("Server: Online".encode())

    start_time = time.time()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        if data.lower() == "login":
            handle_login(conn)
        elif data.lower() == "register":
            handle_registration(conn)
        else:
            conn.send("Invalid command".encode())

    elapsed_time = int(time.time() - start_time)
    print(f"Connection from {conn.getpeername()} closed. Session duration: {elapsed_time} seconds.")

    conn.close()

def handle_login(conn):
    username = conn.recv(1024).decode()
    password = conn.recv(1024).decode()

    response = verify_user(username, password)
    conn.send(response.encode())

def handle_registration(conn):
    username = conn.recv(1024).decode()
    password = conn.recv(1024).decode()

    if not user_exists(username):
        add_user(username, password)
        conn.send("Registration successful".encode())
    else:
        conn.send("Username already exists. Please choose another.".encode())

def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return "Login successful"
    else:
        return "Invalid credentials"

def user_exists(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user = cursor.fetchone()
    conn.close()
    return True if user else False

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute('INSERT INTO users VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    create_user_table()
    start_server()
