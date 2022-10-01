from bs4 import BeautifulSoup
from pip._vendor import requests

search = input("Please enter target family: ")

html_text = requests.get("https://scamit.org/tools/").text
soup = BeautifulSoup(html_text, 'lxml')
Family = soup.find('a', href = '#', text = "Family " + search) #use find_all___[1::] to get all

if Family == None:
	print("No data found\n")
	exit()


Genus_text = Family.next_sibling
Genus_list = Genus_text.find_all('a', href = '#')

print("==========================================")
print("\n" + Family.text + ":\n")
for i in Genus_list:
	if "Subfamily" not in i.text:
		print("\t\t-" + i.text)
	else:
		print("\t" + i.text)
print("\n==========================================")
exit()