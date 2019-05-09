import os
save_path = 'D:\Programming\Python'
print("File Path To Save All Python Programs : " + save_path)
if not os.path.isdir('D:\Programming\Python'):
    print("Directory Unavailable. Created Newly.")
    os.makedirs('D:\Programming\Python',mode=777)
else:
    print("Directory Already Available")
name_of_file = input("What is the name of the file: ")
completeName = os.path.join(save_path, name_of_file+".txt")
file1 = open(completeName, "w")
createUser = 'Home'
createPass = 'password'
file1.write(createUser + '\n')
file1.write(createPass)
userpassfile = file1.read().strip().split()
loginUser = input('What is your username? ')
loginPass = input('What is yout password? ')
if (loginUser and loginPass in userpassfile):
    print('Welcome')
else:
    print('Incorrect password or username!')