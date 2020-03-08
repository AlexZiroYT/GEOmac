import webbrowser
import requests
from bs4 import BeautifulSoup
import os

print("Для программы нужны - BeautifulSoup, Requests, bs4")
install = input("Устанавливать? (y/n) : ")
if install == ("y"):
    bs = 'pip install BeautifulSoup4'
    bs4 = 'pip install bs4'
    rq = 'pip install requests'
    print("Идёт установка нужных пакетов...")
    os.system (bs)
    os.system (bs4)
    os.system (rq)
    print("░██████╗░███████╗░█████╗░  ███╗░░░███╗░█████╗░░█████╗░")
    print("██╔════╝░██╔════╝██╔══██╗  ████╗░████║██╔══██╗██╔══██╗")
    print("██║░░██╗░█████╗░░██║░░██║  ██╔████╔██║███████║██║░░╚═╝")
    print("██║░░╚██╗██╔══╝░░██║░░██║  ██║╚██╔╝██║██╔══██║██║░░██╗")
    print("╚██████╔╝███████╗╚█████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝")
    print("░╚═════╝░╚══════╝░╚════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░")
    print("█▀▄▀█ ▄▀█ █▀▀")
    print("█░▀░█ █▀█ █▄▄")
    print("Пример ввода a12b3cd45ef6")
    mac = input("[*] Mac адрес : ")
    a = mac
    linko = 'http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks='
    linkt = ':-65&app=ymetro'
    link = (linko+a+linkt)

    def get_html(link, params=None):
        r = requests.get(link, params=params)
        return r
        
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find_all('coordinates')
        print("Координаты => ", result)
    def parse():
        html = get_html(link)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Ошибка!')
            print('Возможно, вы ввели не верный mac адрес!')
            stop()
    parse()
    open = input('Открыть результат в браузере? (y/n) : ')
    n = 'Okey...' if open != ("y") else webbrowser.open(link)
    print (n)
elif install == ("n"):
    print("░██████╗░███████╗░█████╗░  ███╗░░░███╗░█████╗░░█████╗░")
    print("██╔════╝░██╔════╝██╔══██╗  ████╗░████║██╔══██╗██╔══██╗")
    print("██║░░██╗░█████╗░░██║░░██║  ██╔████╔██║███████║██║░░╚═╝")
    print("██║░░╚██╗██╔══╝░░██║░░██║  ██║╚██╔╝██║██╔══██║██║░░██╗")
    print("╚██████╔╝███████╗╚█████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝")
    print("░╚═════╝░╚══════╝░╚════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░")
    print("█▀▄▀█ ▄▀█ █▀▀")
    print("█░▀░█ █▀█ █▄▄")
    print("Пример ввода a12b3cd45ef6")
    mac = input("[*] Mac адрес : ")
    a = mac
    linko = 'http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks='
    linkt = ':-65&app=ymetro'
    link = (linko+a+linkt)

    def get_html(link, params=None):
        r = requests.get(link, params=params)
        return r
        
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find_all('coordinates')
        print("Координаты => ", result)
    def parse():
        html = get_html(link)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Ошибка!')
            print('Возможно, вы ввели не верный mac адрес!')
            stop()
    parse()
    open = input('Открыть результат в браузере? (y/n) : ')
    n = 'Okey...' if open != ("y") else webbrowser.open(link)
    print (n)