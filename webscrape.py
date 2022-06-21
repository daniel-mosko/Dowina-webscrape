from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup


def pocet_stran():
    my_url2 = 'https://www.guitarshop.sk/Dowina-c16_141_3.htm?system_params%5Bskladem%5D=1'
    uclient2 = uReq(my_url2)
    page_html2 = uclient2.read()
    uclient2.close()
    page_soup2 = soup(page_html2, "html.parser")
    for x in page_soup2.findAll("input", {"class": "c468"}):
        return int(x.get('max'))


def vypis_produktov():
    for strana in range(pocet_stran()):
        my_url = f'https://www.guitarshop.sk/Dowina-c16_141_3.htm?system_params%5Bskladem%5D={strana}'
        uclient = uReq(my_url)
        page_html = uclient.read()
        uclient.close()
        page_soup = soup(page_html, "html.parser")
        for data in page_soup.findAll('div', {"class": "product"}):
            print(data.a['title'], '-', round(float(data.get('data-price')) * (1 + 20 / 100), 2), 'EUR')


vypis_produktov()
