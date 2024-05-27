#to remove the ith of occurances of given word

a=[]
n=int(input("enter the no of element of list: "))
for x in range(0,n):
    element=input("enter element"+ str(x+1)+ ":")
    a.append(element)
print(a)
    
c=[]
count=0
b=input("enter word to remove:")
n=int(input("enter the occurance to remove:"))
for i in a:
        if(i==b):
            count=count+1
            if(count!=n):
                c.append(i)
            else:
                c.append(i)
                if(count==0):
                    print("item not found")
                else:
                    print("the number of repetition is:",count)
                    print("update list is :",c)
                    print("the distinct element are",set(a))