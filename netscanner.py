# Import modules
import subprocess
import ipaddress

# Input IP address here
net_addr = input("192.168.0.1/24:")

# Create the network
ip_net = ipaddress.ip_network(net_addr)

# Get all hosts
all_hosts = list(ip_net.hosts())

# Configure subprocess to hide the console
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

# For each ip address in the subnet, run the ping command with the subprocess.popen interface
for i in range(len(all_hosts)):
	output = subprocess.Popen(['ping', '-c', '1', '-w', '500', str(all_hosts[i])],
stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

	if "Destination host unreachable" in output.decode('utf-8'):
		print(str(all_hosts[i]), "is Offline")
	elif "Request timed out" in output.decode('utf-8'):
		print(str(all_hosts[i]), "is Offline")
	else:
		print(str(all_hosts[i]), "is Online")
