#!/usr/bin/python3
import json
import socket
import urllib.request as ur

socket.setdefaulttimeout(1)
try:
	webURL = ur.urlopen("http://api.icndb.com/jokes/random?firstName=Chuck&amp;lastName=Norris")
	data = webURL.read()
	encoding = webURL.info().get_content_charset('utf-8')
	A = json.loads(data.decode(encoding))
	joke = "As an infant, Chuck Norris' parents gave him a toy hammer. He gave the world Stonehenge."
	if('value' in A and 'joke' in A['value']):
		joke = A['value']['joke']
except:
	joke = "The movie 'Invasion U.S.A. is, in fact, a documentary."

joke = str.replace(joke,'&quot;',"'")
print(joke)