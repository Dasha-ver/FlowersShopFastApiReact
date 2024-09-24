from bs4 import BeautifulSoup
from parser_for_links import ParserForLinks
import requests
import data_client


class ParserForOneCategory:

    def __init__(self, links_to_parse):
        self.links_to_parse = links_to_parse

    data_client_imp = data_client.PostgresClient()

    @staticmethod
    def get_items_by_link(link):

        cookies = {
            'cf_clearance': '6YenUt_pzj120E72tLk0vj3QQjvNdLG3cR3N5tJrfws-1691757855-0-1-cffaf297.75aa331e.cac3e71-250.2.1691757855',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        }

        response = requests.get(link, cookies=cookies, headers=headers)
        print(response)

        bouquets_of_roses_data = []
        bs = BeautifulSoup(response.text, "html.parser")

        for elem in bs.find_all('div', class_="styles_product__oq6nh"):
            image_link = elem.find('img')
            title = elem.find('h1')
            description = elem.find('div', class_='styles_shortDescription__p9ES8')
            price = elem.find('span', class_='styles_price__oaEr_').text.split('BYN')[0]
            try:
                bouquets_of_roses_data.append((
                    'https://dolinaroz.by' + image_link['src'],
                    title.text,
                    description.text.split('.')[0],
                    float(price)

                ))
            except:
                print(f'Неполная информация. {elem.text}')

        return bouquets_of_roses_data

    def save_to_postgres(self, items, table_name):
        connection = self.data_client_imp.get_connection()
        self.data_client_imp.create_table(connection, table_name)
        for item in items:
            self.data_client_imp.insert(connection, table_name, item[0], item[1], item[2], item[3])

    def run(self, table_name):
        items = []
        for link in self.links_to_parse:
            items.extend(self.get_items_by_link(link))
        self.save_to_postgres(items, table_name)



