from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import csv

display = []
for j in range(6):
    try:
        source = requests.get(
            "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_" +
            str(j) +
            "?ie=UTF8&pg=" +
            str(j))
        cont = BeautifulSoup(source.content, 'html.parser')
        mainfray = cont.find_all('div', class_="zg_itemWrapper")
        l = len(mainfray)
        for i in range(l):
            try:
                bookname = (
                    mainfray[i].find(
                        'div',
                        class_="p13n-sc-truncate p13n-sc-line-clamp-1").get_text().strip()).encode('utf-8')
            except BaseException:
                bookname = "Not Available"
            try:
                url = "https://www.amazon.com" + \
                    (mainfray[i].find('a', class_="a-link-normal")
                     ['href']).encode('utf-8')
            except BaseException:
                url = "Not Available"
            try:
                author = (
                    mainfray[i].find(
                        'div',
                        class_="a-row a-size-small").get_text().strip()).encode('utf-8')
            except BaseException:
                author = "Not Available"
            try:
                price = (
                    mainfray[i].find(
                        'a',
                        class_="a-link-normal a-text-normal").get_text().strip()).encode('utf-8')
            except BaseException:
                price = "Not Available"
            try:
                review_count = (
                    mainfray[i].find(
                        'a',
                        class_="a-size-small a-link-normal").get_text().strip()).encode('utf-8')
            except BaseException:
                review_count = "Not Available"
            try:
                rating = (mainfray[i].find('div',
                                           class_="a-icon-row a-spacing-none").find('a',
                                                                                    class_="a-link-normal")['title']).encode('utf-8')
            except BaseException:
                rating = "Not Available"
            display.append(
                (bookname, url, author, price, review_count, rating))
    except BaseException:
        "do nothing"
'''data=[]
t=1;
for p in display:
    line=[]
    print(t,end='.')
    for j in p:
        line.append(j)
        print(j,end=';')
    print()
    t=t+1
    data.append(line)'''

fil = open('./output/com_books.csv', 'w')

with fil as file:
    # for row in display:
    writer = csv.writer(file, delimiter=str(";"))
    writer.writerows(display)
