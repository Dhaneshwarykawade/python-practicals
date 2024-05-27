#count the occurence of each word in a given string

string=input("enter string :")
word=input("enter word:")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
        print("count of the word is :",count)
