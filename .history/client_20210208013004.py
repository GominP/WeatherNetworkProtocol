# echo_client.py
import socket

host = socket.gethostname()    
port = 60301                 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    province = input("ใส่ชื่อจังหวัด: ")
    s.send(province.encode())
    next = s.recv(1024).decode() 
    if next == 'correct':
        break
    else:
        print('พิมพ์ชื่อไม่ถูก')
while True:
    print('(1) ภูมิอากาศวันนี้')
    print('(2) ข่าวเตือนภัยสภาพอากาศ')
    types = input("กรุณาใส่เลขที่ต้องการ: ")
s.close()
print('Received', repr(data))