import json,pprint
from bs4 import BeautifulSoup 
import requests

ALL_LINKS=["/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_f80a9979-e36a-4480-a578-a130dc8b4309_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=1sa7nn034h9eiry81588079176554&page=1","/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_f80a9979-e36a-4480-a578-a130dc8b4309_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=1sa7nn034h9eiry81588079176554&page=2","/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_f80a9979-e36a-4480-a578-a130dc8b4309_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=1sa7nn034h9eiry81588079176554&page=3","/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_f80a9979-e36a-4480-a578-a130dc8b4309_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=1sa7nn034h9eiry81588079176554&page=4","/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_f80a9979-e36a-4480-a578-a130dc8b4309_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=1sa7nn034h9eiry81588079176554&page=5","/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_f80a9979-e36a-4480-a578-a130dc8b4309_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=1sa7nn034h9eiry81588079176554&page=6","/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_f80a9979-e36a-4480-a578-a130dc8b4309_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=1sa7nn034h9eiry81588079176554&page=7"]

control=1
for link in ALL_LINKS:
	page=requests.get("https://www.flipkart.com"+link)
	soup=BeautifulSoup(page.text,"html.parser")
	main_div = soup.find_all("div",class_="bhgxx2 col-12-12")


	name=[]
	rating_num=[]
	ran_num=[]
	count=0
	print(control)
	for i in main_div:
		all_deatils={}
		if (count>=2 and count<=25):
			# first_i_=i.find("div",class_="col col-7-12")

			one1=i.find("div",class_="_3wU53n").text

			price_of_mobile=i.find("div",class_="_1vC4OE _2rQ-NK").text

			rating=i.find("div",class_="hGSR34").text

			ratings=i.find("span",class_="_38sUEc").text

			features_2_=i.find_all("li",class_="tVe95H")
			all_feauters=[]
			for j in features_2_:
				all_feauters.append(j.text)

			all_list=[]
			

			all_deatils["mobile-name"]=one1
			all_deatils["ratings_number"]=rating
			all_deatils["reviews"]=ratings
			all_deatils["u_features"]=all_feauters
			all_deatils["price"]=price_of_mobile
				# all_list.append(all_deatils)
			pprint.pprint(all_deatils)
			print(count)
		count+=1
	control+=1
	# break

# page_link=soup.find("nav",class_="_1ypTlJ")
# a_tags=page_link.find("a")["href"]
# print(a_tags)
# for link in a_tags:
# 	anchor_tag=link.find("a")
	# print(anchor_tag)
# pprint.pprint(name)
# pprint.pprint(rating_num)

	# co+=1





# for i in main_div:
# 	sub_div=i.find("div",class_="_3wU53n")
# 	one=sub_div.find("div").text
# 	print(one)



