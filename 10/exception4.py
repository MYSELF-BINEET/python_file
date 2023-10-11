name = input("Enter the name of the file : ")
try :
    with open(name,"r") as file :
        content = file.read()
        print("Displaying the content of the file",name,":")
        print(content)
except :
    print("FileNotFoundError")