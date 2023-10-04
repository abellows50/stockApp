import requests

def extractPrice(html):
  numClass = 'BNeawe iBp4i AP7Wnd">'
  start = html.find(numClass) + len(numClass)
  start = html.find(numClass,start) + len(numClass)
  html = html[start:]
  end = html.find("<")
  num = html[:end]
  while "," in num:
    num = num.replace(",","")
  return float(num)

def extractCurrency(html):
  cur = "Currency in "
  start = html.find(cur) + len(cur)
  end = html.find("<",start)
  cur = html[start:end-3]
  return cur
  
def makeSearch(stock):
  stock = stock.replace(" ","+")
  url = f"https://www.google.com/search?channel=fs&client=ubuntu&q={stock}+stock"
  search = requests.get(url)
  try:
    return (extractPrice(search.text), extractCurrency(search.text))
  except:
    return False


def stocks(stockList,startName):
  matches = []
  for stock in stockList:
    if startName.upper() in stock.upper():
      matches.append(stock)
  return matches

# x = makeSearch("AMZN")
# print(x)