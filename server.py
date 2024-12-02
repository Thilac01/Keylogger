import socket

def receive_data():
    server_ip = '0.0.0.0'  # Listen on all available interfaces (this works for local network)
    server_port = 12345     # Same port as the client

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))  # Bind to all interfaces
    server_socket.listen(1)

    print(f"Server listening on {server_ip}:{server_port}...")
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
        
    client_socket.close()
    server_socket.close()

if _name_ == "_main_":
    receive_data()