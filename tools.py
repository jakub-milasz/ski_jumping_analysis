import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


comps = pd.read_csv("data/all_comps.csv")
names = pd.read_csv("data/all_names.csv")
results = pd.read_csv("data/all_results.csv")

def find_codex(name):
    return names[names['name'] == name].iloc[0,1]


merged = results.merge(comps, on="id")
nh = merged[(merged['k-point'] > 75) & (merged['k-point'] < 100)]
lh = merged[(merged['k-point'] > 100) & (merged['k-point'] < 170)]
fh = merged[merged['k-point'] > 170]


def analyse_skijumper(hill, name):
    """
    hill: rodzaj skoczni. Do wyboru: 'normalne', 'duże', 'mamucie'
    name: nazwa skoczka w konwencji: 'nazwisko imię'
    """
    if hill == 'normalne':
        data = nh
    elif hill == 'duże':
        data = lh
    elif hill == 'mamucie':
        data = fh
    res = data[data['codex_x'] == find_codex(name)]
    res = res[['dist', 'k-point', 'codex_y', 'place', 'hill_size_x', 'note_points']]
    # res = res.copy()
    res['coef'] = res['dist'] / res['k-point']
    res['hs-jumps'] = res['dist'] >= res['hill_size_x']
    grouped_coefs = res.groupby('place')['coef'].mean()
    fav_hill = grouped_coefs.idxmax()
    return fav_hill


def analyse_overall_stats(name):
    res = merged[merged['codex_x'] == find_codex(name)]
    res = res[['dist', 'k-point', 'note_points', 'hill_size_x', 'wind_comp']]
    hs_jumps = np.sum(res['dist'] >= res['hill_size_x'])
    mean_notes = res['note_points'].mean()
    average_comp = res['wind_comp'].mean()
    return hs_jumps, mean_notes, average_comp


def plot_histogram(name, dist):
    plt.hist(dist, bins=20)
    plt.title(f"Rozkład odległości uzyskanych przez skoczka {name}")
    plt.show()