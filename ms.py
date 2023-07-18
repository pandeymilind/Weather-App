from bs4 import BeautifulSoup
import requests
import csv
import time

import webbrowser



def webg(url):
    id_list=[]
    result=requests.get(url)

    doc = BeautifulSoup(result.text,"html.parser")

    prt=doc.prettify()


    temprature=doc.find(class_="summaryTemperatureCompact-E1_1 summaryTemperatureHover-E1_1")
    img_temp=doc.find("img")
    temp=temprature["title"]
    return temp,img_temp["src"]


