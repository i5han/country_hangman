import pandas as pd
import operator
import re


def get_counts(list):
    counts = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
        ' ': 0,
        '\'': 0
    }
    for country in list:
        country_chars = ''.join(set(country.lower()))
        # country_chars = country.lower()
        for c in country_chars:
            counts[c] += 1

    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_counts


def filter_list(chars, skip):
    n_data = []
    for country in data.country:
        country = country.lower()
        if (re.match(chars, country) is not None) & char_is_not_present(country, skip):
            n_data.append(country)

    return n_data


def char_is_not_present(country, char):
    for c in country:
        if c in char:
            return False

    return True


def find_closest(count_list, val):
    minimum = 1000
    min_char = 'NA'
    for char, count in count_list:
        diff = abs(count - val)
        if diff < minimum:
            minimum = diff
            min_char = char
    return min_char


def find_highest(count_list):
    return count_list[0]


data = pd.read_csv('countries.csv', header=0)
# data = pd.read_csv('countries_ns.csv', header=0)

fil_list = filter_list('...n..r', 'tl')
char_counts = get_counts(fil_list)
half = len(fil_list) / 2
closest = find_closest(char_counts, half)
# highest = find_highest(char_counts)

# print(char_counts)
print(len(fil_list))
# print(half)
print(fil_list)
print(closest)
