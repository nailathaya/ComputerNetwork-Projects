# import socket module
from socket import * 
import sys # In order to terminate the program 

# Create a TCP/IP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 8080
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(5)

print('Ready to serve...') # Pesan ini hanya dicetak sekali di awal

while True: 
    # Establish the connection 
    connectionSocket, addr = serverSocket.accept() 
    
    try: 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        
        # Check if file exists
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
            
        # Send HTTP header line into socket 
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()
            
    except IOError:
        # Send response message for file not found 
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\nFile not found'.encode())
        connectionSocket.close() 
            
serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
