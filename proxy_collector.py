import os,sys
try:
	import urllib.request
	import urllib.error
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	os.system('pip install urllib3')
	os.system('pip install bs4')
	os.system('pip install numpy')
import time
print("""
______                                _ _           _             
| ___ \                              | | |         | |            
| |_/ / __ _____  ___   _    ___ ___ | | | ___  ___| |_ ___  _ __ 
|  __/ '__/ _ \ \/ / | | |  / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| |  | | | (_) >  <| |_| | | (_| (_) | | |  __/ (__| || (_) | |   
\_|  |_|  \___/_/\_\\__, |  \___\___/|_|_|\___|\___|\__\___/|_|   
                     __/ |                                        
                    |___/                                         
----------------------------
free proxy collector script 
created by abdoxfox
my github link :https://github.com/abdoxfox
telegram id :@Pythonest

+-------------+
""")
def slow(n):
	for i in str(n)+'\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.1)
slow('you will find the proxies in file named "proxy.txt" in this same directory path\nwait a moment please' )
try:
    time.sleep(7)# sleep for 7 (s)
    url = "https://free-proxy-list.net/" # the source
    req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    open_url = urllib.request.urlopen(req)
    data = open_url.read()
    soup = BeautifulSoup(data,'html.parser')
    proxy_file = open("Proxy.txt","w+")
    proxy_data = soup.find_all('tr')
    Pr_list = []
    for i in proxy_data:
        Pr = "{0}:{1}".format(BeautifulSoup(str(list(i)[0]),'html.parser').text,BeautifulSoup(str(list(i)[1]),'html.parser').text)
        Pr_list.append(Pr)
    Pr_list.remove(Pr_list[0])
    Pr_list.remove(Pr_list[-1])
    for p in Pr_list[:-11]:
        proxy_file.write("{0}\n".format(p))
    proxy_file.close()
    print("{0} Proxy chaine was added to the proxy file".format(len(Pr_list)-11))
    slow('you have collect proxies	successfuly .')
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)
