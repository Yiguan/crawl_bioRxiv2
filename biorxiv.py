import requests
import re
from bs4 import BeautifulSoup as BS
from random import randint
from time import sleep

url0 = "https://www.biorxiv.org"
my_header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
r0 = requests.get(url = url0, headers = my_header)
#page = 20

def getProxyPool():
	url = "https://free-proxy-list.net"
	r = requests.get(url = url, headers = my_header)
	soup = BS(r.text, "lxml")
	soup_tr = soup.find("tbody").findAll("tr")
	ip_list = [ip_item[0:2] for ip_item in [td.findAll("td") for td in soup_tr]]
	ip = [tt[0].text + ":" + tt[1].text for tt in ip_list]
	return(ip)

def goItem(a_url,ip_pool):
	sleep(randint(1,10))
	my_proxy = {"http":"http://"+ ip_pool[randint(0,len(ip_pool)-1)]}
	r_item = requests.get(url = a_url, headers = my_header, proxies = my_proxy) # cookies = r0.cookies, 
	if len(re.findall('<div class="article fulltext-view ">', r_item.text))==0:
		ret_line  = "Full text unvailable: " + a_url
	else:
		soup=BS(r_item.text,'lxml')
		div = soup.find('div', class_='article fulltext-view ')
		ret_line = ''
		h2_list = [tt for tt in div.find_all('h2') if "section" in tt.parent.attrs['class']]
		for sec in ["abstract","introduction","method","result","discussion"]:
			w_count = [len(ii.parent.text.split(" ")) for ii in h2_list if sec in ii.text.lower()]
			ret_line = ret_line + sec + "\t" + str(w_count) + "\t"
		#reference number
		w_count = [len(ii.parent.find_all("li")) for ii in h2_list if "reference" in ii.text.lower()]
		ret_line = ret_line + "reference" + "\t" + str(w_count) + "\t" + a_url
	return(ret_line)

def getPage(page_url, ip_pool):
	#page_url = url1
	my_proxy = {"http":"http://"+ ip_pool[randint(0,len(ip_pool)-1)]}
	r_page = requests.get(url = page_url,  headers = my_header, proxies = my_proxy) # cookies = r0.cookies,
	article_url_list = re.findall('<a href="(/content/[0-9].*?/.*?)" class="', r_page.text)
	p_list = []
	for a_url_part in article_url_list:
		print("https://www.biorxiv.org" + a_url_part)
		a_url = "https://www.biorxiv.org" + a_url_part + ".full"
		p_list.append(a_url)
	return(p_list)

if __name__ == '__main__':
	with open("biorxiv_summary.txt", "a") as ff:
		ip_pool = getProxyPool()
		for p in range(0,6199:):
			sleep(randint(5,20))
			if p%100==0:
				ip_pool = getProxyPool()
			print(p)
			url1 = "https://www.biorxiv.org/content/early/recent?page=" + str(p)
			p_list = getPage(url1, ip_pool)
			for url in p_list:
				ff.writelines(goItem(url, ip_pool) + "\n")

