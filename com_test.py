import click 
import numpy as np
from itertools import combinations

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

    ## finds the sum of possible residual combination of 2 that not makes threshold.
    ## These are the patterns that element of subsets of target array must has 
    thres_resi = np.arange(thres, dtype = int)
    tr_coms = np.asarray(list(combinations(thres_resi, 2))).astype(int)
    tr_bool = np.nansum(tr_coms, axis = 1) != thres
    tr_pats = tr_coms[tr_bool]
    print('threshold:', thres)
    print('residual patterns:', tr_pats)
   
    ## residual of target array
    tg_resis = target % thres
    print('original target array:', target)
    print('residual target array:', tg_resis)

    ## counts how many elements in the target array are matched with the 'each' pattern
    pat_check = tg_resis[:, np.newaxis, np.newaxis] == tr_pats[np.newaxis, :, :] 
    pat_count = np.count_nonzero(pat_check, axis = (0, 2))

    ## keeps only one zero. residual zero + residual zero is dividable by thereshold.
    zero_idx = np.sort(tr_pats, axis = 1)[:, 0] == 0
    pat_count[zero_idx] -= np.count_nonzero(tg_resis == 0) - 1  
    print('size of the all subset arrays:', pat_count)
    print('maximum size:', np.nanmax(pat_count))

def main_2(target, thres):
    if len(target) == 0:
        print('nothing in target array')
        return
    if thres % 2 != 1 or thres < 2:
        print('please use odd number and bigger than 1 for now...')
        return

    thres_resi = [th for th in range(thres)]
    tr_pats = []
    for c in range(thres_resi[0], thres_resi[-1] + 1):
        for d in range(c + 1, thres_resi[-1] + 1):
            if (c + d) == thres: continue
            tr_pats.append([c, d])
    print('threshold:', thres)
    print('residual patterns:', tr_pats)

    target = list(map(int, target.split(',')))
    tg_resis = [tg % thres for tg in target]
    print('original target array:', target)
    print('residual target array:', tg_resis)

    num_zeros = tg_resis.count(0) - 1
    pat_count = []
    for pat in tr_pats:
        counts = 0
        for indi in pat:
            counts += tg_resis.count(indi)
            if indi == 0: counts -= num_zeros
        pat_count.append(counts)
    print('size of the all subset arrays:', pat_count)
    print('maximum size:', max(pat_count)) 

if __name__ == "__main__":
    main()
    #main_2('5,9,10,11,16', 3)




