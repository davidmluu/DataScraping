from bs4 import BeautifulSoup
import pandas as pd
import requests 
import time

all_books = [] ## create an empty list to store all books
html = requests.get('https://www.oclc.org/en/worldcat/library100/top500.html').text # link from site to web scrape to csv
soup = BeautifulSoup(html, 'lxml')
table = soup.find_all('table')[0]
rows = table.find_all('tr')[1:]
for row in rows:
    cells = row.find_all(['td', 'th'])
    if len(cells) >= 3:
        rank = cells[0].text.strip()
        title = cells[1].text.strip()
        author = cells[2].text.strip()
        
        book_data = pd.DataFrame([[rank, title, author]], 
                               columns=['rank', 'title', 'author']) # creates table of columns I want (prexisting from site)
        all_books.append(book_data)
    # time.sleep(1)
books_df = pd.concat(all_books)
books_df.to_csv("stats.csv", index=False)