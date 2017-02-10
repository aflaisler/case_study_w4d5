import pandas as pd
from zipfile import ZipFile
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


def load_data(filename):
    '''
    - input: zipfile location containing the data
    - output: pandas dataframe with subset of data with the following features:
        MachineID
        ModelID
        datasource
        YearMade
        c
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
    # selecting specific features we will work with
    keep_cols = ["MachineID", "ModelID", "datasource", "YearMade", "MachineHoursCurrentMeter", "SalePrice",
                 "fiBaseModel", "fiSecondaryDesc", "state", "ProductGroup", "Enclosure", "Ride_Control", "Stick", "Hydraulics"]
    df = df[keep_cols]
    # removing weird year - will focus on those later on if we have time
    df = df.ix[df['YearMade'] > 1900]
    # save df with missing data

    return df
    #, df_year_missing, df_machineHour_missing


def missing_data_imputation(df_train, df_with_missing_data, column_to_fill):
    '''
    - input: pandas dataframe
    - output: pandas dataframe
    - how it works: fill the df with missing data using RF trained on the df with
    data
    '''
    y = np.array(df_train.pop('MachineHoursCurrentMeter').values)
    X = np.array(df_train.values)

    # train a random forest to fill hours
    md = RandomForestRegressor()
    md.fit(X, y)
    return None


if __main__ == '__name__':
    # Don't add the extension to the filename as it will extract zip to csv
    filename = '../data/Train'
    df = load_data(filename)
