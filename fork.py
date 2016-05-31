import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(10)
pid = os.fork()
if pid:
     conn.close() # !!! без этого не проходит проверку
else: # process child -> while True recv sendall etc. conn.close()

     while True:
          conn, addr = sock.accept()
          while True:
               data = conn.recv(1024)
               if not data: break
               conn.send(data)
          conn.close()
