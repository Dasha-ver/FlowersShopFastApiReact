from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class ParserForLinks:

    @staticmethod
    def get_links_by_link(link):

        driver = webdriver.Chrome()

        driver.get(link)

        try:
            button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/button')

            while button.is_displayed():
                button.click()
        except:
            print("На странице менее 10 элементов")

        links_data = []
        source_data = driver.page_source
        bs = BeautifulSoup(source_data, 'html.parser')

        for elem in bs.find_all('a', class_="styles_link__G6iOi"):
            try:
                links_data.append((
                    'https://dolinaroz.by'+elem['href'],
                ))
            except:
                print(f'Неполная информация. {elem.text}')

        return links_data


