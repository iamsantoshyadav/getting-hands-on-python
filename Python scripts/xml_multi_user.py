#%%
#this program is all about xml and json example 
import xml.etree.ElementTree as ET
data = '''
<person>
    <user>
        <name>santosh yadav</name>
        <email> yadav7866@gmail.com</email>
        <phon>8560870589</phon>
    </user>
    <user>
        <name>santosh yadav</name>
        <email> yadav7866@gmail.com</email>
        <phon>8560870589</phon>
    </user>
    
</person>
'''
tree=ET.fromstring(data)
print(tree)
lst=tree.findall("user")
print(lst)
for item in lst :
    print("Name : ",item.find("name").text)
#%%
#here it is an extra example of xml document with atribute
import xml.etree.ElementTree as et
#data variable takes all the xml document here
data='''
<users>
    <user id="001">
        <first_name>Santosh</first_name>
        <last_name>Yadav</last_name>
        <gender>male</gender>
        <age>22</age>
        <contect phone="phone" email="yadav7866@gmail.com">8560870589</contect>
    </user>
    <user id="002">
        <first_name>Shubhanshu</first_name>
        <last_name>Yadav</last_name>
        <gender>male</gender>
        <age>18</age>
        <contect phone="phone" email="yadav7866@gmail.com">8560870589</contect>
    </user>
</users>'''
tree=et.fromstring(data)
lst=tree.findall("user")
for item in lst :
    print("Name : \t",item.find("first_name").text,item.find("last_name").text)
    print("User Id : \t",item.get("id"))
    print("Phone : \t",item.find("contect").get("phone"),"\nEmail : ",item.find("contect").get("email"))
    print("Genger : ",item.find("gender").text)
    print("Age : ",item.find("age").text,"\n")
    