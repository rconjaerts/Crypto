import pandas as pd
import numpy as np

# variables
seq_len = 10
train_size = 0.8

def create_training_test_set(filename, symbol, size, p):
    # read csv data, and only keep bitcoin close prices which will be our target
    data = pd.read_csv(filename)
    a = data.loc[data['symbol'] == symbol, 'close'].values

    # we remove the trend by subtracting the previous value
    a = [x-a[i-1] for x in a]

    complete_set = [a[i:i+size] for i, val in enumerate(a) if i < len(a)-size]
    cutoff = int(np.floor(len(complete_set)*p))
    train_X = complete_set[:cutoff]
    train_y = a[1:cutoff+1]
    test_X = complete_set[cutoff:]
    test_y = a[cutoff+1:]

    return train_X, train_y, test_X, test_y