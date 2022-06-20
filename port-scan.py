import socket
import threading
import queue

target = input("Type the ip or the url: ")
print("")
ip = socket.gethostbyname(target)

q = queue.Queue()

open_ports = []

for i in range(1,1001):
    q.put(i)

def scan():
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((ip, port))
                open_ports.append(port)
                print(f"Port {port} is open!")
            except:
                pass
            q.task_done()




for i in range(40):
    t = threading.Thread(target=scan, daemon=True)
    t.start()

q.join()

print("")
print("Open ports: {}".format(open_ports))
