
#
# tooling for stitching together time series data files
# specific functions for Google Finance API data format
#
# TODO:
# fix logic in stitcher to account for dupes when merging across overlapping files
# add docstrings, fix imports, fix references to conversion functions
#


# function to convert timestamps from Unix Epoch to local exchange time:


def convert_ts(stamp):
    '''Converts timestamps from Unix Epoch time to local time.

    Parameters
    ==========
    stamp : int
        Unix Epoch timestamp

    Returns
    =======
    converted_stamp : Pandas datetime
        Converted timestamp in local time as a Pandas datetime object
    '''
    import pandas as pd
    import time, datetime

    stamp = int(stamp)  # making sure
    converted_stamp = pd.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', \
        time.localtime(stamp)), '%Y-%m-%d %H:%M:%S')
    return converted_stamp

# Google API-specific functions


# function to convert a column of Google API formatted datetimes
def convert_google_timestamps(column):
    # converts column (array) to converted stamp
    import time, datetime
    converted = []
    for i in range(len(column)):
        if column[i][0] == 'a':
            converted.append(convert_ts(column[i][1:len(column[i])]))
        else:
            converted.append(converted[i - 1] + datetime.timedelta(minutes = \
                int(column[i])))
    return converted

# function to read in a batch of files in Google API format


def stitch_directory(filepath, max_length):
    ''' Utility to create a single dataframe from a directory of files.
    Specifically designed to work with files formatted from Google Finance API.

    Parameters
    ==========
    filepath : str
        directory where the files to be stitched together are stored
    max_length : int
        optional paramter to specify the max length of the stitched dataframe

    Returns
    =======
    stitched_df : Pandas dataframe object
    '''
    import pandas as pd
    from os import listdir
    # from nonexistent package import convert_ts, OR define within this function

    cols = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']  # API data format
    clean_cols = cols[1:]  # for returned DTI-indexed dataframe
    files = os.listdir(filepath)
    temp_df = pd.DataFrame()  # to hold intermediate data from files

    for f in files:
        current_f = pd.read_table(filepath + '/' + f, header = 6, sep = ',', \
            names = cols)
        current_f.Date = convert_google_timestamps(current_f.Date)
        temp_df.append(current_f)
        temp_df.sort_values(by = 'Date')
        '''
        there is a bug in here somewhere; doesn't like this sort
        this also has problems with duplicate dates - need to merge somehow
        '''
        if len(temp_df) > max_length:
            temp_df = temp_df[-(len(temp_df) - max_length):]  # trim down to max
        else:
            pass

    dti = pd.DateTimeIndex(temp_df.Date)
    stitched_df = pd.DataFrame(temp_df.as_matrix(columns = clean_cols), \
        index = dti, columns = clean_cols)
    return stitched_df

# the above may not work if files are not read in order - max length trimming
# could break things in current form
# append may also not be working correctly right now
