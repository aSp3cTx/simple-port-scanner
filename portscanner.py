
import socket
import termcolor


def scan(target, ports):
	print(termcolor.colored(('\n' + ' Starting Scan For ' + str(target)) + ':' , 'red'))
	for port in range(1,ports):
		scan_port(target,port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(termcolor.colored(("[+] Port Opened Found, Port Num: " + str(port)), 'green'))
		sock.close()
	except:
		pass

print(termcolor.colored(("[Port Scanner By aspect]"), 'red'))
targets  = input("[*] Enter Targets To Scan: (split them by ,): ")
ports = int(input("[*] How Many Ports You Want To Scan? (1-65535) "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'red'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '),ports)
else:
	scan(targets, ports)


