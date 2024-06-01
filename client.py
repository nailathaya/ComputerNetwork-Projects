import socket
import sys

def http_client(server_host, server_port, path):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))

    # Send HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"
    client_socket.sendall(request.encode())

    # Receive response from the server
    response = b""
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part

    # Close the connection
    client_socket.close()

    # Print the response
    print(response.decode('utf-8'))

if _name_ == "_main_":
    if len(sys.argv) != 4:
        print("Usage: python http_client.py <server_host> <server_port> <path>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    path = sys.argv[3]

    http_client(server_host, server_port, path)