import sys
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

from stock import *
from tkinter import *
import tkinter as tk

with open('stockList.csv','r') as st:
    stockList = [x[:-1] for x in st.readlines()]

root = Tk()

root.title("Stock Tracking Application")
root.geometry("750x250")
label = Label(root,text="Search for a stock: ")
label.grid()
stockSearch = Entry(root,text="Search for a stock", width=10)
stockSearch.grid(column=1,row=0)

options=[]
theStock = StringVar()
matchingStocks = OptionMenu(root,theStock,options)
matchingStocks.grid(column=2, row=0)


def ssearch():
  stock = theStock.get()
  result = makeSearch(stock)
  if result and stock not in stockList:
    stockList.append(stock)
    with open('stockList.csv','w') as st:
      st.write("\n".join(stockList))
      
  popUp = Toplevel(root)
  popUp.title(f"{stock} Search Results")
  popUp.geometry("375x125")
  popUp.configure(bg="green")
  Label(popUp,text=f"Price: {result[0]} {result[1]}").grid()
search =Button(root,text="Search",command=ssearch)
search.grid(column=3,row=0)

last = stocks(stockList,"")
while True:
  if last != stockSearch.get():
    options=stocks(stockList,stockSearch.get())
    if options == []:
      options = [stockSearch.get()]
    matchingStocks['menu'].delete(0,'end')
    for opt in options: 
      matchingStocks['menu'].add_command(label=opt, command=tk._setit(theStock, opt))
    
  last=stockSearch.get()
  root.update_idletasks()
  root.update()
