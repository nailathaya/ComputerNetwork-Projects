import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request: {request}")

    # Parse HTTP request
    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/index.html'

    # Remove leading slash
    filename = filename[1:]

    try:
        with open(filename, 'rb') as file:
            content = file.read()

        response = b'HTTP/1.1 200 OK\r\n'
        response += b'Content-Type: text/html\r\n'
        response += b'Content-Length: ' + str(len(content)).encode('utf-8') + b'\r\n'
        response += b'\r\n'
        response += content

    except FileNotFoundError:
        response = b'HTTP/1.1 404 Not Found\r\n'
        response += b'Content-Type: text/html\r\n'
        response += b'\r\n'
        response += b'<html><body><h1>404 Not Found</h1></body></html>'

    client_socket.send(response)
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("Server listening on port 8080")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
