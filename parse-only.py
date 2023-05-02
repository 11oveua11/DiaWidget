import requests
from bs4 import BeautifulSoup



class Cur_data:

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'yandex_login=; _ym_uid=1678011307203224036; _ym_d=1678011307; tmr_lvid=38f1de275775b6a69d55f50ca33285fd; tmr_lvidTS=1678011306929; dzen-to-bookmarks-repeats=1; this-iz-dzen-repeats=1; zen_sso_checked=1; Session_id=noauth:1679950059; ys=c_chck.3715154140; yandexuid=4107361211678521903; mda2_beacon=1679950059246; sso_status=sso.passport.yandex.ru:synchronized; _ym_isad=2; _yasc=WNiHMz0Pl49HQPBdYJDGNTIcjTRvq9vBIKy689JXHbWoi17lkv8PHLG3EnH9EQ==; tmr_detect=0%7C1679950038831'
        }
        self.url = 'https://dzen.ru/news/quotes/0?issue_tld=ru&utm_referer=sso.dzen.ru'
        self.page = requests.get(self.url, headers=self.headers)

        self.soup = BeautifulSoup(self.page.text, 'html.parser')

        self.table = self.soup.find('div', {'class': 'news-stock-table__content'})

        self.cdate_label = str(self.table.findAll('div', {'class': 'news-stock-table__cell'})[0]).split('>')[1].split('<')[0]
        self.currency_label = str(self.table.findAll('div', {'class': 'news-stock-table__cell'})[1]).split('>')[1].split('<')[0]
        self.cdate = self.table.findAll('div', {'class': 'news-stock-table__cell'})[3::3]
        self.currency = self.table.findAll('div', {'class': 'news-stock-table__cell'})[4::3]
        self.cur_data = []

    def get_cur_data(self):

        for i in range(len(self.cdate)):
            self.cdate[i] = str(self.cdate[i]).split('>')[1].split('<')[0]
            self.currency[i] = float(str(self.currency[i]).split('>')[1].split('<')[0])
            #cur_data[(str(cdate[i]).split('>')[1].split('<')[0])] = (str(currency[i]).split('>')[1].split('<')[0])

            self.cur_data.append((str(self.cdate[i]), float(str(self.currency[i]))))

        return self.cur_data, self.cdate_label, self.currency_label


cd = Cur_data()

print(cd.get_cur_data())

