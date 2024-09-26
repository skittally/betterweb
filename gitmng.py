import os

userInpt = input("git: ")

if userInpt == "pull":
	os.system("git pull origin main")

elif userInpt == "push":
	user2in = input("input your commit name: ")
	os.system("git add .")
	os.system(f'git commit -m "{user2in}"')
	os.system("git push origin master")
else:
	print("INVALID")