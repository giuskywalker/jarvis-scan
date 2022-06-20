import socket
import threading
import queue
from colored import fg, attr

target = input("[URL or IP]: ")
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
                print(f"%s[Port {port} is open] ~ [{ip}:{port} may be vulnerable!] %s" % (fg('green'), attr('reset')))
            except:
                pass
            q.task_done()




for i in range(40):
    t = threading.Thread(target=scan, daemon=True)
    t.start()

q.join()

print("")
print(f"%sOpen ports: {open_ports} %s" % (fg('blue'), attr('reset')))
