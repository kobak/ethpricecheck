import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://ethereumprice.org'

headers = {
	"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

### print the whole website
#print(soup.prettify())

# find_all finds every appearance, limit limits it to the number
#price_array = soup.find_all("span", "value", limit=1)
#print(price_array)

#more elegant is to find just one and use get_text()
price = soup.find("span", "value").get_text()
print('Current $ETH price is: ' + price)
tizedesvesszo = price.find(',')
tizedespont = price.find('.')
price = price[0:tizedesvesszo] + price[tizedesvesszo+1:tizedespont]
#print(price)
priceinnumber = float(price[0:tizedespont])
#stripped dots and commas, converted to float
#print(price)

buyprice = 800
sellprice = 1500


def send_sellmail():
	print('sell!')		

def send_buymail():
	print('sell!')			
	
def send_buymail_SOON():
	server = smtplib.SMTP('smtp.google.com')
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	server.login('email@gmail.com', 'password')
	subject = "Time to buy"
	
	body = 'Time to buy ether. Price is down. Current price is: ' + price + '!'
	
	msg = f"Subject: {subject}\n\n{body}"
	
	server.sendmail(
		'fromemail@gmail.com',
		'toemail@gmail.com',
		msg
	)
	print('email sent')
	server.quit()

		
if priceinnumber < buyprice:
	send_buymail()

if priceinnumber > sellprice:
	send_sellmail()


# <span class="value">1,242.72</span>
