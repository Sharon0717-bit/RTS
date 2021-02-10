import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import datetime

def preprocess(path):
    init_date = datetime.datetime(2016, 4, 20)
    raw = pd.read_csv(path)
    categorical_cols = ['BAITFISHCode',  'AccPreventable', 'vehmake', 'CoDrvSex', 'Roadway', 'RoadwayLightConditions', 'RoadwayWeather', 'RoadwaySurface', 'Addr_Type', 'Neighborhood', 'SpeedLimitCategory']

    # fix future data leakage
    accident = raw.drop(columns=['Retraining', 'Unnamed: 0','AccTypeCodeDescr','AccSubTypeCodeDescr', 'acctype'], axis=1)
    accident['accdate'] =  (pd.to_datetime(raw['accdate']) - init_date).dt.days
    # accident = pd.get_dummies(accident, columns=categorical_cols)

    from sklearn import preprocessing
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(accident)
    accident = pd.DataFrame(scaler.transform(accident), index=accident.index, columns=accident.columns)

    return accident


if __name__ == "__main__":
    preprocess('../data/imputed_v2.csv')
