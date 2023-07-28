f = open("test.txt",'r')
f.read() # read full file
f_list = f.readlines() # readLines will give us list
# read one by one
for line in f:
    print(line)
f.close()

# with way
# it will automatically close the file
with open("text.txt",'r') as f:
    print(f.read())
    for line in f:
        print(line)

# w - overwrite
f = open("text.txt",'w')
f.write('first line')
f.close()

# a - append
f = open("text.txt",'a')
f.write('first line')
f.close()




