# f=open("C:/Users/kgunturu/Desktop/Python/funny.txt","a")
# f.write("\nI love PHP")
# f.close()
#
#
# f=open("C:/Users/kgunturu/Desktop/Python/funny.txt","w")
# f.write("\nI love PHP")
# f.close()


# f=open("C:/Users/kgunturu/Desktop/Python/funny.txt","r")
# print(f.read())
# f.close()


# f=open("C:/Users/kgunturu/Desktop/Python/funny.txt","r")
# for line in f:
#     tokens=line.split(' ')
#     print(str(tokens))
#     print(len(tokens))
#     #print(line)
# f.close()


# f=open("C:/Users/kgunturu/Desktop/Python/funny.txt","r")
# f_out=open("C:/Users/kgunturu/Desktop/Python/funny_wordcnt.txt","w")
# for line in f:
#     tokens=line.split(' ')
#     f_out.write("wordcount is: "+str(len(tokens))+' ' +line)
#     #print(line)
# f.close()
#f_out.close()

# what if we want to close the file automatically instead writing close() --


# with open("C:/Users/kgunturu/Desktop/Python/funny.txt","r") as f:
#     print(f.read())
# print(f.closed)






# r - only read and throws an error if file doesn't exist
# w - opens file writing only. if file doesn't exists then it will create or if it exists then overwrite.
# r+ - opens file for both reading and writing.
# w+ - opens file booth reading and writing. if file doesn't exists then it will create new one. if it exists then it will overwrite it.
# a - opens file in append mode. whatever you write to file will get appended and original content will not be overwritten.







