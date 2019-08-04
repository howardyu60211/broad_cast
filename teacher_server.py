import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8088
# 建立一個socket對象
server = socket.socket()
# 綁定host,port
server.bind((HOST, PORT))
# 開始監聽
server.listen(5)
# 等待客戶端連接
conn, addr = server.accept()
# 接受數據
while True:
    data = conn.recv(1024)
    print("student %s in %s has connect..." %(str(conn), str(addr)))
    if not data:
        print('客戶端斷開了')
    print(data)
    conn.send(data.upper())

# 關閉server
server.close()