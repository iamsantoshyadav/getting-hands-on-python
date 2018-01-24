#%%
#this is an compelete example of json which is self implimented
#JSON USING DICTIONARIES
import json
data='''{
    "name" : "Santosh Yadav",
    "gender" : "Male",
    "contect" : {
        "phone" : 8560870589,
        "email" : "yadav7866@gmail.com",
        "adderess" : "Near pathwari, Gandhi nagar bhilwara rajsthan "
    },
    "interest" : "coding"
}'''
info=json.loads(data)
print("All data is here : ",info)
print("Name : ",info["name"])
print("Gender : ",info["gender"])
print("======Contects========\nPhone : ",info["contect"]["phone"],"\nEmail : ",info["contect"]["email"],"\nAdderess : ",info["contect"]["adderess"],"\n\nIntresr : ",info["interest"])
#%%
#this program is just an example of JSON type script 
import json
data='''{
    "users" : {
        "user_info" : {
            "user_name" : "yadav7866",
            "name" : "Santosh yadav",
            "gender" : "Male",
            "email" : "yadav7866@gmail.com",
            "contect" : {
                "phone" : "8560870589",
                "addr" : "bhilwara"
            }
        }
    }
}'''
info=json.loads(data)
print("No of level 1 tag : ",len(info))
print("No of Level 2 tag : ",len(info["users"]))
print("No of tag in Level 3 : ",len(info["users"]["user_info"]))
print("No of tag in Level 4 : ",len(info["users"]["user_info"]["contect"]))
print("\nName :",info["users"]["user_info"]["name"],"\nUser Name : ",info["users"]["user_info"]["user_name"])
print("Gender : ",info["users"]["user_info"]["gender"],"\nEmail : ",info["users"]["user_info"]["email"])
print("Phone : ",info["users"]["user_info"]["contect"]["phone"],"\nAddress : ",info["users"]["user_info"]["contect"]["addr"])
#%%
#This program is for json using for loop access
import json
data='''{
    "users" : {
        "user_info" : {
            "user_name" : "yadav7866",
            "name" : "Santosh yadav",
            "gender" : "Male",
            "email" : "yadav7866@gmail.com",
            "contect" : {
                "phone" : "8560870589",
                "addr" : "bhilwara"
            }
        },
        "user_status": "paid"
    }
}'''
info=json.loads(data)
for key in info :
    print("Parent : ",key)
    for key1 in info[key]:
        print("Child of ",key,":",key1)
        for key2 in info[key][key1] :
            print("Child of ",key1," : ",key2)