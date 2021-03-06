import pandas as pd
import csv
import numpy as np

glove_data_file = 'glove.6B/glove.6B.200d.txt'

print('Loading glove model')
words = pd.read_table(glove_data_file, sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)
print('Loaded')

norm_mean = 5.5293

composite_words = {
    'pine_tree': 'pine',
    'sweet_pepper': 'pepper',
    'maple_tree': 'maple',
    'aquarium_fish': 'fish',
    'flatfish': 'fish',
    'willow_tree': 'willow',
    'pickup_truck': 'pickup',
    'palm_tree': 'palm',
    'lawn_mower': 'mower',
    'oak_tree': 'oak',
    'streetcar': 'car'
}


def normalize_label(label):
    """Turn composite words to single words"""
    if label in composite_words:
        return composite_words[label]
    else:
        return label


def find_norm_mean():
    """Find the mean norm of the word2vec representations"""
    all_words = words.index.values
    count = .0
    norm_sum = .0

    for w in all_words:
        new_norm = np.linalg.norm(words.loc[w].as_matrix())
        norm_sum += new_norm
        count += 1
    norm_sum /= count
    return norm_sum


def find_word_vec(word):
    """Gets the word2vec representation from a word"""
    try:
        return words.loc[word].as_matrix() / norm_mean
    except:
        return None
