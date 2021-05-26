import requests
from bs4 import BeautifulSoup
import time
import hashlib
import telegram_send as tgsend

url = "https://www.ouka.fi/koronarokotukset"
print("Start tracking "+url)

def get_korona():
 page = requests.get(url)
 soup = BeautifulSoup(page.content, "lxml")
 text = soup.select_one("div.journal-content-article ul").get_text().strip()
 return text

firstHash = hashlib.sha224(get_korona().encode("utf-8")).hexdigest()
#print(time.ctime()+" "+firstHash)
while True:
 time.sleep(600)
 try:
  newHash = hashlib.sha224(get_korona().encode("utf-8")).hexdigest()
#  print(time.ctime()+" "+newHash)
  if newHash == firstHash:
   continue
  else:
   message=time.ctime()+" "+get_korona()
   print(message)
   tgsend.send(messages=[message])
   firstHash = newHash
 except Exception as e:
   message=time.ctime()+" El problem :/"
   print(message)
   tgsend.send(messages=[message])
