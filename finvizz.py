import finviz
from Finviz_data import Finviz_data as FD

def get_finviz_data(ticker):
  print(f"get_ticker: {ticker}")
  try:
    s = finviz.get_stock(ticker)
  except:
    print("Invalid ticker")
    return -1

  news = finviz.get_news(ticker)
  stock_data = FD(
      ticker.upper(),
      s['Company'],
      s['Sector'],
      s['Industry'],
      s['Country'],
      s['Market Cap'],
      s['P/E'],
      s['Price'],
      s['Change'],
      s['Volume'],
      s['Avg Volume'],
      s['Short Float'],
      news[:4],
  )

  print(stock_data.to_string())
  return stock_data

# Make a pretty discord message
def prettify(stock_data):
    return "**:white_check_mark: Finviz Verified ** \n \
        :ticket: Ticker: `{}`\n \
        :classical_building: Company: `{}`\n \
        :fish_cake: Sector: `{}`\n \
        :hindu_temple:  Industry: `{}`\n \
        :map: Country: `{}`\n \
        :billed_cap: Market Cap: `${}` \n \
        :dollar: Price: `${}` \n \
        :chart_with_upwards_trend:  Percent Change: `{}` \n \
        :volcano:  Volume: `{}` \n \
        :cloud_tornado:  Avg Vol: `{}` \n \
        :shorts:  Short float: `{}` \n \
        :newspaper:  News: \n {} \n".format(stock_data.ticker, 
                                                stock_data.company, 
                                                stock_data.sector, 
                                                stock_data.industry, 
                                                stock_data.country, 
                                                stock_data.market_cap,
                                                stock_data.price,
                                                stock_data.percent_change,
                                                stock_data.volume,
                                                stock_data.avg_volume,
                                                stock_data.short_float,
                                                format_news(stock_data.news))

def format_news(news):
  formatted_news = ">>> "
  for article in news:
    formatted_news += article[0] + "\n" + article[1] + "\n\n"
  print(formatted_news)
  return formatted_news