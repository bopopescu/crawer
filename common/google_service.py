#!/usr/bin/python
# coding: UTF-8
import json
import urllib2

import requests
from bs4 import BeautifulSoup

"""
google服务
1.翻译
2.经纬度
"""


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        print("Get HTML Text Failed!")
        return 0


def google_translate_EtoC(to_translate, from_language="en", to_language="ch-CN"):
    # 根据参数生产提交的网址
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, to_translate)

    # 获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")

    # 解析网页得到翻译结果
    try:
        result = soup.find_all("div", {"class": "t0"})[0].text
    except:
        print("Translation Failed!")
        result = ""

    return result


def google_translate_CtoE(to_translate, from_language="ch-CN", to_language="en"):
    # 根据参数生产提交的网址
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, to_translate)

    # 获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")

    # 解析网页得到翻译结果
    try:
        result = soup.find_all("div", {"class": "t0"})[0].text
    except:
        print("Translation Failed!")
        result = ""

    return result


def google_translate_DtoC(to_translate, from_language="de", to_language="ch-CN"):
    # 根据参数生产提交的网址
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, to_translate)

    # 获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")

    # 解析网页得到翻译结果
    try:
        result = soup.find_all("div", {"class": "t0"})[0].text
    except:
        print("Translation Failed!")
        result = ""

    return result


def google_translate_DtoE(to_translate, from_language="de", to_language="en"):
    # 根据参数生产提交的网址
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, to_translate)

    # 获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")

    # 解析网页得到翻译结果
    try:
        result = soup.find_all("div", {"class": "t0"})[0].text
    except:
        print("Translation Failed!")
        result = ""

    return result


def get_geo_for_address(address):
    headers = {
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    }
    position_dict = dict()
    quoto_address = urllib2.quote(address, ':?=/')
    address_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+quoto_address
    print address_url
    result = urllib2.urlopen(address_url).read().decode('utf-8')

    print result
    # 中文url需要转码才能识别
    # response = result.decode('utf-8')
    response_json = json.loads(result)
    lat = '0'
    lng = '0'
    if response_json.get('status') == 'OK':
        lat = response_json.get('results')[0]['geometry']['location']['lat']
        lng = response_json.get('results')[0]['geometry']['location']['lng']
        print(address + '的经纬度是: %f, %f' % (lat, lng))
    position_dict['lng'] = lng
    position_dict['lat'] = lat
    return position_dict


def main():
    words = 'Helle, sanierte 2 Zimmer-Wohnung in sehr guter Lage!'
    print(google_translate_DtoC(words))
    print(google_translate_DtoE(words))

if __name__ == '__main__':
    text = '''Biete meine gut geschnittene 1-Zimmer-Wohnung bester Lage Anbindung nur im Tausch gegen eine WG geeignete 3-4 Zimmerwohnung (1.200-1.600€ warm) an.Diese sollte bestenfalls auch in Friedrichshain sein, nähere Umgebung ist aber auch in Ordnung.Die Wohnung liegt zum Innenhof und ist dadurch sehr ruhig. Ein gemütlicher Balkon, großes Badezimmer mit Dusche und Einbauküche sind vorhanden.Die nächsten Anbindungen sind zum S- und U-Bhf Warschauer Straße, Tram M10, M13 sowie 21 und U5 Frankfurter Tor.Weitere Fotos und mehr Informationen bei realistischer Anfrage.Ich freue mich auf Tauschmöglichkeiten!'''
    print google_translate_DtoE(text)