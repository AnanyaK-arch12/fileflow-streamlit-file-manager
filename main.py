from pathlib import Path
import os

def createfile():
    try:
        name=input("please tell your file name:-")
        path=Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data=input("what you want to write:-")
                fs.write(data)
            print("file created successfully")
        else:
            print("error file name already exists")
    except Exception as err:
        print(f"an error occured as {err}")



def readfile():
    try:
        name=input("Please tell your file name:-")
        path=Path(name)
        if path.exists():
            with open (path,"r") as fs:
                content=fs.read()
                print(f"your file content is \n {content}")
        else:
            print("eror no such file exists")
    except Exception as err:
        print(f"an error occured as {err}")
def updatefile():
    pass
def deletefile():
    pass

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

a=int(input("Tell your response:"))
if a==1:
    createfile()
if a==2:
    readfile()
if a==3:
    updatefile()
if a==4:
    deletefile()

