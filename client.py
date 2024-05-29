import socket

def request_server(file_path):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))

    request = f"GET {file_path} HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client.send(request.encode('utf-8'))

    response = client.recv(4096)
    print(response.decode('utf-8'))
    client.close()

if __name__ == "__main__":
    request_server('/index.html')  # Replace with the desired file path
