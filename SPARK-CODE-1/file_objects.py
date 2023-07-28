f = open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt",'r')
# r - read
# w - write
# a - append
# r+ read & write
# rb - read binary data like images
# wb - write binary data like images
print(f.name)
print(f.mode)

f.close()

# context manager - use with which can automatically close the file

with open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt",'r') as f:
    pass
print(f.closed)

with open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt",'r') as f:
    pass
    # f.read() - read entire file
    # f.readlines() - read file as list (each line as an element in the list)
    # f.readline() - reads first line
    #f_comments = f.read()
    #print(f_comments)

# read one line at a time

with open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt",'r') as f:
    for line in f:
        print(line, end='')

# read 100 characters from file

with open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt",'r') as f:
    f_comments = f.read(100)
    print(f_comments, end='')

# use while loop : read 10 lines at a time untll we reach end of file

with open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt",'r') as f:
    size_to_read = 10
    f_comments = f.read(size_to_read)
    while len(f_comments) > 0:
        print(f_comments,end='')
        f_comments = f.read(size_to_read)

# read from file and write to another file

with open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt",'r') as rf:
    with open("Users/kirangunturu/Documents/WEEK12-SPARK/biglog_123.txt",'w') as wf:
        for line in rf:
            wf.write(line)







