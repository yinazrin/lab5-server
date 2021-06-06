import socket

s = socket.socket()

host_name = socket.gethostname() 
IPADDRESS = socket.gethostbyname(host_name) 

PORT = 9898
print("Enter the server IP address: ", IPADDRESS)
print("listening to port: ", PORT)
print("\n>Waiting for connection....")

s.bind(('', PORT))

s.listen(10)

while True:
    conn, addr = s.accept()

    msg = "\n\nHi, Client [IP address: "+ addr[0] + "], \nThank you for using our storage service. \nYour files are safe with us.\n-Server\n"    
    conn.send(msg.encode())
    
    filename = conn.recv(1024).decode("utf-8")
    file = open(filename, "wb")
    
    RecvData = conn.recv(99999)
    
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(99999)

    file.close()
    print("\n>The file has been copied successfully \n")

    conn.close()
    print(">Connection close \n")

    break
