import random
from api.request import *

def str_Shanse(mt5,symbole,lot):
    num1 = random.randint(0,1)
    positions=mt5.positions_get(symbol='XAUUSD')
    if len(positions) == 0 :
        if num1 == 1:
            buy(mt5,symbole,lot)
        else:
            sell(mt5,symbole,lot)

    # 1 ==buy
    # 2 ==sell

