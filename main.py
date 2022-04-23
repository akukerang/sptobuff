from skinport import getSkinportPrice
from priceEmpireBuff import getBuffPrice


def profitcalculator(skinportPrice, buffPrice):
    afterFees = buffPrice - (buffPrice * 0.025)
    profit = afterFees - skinportPrice
    percentgain = ((profit) / skinportPrice) * 100
    print('Skinport Price: ' + str(skinportPrice))
    print('Buff Price: ' + str(buffPrice))
    print('Buff After Fees: ' + str(afterFees))
    print('Profit:' + str(profit))
    print('Percent Gain:' + str(percentgain))


def getItems(itemname):
    skinportPrice = getSkinportPrice(itemname)
    buffPrice = getBuffPrice(itemname)
    profitcalculator(float(skinportPrice), float(buffPrice))


# item name in form of AK-47 | Aquamarine Revenge (Field-Tested)
print("Enter item name: ")
itemname = str(input())
getItems(itemname)
