from requests_html import HTMLSession
import sqlite3


s = HTMLSession()

query = input("Enter Location:")
url = f'https://www.google.com/search?q=weather+{query}'
url2 = f'https://www.google.com/search?q=time+zone+of+{query}'

r = s.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
r2 = s.get(url2, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})




print("\nWeather Description:")
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
print(desc)
print("\nTemperature:")
temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
print(temp, unit)
print("\nHumidity:")
humidity = r.html.find('span#wob_hm', first=True).text
print(humidity)
print("\nTime Zone:")
timezone = r2.html.find('div', first=True).text

conn = sqlite3.connect('cputest.db')
c = conn.cursor()
c.execute('''CREATE TABLE weather(Location TEXT, Temperature(degree C) INT, Humidity INT, Time_zone INT)''')
c.execute('''INSERT INTO weather VALUES(?,?,?,?)''', (query, temp, unit, desc))
conn.commit()
print('complete')
      





