from bs4 import BeautifulSoup
import urllib2
import time
from multiprocessing import Pool

def link_generator(hash_list):
	char_list=list(chr(i) for i in range(ord('A'),ord('Z')+1))+list(chr(i) for i in range(ord('a'),ord('z')+1))
	for first in char_list:
		for second in char_list:
			for third in char_list:
				for fourth in char_list:
					hash_list.append(str(first)+str(second)+str(third)+str(fourth))

def parse(url):
	try:
		response=urllib2.urlopen(url)
		html=response.read()
		soup=BeautifulSoup(html,'html.parser')
		hash_val=url[len(url)-4:len(url)]
		f = open(hash_val+".txt",'w')
		f.write((soup.get_text())[8:])
		f.close()
	except:
		pass

hash_list=[]
links=[]
link_generator(hash_list)
print(len(hash_list))
prefix="https://p.ip.fi/"
count=0
break_cnt=0
start=time.time()
print("Start time is "+str(start))
for extension in hash_list:
	url=prefix+extension
	links.append(url)

p = Pool(100)  # Pool tells how many at a time
records = p.map(parse, links)
p.terminate()
p.join()

end=time.time()
print("End time is "+str(end))
print("Time Elapsed is "+str(end-start))
print(break_cnt)
print(count)