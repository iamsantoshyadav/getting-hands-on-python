#%%
#This progrbam is about study of list with file and extracting data from that perticular file
fhand=open("file.txt")
for line in fhand :
    line=line.rstrip()
    if not line.startswith("from:") :
        continue
    else :
        list1=line.split()
email=list1[3].split("@")
print("Domain : ",email[1])
    