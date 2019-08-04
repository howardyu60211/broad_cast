import socket

connect_to_teacher = socket.socket()
teacher_host = socket.gethostbyname("Macbook_Liu")
student_host = socket.gethostbyname(socket.gethostname())
connect_to_teacher.connect((teacher_host,8088))
connect_to_teacher.send(student_host.encode())