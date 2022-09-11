from bs4 import BeautifulSoup
from mysql_shema import create_connection_mysql_db
import requests
import datetime
import time


def get_date(connection_db):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) \
                      Chrome/39.0.2171.95 Safari/537.36'}

    my_cursor = connection_db.cursor()
    print('Please wait')

    temp_pagination = ''
    for i in range(1, 50000):
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273?ad=offering'

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text,  "html.parser")

        pagination = soup.find('div', class_='pagination').find('a', class_="rss-link").get('href')

        if pagination != temp_pagination:
            temp_pagination = pagination
        else:
            break

        addresses = soup.find_all('div', class_='search-item')

        for item in addresses:
            image = item.find('div', class_='image')
            image_url = image.find('img').get('data-src')

            title = item.find('div', class_='title').a.text.strip()

            date = item.find('div', class_='location').find('span', {'class': 'date-posted'}).text

            if date[0] == '<':
                date = datetime.datetime.today().strftime("%Y-%m-%d")
            elif date == 'Yesterday':
                date = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 86400))
            else:
                date = date[6:] + "-" + date[3:5] + "-" + date[:2]

            city = item.find('div', class_='location').find('span', {'class': ""}).text.strip()

            beds = item.find('div', class_='rental-info').find('span', {'class': "bedrooms"}).text.strip()[5:].strip()

            description = item.find('div', class_='description').text.strip().split()
            description = ' '.join(description)

            currency = item.find('div', class_='price').text.strip()[0]
            price = item.find('div', class_='price').text.strip()[1:]

            data_parse = {
                'image_url': image_url,
                'title': title,
                'date': date,
                'location': city,
                'beds': beds,
                'description': description,
                'currency': currency,
                'price': price
            }

            try:
                update_table = "INSERT INTO data(image, title, date, location, beds, description, currency, price) \
                            VALUES(%(image_url)s, %(title)s, %(date)s, %(location)s, %(beds)s, %(description)s, \
                                                                                            %(currency)s, %(price)s)"
                my_cursor.execute(update_table, data_parse)
                connection_db.commit()
            except:
                pass
    my_cursor.close()
    connection_db.close()
    print('Operation completed')


get_date(create_connection_mysql_db('my_data_parse'))
