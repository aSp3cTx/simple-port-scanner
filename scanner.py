import socket
import pyfiglet

def scan(targets):
    print("\n" + "[aspect] Started port scanning for " + str(targets) + ":")

    for port in range(1, 65535):
        port_scan(targets, port)

def port_scan(IP, port):
    try:
        sock = socket.socket()
        sock.connect((IP, port))

        print("[+] An open port was found: " + str(port))
        sock.close()
    except:
        pass

art = pyfiglet.figlet_format("Port Scanner")
print(art)

targets = input("[aspect] Enter the target's IP: ")
scan(targets)
