class ShortSqueezeData:
    # Ticker, Company, Short Interest Ratio, Short percent of Float, Short % increase/Decrease, Short Interest (Current), Short Interest (Prior), Shares Float
    def __init__(self, ticker, company, shInterestRatio, shFloat, shPercent, shInterestCurrent, shInterestPrior, shFloatData):
        self.ticker = ticker
        self.company = company
        self.shInterestRatio = shInterestRatio
        self.shFloat = shFloat
        self.shPercent = shPercent
        self.shInterestCurrent = shInterestCurrent
        self.shInterestPrior = shInterestPrior
        self.shFloatData = shFloatData

    def to_string(self):
        return {
            'ticker': self.ticker,
            'company': self.company,
            'Short Interest Ratio': self.shInterestRatio,
            'Short Percent of Float': self.shFloat,
            'Short % Increase/Decrease': self.shPercent,
            'Short Interest (Current)': self.shInterestCurrent,
            'Shares Float': self.shFloatData,
            'Short Interest (Prior)': self.shInterestPrior,
        }


def convert_timesstamp_to_CST(ts):
    hour = int(ts.split("T")[1].split("+")[0].split(":")[0]) - 5
    cst_timestamp = str(hour) + ":" + str(ts.split("T")
                                          [1].split("+")[0].split(":")[1:2][0])
    return cst_timestamp
