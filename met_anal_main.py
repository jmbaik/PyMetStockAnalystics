import datetime
import matplotlib.pyplot as plt
import mpl_finance
from db_anal import *
import matplotlib.ticker as ticker


data_anal = get_met_anal_up("002380", "20190509", "30")
print(data_anal)

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111)


mpl_finance.candlestick2_ohlc(ax, data_anal['SPRICE'], data_anal['HPRICE'], data_anal['LPRICE'], data_anal['EPRICE'], width=0.5, colorup='r', colordown='b')

plt.show()

