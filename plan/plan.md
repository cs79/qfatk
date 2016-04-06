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

### non-price signals
- check quantopian / books / other sources for likely useful signals
- twitter sentiment as described in paper notes
- once identified, find canned (free, hopefully) sources / places to scrape from

## data storage
- not needed for canned per se
- start with csv for scraped
- look for longer term web / db-based format to call FROM using tooling

## data tooling
- pandas, numpy, usual scientific python suspects
- custom scrapers as needed
- custom tooling to call from stored scraped data
- cron jobs to run scrapers
- batch jobs to build aggregated data series from most-granular scraped data (store these too)

## T1 algos
- start with personal ML ideas from project / notes from class / etc.
- integrate "standard" algo trader models (see books)
- start with broader time frames that could be manually tested with human trades
- integrate signals across similar time frames

## T2 algos / programs
- consider capital constraints
- consider simultaneous lookaheads and how fruitful-looking future actions may dictate restraint in present window
- consider "learning" behavior of T1 algos
