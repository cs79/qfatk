# qfatk plan file

## needs:
- data sourcing
- data storage
- data tooling - pulling from sources / storage, common analytics
- T1 algos - signals - ML algos / others
- T2+ algos - programs

## data sourcing
### canned:
- pandas.io.data
- quantmod (maybe?)
- see what is available from quantopian packages if available outside quantopian env

### homebrew / scraped:
- google finance special url
- check bookmarks for others
- get S&P 500 list and scrape regularly
- get zero-commission Fidelity ticker list & scrape regularly
- have "master table" of tickers with columns for attribute flags (s&p500, free trade on X web platform, etc.)

### non-price signals
- check quantopian / books / other sources for likely useful signals
- twitter sentiment as described in paper notes
- once identified, find canned (free, hopefully) sources / places to scrape from

## data storage
- not needed for canned per se
- start with csv for scraped
- look for longer term web / db-based format to call FROM using tooling (mysql, hdf5, etc.)

## data tooling
- pandas, numpy, usual scientific python suspects
- custom scrapers as needed
- custom tooling to call from stored scraped data
- cron jobs to run scrapers
- batch jobs to build aggregated data series from most-granular scraped data (store these too)

## T1 features
- ohlc price data
- volume
- volatility
- computed trailing summary statistics
- physical visual movement
- "vintage" of data (as a proxy for downweighting older data - can downweight not just old, but whatever "vintage" is less useful) - scale as relative or absolute? can try both
- company fundamentals (if ticker is a company) - see where quantopian sources this data
- flags representing higher-level time series aggregates or indicators - either the indicator itself, or a derivative flag (e.g. over-/undershoot on last earnings announcement)

## T1 algos
- start with personal ML ideas from project / notes from class / etc.
- expand those models with additional T1 features not used in original prototypes
- expand to additional untested algos (ANN / Caffe, any newly available deep learning models)
- for classifiers, expand classes to ranges of directional price movement
- integrate "standard" algo trader models (see books)
- start with broader time frames that could be manually tested with human trades
- integrate signals across similar time frames

## T2 algos / programs
- consider capital constraints
- consider simultaneous lookaheads and how fruitful-looking future actions may dictate restraint in present window
- consider "learning" behavior of T1 algos
- MEASURE: score T1 models as they make predictions (can batch this end of day every day or try for near-real time)
