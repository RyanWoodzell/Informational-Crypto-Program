import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
class cryptoInfo:
  #establish class
  def __init__(self):

    #Key for API access
    self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    self.parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }

    self.headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '447f0566-705b-4c69-b4f4-ebeab68ffb1e',
    }

    self.session = Session()
    self.session.headers.update(self.headers)

    try:
      self.response = self.session.get(self.url, params=self.parameters)
      self.data = json.loads(self.response.text)
      print(self.data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

  def findCrypto(self, name):
    #function that finds specific cryptocurrency based off name
    found=0
    for key in self.data['data']:
      crypto=key.get('name')
      #if crypto exists, will fetch specific data about a specified cryptocurrency
      if crypto.lower()== name.lower():

        #updates found variable if crypto is found
        found=1
        print (key.get('name'), " ", "Abbreviation: ", " ", key.get('symbol'))
        priceInfo=key.get('quote')

        #printing of data
        print("Price: ", priceInfo['USD']['price'],"Dollars.\nLast Hour Percent Change: ", priceInfo['USD']['percent_change_1h'],"\nDaily Percent Change: ", priceInfo['USD']['percent_change_24h'], "\nPercent Change This Week: ", priceInfo['USD']['percent_change_7d'], "\nThree Month Percent Change: ", priceInfo['USD']['percent_change_90d'])
        if key.get('infinite_supply')==False:
          print(name, " does not have an infinite supply.")
        elif key.get('infinite_supply')==True:
          print("There is an infinite supply of ", name)
    
    #if cryptocurrency does not exist
    if found==0:
      print("This Cryptocurrency does not exist.")
  
  def bubbleSortLow(self, arrayNames, arrayValue):
    n=len(arrayNames)
    for i in range(n-1):
        for j in range(0, n-i-1):
          if arrayValue[j] > arrayValue[j+1]:
            arrayValue[j], arrayValue[j+1] = arrayValue[j+1], arrayValue[j]
            arrayNames[j], arrayNames[j+1] = arrayNames[j+1], arrayNames[j]
    return [arrayNames, arrayValue]

  def bubbleSortHigh(self, arrayNames, arrayValue):
    n=len(arrayNames)
    for i in range(n-1):
        for j in range(0, n-i-1):
          if arrayValue[j] < arrayValue[j+1]:
            arrayValue[j], arrayValue[j+1] = arrayValue[j+1], arrayValue[j]
            arrayNames[j], arrayNames[j+1] = arrayNames[j+1], arrayNames[j]
    return [arrayNames, arrayValue]
  
  def findHighestDailyChange(self):

    #necessary fields
    pctChange=[]
    names=[]
    index=0
    b=1

    #print seperation
    print("="*20)

    #takes the names and percent change and formats them into a list
    for key in self.data['data']:
      priceInfo=key.get('quote')
      pctChange.append(priceInfo['USD']['percent_change_24h'])
      names.append(key.get('name'))

    #bubble sorts the list from highest to lowest
    sorted = self.bubbleSortHigh(names,pctChange)
    pctChange = sorted[1]
    names=sorted[0]

    #prints the top 5 highest percent changes
    while index<5:
      print(b,".", names[index], " ", pctChange[index])
      index+=1
      b+=1
  
  def findLowestDailyChange(self):

    #necessary fields
    pctChange=[]
    names=[]
    index=0
    b=1

    #print seperation
    print("="*20)

    #takes the names and percent change and formats them into a list
    for key in self.data['data']:
      priceInfo=key.get('quote')
      pctChange.append(priceInfo['USD']['percent_change_24h'])
      names.append(key.get('name'))
    n=len(pctChange)

    #bubble sorts the lists from lowest to highest
    sorted = self.bubbleSortLow(names,pctChange)
    pctChange = sorted[1]
    names=sorted[0]
    #prints the 5 lowest percent changes
    while index<5:
      print(b,".", names[index], " ", pctChange[index])
      index+=1
      b+=1
      
  def findHighest90dChange(self):
      
      #necessary fields
      pctChange=[]
      names=[]
      index=0
      b=1

      #print seperation
      print("="*20)

      #takes the names and percent change and formats them into a list
      for key in self.data['data']:
        priceInfo=key.get('quote')
        pctChange.append(priceInfo['USD']['percent_change_90d'])
        names.append(key.get('name'))

      #bubble sorts the list from highest to lowest
      sorted = self.bubbleSortHigh(names,pctChange)
      pctChange = sorted[1]
      names=sorted[0]
      #prints the top 5 highest percent changes
      while index<5:
        b=1
        print(b,".", names[index], " ", pctChange[index])
        index+=1
        b+=1

  def findLowest90dChange(self):
      
      #necessary fields
      pctChange=[]    
      names=[]
      index=0
      b=1

      #print seperation
      print("="*20)

      #takes the names and percent change and formats them into a list
      for key in self.data['data']:
        priceInfo=key.get('quote')
        pctChange.append(priceInfo['USD']['percent_change_90d'])
        names.append(key.get('name'))
      n=len(pctChange)

      #bubble sorts the list from lowest to highest
      sorted = self.bubbleSortLow(names,pctChange)
      pctChange = sorted[1]
      names=sorted[0]
      
      #prints the top 5 lowest percent changes
      while index<5:
        print(b,".", names[index], " ", pctChange[index])
        index+=1
        b+=1