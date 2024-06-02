import socket

def handle_client(client_socket): 
    # Menerima permintaan dari klien hingga 1024 byte dan mendekodekannya dari bytes ke string UTF-8
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request: {request}")

    # Memisahkan permintaan HTTP ke dalam baris-baris individual
    headers = request.split('\n')
    # Mengambil nama file dari baris pertama permintaan HTTP
    filename = headers[0].split()[1]
    # Menghapus tanda (/) di awal nama file
    filename = filename[1:]

    try:
        # Membuka file dengan nama yang diperoleh dalam mode baca-biner (rb)
        with open(filename, 'rb') as file:
            content = file.read()  # Membaca isi file

        # Membuat respons HTTP dengan status 200 OK
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        # Mengubah respons string menjadi bytes
        response = response.encode('utf-8') + content

    except FileNotFoundError:
        # Membuat respons HTTP dengan status 404 Not Found
        response = 'HTTP/1.1 404 NOT FOUND\n\n404 Not Found'
        # Mengubah respons string menjadi bytes
        response = response.encode('utf-8')

    # Mengirim respons ke klien
    client_socket.send(response)
    # Menutup koneksi ke klien
    client_socket.close()

def main():
    # Membuat objek socket untuk server menggunakan alamat AF_INET dan tipe socket SOCK_STREAM untuk koneksi TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Mengikat server ke alamat 127.0.0.1 (localhost) pada port 8080
    serverport = 8080
    server.bind(('127.0.0.1', serverport))
    # Mendengarkan koneksi masuk, (antrian koneksi) 5
    server.listen(0)
    # Mencetak pesan bahwa server sedang mendengarkan pada server port
    print(f"Server listening on port {serverport}")

    while True:
        # Menerima koneksi masuk dan mengembalikan socket klien dan alamatnya
        client_socket, addr = server.accept()
        # Mencetak pesan bahwa koneksi dari alamat tertentu telah diterima
        print(f"Accepted connection from {addr}")
        # Menangani permintaan klien
        handle_client(client_socket)
        
# Memeriksa apakah skrip sedang dijalankan sebagai program utama atau diimpor sebagai modul ke dalam skrip lain
if __name__ == "__main__":
    main()
