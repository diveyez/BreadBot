class Finviz_data:
    # Ticker, Company, Sector, Industry, Country, Market Cap, P/E, Price, % change, Volume, short float, Avg Volume
    def __init__(self, ticker, company, sector, industry, country, market_cap, pe, price, percent_change, volume, avg_volume, short_float, news):
        self.ticker = ticker
        self.company = company
        self.sector = sector
        self.industry = industry
        self.country = country
        self.market_cap = market_cap
        self.pe = pe
        self.price = price
        self.percent_change = percent_change
        self.volume = volume
        self.avg_volume = avg_volume
        self.short_float = short_float
        self.news = news

    def to_string(self):
        return {
        'ticker': self.ticker, 
        'company': self.company, 
        'industry': self.industry,
        'country': self.country,
        'market_cap': self.market_cap,
        'P/E': self.pe,
        'price': self.price,
        'percent_change': self.percent_change,
        'volume': self.volume,
        'avg_volume': self.avg_volume,
        'short_float': self.short_float,
        'news': self.news
        }

def convert_timesstamp_to_CST(ts):
    hour = int(ts.split("T")[1].split("+")[0].split(":")[0]) - 5
    cst_timestamp = str(hour) + ":" + str(ts.split("T")[1].split("+")[0].split(":")[1:2][0])
    return cst_timestamp