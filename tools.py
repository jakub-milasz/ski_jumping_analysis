import pandas as pd
import numpy as np


comps = pd.read_csv("data/all_comps.csv")
names = pd.read_csv("data/all_names.csv")
results = pd.read_csv("data/all_results.csv")


merged = results.merge(comps, on="id")
nh = merged[(merged['k-point'] > 75) & (merged['k-point'] < 100)]
lh = merged[(merged['k-point'] > 100) & (merged['k-point'] < 170)]
fh = merged[merged['k-point'] > 170]


def analyse_skijumper(hill, name):
    """
    hill: rodzaj skoczni. Do wyboru: 'normalne', 'duże', 'mamucie'/
    name: nazwa skoczka w konwencji: 'nazwisko imię'
    """
    if hill == 'normalne':
        data = nh
    elif hill == 'duże':
        data = lh
    elif hill == 'mamucie':
        data = fh
    codex = names[names['name'] == name].iloc[0,1]
    res = data[data['codex_x'] == codex]
    res = res[['dist', 'k-point', 'codex_y', 'place', 'hill_size_x', 'note_points']]
    # res = res.copy()
    res['coef'] = res['dist'] / res['k-point']
    res['hs-jumps'] = res['dist'] >= res['hill_size_x']
    grouped_coefs = res.groupby('place')['coef'].mean()
    # hs_jumps = res['hs-jumps'].sum()
    fav_hill = grouped_coefs.idxmax()
    return fav_hill


def analyse_overall_stats(name):
    # tutaj pozyskamy ilość skoków za hs, średnią notę za styl oraz procent skoków za punkt K
    codex = names[names['name'] == name].iloc[0,1]
    res = merged[merged['codex_x'] == codex]
    res = res[['dist', 'k-point', 'note_points', 'hill_size_x']]
    hs_jumps = np.sum(res['dist'] >= res['hill_size_x'])
    mean_notes = res['note_points'].mean()
    k_point_jumps = np.sum(res['dist'] >= res['k-point'])/res.shape[0] * 100
    return hs_jumps, mean_notes, k_point_jumps
