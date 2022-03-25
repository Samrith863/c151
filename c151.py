from tkinter import *
root=Tk()
root.title("Sales Application")
root.geometry("400x400")
root.configure(background="blue")
month=("january","febuary","march","april","may","june","july","august","september","october","november","december")
profit=(22000,97000,35000,67000,52000,27000,46000,70000,148000,352000,75000,88000)
label_month=Label(root)
label_profit=Label(root)
label_max_profit=Label(root)
label_min_profit=Label(root)

label_month['text']="Month:"+str(month)
label_profit['text']="Profit:"+str(profit)
def showMonthMaxProfit():
    max_profit=max(profit)
    max_profit_index=profit.index(max_profit)
    max_profit_month=month[max_profit_index]
    label_max_profit['text']="Maximum Profit of "+str(max_profit)+" In the Month of "+str(max_profit_month)
    
    
def showMonthMinProfit():
    min_profit=min(profit)
    min_profit_index=profit.index(min_profit)
    min_profit_month=month[min_profit_index]
    label_min_profit['text']="Minimum Profit of "+str(min_profit)+" In the Month of "+str(min_profit_month)
    

btn_month_max=Button(root,text="Show Month of Max Profit",bg="black",fg="white",command=showMonthMaxProfit)
btn_month_min=Button(root,text="Show Month of Min Profit",bg="black",fg="white",command=showMonthMinProfit)

btn_month_max.place(relx=0.5,rely=0.4,anchor=CENTER)
btn_month_min.place(relx=0.5,rely=0.6,anchor=CENTER)
label_max_profit.place(relx=0.5,rely=0.5,anchor=CENTER)
label_min_profit.place(relx=0.5,rely=0.7,anchor=CENTER)
label_month.place(relx=0.5,rely=0.2,anchor=CENTER)
label_profit.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()

