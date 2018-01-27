import pandas as pd
import numpy as np

# variables
seq_len = 10
train_size = 0.8

def create_training_test_set(filename, symbol, size, p):
    # read csv data, and only keep bitcoin close prices which will be our target
    data = pd.read_csv(filename)
    a = data.loc[data['symbol'] == symbol, 'close'].values

    complete_set = [a[i:i+size] for i, val in enumerate(a) if i < len(a)-size]
    cutoff = int(np.floor(len(complete_set)*p))
    train = complete_set[:cutoff]
    test = complete_set[cutoff:]

    np.savetxt("./data/train.csv", train, delimiter=",")
    np.savetxt("./data/test.csv", test, delimiter=",")

create_training_test_set('./data/crypto_markets.csv', 'BTC', seq_len, train_size)