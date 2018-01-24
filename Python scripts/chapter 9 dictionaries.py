#%%
#This program is about practice for dictionary
dic=dict()
dic={"Money":300,B"Bank balance ":30000}
print(dic)
print(dic["Money"])
#%%
# here i am implimenting no of time occurance of any word
""" Counting no of time a perticular word occured by if else condition"""
ip=input("Enter your statments here : ")
word=ip.split()
dic=dict()
for words in word:
    if words in dic:
        dic[words]=dic[words]+1
    else :
        dic[words]=1
#this is double iteration variable where we can use two different variable for iteration
for key,value in dic.items():
    print(key,"\t\t",value)
    
print(dic)

#%%
count=dict()
fhand=open("words.txt")
words=fhand.read()
words=words.split()
for word in words :
    """Following logic can also be used for same operation as we have performed before by using if-else"""
    count[word]=count.get(word,0)+1
print(count)
larg_val=None
larg_word=None
for key,value in count.items():
    if larg_val is None or value >larg_val:
        larg_val=value
        larg_word=key
print("Large word : ",larg_word,"\n","Large value : ",larg_val)