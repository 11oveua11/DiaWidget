import requests
from bs4 import BeautifulSoup

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import matplotlib.pyplot as plt

Window.size = (800 , 600)
Window.clearcolor = ( 100/255, 100/255, 100/255, 1)
Window.title = "CourseGraph"






class MyApp (App):

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def build(self):
        box = BoxLayout()
        ltxt1 = Label(text='')
        ltxt2 = Label(text='')
        ltxt3 = Label(text="txt3")
        ltxt4 = Label(text="txt4")
        ltxt5 = Label(text="txt5")
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        #box.add_widget(ltxt2)

        return box


if __name__ == "__main__":

    def get_cur_data():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'yandex_login=; _ym_uid=1678011307203224036; _ym_d=1678011307; tmr_lvid=38f1de275775b6a69d55f50ca33285fd; tmr_lvidTS=1678011306929; dzen-to-bookmarks-repeats=1; this-iz-dzen-repeats=1; zen_sso_checked=1; Session_id=noauth:1679950059; ys=c_chck.3715154140; yandexuid=4107361211678521903; mda2_beacon=1679950059246; sso_status=sso.passport.yandex.ru:synchronized; _ym_isad=2; _yasc=WNiHMz0Pl49HQPBdYJDGNTIcjTRvq9vBIKy689JXHbWoi17lkv8PHLG3EnH9EQ==; tmr_detect=0%7C1679950038831'
        }
        url = 'https://dzen.ru/news/quotes/0?issue_tld=ru&utm_referer=sso.dzen.ru'
        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.text, 'html.parser')

        table = soup.find('div', {'class': 'news-stock-table__content'})

        cdate_label = str(table.findAll('div', {'class': 'news-stock-table__cell'})[0]).split('>')[1].split('<')[0]
        currency_label = str(table.findAll('div', {'class': 'news-stock-table__cell'})[1]).split('>')[1].split('<')[0]
        cdate = table.findAll('div', {'class': 'news-stock-table__cell'})[3::3]
        currency = table.findAll('div', {'class': 'news-stock-table__cell'})[4::3]
        #cur_data = {}
        for i in range(len(cdate)):
            cdate[i] = str(cdate[i]).split('>')[1].split('<')[0]
            currency[i] = float(str(currency[i]).split('>')[1].split('<')[0])
            #cur_data[(str(cdate[i]).split('>')[1].split('<')[0])] = (str(currency[i]).split('>')[1].split('<')[0])

        return cdate_label, cdate, currency_label, currency

    #cur_data = get_cur_data()
    cdate_label, cdate, currency_label, currency = get_cur_data()

    plt.figure(figsize=[8,6], facecolor='grey')
    #plt.style = 1
    plt.title("Курс USD")
    plt.xlabel(cdate_label)
    plt.ylabel(currency_label)
    plt.plot(cdate, currency)




    MyApp().run()




