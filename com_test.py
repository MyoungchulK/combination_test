import numpy as np
from itertools import combinations

arr = np.sort(np.random.choice(np.arange(1, 20), size = 5, replace = False))
#arr = np.array([ 5,  9, 10, 11, 16], dtype = int) # for test
print('ori arr:', arr)

def func(target, thres = 3):

    ## array that contains possible residuals by threshold
    thres_resi = np.arange(thres, dtype = int)
    print('possible residuals:', thres_resi) 

    ## find sum of combination of 2 that not makes threshold. 
    ## These are the patterns we are looking for from the target array combination
    tr_coms = np.asarray(list(combinations(thres_resi, 2))).astype(int)
    tr_bool = np.nansum(tr_coms, axis = 1) != thres
    tr_pats = tr_coms[tr_bool]
    tr_pat_len = len(tr_pats)
    print('combination patterns:', tr_pats)
    
    ## make combination of target array
    tg_coms = np.asarray(list(combinations(target, 2))).astype(int)
    print('combination of target array:', tg_coms)

    ## convert number in combination array to just residual 
    tg_resis = tg_coms % thres
    print('residual of combination of target array:', tg_resis)

    ## find the index of combinations that match the 'each' pattern
    tg_resi_sort = np.sort(tg_resis, axis = 1)
    pat_diff = tg_resi_sort[:, np.newaxis, :] - tr_pats[np.newaxis, :, :]
    diff_bool = np.nansum(pat_diff == 0, axis = 2) == 2 

    ## find the actual numbers that make the survived combination
    nums = []
    counts = np.full((tr_pat_len), 0, dtype = int)
    for c in range(tr_pat_len):
        num_per_pat = np.unique(tg_coms[diff_bool[:, c]])
        nums.append(num_per_pat)
        counts[c] = len(num_per_pat)
    print('numbers that found by combination patterns:', nums)
    max_idx = np.nanargmax(counts)
    print(f'maximum size: {counts[max_idx]}, corresponding array: {nums[max_idx]}')


func(arr)
