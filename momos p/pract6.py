#check if a substring is present in a string 
string= input("enter string:")
sub_string = input("enter substring :")
if(string.find(sub_string) == -1):
    print("substring is not found ")
else:
    print("substring in string")