import socket

def scan(targets, ports):
    print("\n" + "[aspect] Started port scanning for: " + str(targets) + ":")

    for port in range(1, ports):
        port_scan(targets, port)

def port_scan(IP, port):
    try:
        sock = socket.socket()
        sock.connect((IP, port))

        print("[+] An open port was found: " + str(port))
        sock.close()
    except:
        pass

print("[aspect] Port Scanner")

targets = input("[aspect] Enter the target's IP ")
ports = int(input("[aspect] How many ports you want to scan? (1-65535) "))

scan(targets, ports)
