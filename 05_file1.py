import os
print("*******************************File Operations*******************************")
save_path = 'D:\Programming\Python'
filetype = "*.txt"
print("Current File Path Defined To Save All Python Programs : " + save_path)
# Check if the defined path is available
if not os.path.isdir('D:\Programming\Python'):
    print("Directory is Unavailable. Created Newly.")
    os.makedirs('D:\Programming\Python',mode=777)
else:
    print("Directory is Already Available")
password_file_exists = os.path.isfile(save_path + "\\" + filetype)
print(save_path + "\\" + filetype)
print(password_file_exists)
if password_file_exists:
    for file in os.listdir(save_path):
        if file.endswith(".txt"):
            print("There is Already a File Available : " + os.path.join(save_path, file))
            # os.remove("D:\Programming\Python\*.txt")
else:
    name_of_file = input("Create a Password file. Provide FileName : ")
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