import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8088

connect_to_teacher = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
teacher_host = socket.gethostbyname("Macbook_Liu")
student_host = socket.gethostbyname(socket.gethostname())
connect_to_teacher.connect((teacher_host, 8088))