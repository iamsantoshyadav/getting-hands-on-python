#%%
import json
data='''[
    { "user_id" : "yadav7866",
      "name" : "Santosh Yadav",
      "email" : "yadav7866@gmail.com"
    },
    { "user_id" : "shubhanshu",
      "name" : "Shubhanshu Yadav",
      "email" : "shubhanshuemail@gmail.com"
    }
]'''
info = json.loads(data)
print(info)
for item in info :
    print("Name : ",item["name"])
    print("User ID : ",item["user_id"])
    print("Email : ",item["email"])