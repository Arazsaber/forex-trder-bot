import MetaTrader5 as mt5
import pandas as pd
from api.request import *
from stratgi_Shanse.str import *
import time

# اتصال به MT5

if not mt5.initialize(login=, password='', server=''):
    print("initialize() failed, error code =",mt5.last_error())
    quit()
symbol = 'XAUUSD'
lot = 1.0
while True:
    str_Shanse(mt5,symbol,lot)
    time.sleep(1)

# buy(mt5,"XAUUSD",1.0)
# sell(mt5,'XAUUSD',1.0)
# buy(mt5,'XAUUSD',1.0)
# # 3
# for i in range(3):
#     buy(mt5,'XAUUSD',1.0)


positions=mt5.positions_get(symbol='XAUUSD')
# print(positions[0].ticket)
# print(len(positions))
# for position in positions:
#     print(position)
# 
# for i in range(1,3):
#     close(mt5,positions[0],1.0)

# close(mt5,positions[0],1.0)
# type 0 === buy
# type 1 === sell

symbol_info = mt5.symbol_info('XAUUSD')
print(symbol_info.point)
# if symbol_info is None:
#     print(symbol, "not found, can not call order_check()")
#     mt5.shutdown()
#     quit()
 
# # if the symbol is unavailable in MarketWatch, add it
# if not symbol_info.visible:
#     print(symbol, "is not visible, trying to switch on")
#     if not mt5.symbol_select(symbol,True):
#         print("symbol_select({}}) failed, exit",symbol)
#         mt5.shutdown()
#         quit()
 



 
# send a trading request

# check the execution result
