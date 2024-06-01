import socket
import sys

# Fungsi untuk client mengirim request ke server
def http_client(server_host, server_port, path):
    # Membuat socket objek baru
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Memulai koneksi dengan server
    client_socket.connect((server_host, server_port))

    # Mengirim HTTP GET Request 
    request = f"GET {path} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"

    #Mengirim request yang di decode ke dalam bytes ke server
    client_socket.sendall(request.encode())

    # Menerima respons dari server (permintaan diterima atau file path tidak ditemukan.)
    response = b""                       # Menginisialisasi variabel response dengan string kosong berupa bytes
    while True:                          # Melakukan looping tidak terbatas
        part = client_socket.recv(1024)  # Menerima respons dari server
        if not part:                     # Memeriksa apakah tidak ada lagi response yang diterima.
            break                        # jika memenuhi, maka loop berhenti
        response += part                 # tambahkan part dalam bentuk bytes tersebut ke variabel response

    # Menutup koneksi dengan server
    client_socket.close()

    # Mengoutputkan response dalam bentuk string
    print(response.decode('utf-8'))

if __name__ == "__main__":
    # Permisalan panjang argumen (termasuk nama script, contoh: "client.py") 
    # tidak sepanjang 4, maka beri pemberitahuan cara penggunaan yang benar.
    if len(sys.argv) != 4: 
        print("Cara Penggunaan: py client.py <server_host> <server_port> <path>")
        # Menghentikan eksekusi dan client dapat mengeksekusi kembali client.py 
        # dengan penggunaan argumen yang benar
        sys.exit(1) 

    server_host = sys.argv[1]          # Inisialisasi argumen 1 = <server host> ke dalam server_host
    server_port = int(sys.argv[2])     # Inisialisasi argumen 2 = <server port> ke dalam server_port
    path = sys.argv[3]                 # Inisialisasi argumen 3 = <path> ke dalam path

    # Memanggil fungsi http client dengan argumen server host, server port, 
    # dan path yang akan di request ke server
    http_client(server_host, server_port, path)

    