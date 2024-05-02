import click
import numpy as np 
from itertools import combinations

@click.command()
@click.option('-tg', '--target', default = '1,8')
def main(target):

    tg_param = list(map(int, target.split(',')))
    com = []
    for c in range(tg_param[0], tg_param[1] + 1):
        for d in range(tg_param[0], tg_param[1] + 1):
            if c >= d: continue 
            com.append([c, d])
    print(com)
    print(len(com))       
 

def main_2(target):

    tg_param = list(map(int, target.split(',')))
    com = []
    for c in range(tg_param[0], tg_param[1] + 1):
        for d in range(c + 1, tg_param[1] + 1):
            com.append([c, d])
    print(com)
    print(len(com))

def main_3(target):

    tg_param = list(map(int, target.split(',')))
    tg_range = np.arange(tg_param[0], tg_param[1] + 1, dtype = int)
    com = list(map(list, combinations(tg_range, 2)))
    print(com)
    print(len(com))

"""
def main_4(target, thres):

    if thres == 0: return [[]]

    tg_param = list(map(int, target.split(',')))
    com = []
    for c in range(tg_param[1] - tg_param[0] + 1):
         
        m = c
        remLst = lst[i + 1:]
         
        remainlst_combo = n_length_combo(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])
"""

if __name__ == "__main__":
    #main()
    #main_2('1,8')
    main_3('1,8')
    #main_4('1,8', 2)
