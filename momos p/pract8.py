#count the frequency of word appearing in a string using dictionary
str=input("enter string:")
list=[]
list=str.split()
word_freq=[list.count(i) for i in list]
print("freq of a word in a string are:", word_freq)
print(dict(zip(list,word_freq)))