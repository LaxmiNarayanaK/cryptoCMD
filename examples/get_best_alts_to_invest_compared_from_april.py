from cryptocmd import CmcScraper
from tqdm import tqdm
import requests,pandas as pd

FAV_COINS = ["BTC","GALA","SOL","ADA","BNB","DOGE","SAND","OP","ATOM","NEAR","FTM","AVAX","GRT","SUSHI","AAVE","AXS","ROSE","ONE","WOO","RUNE","PYR","HNT","INJ"]
FAV_COINS_TABLE = [[coin] for coin in FAV_COINS]
USD_TO_INR = 82.21

for i in tqdm (range(len(FAV_COINS)),
			desc="LOADING>>>>>>>>>",
			ascii=False, ncols=75):
    try :
        scraper = CmcScraper(FAV_COINS[i], "01-03-2022", "01-05-2022")
        # scraper = CmcScraper(FAV_COINS[i], "01-10-2021", "01-12-2021")
        high = (float(scraper.get_dataframe()['High'].max())*USD_TO_INR)
        FAV_COINS_TABLE[i].append(round(high,4))
    except :
        FAV_COINS_TABLE[i].append(0)
    if(FAV_COINS[i]=="HNT"):
        FAV_COINS_TABLE[i].append(round(float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=HNTBUSD").json()['price'])*USD_TO_INR,4))
    else:
        FAV_COINS_TABLE[i].append(round(float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+FAV_COINS[i]+"USDT").json()['price'])*USD_TO_INR,4))

    FAV_COINS_TABLE[i].append(FAV_COINS_TABLE[i][1]/FAV_COINS_TABLE[i][2])


df = pd.DataFrame(FAV_COINS_TABLE,columns=["COIN","MINI LAST PUMP","CURRENT PRICE","x TIMES"])
print(df)
df.sort_values(by="x TIMES", ascending = False).to_excel("BETTER_TO_BUY_COINS.xlsx",index=False)





# # get raw data as list of list
# headers, data = scraper.get_data()
# print(data)

# # get data in a json format
# json_data = scraper.get_data("json")
# print(json_data)

# export the data to csv
# scraper.export("csv")