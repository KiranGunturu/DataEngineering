Indian=["samosa","Dal","Naan"]
Chineese=["Egg Role","Pot sticeker","fried rice"]
Italina=["Pizza","Pasta","risotto"]

dish=input("Enter your dish: ")

if dish in Indian:
    print("it is indian")
elif dish in Chineese:
    print("it is chineese")
elif dish in Italina:
    print("it is an italian")
else:
    print("i do not have any idea which cuisine it is:", dish)

