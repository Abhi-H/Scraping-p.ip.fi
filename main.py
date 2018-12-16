from bs4 import BeautifulSoup
import urllib2
import time

def link_generator(hash_list):

	char_list=list(chr(i) for i in range(ord('A'),ord('Z')+1))+list(chr(i) for i in range(ord('a'),ord('z')+1))
	for first in char_list:
		for second in char_list:
			for third in char_list:
				for fourth in char_list:
					hash_list.append(str(first)+str(second)+str(third)+str(fourth))


hash_list=[]
link_generator(hash_list)
print(len(hash_list))
prefix="https://p.ip.fi/"
count=0
break_cnt=0
start=time.time()
print("Start time is "+str(start))
for extension in hash_list:
	url=prefix+extension
	break_cnt=break_cnt+1

	if(count==1):
		break
	try:
		response=urllib2.urlopen(url)
		html=response.read()
		soup=BeautifulSoup(html,'html.parser')
		print(soup.get_text())[8:]
		count=count+1

	except:
		pass
end=time.time()
print("End time is "+str(end))
print("Time Elapsed is "+str(end-start))
print(break_cnt)
print(count)