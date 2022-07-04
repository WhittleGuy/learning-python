#!bin/bash/python

# Original data


hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Original with $5 discount
newPrices = [price - 5 for price in prices]

# Advertise haircuts that cost < $30
cheapHaircuts = [hairstyles[i]
                 for i in range(len(newPrices)) if newPrices[i] < 30]


# newList = []
# for i in range(len(newPrices)):
#   if(newPrices[i] < 30):
#     newList.append(hairstyles[i])
# print(newList)
