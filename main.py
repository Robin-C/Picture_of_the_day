#!/Users/Robin/myfirstvenv/bin/python

from DB import lien
from sqlalchemy import *
from sqlalchemy.orm import *
import urllib, json, urllib2, os.path

#URL of json
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
response = urllib.urlopen(url) #open the json

#parse the json
data = json.loads(response.read())
URLPath = data["images"][0]["url"]
datePic = data["images"][0]["startdate"]
description = data["images"][0]["copyright"]
pictureURL = "http://www.bing.com/" +URLPath

print pictureURL
# config path to save and filename
path = "/Users/$name/save/at/this/path" #change the path here
filename = datePic + ".jpg"
pathAndName = os.path.join(path, filename)

#open url, save file as .jpg

img = urllib2.urlopen(pictureURL)
localFile = open(pathAndName, 'wb')
localFile.write(img.read())
localFile.close()

#Connection to the DB

from sqlalchemy import create_engine
engine = create_engine('mysql://user:pwd@localhost:3306/yourdb')
Session = sessionmaker(bind=engine)
session = Session()

#store the URL to the table lien

url = lien(URL=pictureURL, date=datePic)
session.add(url)
session.commit()
#todo: add description to the DB (must remove weird characters first

quit()