import click 
import numpy as np
from itertools import combinations

## for debugging...
#arr = np.sort(np.random.choice(np.arange(1, 20), size = 6, replace = False))
#arr = np.array([5,  9, 10, 11, 16], dtype = int) # for test
#arr = np.array([1,  3,  8, 14, 15], dtype = int) # for test

@click.command()
@click.option('-tg', '--target', default = '5,9,10,11,16')
@click.option('-tr', '--thres', default = 3, type = int)
def main(target, thres):
    if len(target) == 0: 
        print('nothing in target array')
        return
    if thres % 2 != 1 or thres < 2:
        print('please use odd number and bigger than 1 for now...')
        return

    target = np.asarray(target.split(',')).astype(int)    

    ## array that contains possible residuals by threshold
    thres_resi = np.arange(thres, dtype = int)
    print('threshold:', thres)
    print('possible residuals:', thres_resi) 

    ## find sum of combination of 2 that not makes threshold. 
    ## These are the patterns we are looking for from the target array combination
    tr_coms = np.asarray(list(combinations(thres_resi, 2))).astype(int)
    tr_bool = np.nansum(tr_coms, axis = 1) != thres
    tr_pats = tr_coms[tr_bool]
    print('combination patterns:', tr_pats)
    
    ## make combination of target array
    tg_coms = np.asarray(list(combinations(target, 2))).astype(int)
    print('original target array:', target)
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
    counts = []
    for c in range(diff_bool.shape[1]):
        num_per_pat = np.unique(tg_coms[diff_bool[:, c]])
        zero_check = num_per_pat % 3 == 0
        if np.count_nonzero(zero_check) > 1: # not satisfying solution...
            zero_val = num_per_pat[zero_check]
            for z in range(len(zero_val)):
                num_per_pat_v2 = np.append(num_per_pat[~zero_check], zero_val[z])
                nums.append(num_per_pat_v2)
                counts.append(len(num_per_pat_v2)) 
        else:
            nums.append(num_per_pat)
            counts.append(len(num_per_pat))
    print('numbers that found by combination patterns:', nums)
    print(f'maximum size: {max(counts)}')

## for debugging...
#main(arr)

if __name__ == "__main__":
    main()
