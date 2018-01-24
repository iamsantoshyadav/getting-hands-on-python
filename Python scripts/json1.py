#%%
#this program is just an example of JSON sxripe and implimentation of JSON
import json
data ='''{
    "name" : "santosh",
    "gender" : "male",
    "phone" : {
        "type" : "intl",
        "number" : "856087058"
    },
    "email" : {
        "hide" : "yes"       
    }
}'''
info=json.loads(data)
print(info["name"])
