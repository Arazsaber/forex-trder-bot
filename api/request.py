# import MetaTrader5 as mt5

# buy_def
def buy(mt5,symbol,lot):
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    deviation = 20
    sl = price - 0.5
    tp = price + 0.5
    request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    # "sl": price - 100 * point,
    # "tp": price + 100 * point,
    "sl": sl,
    "tp": tp,
    # "deviation": deviation,
    # "magic": 234000,
    "comment": "python script open",
    # "type_time": mt5.ORDER_TIME_GTC,
    # "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    result = mt5.order_send(request)
    print('BUY: ',result)


# sell_def
def sell(mt5,symbol,lot,):
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).bid
    deviation = 20
    sl = price + 0.5
    tp = price - 0.5
    request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "price": price,
    "sl": sl,
    "tp": tp,
    # "sl": price - 100 * point,
    # "tp": price + 100 * point,
    # "deviation": deviation,
    # "magic": 234000,
    "comment": "python script open",
    # "type_time": mt5.ORDER_TIME_GTC,
    # "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    result = mt5.order_send(request)
    print('SELL: ',result)


# close position
def close(mt5,info,lot):
    ticket=info.ticket
    if info.type == 0:
        price = mt5.symbol_info_tick(info.symbol).bid
        type_p = mt5.ORDER_TYPE_SELL
    else:
        price=mt5.symbol_info_tick(info.symbol).ask
        type_p = mt5.ORDER_TYPE_BUY

    deviation=20
    request={
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": info.symbol,
        "volume": lot,
        "type": type_p,
        "position": ticket,
        "price": price,
        "deviation": deviation,
        # "magic": 234000,
        "comment": "python script close",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    # send a trading request
    result=mt5.order_send(request)
    print('closr: ',result)