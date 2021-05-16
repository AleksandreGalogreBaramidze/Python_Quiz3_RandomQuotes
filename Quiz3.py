import requests
import json
import sqlite3
chelseaPhoto = requests.get('https://scontent.ftbs6-1.fna.fbcdn.net/v/t1.6435-9/182805797_1373424876372475_5652441314783625565_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=730e14&_nc_ohc=viRrtqqCEMsAX9YJCyf&_nc_ht=scontent.ftbs6-1.fna&oh=63f57c913052655412c0d97ae787d429&oe=60C7DEAB')
print(chelseaPhoto)
print(chelseaPhoto.status_code)
print(chelseaPhoto.headers)
print(chelseaPhoto.headers['Content-Type'])
image = open('chelseaphoto.png', 'wb')
image.write(chelseaPhoto.content)
image.close()

url = 'https://api.quotable.io/random'
urlRequest = requests.get(url)
print(urlRequest.text)
res = json.loads(urlRequest.text)
res_structured = json.dumps(res, indent=4)
newFile = open('quote.json', 'w')
newFile.write(res_structured)
newFile.close()
print(res['content'])

conn = sqlite3.connect('random_quotes.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS quotes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote VARCHAR(1000),
                author VARCHAR(100))''')

quote = res['content']
author = res['authorSlug']
print(author)

cursor.execute('insert into quotes (quote,author) values(?,?)', (quote, author))
conn.commit()
