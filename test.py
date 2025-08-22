h = input("Your name: ")
k = input("Your notes: ")
with open("file.txt", "w") as f:
    f.write(h + "\n" + k)
