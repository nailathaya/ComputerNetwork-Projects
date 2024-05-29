# Computer-Network
Create A Server/ Socket Programming

Berikut spesifikasi yang harus dipenuhi pada Web Server yang dibuat:
1. Anda akan mengembangkan sebuah server web yang menangani satu request HTTP pada 
satu waktu. Server web harus 
    a. accept dan parse request HTTP, mendapatkan file yang diminta dari sistem file server, 
    b. membuat message response HTTP yang terdiri dari file yang requested yang didahului oleh baris header, dan 
    c. kemudian send response langsung ke klien. Jika file yang diminta tidak ada di server, server harus mengirimkan message HTTP "404 Not Found" kembali ke klien.

2. Saat ini, server web hanya menangani satu request HTTP pada satu waktu. Implementasikan 
sebuah server multithread yang mampu melayani beberapa requests secara simultan. Dengan 
menggunakan threading, pertama-tama buat sebuah thread utama di mana server yang 
dimodifikasi listens klien pada port tertentu. 
Ketika menerima request koneksi TCP dari 
seorang klien, server akan menyiapkan koneksi TCP melalui port lain dan melayani 
permintaan klien dalam sebuah thread terpisah. Akan ada sebuah koneksi TCP terpisah 
dalam sebuah utas terpisah untuk setiap pasangan permintaan/respons.

