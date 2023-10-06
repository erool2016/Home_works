import requests
import re
from bs4 import BeautifulSoup
from fake_headers import Headers
import json
#id_regex = re.compile(r"\d+")

headers_gen = Headers(os="win", browser="chrome")
url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
url2 ='https://spb.hh.ru/search/vacancy?area=1&area=2&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&L_save_area=true&text=python'
list_for_find = [ 'Django', 'Flask']
final_list = []
def requests_get_(url):
    resp = requests.get(url,headers=headers_gen.generate())
    return resp.text
def soup_obj(url):
    html = requests_get_(url2)
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="serp-item")
    print(len(items))
    for item in items:

        soup_obj_item(item)

def soup_obj_item(item):

    dict_item = {}
    dict_item['title'] = item.find("a", class_="serp-item__title").text
    dict_item['href'] = item.find("a", class_="serp-item__title").get("href")
    # print(title)
    dict_item['company'] = item.find("div", class_="vacancy-serp-item__info").get_text()
    dict_item['cont'] = item.find("div", class_='g-user-content').get_text()
    check_cont(dict_item)
    price = item.find("span", class_="bloko-header-section-2")
    if price:
        dict_item['price'] = price.text
    dict_item['city'] = item.find("div", class_="bloko-text", attrs={"data-qa": "vacancy-serp__vacancy-address"}).get_text()

def check_cont(dict):
    words = re.findall(r'[\w]+', dict['cont'])
    # print(words)
    for item in list_for_find:
        if item in words:
            if check_list(dict) is False:
                final_list.append(dict)
                # print(f'yes,заголовок{dict["title"]} добавлен в список final_list')
            else:
                # print(f'yes,заголовок{dict["title"]} найдено в списке {final_list}')
                continue


def check_list(dict):
    # print('check list')
    # print('dict title',dict['title'])
    for item in final_list:
        # print('item title',item['title'])
        if item['title'] == dict['title']:
            # print(f'yes,заголовок{dict["title"]} найдено в списке {final_list}')
            return True
    return False


def save_json_file(final_list):
    print('final list',final_list)
    dict_for_save = {}
    dict_for_save['list'] = []
    for item in final_list:
        dict_for_save['list'].append(item)
    print(dict_for_save)
    with open('final_list.json', 'w') as outfile:
        json.dump(dict_for_save, outfile)
    print(f'файл final_list.json сохранен')


if __name__ == '__main__':

    print(soup_obj(url))
    save_json_file(final_list)
    # print(f'итоговый список, всего {len(final_list)}')
    # for item in final_list:
    #     print(f'{item["title"]}\n{item["href"]}')