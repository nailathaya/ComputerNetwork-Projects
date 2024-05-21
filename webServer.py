# import modul socket untuk membuat server TCP sederhana 
from socket import *

# import modul threading agar bisa meng-handle banyak client
import threading 
import mimetypes as mt
# membuat fungsi content-type
def getType(file_path):
    # mencari tahu tipe konten dari file yang direquest oleh client
    # menggunakan library mimetypes
    content_type, _ = mt.guess_type(file_path)
    return content_type if content_type else 'application/octet-stream'

# membuat fungsi handle_client
def handle_client(client_connection):
    # menerima request dan mendecode permintaan
    request = client_connection.recv(1024).decode()
    print(request)

    #melakukan split header per baris
    headers = request.split('\n')

    # mendapatkan file yang diminta pada header baris pertama
    file_requested = headers[0].split()[1]

    # jika request yang diminta mengandung '/', maka diganti dengan '/index.html'
    if file_requested == '/':
        file_requested = '/index.html'

    try:
        # membuka file yang diminta oleh client
        with open('./data/'+ file_requested[1:], 'rb') as file:
            content = file.read()

        # mengambil content-type dari request client
        content_type = getType(file_requested)
        print(content_type)
        
        # membuat response header dengan kode 200 OK dan tipe content
        response_header = f'HTTP/1.0 200 OK\nContent-Type: {content_type}\n\n'.encode()
        response_content = content
        client_connection.send(response_header+response_content)
    except FileNotFoundError:

        # jika file tidak ditemukan, buat response dengan kode 404 NOT FOUND
        response_header = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'.encode()
        response_content = b''
        client_connection.send(response_header+response_content)
    client_connection.close()

# membuat fungsi run_server 
def run_server(server_hostname, server_port):
    # membuat socket server
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # mengaitkan antara serverPort dan ServerHostname
    serverSocket.bind((server_hostname, server_port))

    # mendengarkan koneksi dari client
    serverSocket.listen(1)

    # mencetak string sebagai penanda dimulainya koneksi server
    print(f'[*] Listening on {server_hostname}:{server_port}...')
    while True:
        # server menerima koneksi baru dari client
        client_connection, client_address = serverSocket.accept()

        # mencetak string sebagai penanda server menerima koneksi dari client
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
        
         # menghandle banyak request browser dalam 1 waktu
        client_handler = threading.Thread(target=handle_client, args=(client_connection,))
        client_handler.start()

# membuat fungsi main()
def main():

    # inisialisasi 'localhost' sebagai alamat host
    server_hostname = 'localhost'  

    # Inisialisasi 5555 sebagai alamat port
    server_port = 5555 
    
    # memulai server dengan host dan port yang ditentukan
    run_server(server_hostname, server_port)

# Memanggil fungsi main
main()


