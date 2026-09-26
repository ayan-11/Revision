with open("file.txt","a+") as file:
    file.write("Hiiii")
    file.seek(0)
    print(file.read())    