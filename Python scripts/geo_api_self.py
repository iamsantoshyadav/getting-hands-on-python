#%%
'''
this is self implemented prorgarm which is a basic api of google geometric
in this following code we are going to connect with google and we wil give a address to the google
an google wil return us latitude and longitude
'''
import json
import urllib.request, urllib.parse, urllib.error
serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"
while True :
    address=input("Enter location : ")
    if len(address)<1:
        break
    url=serviceurl+urllib.parse.urlencode({"address" : address})
    print("connecting to.........",url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    try :
        js=json.loads(data)
    except :
        js=None
    if not js or "status" not in js or js["status"]!="OK":
        print("=====Failed to Retrived=====")
        print(data)
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    add=js["results"][0]["formatted_address"]
    print("latitude : ",lat)
    print("Longitude : ",lng)
    print("Full Address : ",add)