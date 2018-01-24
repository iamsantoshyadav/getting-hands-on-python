#%%
import xml.etree.ElementTree as ET
data = '''
<Person>
    <Name>Santosh yadav</Name>
    <phone type="intl">
        8560870589
    </phone>
    <email hide="yes"/>
</Person>'''
tree=ET.fromstring(data)
print("Name : ",tree.find("Name").text)
print("Addr :",tree.find("email").get("hide"))