from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.branch import concatenateList
import pandas as pd

def toDataFrame():
    dataCsv = CsvFactory.main()
    dataJson = JsonFactory.main()
    dataHtml = HtmlFactory.main()
    globalData = dataCsv + dataJson + dataHtml
    data = pd.DataFrame.from_dict(globalData, orient = 'columns')
    return data


if __name__ == '__main__':
    print(Utils.divider())
    print(JsonFactory.main())
    print('\n')
    print(Utils.divider())
    print(CsvFactory.main())
    print('\n')
    print(Utils.divider())
    print(HtmlFactory.main())
    print('\n')
    print(concatenateList.concatenate(HtmlFactory.main(), CsvFactory.main(), JsonFactory.main() ))