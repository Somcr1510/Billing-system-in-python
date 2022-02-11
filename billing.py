from cgitb import text
from logging import root
from tkinter import*

root=Tk()
root.geometry("500x320")
root.minsize(500,320)
root.config(bg="cadetblue1")
root.resizable(True,True)
Label(root,text="Billing System",font="comicansms 13 bold",bg="cadetblue1",pady=15).grid(row=0,column=2)

#labels
misal=Label(root,text="Misal",pady=5,bg="deepskyblue1").grid(row=1,column=1,sticky="nswe")
samosa=Label(root,text="Samosa",pady=5,bg="royalblue1").grid(row=2,column=1,sticky="nswe")
khichadi=Label(root,text="Khichadi",pady=5,bg="deepskyblue1").grid(row=3,column=1,sticky="nswe")
vadapav=Label(root,text="Vada-Pav",pady=5,bg="royalblue1").grid(row=4,column=1,sticky="nswe")
uthapa=Label(root,text="Uthapa",pady=5,bg="deepskyblue1").grid(row=5,column=1,sticky="nswe")
udinvada=Label(root,text="Udin-vada",pady=5,bg="royalblue1").grid(row=6,column=1,sticky="nswe")
kurmapuri=Label(root,text="Kurmapuri",pady=5,bg="deepskyblue1").grid(row=7,column=1,sticky="nswe")
tea=Label(root,text="Tea",pady=5,bg="deepskyblue1").grid(row=1,column=4,sticky="nswe")
coffee=Label(root,text="Coffee",pady=5,bg="royalblue1").grid(row=2,column=4,sticky="nswe")


#extlabels
tax=Label(root,text="Tex",pady=5,padx=30,bg="mediumpurple1").grid(row=6,column=4,sticky="nswe")
total=Label(root,text="Total Bill",padx=30,pady=5,bg="slateblue1").grid(row=7,column=4,sticky="nswe")

cc=Label(root,text="@Created by Som Revankar",font="arial 8 bold",pady=5,bg="cadetblue1").grid(row=8,column=5,sticky="nswe")
#variables
misalval=IntVar()
samosaval=IntVar()
khichadival=IntVar()
vadapavval=IntVar()
uthapaval=IntVar()
udinvadaval=IntVar()
kurmapurival=IntVar()
teaval=IntVar()
coffeeval=IntVar()
total_val=IntVar()
tax_val=IntVar()

#entries
misalent=Entry(root,textvariable=misalval).grid(row=1,column=2,sticky="nswe",padx=20,pady=5)
samosaent=Entry(root,textvariable=samosaval).grid(row=2,column=2,sticky="nswe",padx=20,pady=5)
khichadent=Entry(root,textvariable=khichadival).grid(row=3,column=2,sticky="nswe",padx=20,pady=5)
vadapavent=Entry(root,textvariable=vadapavval).grid(row=4,column=2,sticky="nswe",padx=20,pady=5)
uthapaent=Entry(root,textvariable=uthapaval).grid(row=5,column=2,sticky="nswe",padx=20,pady=5)
udinvadaent=Entry(root,textvariable=udinvadaval).grid(row=6,column=2,sticky="nswe",padx=20,pady=5)
kurmapurient=Entry(root,textvariable=kurmapurival).grid(row=7,column=2,sticky="nswe",padx=20,pady=5)
teaent=Entry(root,textvariable=teaval).grid(row=1,column=5,sticky="nswe",padx=20,pady=5)
coffeeent=Entry(root,textvariable=coffeeval).grid(row=2,column=5,sticky="nswe",padx=20,pady=5)


#funcion
def make_bill():
    misalqt=int(misalval.get())
    samosaqt=int(samosaval.get())
    khichadiqt=int(khichadival.get())
    vadapavqt=int(vadapavval.get())
    uthapaqt=int(uthapaval.get())
    udinvadaqt=int(udinvadaval.get())
    kurmapuriqt=int(kurmapurival.get())
    teaqt=int(teaval.get())
    coffeeqt=int(coffeeval.get())
    total_v=(misalqt*20)+(samosaqt*10)+(khichadiqt*15)+(vadapavqt*10)+(uthapaqt*20)+(udinvadaqt*20)+(kurmapuriqt*25)+(teaqt*7)+(coffeeqt*10)
    print(total_v)
    tax_vl=total_v*0.03
    total_vl=total_v+tax_vl
    tax_val.set(tax_vl)
    total_val.set(total_vl)
    f=open('bill.txt','w')
    f.write(f"\tItem\t\tQuantity\t\tPrice\t\n")
    f.write(f"\tMisel:\t\t\t{misalqt}\t\t\t{misalqt*20}\t\n")
    f.write(f"\tSamosa:\t\t\t{samosaqt}\t\t\t{samosaqt*10}\t\n")
    f.write(f"\tKhichadi:\t\t{khichadiqt}\t\t\t{khichadiqt*15}\t\n")
    f.write(f"\tVada-Pav:\t\t{vadapavqt}\t\t\t{vadapavqt*10}\t\n")
    f.write(f"\tUthapa:\t\t\t{uthapaqt}\t\t\t{uthapaqt*20}\t\n")
    f.write(f"\tUdinvada:\t\t{udinvadaqt}\t\t\t{udinvadaqt*20}\t\n")
    f.write(f"\tKurmapuri:\t\t{kurmapuriqt}\t\t\t{kurmapuriqt*25}\t\n")
    f.write(f"\tTea:\t\t\t{teaqt}\t\t\t{teaqt*7}\t\n")
    f.write(f"\tCoffee:\t\t\t{coffeeqt}\t\t\t{coffeeqt*10}\t\n")
    f.write(f"\n\tTax:\t\t\t{tax_vl}\t\n")
    f.write(f"\n\tTotal:\t\t\t{total_vl}\t\n")
    print("FILE IS CREATED SUCCEFULLY")


#button
getbill=Button(text="Get Bill",command=make_bill,bg="steelblue1").grid(row=8,column=2,pady=10)

#anslabels
taxans=Entry(root,textvariable=tax_val).grid(row=6,column=5)
totalans=Entry(root,textvariable=total_val).grid(row=7,column=5)

root.mainloop()