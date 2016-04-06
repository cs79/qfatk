# imports
import time
import urllib
import os

## TODO:
## error handling if source unavailable

# manually define tickers of interest
tickers = ['AAPL', 'DGS', 'DTN', 'EWJ', 'FNCL', 'FTEC', 'IBB', 'IVV', 'IXJ', 'JXI', 'ONEQ', 'SPX', 'QQQ', 'VEU', 'VGT', 'VTI']

# define function to pull arbitrary ticker data:
def get_tickers(tickers, wait=1, dest='tickerdata/'):
    if type(tickers) == str:
        tickers = tickers.split()
    dest = dest
    for ticker in tickers:
        # create url string for Google Finance API:
        turl  = 'http://www.google.com/finance/getprices?i=60&p=20d&f=d,o,h,l,c,v&df=cpct&q=' + str(ticker)

        # set destination dir; create if doesn't exist
        tickerdest = dest + str(ticker) + '/'
        if not os.path.exists(tickerdest):
            os.makedirs(tickerdest)

        # set file name
        now = str(time.ctime())
        fname = str(ticker) + '_' + now[4:7] + '_' + now[8:10] + '_' + now[-4:] + '.txt'

        # request data & save to destfile; overwriting is not an issue as we always want latest
        urllib.urlretrieve(turl, tickerdest + fname)
        # notify
        print('Fetched ' + ticker + ' data to file: ' + dest + ' at ' + now[11:19])
        # sleep if specified to not overload API
        time.sleep(wait)


# run loop periodically to fetch ticker data:
get_tickers(tickers)
