#!/Users/Robin/myfirstvenv/bin/python

from DB import lien
from sqlalchemy import *
from sqlalchemy.orm import *
import urllib, json, urllib2, os.path

#URL of json
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
response = urllib.urlopen(url)

#parse the json
data = json.loads(response.read())
URLPath = data["images"][0]["url"]
datePic = data["images"][0]["startdate"]
description = data["images"][0]["copyright"]
pictureURL = "http://www.bing.com/" +URLPath

# config path to save and filename
path = "/Users/Robin/google drive/misc/picture of the day"
filename = datePic + ".jpg"
pathAndName = os.path.join(path, filename)

#open url, save file as .jpg

img = urllib2.urlopen(pictureURL)
localFile = open(pathAndName, 'wb')
localFile.write(img.read())
localFile.close()

#Connection to the DB

from sqlalchemy import create_engine
engine = create_engine('mysql://root:azerty@localhost:3306/madb')
Session = sessionmaker(bind=engine)
session = Session()

#check the last record in the db

id = session.query(lien).order_by(lien.id.desc()).first()

# if last record's URL is the same as the new URL we want to push then it means the script already ran that day and
# we don't want to add it to the DB.

if id.URL == pictureURL:
  quit()

else:
  url = lien(URL=pictureURL, date=datePic)
  session.add(url)
  session.commit()

