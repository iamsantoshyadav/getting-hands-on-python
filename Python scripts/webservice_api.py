#%%
#this program is an basic example of API
import urllib.request,urllib.parse,urllib.error
import json
serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"#Google geomap url
while True :
    address=input("Enter location : ") #here our address has to filled up
    if len(address)<1 :
        break
    url=serviceurl+urllib.parse.urlencode({"address" : address}) 
    print("Conecting to : ",url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print("Retrived ",len(data)," cheracters")
    try :
        js=json.loads(data)
    except :
        js=None
    if not js or "status" not in js or js["status"]!="OK" :
        print("====Failed to Retrive====")
        print(data)
        continue
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print("Lattitude : ",lat,"\n Longitude : ",lng)