import requests
from bs4 import BeautifulSoup

#works for men shoes, some women shoes image has $ and it will not work
url = 'http://store.nike.com/us/en_us/pd/usab-hyperdunk-2016-low-lmtd-unisex-basketball-shoe-mens-sizing/pid-11221034/pgid-11400121'

r = requests.get(url)

image_rule = '?wid=2100&hei=2100&fmt=jpeg&qlt=85&bgc=F5F5F5'
real_link = ''
image_link_list = []

soup = BeautifulSoup(r.content, "html.parser")
#print soup
#print soup

# image_links = soup.find_all('img',{''})
# print image_links

links = soup.find_all('div', {'class': 'hero-image-container'})
#print links
for link in links:
	print link.contents
	og_link = link.contents[1].get('data-src-large')
	print og_link
	temp_link = str(og_link).replace('images','images2') #text.replace('images','images2')

	#print next_image
	print temp_link
	current_link = temp_link + image_rule
	print current_link
	image_link_list.append(current_link)
	lettter_list = ['A', 'B', 'C','D', 'E', 'F','G']
	for index in range(0,7):
		try:
			current = lettter_list[index]
			print current
			next = lettter_list[index+1]
			print next
			to_be_replaced = current + '_PREM'
			new_name = next + '_PREM'
			next_image = temp_link.replace(to_be_replaced, new_name)
			print next_image
			temp_link = next_image
			real_link = next_image + image_rule
			print real_link
			image_link_list.append(real_link)
		except:
			pass

	print image_link_list
	# for letter in lettter_list:
	# 	current = lettter_list[0]
	# 	to_be_replaced = letter+'_PREM'
	# 	next_image = temp_link.replace('A_PREM', 'B_PREM')

	# real_link = temp_link + image_rule
	# print real_link


# http://images2.nike.com/is/image/DotCom/PDP_HERO/W-ZOOM-LAUDERDALE--FRAGMENT-864294_100_A_PREM.jpg?wid=1860&hei=1860&fmt=jpeg&qlt=85&bgc=F5F5F5
# http://images.nike.com/is/image/DotCom/PDP_HERO/W-ZOOM-LAUDERDALE--FRAGMENT-864294_100_A_PREM.jpg   Large