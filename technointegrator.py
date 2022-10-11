import os
#os.system("espeak-ng -s 80 'hello everyone weee aare glad that your here!'")
#os.system("zenity --entry --text='we understand your needs, Tell us if u have any query' --title='MAIN MENU'")
os.system("tput setaf 3")
print("\t\t\twelcome to the menu")
print("\t\tplease follow the below options to proceed")
os.system("tput setaf 7")
print("\t\t\t-------------------")
print()
print()

while True:
	os.system("tput setaf 14")
	print("""

##############   #######################   #################  ############
#            #   #                     #   #               #  #          #
#   1.Linux  #   #  2.Computer Vision  #   #  5.AWS Cloud  #  #   7.K8s  #
#            #   #                     #   #               #  #          #
##############   #######################   #################  ############


##############   ########################  ###############    ############
#            #   #                      #  #             #    #          #
#  3.DOCKER  #   #  4.Machine Learning  #  #  6.Ansible  #    #  8.EXIT  #
#            #   #                      #  #             #    #          #
##############   ########################  ###############    ############
	""")
	ch = int(input("Enter your choice : "))
	if ch == 1:
		import os
		os.system("tput setaf 2")
		print("""
#########################################
#                                       #
#                                       #
#            Linux Commands             #
#                                       #
#########################################

_________________________________________
_________________________________________
		""")
		while True:
			os.system("tput setaf 2")
			print("""
 1. Date                             21. Do remote login
 2. Calendar                         22. Transfer file remotely
 3. Files/folders in current folder  23. Login details
 4. run any program/cmd              24. To find software for any cmd/program
 5. IP address                       25. Create a unit file for a program
 6. Install Anyprogram/cmd           26. Path of executable file
 7. Uninstall Anyprogram/cmd         27. Check system-calls of any file
 8. Processes running in background  28. Public IP of the system
 9. CLI mode                         29. Public IP of a website
10. Start services of a program      30. Port numbers
11. Status of a program              31. cpu details
12. Manual of program/cmd            32. Number of processor's
13. Last 10 lines of a file          33. Change cpu Affinity
14. Process running                  34. Hardware details
15. Process id of any program        35. Check which program running on which cpu
16. Make any file executable         36. Login to different user
17. Make any file un-executable      37. Display name of the current user
18. Add new user                     38. Check if anyone tries to login your system
19. Delete a user                    39. zenity
20. Session details                  40. Main menu
			""")
			os.system("tput setaf 7")
			print("Please Enter Your Choice:  " , end='')
			x=int(input())
			if x == 1:
				os.system("date")
			
			elif x == 2:
				os.system("cal")

			elif x == 3:
				os.system("ls")

			elif x == 4:
				cmd = input("Enter cmd/program name: ")
				os.system("{}".format(cmd))

			elif x == 5:
				os.system('ifconfig enp0s3')

			elif x == 6:
				cmd = input("Enter software name: ")
				os.system("dnf install {}".format(cmd))

			elif x == 7:
				cmd = input("Enter program/cmd name: ")
				os.system("dnf remove {}".format(cmd))

			elif x == 8:
				os.system("jobs")

			elif x == 9:
				os.system("chvt 3")

			elif x == 10:
				cmd = input("Enter the program name: ")
				os.system("systemctl start {}".format(cmd))

			elif x == 11:
				cmd = input("Enter the program name: ")
				os.system("systemctl status {}".format(cmd))

			elif x == 12:
				cmd = input("Enter program/cmd name: ")
				os.system("man {}".format(cmd))

			elif x == 13:
				cmd = input("Enter file name: ")
				os.system("tail {}".format(cmd))
			
			elif x == 14:
				os.system("ps -aux | less")
			
			elif x == 15:
				cmd = input("Enter program name: ")
				os.system("pidof {}".format(cmd))
			
			elif x == 16:
				cmd = input("Enter file name: ")
				os.system("chmod +x {}".format(cmd))
			
			elif x == 17:
				cmd = input("Enter file name: ")
				os.system("chmod -x {}".format(cmd))
			
			elif x == 18:
				name = input("User name: ")  
				os.system("useradd {}".format(name))
				os.system("passwd {}".format(name))
			
			elif x == 19:
				name = input("User name: ")  
				os.system("userdel {}".format(name))

			elif x == 20:
				os.system("loginctl")

			elif x == 21:
				user = input("Enter username of remote-host: ")
				ip = input("Enter IP address of remote-host: ")
				os.system("ssh {}@{}".format(user,ip))
			
			elif x == 22:
				f_name = input("Enter file-name: ")
				user = input("Enter username of remote-host: ")
				ip = input("Enter IP address of remote-host: ")
				dest_path = input("Destination path: ")
				os.system("scp {} {}@{}:{}".format(f_name,user,ip,dest_path))

			elif x == 23:
				os.system("w")

			elif x == 24:
				cmd = input("Enter the cmd/program: ")
				os.system("dnf whatprovides {}".format(cmd))

			elif x == 25:
				cmd = input("Enter program/cmd name: ")
				os.system("systemd-run {}".format(cmd))		

			elif x == 26:
				cmd = input("Enter program/cmd name: ")
				os.system("which {}".format(cmd))

			elif x == 27:
				cmd = input("Enter program/cmd name: ")
				os.system("strace -c {}".format(cmd))

			elif x == 28:
				os.system("curl ifconfig.me")

			elif x == 29:
				url = input("Enter the url: ")
				os.system("nslookup {}".format(url))

			elif x == 30:
				os.system("netstat -tnlp")
			
			elif x == 31:
				os.system("lscpu")
			
			elif x == 32:
				os.system("nproc")

			elif x == 33:
				print("""
1.cpu0
2.cpu1
				""")
				choice = int(input("Enter your choice: "))
				if choice == 1:
					print("""
1. online : on the cpu
2. offline : off the cpu
					""")
					switch = int(input("Enter your choice: "))
					if switch == 1:
						os.system("echo 1 > /sys/devices/system/cpu/cpu0/online")
					elif switch == 2:
						os.system("echo 0 > /sys/devices/system/cpu/cpu0/online")
				elif choice == 2:
					print("""
1. online : on the cpu
2. offline : off the cpu
					""")
					switch = int(input("Enter your choice: "))
					if switch == 1:
						os.system("echo 1 > /sys/devices/system/cpu/cpu1/online")
					elif switch == 2:
						os.system("echo 0 > /sys/devices/system/cpu/cpu1/online")

			elif x == 34:
				os.system("lshw")

			elif x == 35:
				cmd = input("Enter the cmd/program: ")
				os.system("tuna -t {} -P".format(cmd))	

			elif x == 36:
				user = input("User name: ") 
				os.system("su {}".format(user))

			elif x == 37:
				os.system("whoami")

			elif x == 38:
				os.system("lastb")

			elif x == 39:
				while True:
					print("""
 1: to run date
 2: to run cal
 3: to run ls
 4: to run firefox
 5: to run fortune cmd
 6: to type something in dialog box
 7: to fill a form
 8: to run jobs command
 9: to select files to get their location
10: to stop the system for 10seconds
11: Main menu
press anyother number to exit
					""")
					print("Please Enter Your Choice:  " , end='')
					x=int(input())
					if x == 1:
						os.system('zenity --info --text="$(date)"')
					elif x == 2:
						os.system("zenity --calendar")
					elif x == 3:
						os.system('zenity --info --text="$(ls)"')
					elif x == 4:
						os.system('zenity --info --text="$(firefox)"')
					elif x == 5:
						os.system('zenity --info | fortune')
					elif x == 6:
						os.system('zenity --entry --text="type anything u want" --title="your type box"')
					elif x == 7:
						os.system('zenity --forms --add-entry="name"  --add-entry="gender" --add-entry="school name" --add-entry="college name" --add-entry="GF name" --add-entry="your crush name" --add-entry="best memmories at school" --add-entry="whats your lesson from life" --add-entry="best day of college" --add-entry="how many kids your planning for"  --text="enter your details" --title="DONT WORRY YOUR DATA IS NOT STORING ANYWHERE"')
					elif x == 8:
						os.system('zenity --info --text="$(jobs)"')
					elif x == 9:
						os.system("zenity  --file-selection --multiple")
					elif x == 10:
						os.system('zenity --info --text="$(sleep 10)"')

					elif x == 11:
						print("Heading towards main menu...")
						break

					else:
						print("Heading towards main menu...")
						break
					input("press enter to continue..............")
					os.system("clear")	


			elif x == 40:
				print("Heading towards main menu")
				break
			
			else:
				print("Heading towards main menu")
				break

			input("press enter to continue..............")
			os.system("clear")

	elif ch == 2:
		import cv2
		import os
		cap=cv2.VideoCapture(0)
		ret,photo = cap.read()
		model = cv2.CascadeClassifier("/root/Downloads/haarcascade_frontalface_alt.xml")
		os.system("tput setaf 3")

		print("""
#########################################
#                                       #
#                                       #
#            Computer Vision            #
#                                       #
#########################################

_________________________________________
_________________________________________
		""")

		while True:
			os.system("tput setaf 3")
			print("""
Enter your choice
1.draw a line using mouse on photo     8.draw a rectangle on face in livevideo
2.draw a circle on photo               9.crop face of two photos and join them
3.draw a rectangle on photo            10.crop face of a photo
4.draw a rectangle on a dynamic image  11.blur the face in livevideo
5.start a live video                   12.Crop on run time
6.show only face in a livevideo        13.To have a side window in the photo
7.show only blur face in a livevideo   14.For main menu
			""")
			os.system("tput setaf 7")
			print('Note: Press "ENTER" to exit from the window')
			ch =int(input("Enter your choice: "))
			if ch == 1:
					def cir(a,b,c,d,e):
						if a==cv2.EVENT_MOUSEMOVE:
							print("hii")
							cv2.circle(photo,(b,c),5,[0,255,0],-1)
					cv2.namedWindow("hii")
					cv2.setMouseCallback("hii",cir)
					while True:
						cv2.imshow("hii",photo)
						if cv2.waitKey(100)==13:
							break
					cv2.destroyAllWindows()
			elif ch == 2:
				os.system("clear")
				os.system("tput setaf 1")
				print("Press left mouse_button to draw a circle")
				os.system("sleep 3")
				os.system("tput setaf 7")
				def cir(a,b,c,d,e):
					if a == cv2.EVENT_LBUTTONDOWN:
						print("hii")
						cv2.circle(photo,(b,c),50,[0,255,0],5)
				cv2.namedWindow("hii")
				cv2.setMouseCallback("hii",cir)
				while True:
					cv2.imshow("hii" , photo)
					if cv2.waitKey(1) == 13:
						break
				cv2.destroyAllWindows()
			elif ch == 3:
				os.system("clear")
				os.system("tput setaf 1")
				print("Press left mouse_button to draw a rectangle")
				os.system("sleep 3")
				os.system("tput setaf 7")
				def reci(a,b,c,d,e):
					if a == cv2.EVENT_LBUTTONDOWN:
						print("hii")
						cv2.rectangle(photo,(b,c),(b+150,c+160),[0,255,0],5)
				cv2.namedWindow("hii")
				cv2.setMouseCallback("hii",reci)
				while True:
					cv2.imshow("hii" , photo)
					if cv2.waitKey(1000) == 13:
						break
				cv2.destroyAllWindows()
			elif ch == 4:
				os.system("clear")
				os.system("tput setaf 1")
				print("Press left mouse_button to draw a rectangle")
				os.system("sleep 3")
				os.system("tput setaf 7")
				cv2.namedWindow("hi")
				def rec(a,b,c,d,e):
					ret , photo = cap.read()
					if a == cv2.EVENT_LBUTTONDOWN:
						print("hi")
						new = cv2.rectangle(photo,(b,c),(b+150,c+160),[0,255,0],5)
						cv2.imshow("hi" ,photo)
						cv2.waitKey()
						cv2.destroyAllWindows()
				cv2.setMouseCallback("hi",rec)
				cv2.imshow("hi" , photo)
				cv2.waitKey()
				cv2.destroyAllWindows()
			elif ch == 5:
				while True:
					ret,photo = cap.read()
					cv2.imshow("hello" , photo)
					if cv2.waitKey(10) == 13:  
							break
				cv2.destroyAllWindows()
			elif ch == 6:
				while True:
					ret,photo = cap.read()
					fdetect = model.detectMultiScale(photo)
					if len(fdetect) == 0:
						print("face not detected")
					else:    
						x1 = fdetect[0][0]
						y1 = fdetect[0][1]
						x2 = fdetect[0][2] + x1
						y2 = fdetect[0][3] + y1
						b = photo[y1:y2,x1:x2]
						cv2.imshow("hi", b)
						if cv2.waitKey(100) == 13:
							break
					cv2.destroyAllWindows()
			elif ch == 7:
				while True:
					ret,photo = cap.read()
					fdetect = model.detectMultiScale(photo)
					if len(fdetect) == 0:
						print("face not detected")
					else:    
						x1 = fdetect[0][0]
						y1 = fdetect[0][1]
						x2 = fdetect[0][2] + x1
						y2 = fdetect[0][3] + y1
						b = photo[y1:y2,x1:x2]
						blur = cv2.blur(b,(15,15))
						cv2.imshow("hi", blur)
						if cv2.waitKey(100) == 13:
							break
					cv2.destroyAllWindows()
			elif ch == 8:
				while True:
					ret,photo = cap.read()
					fdetect = model.detectMultiScale(photo)
					if len(fdetect) == 0:
						print("face not detected")
					else:    
						x1 = fdetect[0][0]
						y1 = fdetect[0][1]
						x2 = fdetect[0][2] + x1
						y2 = fdetect[0][3] + y1
						rec = cv2.rectangle(photo,(x1,y1),(x2,y2),0,5)
						cv2.imshow("hi", rec)
						if cv2.waitKey(100) == 13:
							break
					cv2.destroyAllWindows()
			elif ch == 9:
				i = input("Enter the location of 1st photo: ")
				j = input("Enter the location of 2nd photo: ")
				photo1 = cv2.imread(i)
				fdetect = model.detectMultiScale(photo1)
				if len(fdetect)==0:
					print("no face found")
					
				x1 = fdetect[0][0]
				y1 = fdetect[0][1]
				x2 = fdetect[0][2] + x1
				y2 = fdetect[0][3] + y1
				test1 = photo1[y1:y2,x1:x2]
				photo2 = cv2.imread(j)
				fdetect1 = model.detectMultiScale(photo2)
				if len(fdetect1)==0:
					print( "no face found")

				a1 = fdetect1[0][0]
				b1 = fdetect1[0][1]
				a2 = fdetect1[0][2] + a1
				b2 = fdetect1[0][3] + b1



				test2 = photo2[b1:b2,a1:a2]
				import numpy as np
				t_1 = cv2.resize(test1,(80,80))
				t_2 = cv2.resize(test2,(80,80))

				ch =input("""
				press h for horizontal attachment
				press y for vertical attachment
							 :  """)
				if "h" in ch:
					f_test = np.hstack((t_1,t_2))
					cv2.imshow("hello",f_test)
					cv2.waitKey()
					cv2.destroyAllWindows()
				elif "v" in ch:
					f_test = np.vstack((t_1,t_2))
					cv2.imshow("hello",f_test)
					cv2.waitKey()
					cv2.destroyAllWindows()
				else:
					print("u did not press the correct key")
				save =input('Press "s" to save photo: ')
				if "s" in save:
					cv2.imwrite("concat.png",f_test)
			elif ch == 10:
				x=input("Enter the location of the file:")
				photo1 = cv2.imread(x)
				fdetect = model.detectMultiScale(photo1)
				x1 = fdetect[0][0]
				y1 = fdetect[0][1]
				x2 = fdetect[0][2] + x1
				y2 = fdetect[0][3] + y1
				if len(fdetect) == 0:
					print("face not detected")
				else:
					b = photo1[y1:y2,x1:x2]
					cv2.imshow("hi",b)
					cv2.waitKey()
					cv2.destroyAllWindows()
					cv2.imwrite("crop.png" , b)
			elif ch == 11:
				while True:
					ret,photo = cap.read()
					fdetect = model.detectMultiScale(photo)
					if len(fdetect) == 0:
						print("face not detected")
					else:    
						x1 = fdetect[0][0]
						y1 = fdetect[0][1]
						x2 = fdetect[0][2] + x1
						y2 = fdetect[0][3] + y1
						b = photo[y1:y2,x1:x2]
						blur = cv2.blur(b,(20,20))
						photo[y1:y2,x1:x2] = blur
						cv2.imshow("hi",photo)
						if cv2.waitKey(100) == 13:
							break
				cv2.destroyAllWindows()
			
			elif ch == 12:
				os.system("clear")
				os.system("tput setaf 1")
				print("Press left mouse_button and drag to crop")
				os.system("sleep 3")
				os.system("tput setaf 7")
				ret,photo = cap.read()
				a=[]
				def lw(event,x,y,d,e):
					global a
					while event == 1 or event == 4:
						if event == 1:
							a.append(x)
							a.append(y)
							print(x,y)
							break
						if event == 4:
							print(x,y)
							a.append(x)
							a.append(y)
							break
					while event == 4:
						print(a)
						x1 = a[0]
						y1 = a[1]
						x2 = a[2]
						y2 = a[3]
						cv2.rectangle(photo,(x1,y1),(x2,y2),[0,255,0])
						global n_photo
						n_photo = photo[y1:y2,x1:x2]
						break
				cv2.namedWindow("hi")
				cv2.setMouseCallback("hi",lw)
				while True:
					cv2.imshow("hi",photo)
					if cv2.waitKey(1) == 13:
						break
				cv2.destroyAllWindows()
				while True:
					cv2.imshow("hi",n_photo)
					if cv2.waitKey(1) == 13:
						break
				cv2.destroyAllWindows()

			elif ch == 13:
				while True:
					ret,photo = cap.read()
					scale_percent = 30
					width = int(photo.shape[1] * scale_percent /100)
					height = int(photo.shape[0] * scale_percent /100)
					dim = (width,height)
					resize = cv2.resize(photo,dim,interpolation = cv2.INTER_AREA)
					photo[0:height,0:width] = resize
					cv2.imshow("hi",photo)
					if cv2.waitKey(1) == 13:
						break
				cv2.destroyAllWindows()

			elif ch == 14:
				break

			else:
				os.system("clear")
			input("press enter to continue..............")
			os.system("clear")	
	elif ch == 3:
		import os
		os.system("tput setaf 11")

		print("""
#########################################
#                                       #
#                                       #
#               DOCKER                  #
#                                       #
#########################################

_________________________________________
_________________________________________
		""")

		while True:
			print("""
1.To install docker                  13.To delete all the images
2.To start docker services           14.To create an image
3.Login to dockerhub                 15.To save an image
4.docker information                 16.To load an image
5.To download docker images          17.To change image name
6.To launch docker container         18.Upload image to docker registry
7.To copy a file inside container    19.Details of image/container
8.To see running containers          20.To run a cmd and exit 
9.To see all containers              21.To list all networks
10.To delete a container             22.To inspect any network
11.To delete all the containers      23.To check history of images
12.To delete any image               24. For main menu
			""")
			ch =int(input("Enter your choice: "))
			if ch == 1:
				os.system("yum install -y yum-utils")
				os.system("yum-config-manager \
				--add-repo \
				https://download.docker.com/linux/centos/docker-ce.repo")
				os.system("yum install docker-ce -y -y")

			elif ch == 2:
				os.system("systemctl start docker")

			elif ch == 3:
				os.system("docker login")

			elif ch == 4:
				os.system("docker info")	



			elif ch == 5:
				img = input("Enter image name: ")
				os.system("docker pull {}".format(img))

			elif ch == 6:
				img =input("Enter image name:")
				env =input("Want any environmental variable(y/n): ")
				if env == "n":
					gui =input("Want to run GUI programs(y/n): ")
					if gui == "n":
						pat = input("Want to have patting enabled?(y/n): ")
						if pat == "n":
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it --name {} {}".format(name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it --name {} -v {}:{}  {}".format(name,h_path,c_path,img))
						elif pat == "y":
							print("NOTE: Your image should contain EXPOSE keyword to use patting")
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it --name {} -P {}".format(name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it --name {} -v {}:{} -P {}".format(name,h_path,c_path,img))
					elif gui == "y":
						pat = input("Want to have patting enabled?(y/n): ")
						if pat == "n":
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it -e DISPLAY --net=host --name {} {}".format(name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it -e DISPLAY --net=host --name {} -v {}:{} {}".format(name,h_path,c_path,img))
						elif pat == "y":
							print("NOTE: Your image should contain EXPOSE keyword to use patting")
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it -e DISPLAY --net=host --name {} -P {}".format(name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it -e DISPLAY --net=host --name {} -P -v {}:{} {}".format(name,h_path,c_path,img))
				elif env == "y":
					env1 = input("Enter environmental variable: ")
					gui = input("Want to run GUI programs(y/n): ")
					if gui == "n":
						pat = input("Want to have patting enabled?(y/n): ")
						if pat == "n":
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} --name {} {}".format(env,name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} --name {} -v {}:{}  {}".format(env,name,h_path,c_path,img))
						elif pat == "y":
							print("NOTE: Your image should contain EXPOSE keyword to use patting")
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} -P --name {} {}".format(env1,name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} -P --name {} -v {}:{}  {}".format(env1,name,h_path,c_path,img))
					elif gui == "y":
						pat = input("Want to have patting enabled?(y/n): ")
						if pat == "n":
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} -e DISPLAY --net=host --name {}  {}".format(env1,name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} -e DISPLAY --net=host --name {} -v {}:{}  {}".format(env1,name,h_path,c_path,img))
						elif pat == "y":
							print("NOTE: Your image should contain EXPOSE keyword to use patting")
							mount = input("want to link storage to docker host(y/n): ")
							if mount == "n":
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} -P -e DISPLAY --net=host --name {} {}".format(env,name,img))
							elif mount == "y":
								h_path = input("docker host path: ")
								c_path = input("container path: ")
								name = input("Enter your container name: ")
								os.system("docker run -it -e {} -P -e DISPLAY --net=host --name {} -v {}:{} {}".format(env,name,h_path,c_path,img))
			elif ch == 7:
				file = input("Enter filename to be copied: ")
				name= input("Enter container name where the file is to be copied: ")
				dest = input("Enter destination path: ")
				os.system("docker cp {} {}:{}".format(file,name,dest))
			

			elif ch == 8:
				os.system("docker ps")


			elif ch == 9:
				os.system("docker ps -a")


			elif ch == 10:
				name = input("Enter your container name/ID: ")
				os.system("docker rm -f {}".format(name))

			elif ch == 11:
				os.system("docker rm -f $(docker ps -a -q)")


			elif ch == 12:
				img = input("Enter image name: ")
				os.system("docker rmi -f {}".format(img))

			elif ch == 13:
				os.system("docker rmi -f $(docker images -a -q)")

			elif ch == 14:
				location = input("Enter new location to create Dockerfile: ")
				os.system("mkdir {}".format(location))
				os.chdir(location)
				img_name =input("Enter image name: ")
				os.system("vim Dockerfile")
				os.system("docker build -t {} {}".format(img_name,os.getcwd()))
				print(os.getcwd())

			elif ch == 15:
				img = input("Image name : ")
				os.system("tput setaf 1")
				print("Note: File name should be provided with '(.tar)' extension")
				os.system("tput setaf 7")
				f_name = input("File name: ")
				os.system("docker save {} -o {}".format(img,f_name))
			
			elif ch == 16:
				f_name = input("File name: ")
				os.system("docker load -i {}".format(f_name))
			
			elif ch == 17:
				c_name = input("Current name: ")
				n_name = input("New name: ")
				os.system("docker tag {} {}".format(c_name,n_name))

			elif ch == 18:
				os.system("tput setaf 1")
				print("""
			Note:Your image should be saved in the below format
					   dockerid/imagename
				""")
				os.system("tput setaf 7")
				img = input("Enter image name: ")
				os.system("docker push {}".format(img))	

			elif ch == 19:
				name = input("Enter conatiner/image name: ")
				os.system("docker inspect {}".format(name))

			elif ch == 20:
				name = input("Enter container name: ")
				os.system("docker start {}".format(name))
				cmd = input("command: ")
				os.system("docker exec {} {}".format(name,cmd))
			
			elif ch == 21:
				os.system("docker network ls")
			
			elif ch == 22:
				net = input("Enter network name: ")
				os.system("docker network inspect {}".format(net))
			elif ch == 23:
				img = input("Enter image name: ")
				os.system("docker history {}".format(img))	
			
			elif ch == 24:
				break
			input("Press enter to continue........")
			os.system("clear")
	


	elif ch == 4:
		os.system("tput setaf 39")
		print("""
#########################################
#                                       #
#                                       #
#            Machine Learning           #
#                                       #
#########################################

_________________________________________
_________________________________________
		""")

		while True:
			
			print("""
1.Linear Regression
2.Logistic Regression
3.ANN
4.Load a model
5.Load ANN model
6.Main Menu
			""")
			ch = int(input("Enter your choice: "))
			if ch == 1:
				import numpy as np
				import pandas as pd
				import joblib
				import os
				os.system("tput setaf 21")
				print("""
Our model will only work if your
dataset has undergone preprocessing
and 
the output column name should be 'y'
				""")
				os.system("tput setaf 7")
				location = input("Enter the location of dataset: ")
				data = pd.read_csv(location)
				x = data.drop('y',axis=1)
				y = data[['y']]
				from sklearn.model_selection import train_test_split
				x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
				from sklearn.linear_model import LinearRegression
				model = LinearRegression()
				model.fit(x,y)
				model.predict(x)
				while True:
					ch = int(input("""
					1. To predict
					2. Bias 
					3. Weight 
					4. To exit
					Enter your choice: """))
					if ch == 1:
						x_input = (input("Enter your x values in order: "))
						y_pred = model.predict([list(x_input.split(","))])
						os.system("tput setaf 34")
						print(y_pred)
						os.system("tput setaf 7")
						
					elif ch == 2:
						bias = model.intercept_
						os.system("tput setaf 34")
						print(bias)
						os.system("tput setaf 7")

					elif ch == 3:
						os.system("tput setaf 34")
						weight = model.coef_
						print(weight)
						os.system("tput setaf 7")

					elif ch == 4:
						break

				save = input("want to save the model(y/n): ")
				if save == "y":
					os.system("tput setaf 1")
					print("Note:Extension should be 'pk1'")
					os.system("tput setaf 7")
					dump = input("Enter your model name: ")
					joblib.dump(model,"{}".format(dump))

			elif ch == 2:
				import numpy as np
				import pandas as pd
				import joblib
				import os
				os.system("tput setaf 21")
				print("""
Our model will only work if your
dataset has undergone preprocessing
and 
the output column name should be 'y'
				""")
				os.system("tput setaf 7")
				location = input("Enter the location of dataset: ")
				data = pd.read_csv(location)
				x = data.drop('y',axis=1)
				y = data[['y']]
				from sklearn.model_selection import train_test_split
				x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
				from sklearn.linear_model import LogisticRegression
				model = LogisticRegression()
				model.fit(x,y)
				model.predict(x)
				while True:
					ch = int(input("""
					1. To predict
					2. Bias 
					3. Weight 
					4. To exit
					Enter your choice: """))
					if ch == 1:
						x_input = (input("Enter your x values in order: "))
						y_pred = model.predict([list(x_input.split(","))])
						os.system("tput setaf 34")
						print(y_pred)
						os.system("tput setaf 7")
						
					elif ch == 2:
						bias = model.intercept_
						os.system("tput setaf 34")
						print(bias)
						os.system("tput setaf 7")

					elif ch == 3:
						os.system("tput setaf 34")
						weight = model.coef_
						print(weight)
						os.system("tput setaf 7")

					elif ch == 4:
						break

				save = input("want to save the model(y/n): ")
				if save == "y":
					os.system("tput setaf 1")
					print("Note:Extension should be 'pk1'")
					os.system("tput setaf 7")
					dump = input("Enter your model name: ")
					joblib.dump(model,"{}".format(dump))
			
			if ch == 3:
				import os
				import pandas as pd
				os.system("tput setaf 21")
				print("""
the output column name should be 'y'
				""")
				os.system("tput setaf 7")
				location = input("Enter the location of dataset: ")
				data = pd.read_csv(location)
				x = data.drop('y',axis=1)
				y = data['y']
				from keras.models import Sequential
				model = Sequential()
				from keras.layers import Dense
				iteration = int(input("How many layers you need: "))
				n=1
				n_neurons = int(input("Enter the number of neurons for layer {}: ".format(n)))
				activation = input("Enter activation function for layer {}: ".format(n))
				in_shape = int(input("Enter the number of input column shape: "))

				model.add(Dense(
						units=n_neurons,
						activation=activation,
						input_shape= (in_shape,)
				))

				for i in range(iteration-1):
					n += 1  
					n_neurons = int(input("Enter the number of neurons for layer {}: ".format(n)))
					activation = input("Enter activation function for layer {}: ".format(n))
					model.add(Dense(
						units=n_neurons,
						activation=activation
					))

				loss_func = input("Enter loss func: ")
				#"mean_squared_error"
				Optimizer = input("Optimizer: ")
				#"adam"
				model.compile(loss = loss_func , optimizer = Optimizer ,metrics=['accuracy'])

				e = int(input("Enter epoch: "))
				model.fit(x,y,epochs=e , validation_split = .2)

				while True:
					ch = int(input("""
1. To predict
2. Column names
3. Dataset
4. Dataset information
5. Layers details
6. Number of layers
7. Model weight
8. Exit
Enter your choice: """))
					if ch == 1:
						x_input = input("Enter your x values in order: ")
						list_x = list(x_input.split(","))
						int_x = [float(x) for x in list_x]
						y_pred = model.predict(int_x)
						os.system("tput setaf 34")
						print(y_pred)
						os.system("tput setaf 7")
						
					elif ch == 2:
						os.system("tput setaf 34")
						print(data.columns)
						os.system("tput setaf 7")

					elif ch == 3:
						os.system("tput setaf 34")
						print(data.head)
						os.system("tput setaf 7")

					elif ch == 4:
						os.system("tput setaf 34")
						print(data.info())
						os.system("tput setaf 7")

					elif ch == 5:
						os.system("tput setaf 34")
						print(model.get_config())
						os.system("tput setaf 7")

					elif ch == 6:
						os.system("tput setaf 34")
						print(model.summary())
						os.system("tput setaf 7")

					elif ch == 7:
						os.system("tput setaf 34")
						weight = model.get_weights()
						print(weight)
						os.system("tput setaf 7")

					elif ch == 8:
						break
					input("Press Enter to continue..........")
					os.system("clear")
				save = input("want to save the model(y/n): ")
				if save == "y":
					os.system("tput setaf 1")
					print("Note:Extension should be 'h5'")
					os.system("tput setaf 7")
					dump = input("Enter your model name: ")
					model.save("{}".format(dump))

			elif ch == 4:
				import numpy as np
				import pandas as pd
				import joblib
				import os
				location = input("Enter the location of pk1 file: ")
				model = joblib.load(location)
				y_pred = input("Enter x values in order: ")
				o = model.predict([list(y_pred.split(","))])
				print(o)
			
			elif ch == 5:
				from keras.models import load_model
				model_name = input("Enter model name: ")
				model = load_model("{}".format(model_name))
				while True:
					ch = int(input("""
1. To predict
2. Layers details
3. Number of layers
4. Model weight
5. Exit
Enter your choice: """))
					if ch == 1:
						x_input = input("Enter your x values in order: ")
						list_x = list(x_input.split(","))
						int_x = [float(x) for x in list_x]
						y_pred = model.predict(int_x)
						os.system("tput setaf 34")
						print(y_pred)
						os.system("tput setaf 7")

					elif ch == 2:
						os.system("tput setaf 34")
						print(model.get_config())
						os.system("tput setaf 7")

					elif ch == 3:
						os.system("tput setaf 34")
						print(model.summary())
						os.system("tput setaf 7")

					elif ch == 4:
						os.system("tput setaf 34")
						weight = model.get_weights()
						print(weight)
						os.system("tput setaf 7")

					elif ch == 5:
						break
					input("Press Enter to continue..........")
					os.system("clear")
			
			elif ch == 6:
				break

	elif ch == 5:
		import os
		os.system("tput setaf 112")
		print("""
		#########################################
		#                                       #
		#                                       #
		#            AWS Cloud                  #
		#                                       #
		#########################################
		_________________________________________
		_________________________________________
		""")
		while True:
			os.system("tput setaf 114")
			import os
			print("""
1. To launch an ec2 instance on AWS Cloud
2. To connect to the ec2-instance
3. Main Menu
			""")
			choice = int(input("Enter your choice: "))
			if choice == 1:
				print("Please use '}' in the end")
				name = input("Enter the name for instance: ")
				tag = "{Key=Name,Value="
				os.system(f"aws ec2 run-instances --image-id ami-079b5e5b3971bd10d --instance-type t2.micro --key-name linux_hash13_key --security-group-ids sg-0b021ca763799fc56 --count 1 --tag-specifications 'ResourceType=instance,Tags=[{tag}{name}]'")


			elif choice == 2:
				value = input("Which instance you want to connect: ")
				os.system(f"aws ec2 describe-instances --filters 'Name=tag:Name,Values={value}'   --output text --query 'Reservations[].Instances[].InstanceId' > a.txt")
				os.system("aws ec2 describe-instances --instance-ids $(cat a.txt) --query  Reservations[].Instances[].PublicIpAddress --output text > b.txt")
				name = input("Enter user name to connect: ")
				os.system(f"ssh $(cat b.txt) -l {name} -i linux_hash13_key.pem")
			else: 
				print("Heading towards main menu")
				break
			input("press enter to continue..............")
			os.system("clear")

	elif ch == 6:
		os.system("python3 ansible.py")
	elif ch == 7:
		print("""
		#########################################
		#                                       #
		#                                       #
		#            Kubernetes                 #
		#                                       #
		#########################################
		_________________________________________
		_________________________________________
		""")
		os.system("python3 /root/kube.py")
	elif ch == 8:
		break
