import optparse
import os 

parser = optparse.OptionParser()
parser.add_option('-u','--username',dest='user')
parser.add_option('-p','--password',dest='passw')

opts,args = parser.parse_args()

username = opts.user.capitalize()
password = opts.passw 

PATH = os.getcwd()
myUserName = os.getlogin()

host = os.environ['username']

os.chdir(PATH)

if myUserName in PATH:
	PATH = PATH.replace(myUserName,username)

lego = None

if username != host:
	print('Logged into a random account named %s' %PATH)
	lego = PATH
elif username == host:
	print('Logged into %s' %host)
	lego = host
else:
	print(None)

iterations = 0

while iterations < 3:
	value = input("%s> " %lego)
	os.system(value)
	iterations += 1

	if iterations == 3:
		exit(0)

