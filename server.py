import socket

soc=socket.socket()
host="localhost"
port=5000
soc.bind((host,port))
soc.listen(5)
while True:
    conn,addr=soc.accept()
    print ("Got connection from",addr)
    msg=conn.recv(1024)
    print(str(msg))
    if(msg=="Hello Server"):
        print("hii everyone")
    else:
        print("Go away")