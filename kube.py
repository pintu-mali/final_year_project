while True:
	import cgi
	import subprocess as sp

	cmd=input("Enter your requirement:")
	#cmd = cgi.FieldStorage().getvalue("x")
	#n = cgi.FieldStorage().getvalue("n") #y will mostly have the name
	#a = cgi.FieldStorage().getvalue("a") #z and f are extra arguments that has a value=0 by defalut
	#f = cgi.FieldStorage().getvalue("f")

	# get pods deploy svc rc
	if ("show" in cmd or "list" in cmd or "display" in  cmd) and ("deploy" in cmd or "deployment" in cmd or "pod" in cmd or "container" in cmd or "svc" in cmd or "service" in cmd or "rc" in cmd):
		if ("deploy" in cmd or "deployement" in cmd):
			op = sp.getoutput('sudo ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com  sudo kubectl get deployment')  #list deployment

		elif ("pod" in cmd or "containers" in cmd or "pods" in cmd):
			op = sp.getoutput('ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl get pods')  #list pods.
		elif ("rc" in cmd):
			op = sp.getoutput('ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl get rc') # list rc
		else:
			op = sp.getoutput('ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl get svc') # list svc

	# create pods deploy

	elif ("create" in cmd or "launch" in cmd or "build" in cmd ) and ("deployment" in cmd or "deploy" in cmd or "pod" in cmd or "container" in cmd):
		n=input("Enter the name:")
		a=input("Enter the image name")
		if ("deployment" in cmd or "deploy" in cmd):
			op = sp.getoutput(f'ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl create deployment {n} --image={a}') #create deployment

		else:
			op = sp.getoutput(f' ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl run {n} --image={a}')
		# get nodes
	elif ("list" in cmd or "show" in cmd or "display" in cmd) and ("nodes" in cmd):
		op = sp.getoutput('ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl get nodes')

	# kubectl expose deployment pods
	elif ("expose" in cmd or "disclose" in cmd or "create" in cmd) and ("pods"in cmd or "pod" in cmd or "container" in cmd or "deploy" in cmd or "deployment" in cmd or "loadbalancer" in cmd) :
		n=input("Enter the name:")
		a=input("Enter the port number:")

		if ("deployment" in cmd or "deploy" in cmd):
			op = sp.getoutput(f'ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl expose deployment {n} --port={a} --type=NodePort')

		else:
			op = sp.getoutput(f'ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl expose pod {n} --port={a} --type=NodePort')

	# scale the deployment
	elif ("create" in cmd or "scale" in cmd or "replicate" in cmd) and ("deploy" in cmd or "deployment" in cmd or "replica" in cmd or "replicas" in cmd):
		n=input("Enter the name:")
		a=input("Enter the no of replicas")

		op = sp.getoutput(f'ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl scale deployment {n} --replicas={a}')

	# delete the pod deploy svc
	elif ("delete" in cmd or "remove" in cmd ) and ("deploy" in cmd or "deployment" in cmd or "pod" in cmd or "container" in cmd or "svc" in cmd or "service" in cmd):
		n=input("Enter the name:")
		if ("deploy" in cmd or "deployement" in cmd):
			op = sp.getoutput(f'ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl delete deployment {n}')

		elif ("pod" in cmd or "pods" in cmd or "container" in cmd):
			op = sp.getoutput(f'ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl delete pod {n} ')

		else:
			op = sp.getoutput(f'ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl delete svc {n} ')

	# delete entire infrastructure
	elif ("delete" in cmd or "remove" in cmd or "destroy" in cmd  or "clean" in cmd) and ("infrastructure" in cmd or "all" in cmd or "environment" in cmd):
		op = sp.getoutput('ssh -i "linux_hash13_key.pem" ec2-user@ec2-43-205-118-93.ap-south-1.compute.amazonaws.com sudo kubectl delete all --all')

	elif("break" in cmd  or "exit" in cmd ):
		break
	else:
		print("Your requirement is not satisfied !")


	print(op)

