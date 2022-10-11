import os
os.system("tput setaf 11")

print("""
#########################################
#                                       #
#                                       #
#               ANSIBLE                 #
#                                       #
#########################################

_________________________________________
_________________________________________
""")

while True:
	print("""
	1.Configuration file             
	2.Inventory file          
	3.Configure Local system                 
	4.Configure Remote system                 
	5.Main Menu          
	""")
	ch =int(input("Enter your choice: "))
	if ch == 1:
		os.system("vi ansible.cfg")

	elif ch == 2:
		os.system("vi /etc/ansible/hosts")

	elif ch == 3:
		while True:
			print("""
			1.Docker Env             
			2.ML Env         
			3.AWS Env                 
			4.Main Menu          
			""")
			choice = int(input("Enter your choice: "))
			if choice == 1:
				os.system("ansible-playbook docker.yml")

			elif choice == 2:
				os.system("ansible-playbook ml.yml")
			elif choice == 3:
				os.system("ansible-playbook aws.yml")
			else:
				print("Heading towards main menu")
				break

			input("press enter to continue..............")
			os.system("clear")
	elif ch == 4:
		while True:
			print("""
			1.Docker Env             
			2.ML Env         
			3.AWS Env                 
			4.Main Menu          
			""")
			choice = int(input("Enter your choice: "))
			if choice == 1:
				os.system("ansible-playbook docke.yml")

			elif choice == 2:
				os.system("ansible-playbook mll.yml")
			elif choice == 3:
				os.system("ansible-playbook awss.yml")
			else:
				print("Heading towards main menu")
				break

			input("press enter to continue..............")
			os.system("clear")
	else:
		print("Heading towards main menu")
		break

	input("press enter to continue..............")
	os.system("clear")
		









