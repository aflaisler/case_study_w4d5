import pandas as pd
from zipfile import ZipFile
import matplotlib.pyplot as plt


def load_data(filename):
    '''
    - input: zipfile location containing the data
    - output: pandas dataframe with subset of data with the following features:
        MachineID
        ModelID
        datasource
        YearMade
        MachineHoursCurrentMeter
        Saleprice
        fiBaseModel
        fiSecondaryDesc
        State
        ProductGroup
        Enclosure
        Ride_Control
        Stick
        Hydraulics
    - how it works: unzip the data, load data from zip file to a pandas df,
    select the features previously identify during EDA, remove missing data and outliers
    - DtypeWarning: Columns (13,39,40,41) have mixed types but we won't use them
    '''
    zf = ZipFile(filename + '.zip')
    df = pd.read_csv(filename + '.csv')
    # removing weird year - will focus on those later on if we have time
    df = df.ix[df['YearMade'] > 1900].shape
    year = year[year != 1000]

    price_v_year = df[['SalePrice', 'YearMade']]


if __main__ == '__name__':
    # Don't add the extension to the filename as it will extract zip to csv
    filename = '../data/Train'
