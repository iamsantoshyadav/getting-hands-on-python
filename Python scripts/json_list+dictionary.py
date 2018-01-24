#%%
#this program is just implimentation of json document using list
import json
data ='''{
    "status" : "ok",
    "result" : [
        {
            "user_details" :{
                "user_name" : "santosh yadav",
                "user_id" : "yadav7866",
                "user_email" : "yadav7866@gmail.com"
            },
            "user_contect" : {
                "phone" : "8560870589",
                "email" : "yadav7866@gmail.com",
                "addr" : "near pathwari gandhi nagar bhilwara"
            }
        }
    ]
}'''
info=json.loads(data)
print(info)
print("Name : ",info["result"][0]["user_details"]["user_name"])