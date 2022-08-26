import json
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import random

PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts'
URL = f'https://www.bceao.int/fr/{PATH_URL}'

class SouperData(object):
    @classmethod
    def Fetch(cls, URL):
       with requests.Session() as session:
        outcome = session.get(URL)
        outcome = outcome.text
        return outcome

class CashTool(object):
    @classmethod
    def scrapLink(cls,URL):
        return SouperData\
            .Fetch(URL)
    
    @classmethod
    def souper(cls,URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result,
            'html.parse')

    @classmethod
    def getCourse(cls, URL):
        sp = cls.souper(URL)
        sp = sp \
            .find_all(trs={
                'id': 'course'})
        if sp:
            datatable= sp[0].datatable
            return datatable
        return None
    
    
    @classmethod
    def buildcashList(cls, URL):
        sp= cls.getCourse(URL)
        if sp:
            trs = sp.find_all('tr')
            factory = [
                item.find_all('td')
                for item in trs
            ][1:]
            factory = [
                {
                    'Currency': x.string.strip(),
                    'purchase': float(y.string.strip().replace(',', '.')),
                    'Sales': float(z.string.strip().replace(',', '.')),
                }
                for (x, y, z) in factory
            ]
            return factory
        return None

    @classmethod
    def addDevise(cls, factory):
        d = ["Euro", "Dollar", "Yen"]
        for item in factory:
            item.update( {"new_devise":random.choice(d)})
        return factory

    @classmethod
    def addXofConversion(cls, factory):
        for item in factory:
            if item["new_currency"] == "Euro":
                item.update( {"XOF_conversion": item["Sales"] * 654.23 })
            elif item["new_devise"] == "Dollar":
                item.update( {"XOF_conversion": item["Sales"] * 656.50 })
            else:
                item.update( {"XOF_conversion": item["Sales"] * 4.80 })
        return factory

    @classmethod
    def main(cls):
        data = CashTool.buildcashList(URL)
        result = CashTool.addDevise(data)
        myList = CashTool.addXofConversion(result)
        
        return list
        

CashTool.main()
