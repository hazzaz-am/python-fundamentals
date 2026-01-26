# file read
r = open(r'index.py')
cv = open(r"A:\personal\slack_backup.txt")
print(cv.read())

# create file
f  = open("personal.txt", "w")
f.write("My name is Hazzaz. I am a Junior Software Developer.")
f = open("personal.txt", "a")
f.write(" I work at NAFS technologies.")
f.close()