
#This program is about basic concept of extracting data from the file
fhand=open("mbox-short.txt")
allemails=[]
for line in fhand:
    line=line.strip()
    if line.startswith("From"):
        word=line.split()
        allemails.append(word[1]) #Putting all emails in single list
        if len(word)>2:
            print("Email : ",word[1],"\t","Date : ",word[2],word[3]) #taking out all emails and date from the data 
        else :
            continue
print("Here all ",len(allemails),"emails : ",allemails,"\n\n")
allemails.sort()
print("Sorted email list : ",allemails)
count =0
for email in allemails :
    email=email.split("@")
    if email[1]=="uct.ac.za" :
        count=count+1
print("In this list there are ",count,"no os uct.ac.za domain email")
    
