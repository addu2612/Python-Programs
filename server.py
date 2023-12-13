import socket

def send_message():
    host='127.0.0.1'
    port=6000
    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    print("Waiting for connection")
    c, addr=s.accept()
    print("Connection established")
    print("Client Address",addr)
    while True:
        try:
            print()
            data=c.recv(1024)
            d=data.decode('ascii')
            print("Client:",d)
            print()
            x=input("Enter new message:")
            y=x.encode('ascii')
            c.send(y)
        except KeyboardInterrupt:
            print()
            print("Connection terminated!")
            break

send_message()
    