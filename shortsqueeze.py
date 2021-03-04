import requests
from bs4 import BeautifulSoup
from ShortSqueezeData import ShortSqueezeData as SD


def get_shortSqueeze_data(ticker):
    x = requests.get(f'https://shortsqueeze.com/?symbol={ticker.upper()}')
    response = x.content
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find_all('table')
    company = table[10].select('table table table')[
        9].select('td')[0].get_text().strip()
    if (company == 'Not Available - Try Again'):
        print("Ticker Data Not Available")
        return -1
    else:
        try:
            ticker = table[10].select('table table table')[
                9].select('td')[2].get_text().strip()
            shInterestRatio = table[10].select('table table table')[
                10].select('td')[5].get_text().strip()
            shFloat = table[10].select('table table table')[10].select('td')[
                7].get_text().strip().replace(" ", "")
            shPercent = table[10].select('table table table')[
                10].select('td')[9].get_text().strip()
            shInterestCurrent = table[10].select('table table table')[10].select('td')[
                11].get_text().strip()
            shFloatData = table[10].select('table table table')[10].select('td')[
                13].get_text().strip()
            shInterestPrior = table[10].select('table table table')[10].select('td')[
                15].get_text().strip()

        except:
            print("Data Error")
            return -1

    data = SD(ticker.upper(), company, shInterestRatio, shFloat,
              shPercent, shInterestCurrent, shInterestPrior, shFloatData)
    print(data.to_string())
    return data


def prettify(data):
    return f"**:white_check_mark: Short Squeeze ** \n \
        :ticket: Ticker: {data.ticker}\n \
        :classical_building: Company: {data.company}\n \
        :arrow_down: Short Interest Ratio: {data.shInterestRatio}\n \
        :hindu_temple:  Short Percent of Float: {data.shFloat}\n \
        :scales: Short % Increase/Decrease: {data.shPercent}\n \
        :dollar: Short Interest (Current): {data.shInterestCurrent} \n \
        :dollar: Shares Float: {data.shFloatData} \n \
        :clock1: Short Interest (Prior): {data.shInterestPrior} \
        \n"
