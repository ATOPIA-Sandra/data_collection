import requests
import random
import pandas as pd
from bceao import CashTool

URL = 'https://restcountries.com/v2/all'


class SouperData(object):
    @classmethod
    def jsonFetch(cls, URL):
        with requests.Session() as session:
            outcome = session.get(URL)
            outcome = outcome.json()
            return outcome

class CountryFetch(object):
    @classmethod
    def getRequest(cls, URL):
        return SouperData \
            .jsonFetch(URL)

    @classmethod
    def getCountryName(cls, URL):
        jsonCountries = cls.getRequest(URL)
        branch = [
            [item['name'], item['flag']] 
            for item in jsonCountries
            ]
        return branch

    @classmethod
    def addCountry(cls, branch):
        countries = cls.getCountryName(URL)
        
        for item in branch:
            random_country = random.choice(countries)
            item.update( {'Country': random_country[0], 'Flag': random_country[1]})
        return branch   

    @classmethod
    def main(cls):
        data = CashTool.main()

        result1 = CountryFetch.addCountry(data)

        df=pd.DataFrame(result1)
        print(df)

        return result1

CountryFetch.main()
