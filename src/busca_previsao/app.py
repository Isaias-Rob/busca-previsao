"""
buscar previsao
"""
import toga
import requests
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import datetime
#import httpx

class busca_previsao(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction = COLUMN))
        today_box = toga.Box(style=Pack(direction = ROW))
        semana_box = toga.Box(style=Pack(direction = COLUMN))
        title_label = toga.Label(text=str(self.pega_cidade()),style=Pack(text_align = "center",font_family = "fantasy",font_size = 18, color = "Green"))
        hoje_label = toga.Label(text="Hoje: ", style=Pack(font_family = "monospace", color = "Grey"))
        max_label_hj = toga.Label(text=str("Maxima: ")+str(self.pega_maxima_hoje()),style=Pack(color = "Red"))
        min_label_hj = toga.Label(text=str("Minima: ")+str(self.pega_minima_hoje()),style=Pack(color = "Blue"))
        atual_label = toga.Label(text=str(self.pega_temperatura_atual())+str("º"),style=Pack(color='Green',font_size=12))
        desc_label_hj = toga.Label(text=str("                             ")+str(self.pega_description()),style=Pack(color = "Black",font_size=12))
        sep_label = toga.Label(text="\n\n\n\n")
        semana_table = toga.Table(headings=["Dia", "Max", "Min"],missing_value="Null")
        self.pega_previsao(semana_table)

        main_box.add(title_label)
        main_box.add(hoje_label)
        today_box.add(max_label_hj)
        today_box.add(min_label_hj)
        today_box.add(desc_label_hj)
        today_box.add(atual_label)
        semana_box.add(sep_label)
        semana_box.add(semana_table)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.content.add(today_box)
        self.main_window.content.add(semana_box)
        self.main_window.show()
    
    def pega_maxima_hoje(self):
        url_api = "https://api.hgbrasil.com/weather?woeid=455822"
        response = requests.get(url_api)
        #response = httpx.get(url_api)
        result = response.json() if response.status_code == 200 else None
        now = datetime.datetime.now()
        now_day_month = str(f"{now.day:02d}")+"/"+str(now.month)
        for res in result["results"]["forecast"]:
            if now_day_month == res["date"]:
                return res["max"]
        return "Nulo"
        #return result["results"]["forecast"][0]["max"] if not result == None else "Nulo"

    def pega_cidade(self):
        url_api = "https://api.hgbrasil.com/weather?woeid=455822"
        response = requests.get(url_api)
        #response = httpx.get(url_api)
        result = response.json() if response.status_code == 200 else None
        return result["results"]["city"] if not result == None else "Nulo"

    def pega_minima_hoje(self):
        url_api = "https://api.hgbrasil.com/weather?woeid=455822"
        response = requests.get(url_api)
        #response = httpx.get(url_api)
        result = response.json() if response.status_code == 200 else None
        now = datetime.datetime.now()
        now_day_month = str(f"{now.day:02d}")+"/"+str(now.month)
        for res in result["results"]["forecast"]:
            if now_day_month == res["date"]:
                return res["min"]
        return "Nulo"
    
    def pega_previsao(self, semana_table):
        url_api = "https://api.hgbrasil.com/weather?woeid=455822"
        response = requests.get(url_api)
        #response = httpx.get(url_api)
        result = response.json() if response.status_code == 200 else None
        for res in result["results"]["forecast"]:
            semana_table.data.append(res["weekday"],res["max"],res["min"])
        return

    def pega_description(self):
        url_api = "https://api.hgbrasil.com/weather?woeid=455822"
        response = requests.get(url_api)
        #response = httpx.get(url_api)
        result = response.json() if response.status_code == 200 else None
        return result["results"]["description"] if not result == None else "Nulo"

    def pega_temperatura_atual(self):
        url_api = "https://api.hgbrasil.com/weather?woeid=455822"
        response = requests.get(url_api)
        #response = httpx.get(url_api)
        result = response.json() if response.status_code == 200 else None
        return result["results"]["temp"] if not result == None else "Nulo"

def main():
    return busca_previsao()
