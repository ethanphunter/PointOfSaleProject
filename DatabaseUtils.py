from Database import Database
from random import randint


db = Database()


def moneyMadeFromProduct(productId):
    productBuyPrice = db.getById(productId)[0][2]
    productSellPrice = db.getById(productId)[0][3]
    howManySold = db.totalItemsSoldFromProductId(productId)[0][0]
    howManyBought = db.totalItemsBoughtFromProductId(productId)[0][0]
    boughtAmount = howManyBought * productBuyPrice
    soldAmount = howManySold * productSellPrice
    profit = soldAmount - boughtAmount
    return profit


def newCustomer(customerName, customerEmail):
    db.writeEmailToDatabase(customerName, customerEmail)

def newTransaction(paymentMethod,paymentAmount,itemsPurchasedList):
    db.insertNewTransaction(randint(0,1000000),paymentMethod,paymentAmount,listToString(itemsPurchasedList))

def listToString(itemsPurchasedList):
    newString = ""
    for item in itemsPurchasedList:
        newString = newString + ", " + item
    return newString

def createSale(productId, newPrice):
    db.createSale(productId, newPrice)


def generateReport():
    profitString = "productId, Name, profitOfItem \n"
    productIds = db.getAllProductIds()
    for t in productIds:
        for productId in t:
            item = db.getById(productId)
            profit = moneyMadeFromProduct(productId)
            profitString = profitString + str(productId) + ", " + str(item[0][0]) + ", " + str(profit) + "\n"
    print(profitString)
    return profitString

def purchasedItems(productId,howManyPurchased):
    db.updateInventoryLog(productId,howManyPurchased)
