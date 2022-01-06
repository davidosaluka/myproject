from bs4 import BeautifulSoup
import requests
import re
gpu = input('what product do you want: ')
url = requests.get(f'https://www.newegg.com/p/pl?d={gpu}&N=4131').text
soup = BeautifulSoup(url, 'lxml')
page_num = soup.find(class_='list-tool-pagination-text').strong
real_page_num = int(str(page_num).split('/')[1].split('>')[-1][:2])
print(real_page_num)

items_found = {}
for page in range(1, real_page_num+1):
    url = requests.get(f'https://www.newegg.com/p/pl?d={gpu}&N=4131&page={page}').text
    soup = BeautifulSoup(url, 'lxml')
    div = soup.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
    items = div.find_all(text=re.compile(gpu))
    for item in items:
        parent = item.parent
        if parent.name != 'a':
            continue

        link = parent['href']
        next_parent = item.find_parent(class_='item-container')
        try:
            price = next_parent.find(class_='price-current').strong.string

            items_found[item] = {'price': int(price.replace(",", "")), 'link': link}
        except:
            pass
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])
for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print('__________________________________________')
