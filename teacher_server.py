import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8088
# 建立一個socket對象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 綁定host,port
server.bind((HOST, PORT))
# 開始監聽
server.listen(1)
# 等待客戶端連接
while True:
    conn, addr = server.accept()
    # 接受數據
    data = conn.recv(1024)
    print("student %s in %s has connect..." %(str(conn), str(addr)))
    if not data:
        print('客戶端斷開了')
    print(data)
    # 關閉server
    server.close()