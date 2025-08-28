#code 1
with open ("example.txt","w") as f:
    f.write("Hello, World!")
    #code 2
f1=open("data1.txt","w")
f2=open("data2.txt","w")
f1.write("First file content.\n")
f2.write("Second file content.\n")
print("file written successfully")
#code 3
data=open("input.txt","r")
output=open("output.txt","w")
for line in data:
    output.write(line.upper())
    print("proccesing done")
    #code 4
f=open("numbers.txt","r")
nums=f.readlines()
squars=[]
for n in nums:
    squars.append(str(int(n)* int(n)))
f2=open("squares.txt","w")
for s in squars:
    f2.write(str(sq)+"\n")
print("squares written ")

    