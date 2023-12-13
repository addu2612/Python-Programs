import socket

def send_message():
    host='127.0.0.1'
    port=6000
    s=socket.socket()
    s.connect((host,port))
    print("Connection Established!")
    while True:
        try:
            print()
            x=input("Enter new message")
            y=x.encode('ascii')
            s.send(y)
            print()
            data=s.recv(1024)
            d=data.decode('ascii')
            print('Server:',d)
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            s.send("Connection from client terminated".encode('ascii'))
            break

send_message()  
