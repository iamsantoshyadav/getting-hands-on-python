#%%
data=[]
ip =  input("Enter  the five no here : ")
for no in ip.split():
    try :
        no=int(no)
        data.append(no)
    except :
        print("You did not have entered a valid value")
largest= -1
for nos in data:
    if nos>largest:
        largest = nos
print("Largest no is ",largest)
    