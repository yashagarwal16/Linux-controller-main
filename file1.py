import os
import subprocess
# import file11

# def date_command():
# 	return os.system("cd")
    # os.system("date")

def date_c():
	proc = subprocess.Popen(["date"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print("program output:", out)
	return out

# import subprocess

# proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
# (out, err) = proc.communicate()
# print("program output:", out)




# import subprocess
# getVersion =  subprocess.Popen("awk '{print $7}' /etc/redhat-release", shell=True, stdout=subprocess.PIPE).stdout
# version =  getVersion.read()

# print("My version is", version.decode())

def cal_command():
    # os.system("cal")
	proc = subprocess.Popen(["cal"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print("program output:", out)
	return out

def ssh_command(ip_address,command):
    ip = ip_address
    os.system(f"ssh -l root {ip} {command} && exit")

def config_httpd():
    # os.system("yum install httpd -y && systemctl start httpd --now")
	proc = subprocess.Popen(["yum install httpd -y && systemctl start httpd --now"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print("program output:", out)
	return out





def opt(y):
	while True:
		x = int(y)
		if x==1:
			print("You have choosed 1 option")
			cmd_output = date_c()
		elif x==2:
			print("You have choosed 2 option")
			cmd_output = cal_command()
		elif x==3:
			print("You have choosed 3 option")
			ip_address = input("Please enter the IP address of the computer you want to connect: ")
			command = input("Please enter the command which you want to run on the other machine: ")
			# [ip_address,command] = file11.ssh_func()
			cmd_output = ssh_command(ip_address,command)
		elif x==4:
			print("You have choosed to configure the HTTPD server, so you can connect to the IP address 172.16.89.160:80")
			cmd_output = config_httpd()
			os.system("exit()")
		elif x==5:
			print("You have choosed 5 option")
			cmd_output = os.system("clear")
		# print("After this we have return the variable")
		return cmd_output
	



