import json
from .utils import Utils
from bs4 import BeautifulSoup


BASE_URL = 'DATA-COLLECTION-DIT/COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data
    @classmethod
    def fetchData(cls,data):
        DATA =[]
        trs = data.find_all('tr')
        for tr in trs[1::]:
            tds = tr.find_all('td')
            DATA.append(
                {
                    'name' : tds[0].text,
                    'phone' : tds[1].text,
                    'email' : tds[3].text,
                    'lonlat' : tds[3].text, 
                    'salary' : tds[4].text,
                    'age': tds[5].text   
                }
            )
        return (DATA)
    
    @classmethod
    def naming(cls,data):
        def name(x):
            x['name'] = x['name'].split(' ')
            last_name = x['name'][-1].upper()
            first_name = x['name'][0].capitalize()
            x['name'] = ' '.join([first_name, last_name])
            return x
        data = map(name, data)
        return list(data)

    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.fetchData(data)
        data = cls.naming(data)
        return data