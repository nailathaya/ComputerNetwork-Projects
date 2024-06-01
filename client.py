import socket
import sys

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
    response = b""                           # Menginisialisasi variabel response dengan string kosong berupa bytes
    while True:                              # Melakukan looping
        part = client_socket.recv(2048)      # Menerima respons dari server
        if not part:                         # Jika respons yang diterima bukan respons
            break                            # bukan respons dari server, maka loop berhenti
        response += part                     # tambahkan part dalam bentuk bytes tersebut ke variabel response

    # Menutup koneksi dengan server
    client_socket.close()

    # Mengoutputkan response dalam bentuk string
    print(response.decode('utf-8'))

if __name__ == "__main__":
    # Permisalan panjang argumen (termasuk nama script, contoh: "client.py") 
    # tidak sepanjang 4, maka beri pemberitahuan cara penggunaan yang benar.
    if len(sys.argv) != 4: 
        print("Usage: py client.py <server_host> <server_port> <path>")
        sys.exit(1)

    server_host = sys.argv[1]          # Inisialisasi argumen 1 = <server host> ke dalam server_host
    server_port = int(sys.argv[2])     # Inisialisasi argumen 2 = <server port> ke dalam server_port
    path = sys.argv[3]                 # Inisialisasi argumen 3 = <path> ke dalam path

    # Memanggil fungsi http client dengan argumen server host, server port, dan path yang akan di request ke server
    http_client(server_host, server_port, path)