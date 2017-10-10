from sklearn.preprocessing import LabelBinarizer
import numpy as np
import pickle
import math
import random

random.seed(0)

print('LOADING DATA')
target_data = pickle.load(open('pickle_files/target_data.pickle', 'rb'))
len_data = len(target_data)
size_train = int(2.0*len_data/3.0)
random.shuffle(target_data)

train_data = target_data[:size_train]
test_data = target_data[size_train:]

vectorizer = pickle.load(open('pickle_files/vectorizer.pickle', 'rb'))
print('DATA LOADED')

def get_batches(data, size_batch):
    len_data = len(data)
    num_batches = math.ceil(len_data/size_batch)
    for i in range(num_batches):
        new_batch = data[i*size_batch:min(len_data, (i+1)*size_batch)]
        Xs = [b[0] for b in new_batch]
        raw_Ys = [b[1] for b in new_batch]
        Ys = vectorizer.transform(raw_Ys)
        yield [Xs, Ys]