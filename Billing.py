import pymysql as py
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
import math
import random
root = Tk()
root.title("billing")
root.geometry("655x400")
l1 = Label(root, text="Welcome in Billing Software", padx=34, pady=34, font="comicsansms 43 bold")
l1.pack(side="top", fill=X)
def mymet():
    ##cosmetics##
     global soap_price
     global detergent_price
     global deodrants_price
     global facewash_price
     global hairgel_price
     global moisturecream_price
     global c_tax
     soap_price=Soap.get() * 10
     detergent_price=Detergent.get() * 30
     deodrants_price=Deodrants.get() * 200
     facewash_price=Facewash.get() * 80
     hairgel_price=Hairgel.get() * 100
     moisturecream_price=Moisturecream.get() * 150
     total_cosmetics_price=(soap_price + detergent_price + deodrants_price + facewash_price+
                            moisturecream_price)
     cosmetics_price.set("Rs. "+str(total_cosmetics_price))
     c_tax=total_cosmetics_price * 0.05
     cosmetics_tax.set("Rs. "+str(c_tax))

     ##grocery##
     global grainsbread_price
     global oilfat_price
     global dairyeggs_price
     global salt_price
     global meatfish_price
     global driedproduce_price
     global g_tax
     grainsbread_price=Grainsbread.get() * 200
     oilfat_price=Oilfat.get() * 300
     dairyeggs_price=Dairyeggs.get() * 70
     salt_price=Salt.get() * 80
     meatfish_price=Meatfish.get() * 250
     driedproduce_price=Driedproduce.get() * 100
     total_grocery_price = (grainsbread_price + oilfat_price + dairyeggs_price + salt_price+
                               meatfish_price + driedproduce_price)
     grocery_price.set("Rs. "+str(total_grocery_price))
     g_tax=total_grocery_price * 0.05
     grocery_tax.set("Rs. "+str(g_tax))
     ##softdrink
     global cocacola_price
     global redbull_price
     global nescafe_price
     global pepsi_price
     global tropicana_price
     global sprite_price
     global s_tax
     cocacola_price=cocacola.get() * 20
     redbull_price=redbull.get() * 300
     nescafe_price=nescafe.get() * 70
     pepsi_price=pepsi.get() * 80
     tropicana_price=tropicana.get() * 250
     sprite_price=sprite.get() * 100
     total_softdrink_price = (cocacola_price + redbull_price + nescafe_price + pepsi_price +
                            tropicana_price + sprite_price )
     softdrink_price.set("Rs. "+str(total_softdrink_price))
     s_tax=total_softdrink_price * 0.05
     softdrink_tax.set("Rs. "+str(s_tax))

     ##household
     global lamps_price
     global tableware_price
     global bottles_price
     global glassware_price
     global stoves_price
     global flask_price
     global h_tax
     global Total_bill
     lamps_price=lamps.get() * 200
     tableware_price=tableware.get() * 350
     bottles_price=bottles.get() * 70
     glassware_price=glassware.get() * 180
     stoves_price=stoves.get() * 250
     flask_price=flask.get() * 100
     total_household_price = (lamps_price + tableware_price + bottles_price + glassware_price +
                              stoves_price + flask_price)
     household_price.set("Rs. "+str(total_household_price))
     h_tax=total_household_price * 0.05
     household_tax.set("Rs. "+str(h_tax))
     Total_bill=(total_cosmetics_price + total_grocery_price + total_softdrink_price +
                total_household_price + c_tax + g_tax + s_tax + h_tax)

def welcome_bill():
    txtbox.delete('1.0',END)
    txtbox.insert(END,"\tWelcome in Bill Area \n")
    txtbox.insert(END,f"\n Bill Number: {customer_billno.get()}")
    txtbox.insert(END, f"\n Customer Name: { customer_name.get()}")
    txtbox.insert(END, f"\n Phone Number: {customer_phone.get()}")
    txtbox.insert(END, f"\n ************************************")
    txtbox.insert(END, f"\n Product\t\tQuantity\t\tPrice")
    txtbox.insert(END,f"\n *************************************")
def bill_area():
    welcome_bill()
    ##cosmetics
    if Soap!=0:
        txtbox.insert(END, f"\n Soap\t\t{Soap.get()}\t\t{soap_price}")
    if Detergent != 0:
        txtbox.insert(END, f"\n Detergent\t\t{Detergent.get()}\t\t{detergent_price}")
    if Deodrants != 0:
        txtbox.insert(END, f"\n Deodrants\t\t{Deodrants.get()}\t\t{deodrants_price}")
    if Facewash != 0:
        txtbox.insert(END, f"\n Facewash\t\t{Facewash.get()}\t\t{facewash_price}")
    if Hairgel != 0:
        txtbox.insert(END, f"\n Hairgel\t\t{Hairgel.get()}\t\t{hairgel_price}")
    if Moisturecream != 0:
        txtbox.insert(END, f"\n Moisturecream\t\t{Moisturecream.get()}\t\t{moisturecream_price}")
     ##grocery
    if Grainsbread!=0:
        txtbox.insert(END, f"\n Grainsbread\t\t{Grainsbread.get()}\t\t{grainsbread_price}")
    if Oilfat != 0:
        txtbox.insert(END, f"\n Oilfat\t\t{Oilfat.get()}\t\t{oilfat_price}")
    if Dairyeggs != 0:
        txtbox.insert(END, f"\n Dairyeggs\t\t{Dairyeggs.get()}\t\t{dairyeggs_price}")
    if Salt != 0:
        txtbox.insert(END, f"\n Salt\t\t{Salt.get()}\t\t{salt_price}")
    if Meatfish != 0:
        txtbox.insert(END, f"\n Meatfish\t\t{Meatfish.get()}\t\t{meatfish_price}")
    if Driedproduce != 0:
        txtbox.insert(END, f"\n Driedproduce\t\t{Driedproduce.get()}\t\t{driedproduce_price}")
    ##softdrink##
    if cocacola!=0:
        txtbox.insert(END, f"\n cocacola\t\t{cocacola.get()}\t\t{cocacola_price}")
    if redbull != 0:
        txtbox.insert(END, f"\n redbull\t\t{redbull.get()}\t\t{redbull_price}")
    if nescafe != 0:
        txtbox.insert(END, f"\n nescafe\t\t{nescafe.get()}\t\t{nescafe_price}")
    if glassware != 0:
        txtbox.insert(END, f"\n glassware\t\t{glassware.get()}\t\t{glassware_price}")
    if tropicana != 0:
        txtbox.insert(END, f"\n tropicana\t\t{tropicana.get()}\t\t{tropicana_price}")
    if sprite != 0:
        txtbox.insert(END, f"\n sprite\t\t{sprite.get()}\t\t{sprite_price}")
    ##household
    if lamps!=0:
        txtbox.insert(END, f"\n lamps\t\t{lamps.get()}\t\t{lamps_price}")
    if tableware != 0:
        txtbox.insert(END, f"\n tableware\t\t{tableware.get()}\t\t{tableware_price}")
    if bottles != 0:
        txtbox.insert(END, f"\n bottles\t\t{bottles.get()}\t\t{bottles_price}")
    if pepsi != 0:
        txtbox.insert(END, f"\n pepsi\t\t{pepsi.get()}\t\t{pepsi_price}")
    if stoves != 0:
        txtbox.insert(END, f"\n stoves\t\t{stoves.get()}\t\t{stoves_price}")
    if flask != 0:
        txtbox.insert(END, f"\n flask\t\t{flask.get()}\t\t{flask_price}")
    txtbox.insert(END, f"\n **************************************")
    txtbox.insert(END, f"\n Total Bill: \t\t\tRs. {Total_bill}")
def clear_data():
    Soap.set(0)
    Detergent.set(0)
    Deodrants.set(0)
    Facewash.set(0)
    Hairgel.set(0)
    Moisturecream.set(0)
    ###grocery variable
    Grainsbread.set(0)
    Oilfat.set(0)
    Dairyeggs.set(0)
    Salt.set(0)
    Meatfish.set(0)
    Driedproduce.set(0)
    ##softdrink variable
    cocacola.set(0)
    redbull.set(0)
    nescafe.set(0)
    pepsi.set(0)
    tropicana.set(0)
    sprite.set(0)
    ###household###
    lamps.set(0)
    tableware.set(0)
    bottles.set(0)
    glassware.set(0)
    stoves.set(0)
    flask.set(0)
    ##prices
    grocery_price.set("")
    cosmetics_price.set("")
    softdrink_price.set("")
    household_price.set("")
    ##taxes##
    cosmetics_tax.set("")
    grocery_tax.set("")
    softdrink_tax.set("")
    household_tax.set("")
    ##customer
    customer_name.set("")
    customer_phone.set("")
    customer_billno.set("")
    a = random.randint(1100, 9999)
    customer_billno.set(str(a))
    customer_search.set("")
    welcome_bill()
def exit_bill():
    op=messagebox.askyesno("Exit","exit")
    root.destroy()
def cosmo():
    top=Toplevel()
    top.title("Billing System")
    # customer details
    global Soap
    global Detergent
    global Deodrants
    global Facewash
    global Hairgel
    global Moisturecream

    global Grainsbread
    global Oilfat
    global Dairyeggs
    global Salt
    global Meatfish
    global Driedproduce

    global cocacola
    global redbull
    global nescafe
    global pepsi
    global tropicana
    global sprite

    global lamps
    global tableware
    global bottles
    global glassware
    global stoves
    global flask
    global cosmetics_price
    global grocery_price
    global softdrink_price
    global household_price


    global cosmetics_tax
    global grocery_tax
    global softdrink_tax
    global household_tax


    global customer_billno
    global customer_phone
    global customer_name
    global customer_search
    ##cosmeticsvariable##
    Soap=IntVar()
    Detergent=IntVar()
    Deodrants=IntVar()
    Facewash=IntVar()
    Hairgel=IntVar()
    Moisturecream=IntVar()
    ###grocery variable
    Grainsbread=IntVar()
    Oilfat=IntVar()
    Dairyeggs=IntVar()
    Salt=IntVar()
    Meatfish=IntVar()
    Driedproduce=IntVar()
    ##softdrink variable
    cocacola=IntVar()
    redbull=IntVar()
    nescafe = IntVar()
    pepsi = IntVar()
    tropicana = IntVar()
    sprite = IntVar()
    ###household###
    lamps=IntVar()
    tableware=IntVar()
    bottles=IntVar()
    glassware=IntVar()
    stoves=IntVar()
    flask=IntVar()
     ##prices
    grocery_price=StringVar()
    cosmetics_price=StringVar()
    softdrink_price=StringVar()
    household_price=StringVar()
    ##taxes##
    cosmetics_tax=StringVar()
    grocery_tax=StringVar()
    softdrink_tax=StringVar()
    household_tax=StringVar()
    ##customer
    customer_name=StringVar()
    customer_phone=StringVar()
    customer_billno=StringVar()
    a=random.randint(1100,9999)
    customer_billno.set(str(a))
    customer_search=StringVar()
    f1 = LabelFrame(top, bd=10, text="Customer Details", font=("times new roman", 15, "bold"), bg="yellow", fg="green", relief=SUNKEN)
    f1.pack(side="top",fill=X)
    custom_name = Label(f1, text="Customer Name :", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    custom_name.grid(row=0, column=0, padx=20, pady=5)
    custom_text = Entry(f1, width=10, font="comicsansms 15",textvariable=customer_name, bd=6, relief=SUNKEN)
    custom_text.grid(row=0, column=1)
    custom_phone = Label(f1, text="Customer Phone No :", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    custom_phone.grid(row=0, column=2, padx=20, pady=5)
    custom_text = Entry(f1, width=10, font="comicsansms 15 bold",textvariable=customer_phone, bd=6, relief=SUNKEN)
    custom_text.grid(row=0, column=3)
    ##cosmetics products
    f3 = LabelFrame(top, bd=10, text="Cosmetics Products", font=("times new roman", 15, "bold"), bg="yellow", fg="green", relief=SUNKEN)
    f3.place(x=4, y=105, width=350, height=305)
    c1_product1 = Label(f3, text="Soap", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    c1_product1.grid(row=0, column=0, padx=20, pady=5)
    c1_product1 = Entry(f3, width=8, font="comicsansms 15 bold",textvariable=Soap, bd=6, relief=SUNKEN)
    c1_product1.grid(row=0, column=1)
    c2_product2 = Label(f3, text="Detergent", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    c2_product2.grid(row=1, column=0, padx=20, pady=5)
    c2_product2 = Entry(f3, width=8,textvariable=Detergent, font="comicsansms 15 bold", bd=6, relief=SUNKEN)
    c2_product2.grid(row=1, column=1)
    c3_product3 = Label(f3, text="Deodrants", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    c3_product3.grid(row=2, column=0, padx=20, pady=5)
    c3_product3 = Entry(f3, width=8, font="comicsansms 15 bold",textvariable=Deodrants, bd=6, relief=SUNKEN)
    c3_product3.grid(row=2, column=1)
    c4_product4 = Label(f3, text="Face Wash", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    c4_product4.grid(row=3, column=0, padx=20, pady=5)
    c4_product4 = Entry(f3, width=8, font="comicsansms 15 bold",textvariable=Facewash, bd=6, relief=SUNKEN)
    c4_product4.grid(row=3, column=1)
    c5_product5 = Label(f3, text="Hair Gel", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    c5_product5.grid(row=4, column=0, padx=20, pady=5)
    c5_product5 = Entry(f3, width=8, font="comicsansms 15 bold",textvariable=Hairgel, bd=6, relief=SUNKEN)
    c5_product5.grid(row=4, column=1)
    c6_product6 = Label(f3, text="Moisture Cream", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    c6_product6.grid(row=5, column=0, padx=20, pady=5)
    c6_product6 = Entry(f3, width=8, font="comicsansms 15 bold", bd=6,textvariable=Moisturecream, relief=SUNKEN)
    c6_product6.grid(row=5, column=1)
    # Grocery products################
    f2 = LabelFrame(top, bd=10, text="Grocery Products", font=("times new roman", 15, "bold"), bg="yellow", fg="green", relief=SUNKEN)
    f2.place(x=350, y=105, width=325, height=305)
    g1_product1 = Label(f2, text="Grains&bread", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    g1_product1.grid(row=0, column=0, padx=20, pady=5)
    g1_product1 = Entry(f2, width=8,textvariable=Grainsbread, font="comicsansms 15 bold", bd=6, relief=SUNKEN)
    g1_product1.grid(row=0, column=1)
    g2_product2 = Label(f2, text="Oil&fat", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    g2_product2.grid(row=1, column=0, padx=20, pady=5)
    g2_product2 = Entry(f2, width=8,textvariable=Oilfat, font="comicsansms 15 bold", bd=6, relief=SUNKEN)
    g2_product2.grid(row=1, column=1)
    g3_product3 = Label(f2, text="Dairy&Eggs", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    g3_product3.grid(row=2, column=0, padx=20, pady=5)
    g3_product3 = Entry(f2, width=8,textvariable=Dairyeggs, font="comicsansms 15 bold", bd=6, relief=SUNKEN)
    g3_product3.grid(row=2, column=1)
    g4_product4 = Label(f2, text="Salt", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    g4_product4.grid(row=3, column=0, padx=20, pady=5)
    g4_product4 = Entry(f2, width=8,textvariable=Salt, font="comicsansms 15 bold", bd=6, relief=SUNKEN)
    g4_product4.grid(row=3, column=1)
    g6_product6 = Label(f2, text="Meat&fish", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    g6_product6.grid(row=5, column=0, padx=20, pady=5)
    g6_product6 = Entry(f2, width=8,textvariable=Meatfish, font="comicsansms 15 bold", bd=6, relief=SUNKEN)
    g6_product6.grid(row=5, column=1)
    g7_product7 = Label(f2, text="Dried produce", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    g7_product7.grid(row=6, column=0, padx=20, pady=5)
    g7_product7 = Entry(f2, width=8,textvariable=Driedproduce, font="comicsansms 15 bold", bd=6, relief=SUNKEN)
    g7_product7.grid(row=6, column=1)
    ###softdrink
    f4 = LabelFrame(top, bd=10, text="Softdrinks Products", font=("times new roman", 15, "bold"), bg="yellow", fg="green", relief=SUNKEN)
    f4.place(x=680, y=105, width=300, height=305)
    co1_product1 = Label(f4, text="Coca-Cola", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co1_product1.grid(row=0, column=0, padx=20, pady=5)
    co1_product1 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=cocacola, bd=6, relief=SUNKEN)
    co1_product1.grid(row=0, column=1)
    co2_product2 = Label(f4, text="Red Bull", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co2_product2.grid(row=1, column=0, padx=20, pady=5)
    co2_product2 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=redbull, bd=6, relief=SUNKEN)
    co2_product2.grid(row=1, column=1)
    co3_product3 = Label(f4, text="Nescafe", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co3_product3.grid(row=2, column=0, padx=20, pady=5)
    co3_product3 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=nescafe, bd=6, relief=SUNKEN)
    co3_product3.grid(row=2, column=1)
    co4_product4 = Label(f4, text="Pepsi", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co4_product4.grid(row=3, column=0, padx=20, pady=5)
    co4_product4 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=pepsi, bd=6, relief=SUNKEN)
    co4_product4.grid(row=3, column=1)
    co5_product5 = Label(f4, text="Tropicana", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co5_product5.grid(row=4, column=0, padx=20, pady=5)
    co5_product5 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=tropicana, bd=6, relief=SUNKEN)
    co5_product5.grid(row=4, column=1)
    co6_product6 = Label(f4, text="Sprite", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co6_product6.grid(row=6, column=0, padx=20, pady=5)
    co6_product6 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=sprite, bd=6, relief=SUNKEN)
    co6_product6.grid(row=6, column=1)
    ###Household

    f4 = LabelFrame(top, bd=10, text="Household Products", font=("times new roman", 15, "bold"), bg="yellow", fg="green", relief=SUNKEN)
    f4.place(x=985, y=105, width=290, height=305)
    co1_house1 = Label(f4, text="Lamps", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co1_house1.grid(row=0, column=0, padx=20, pady=5)
    co1_house1 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=lamps, bd=6, relief=SUNKEN)
    co1_house1.grid(row=0, column=1)
    co2_house2 = Label(f4, text="Tableware", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co2_house2.grid(row=1, column=0, padx=20, pady=5)
    co2_house2 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=tableware, bd=6, relief=SUNKEN)
    co2_house2.grid(row=1, column=1)
    co3_house3 = Label(f4, text="Bottles", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co3_house3.grid(row=2, column=0, padx=20, pady=5)
    co3_house3 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=bottles, bd=6, relief=SUNKEN)
    co3_house3.grid(row=2, column=1)
    co4_house4 = Label(f4, text="Glassware", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co4_house4.grid(row=3, column=0, padx=20, pady=5)
    co4_house4 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=glassware, bd=6, relief=SUNKEN)
    co4_house4.grid(row=3, column=1)
    co5_house5 = Label(f4, text="Stove", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co5_house5.grid(row=4, column=0, padx=20, pady=5)
    co5_house5 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=stoves, bd=6, relief=SUNKEN)
    co5_house5.grid(row=4, column=1)
    co6_house6 = Label(f4, text="Flask", font=("times new roman", 19, "bold"), bg="yellow", fg="red")
    co6_house6.grid(row=5, column=0, padx=20, pady=5)
    co6_house6 = Entry(f4, width=8, font="comicsansms 15 bold",textvariable=flask, bd=6, relief=SUNKEN)
    co6_house6.grid(row=5, column=1)
    ##Bill Area
    global txtbox
    frame = Frame(top, bd=10, relief=SUNKEN)
    frame.place(x=5, y=410, width=340, height=325)
    label = Label(frame, text="Bill Area", font="comicsansms 19 bold", bd=7, relief=GROOVE)
    label.pack()
    xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
    xscrollbar.pack(side="bottom", fill=X)
    yscrollbar = Scrollbar(frame)
    yscrollbar.pack(side="right", fill=Y)
    txtbox = Text(frame, wrap=NONE, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
    txtbox.pack()
    xscrollbar.config(command=txtbox.xview())
    yscrollbar.config(command=txtbox.yview())
    ##button frame###################################
    f5 = LabelFrame(top, bd=10, text="Bill Menu", font=("times new roman", 15, "bold"), bg="yellow", fg="green", relief=SUNKEN)
    f5.place(x=345, y=400, relwidth=1, height=250)
    l1=Label(f5,text="Total_Cosmetics_Price",font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l1.grid(row=0,column=0,padx=20,pady=1)
    e1=Entry(f5,font=("times new roman", 15, "bold"),width=15,textvariable=cosmetics_price,bd=10,relief=SUNKEN)
    e1.grid(row=0,column=1,padx=20,pady=5)
    l2 = Label(f5, text="Total_Grocery_Price", font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l2.grid(row=1, column=0, padx=20, pady=1)
    e2 = Entry(f5, font=("times new roman", 15, "bold"),textvariable=grocery_price, width=15, bd=10, relief=SUNKEN)
    e2.grid(row=1, column=1, padx=20, pady=5)
    l3=Label(f5,text="Total_Softdrink_Price",font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l3.grid(row=2,column=0,padx=20,pady=1)
    e3=Entry(f5,font=("times new roman", 15, "bold"),textvariable=softdrink_price,width=15,bd=10,relief=SUNKEN)
    e3.grid(row=2,column=1,padx=20,pady=5)
    l4 = Label(f5, text="Total_Household_Price", font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l4.grid(row=3, column=0, padx=20, pady=1)
    e4 = Entry(f5, font=("times new roman", 15, "bold"),textvariable=household_price, width=15, bd=10, relief=SUNKEN)
    e4.grid(row=3, column=1, padx=20, pady=5)
    l11 = Label(f5, text="Cosmetics_Tax", font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l11.grid(row=0, column=2, padx=20, pady=1)
    e11 = Entry(f5, font=("times new roman", 15, "bold"),textvariable=cosmetics_tax, width=15, bd=10, relief=SUNKEN)
    e11.grid(row=0, column=3, padx=20, pady=5)
    l22 = Label(f5, text="Grocery_Tax", font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l22.grid(row=1, column=2, padx=20, pady=1)
    e22 = Entry(f5, font=("times new roman", 15, "bold"),textvariable=grocery_tax, width=15, bd=10, relief=SUNKEN)
    e22.grid(row=1, column=3, padx=20, pady=5)
    l33 = Label(f5, text="Softdrink_Tax", font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l33.grid(row=2, column=2, padx=20, pady=1)
    e33 = Entry(f5, font=("times new roman", 15, "bold"),textvariable=softdrink_tax, width=15, bd=10, relief=SUNKEN)
    e33.grid(row=2, column=3, padx=20, pady=5)
    l44 = Label(f5, text="Household_Tax", font=("times new roman", 15, "bold"), bg="yellow", fg="green")
    l44.grid(row=3, column=2, padx=20, pady=1)
    e44 = Entry(f5, font=("times new roman", 15, "bold"), width=15,textvariable=household_tax, bd=10, relief=SUNKEN)
    e44.grid(row=3, column=3, padx=20, pady=5)
    f7 = LabelFrame(top, bd=10, font=("times new roman", 15, "bold"), bg="yellow", relief=SUNKEN)
    f7.place(x=345, y=645, relwidth=1, height=250)
    btn=Button(f7,text="Total",font=("times new roman", 15, "bold"), width=15, bd=10,command=mymet)
    btn.grid(row=0,column=0,padx=20,pady=5)
    btn1 = Button(f7, text="Bill",command=bill_area, font=("times new roman", 15, "bold"), width=15, bd=10)
    btn1.grid(row=0, column=1, padx=20, pady=5)
    btn2=Button(f7,text="Clear",font=("times new roman", 15, "bold"), width=15, bd=10,command=clear_data)
    btn2.grid(row=0, column=2, padx=20, pady=5)
    btn3 = Button(f7, text="Quit",command=exit_bill, font=("times new roman", 15, "bold"), width=12, bd=10)
    btn3.grid(row=0, column=3, padx=20, pady=5)
    welcome_bill()
def billing():
    f3 = LabelFrame(top, text="Cosmetics Products",fg="green")
    f3.place(x=450, y=70, width=450, height=330)
    serialno = Label(f3, text="serialno", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
    serialno.grid(row=0, column=0, padx=20, pady=5)
    Prod_Name = Label(f3, text="Prod_Name", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
    Prod_Name.grid(row=0, column=1, padx=20, pady=5)
    Rupees = Label(f3, text="Rupees", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
    Rupees.grid(row=0, column=2, padx=20, pady=5)
    b = pymysql.connect(user='root', password='Lucknow@123', host='localhost', database='cosmetics')
    mycursor = b.cursor()
    myquery = "select * from cosmetics"
    mycursor.execute(myquery)
    index = 1
    for rec in mycursor:
        Label(f3, text=rec[0], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=0)
        Label(f3, text=rec[1], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=1)
        Label(f3, text=rec[2], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=2)
        index = index + 1
    mycursor.close()
    b.close()
def submit1():
     b = py.connect(user='root', password='Lucknow@123', host='localhost', database='customer')
     str11 = text_rec.get()
     str22 = text_rec1.get()
     str33 = text_rec2.get()
     str44 = text_rec3.get()
     str55 = text_rec4.get()
     str66 = text_rec5.get()
     mycursor = b.cursor()
     myquery = "insert into customer values(%s,%s,%s,%s,%s,%s)"
     tuple = (str11, str22, str33, str44, str55, str66)
     mycursor.execute(myquery, tuple)
     b.commit()
     b.close()
     print("data inserted")
     top=Toplevel()
     title = Label(top, text="Billing Software ", font=("times new roman", 30, "bold"), bd=12,fg="green",bg="yellow",relief=SUNKEN)
     title.place(x=0, y=0, relwidth=1)
    ###########Customer details
     f3 = LabelFrame(top, text="Cosmetics Products",font=("times new roman", 15, "bold"),bg="yellow",fg="black",relief=SUNKEN,bd=12)
     f3.place(x=5, y=70, width=450, height=330)
     serialno = Label(f3, text="serialno", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     serialno.grid(row=0, column=0, padx=20, pady=5)
     Prod_Name = Label(f3, text="Prod_Name", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Prod_Name.grid(row=0, column=1, padx=20, pady=5)
     Rupees = Label(f3, text="Rupees", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Rupees.grid(row=0, column=2, padx=20, pady=5)
     b = py.connect(user='root', password='Lucknow@123', host='localhost', database='cosmetics')
     mycursor = b.cursor()
     myquery = "select * from cosmetics"
     mycursor.execute(myquery)
     index = 1
     for rec in mycursor:
                Label(f3, text=rec[0], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=0)
                Label(f3, text=rec[1], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=1)
                Label(f3, text=rec[2], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=2)
                index = index + 1
     mycursor.close()
     b.commit()
     b.close()
     f4 = LabelFrame(top, text="Grocery Products", font=("times new roman", 15, "bold"),fg="green",bg="yellow",relief=SUNKEN,bd=12)
     f4.place(x=850, y=70, width=450, height=330)
     serialno = Label(f4, text="serialno", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     serialno.grid(row=0, column=0, padx=20, pady=5)
     Prod_Name = Label(f4, text="Prod_Name", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Prod_Name.grid(row=0, column=1, padx=20, pady=5)
     Rupees = Label(f4, text="Rupees", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Rupees.grid(row=0, column=2, padx=20, pady=5)
     b = py.connect(user='root', password='Lucknow@123', host='localhost', database='grocery')
     mycursor = b.cursor()
     myquery = "select * from grocery"
     mycursor.execute(myquery)
     index = 1
     for rec in mycursor:
         Label(f4, text=rec[0], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=0)
         Label(f4, text=rec[1], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=1)
         Label(f4, text=rec[2], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=2)
         index = index + 1
     mycursor.close()
     b.commit()
     b.close()
     f5 = LabelFrame(top, text="Softdrinks Products", font=("times new roman", 15, "bold"),fg="green",bg="yellow",relief=SUNKEN,bd=12)
     f5.place(x=5, y=420, width=450, height=330)
     serialno = Label(f5, text="serialno", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     serialno.grid(row=0, column=0, padx=20, pady=5)
     Prod_Name = Label(f5, text="Prod_Name", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Prod_Name.grid(row=0, column=1, padx=20, pady=5)
     Rupees = Label(f5, text="Rupees", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Rupees.grid(row=0, column=2, padx=20, pady=5)
     b = py.connect(user='root', password='Lucknow@123', host='localhost', database='softdrinks')
     mycursor = b.cursor()
     myquery = "select * from softdrinks"
     mycursor.execute(myquery)
     index = 1
     for rec in mycursor:
           Label(f5, text=rec[0], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=0)
           Label(f5, text=rec[1], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=1)
           Label(f5, text=rec[2], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=2)
           index = index + 1
     mycursor.close()
     b.commit()
     b.close()
     f6 = LabelFrame(top, text="Household Products", font=("times new roman", 15, "bold"),fg="green",bg="yellow",bd=12,relief=SUNKEN)
     f6.place(x=850, y=420, width=450, height=330)
     serialno = Label(f6, text="serialno", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     serialno.grid(row=0, column=0, padx=20, pady=5)
     Prod_Name = Label(f6, text="Prod_Name", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Prod_Name.grid(row=0, column=1, padx=20, pady=5)
     Rupees = Label(f6, text="Rupees", font=("times new roman", 19, "bold"),bg="yellow",fg="black")
     Rupees.grid(row=0, column=2, padx=20, pady=5)
     b = py.connect(user='root', password='Lucknow@123', host='localhost', database='household')
     mycursor = b.cursor()
     myquery = "select * from household"
     mycursor.execute(myquery)
     index = 1
     for rec in mycursor:
        Label(f6, text=rec[0], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=0)
        Label(f6, text=rec[1], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=1)
        Label(f6, text=rec[2], font=("times new roman", 19, "bold"),bg="yellow",fg="black").grid(row=index, column=2)
        index = index + 1
     mycursor.close()
     b.commit()
     b.close()

     btn=Button(top, text="Next",font=("times new roman", 19, "bold"), bg="black", fg="white", command=cosmo)
     btn.place(x=600,y=640,width=165,height=50)


def showlog():
    b = py.connect(user='root', password='Lucknow@123', host='localhost', database='managementsystemdb')
    usertext=text10.get()
    usertext1=text11.get()
    x=0
    mycursor=b.cursor()
    myquery="select * from register"
    mycursor.execute(myquery)
    allrows=mycursor.fetchall()
    for row in allrows:
        if row[0] == usertext and row[1] == usertext1:
            messagebox.showinfo("Login","login successfully")
            top=Toplevel()
            top.title("Billing Management System")
            top.geometry("655x400")
            title=Label(top,text="Customer Records",font=("times new roman", 30, "bold"),bg="Yellow",fg="Green",relief=SUNKEN,bd=12)
            title.place(x=0,y=0,relwidth=1)
            global text_rec
            global text_rec1
            global text_rec2
            global text_rec3
            global text_rec4
            global text_rec5
            f = Label(top, text="Customer_ID", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
            f.place(x=350, y=150)
            text_rec = Entry(top, width=15, font="comicsansms 19 bold",relief=SUNKEN,bd=12)
            text_rec.place(x=350, y=180)
            f1 = Label(top, text="Customer_fName", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
            f1.place(x=350, y=240)
            text_rec1 = Entry(top, width=15, font="comicsansms 19 bold",relief=SUNKEN,bd=12)
            text_rec1.place(x=350, y=270)
            f2 = Label(top, text="Customer_Contact", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
            f2.place(x=360, y=325)
            text_rec2 = Entry(top, width=15, font="comicsansms 19 bold",relief=SUNKEN,bd=12)
            text_rec2.place(x=345, y=360)
            f3 = Label(top, text="Customer_Address", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
            f3.place(x=700, y=150)
            text_rec3 = Entry(top, width=15, font="comicsansms 19 bold",relief=SUNKEN,bd=12)
            text_rec3.place(x=665, y=180)
            f4 = Label(top, text="Customer_LName", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
            f4.place(x=700, y=240)
            text_rec4 = Entry(top, width=15, font=("comicsansms 19 bold"),relief=SUNKEN,bd=12)
            text_rec4.place(x=665, y=271)
            f5 = Label(top, text="Customer_email", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
            f5.place(x=700, y=327)
            text_rec5 = Entry(top, width=15, font=("comicsansms 19 bold"),relief=SUNKEN,bd=12)
            text_rec5.place(x=665, y=360)
            btn=Button(top, text="Submit",font=("times new roman", 19, "bold"),command=submit1,bg="Black",fg="White")
            btn.place(x=550,y=450,width=165,height=50)
    mycursor.close()
    b.commit()
    b.close()
def show():
    b=py.connect(user='root',password='Lucknow@123',host='localhost',database='managementsystemdb')
    str1=text.get()
    str2=text1.get()
    str3=text2.get()
    str4=text3.get()
    str5=text4.get()
    str6=text5.get()
    str7=text6.get()
    str8=text7.get()
    str9=cmb.get()
    str10=text9.get()

    mycursor=b.cursor()
    myquery="insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    tuple=(str1,str2,str3,str4,str5,str6,str7,str8,str9,str10)
    mycursor.execute(myquery,tuple)
    b.commit()
    b.close()
    messagebox.showinfo("Registered","You are Registered Successfully")
def abt():
    top=Toplevel()
    top.title("About US")
    top.geometry("655x500")
    load=Image.open("C:\\Users\\PC\\Downloads\\WhatsApp Image 2020-05-18 at 11.35.40 PM.jpeg")
    render=ImageTk.PhotoImage(load)
    load=load.resize((200,200))
    l1=Label(top,image=render)
    l1.place(x=5,y=4)
    l2=Label(top,text="Welcome in our Billing Software\n This project is made by Shivam Saxena\n.I am "
                      "a native of Lucknow and a\n student of Babu Banarsi Das\n Engineering College Lucknow.\n\nI have made this "
                      "project on Python\n Language to increase my knowledge\n in coding and traditional life.   ",
             fg="black",
             font="comicsansms 19 bold")
    l2.place(x=790,y=12)
    top.mainloop()

def reg():
    top=Toplevel()
    top.geometry("655x400+0+0")
    top.title("Registration Window")
    global text
    global text1
    global text2
    global text3
    global text4
    global text5
    global text6
    global text7
    global cmb
    global text9
    title = Label(top, text="Register Screen", font=("times new roman", 30, "bold"),fg="green", bd=12, relief=SUNKEN)
    title.place(x=0, y=0, relwidth=1)
    l1=Label(top,text="user_id",width=15,padx=5,pady=3,font=("times new roman", 15, "bold"),fg="grey")
    l1.place(x=350,y=150)
    text=Entry(top,width=15,font="comicsansms 19 bold")
    text.place(x=350,y=180)
    l2 = Label(top, text="user_pass", width=15, padx=5, pady=3,font=("times new roman",15,"bold"),fg="grey")
    l2.place(x=750, y=150)
    text1 = Entry(top, width=15,font="comicsansms 19 bold")
    text1.place(x=750, y=185)
    l3 = Label(top, text="user_fname", width=15, padx=5, pady=3,font=("times new roman", 15, "bold"),fg="grey")
    l3.place(x=365, y=250)
    text2 = Entry(top, width=15,font="comicsansms 19 bold")
    text2.place(x=345, y=280)
    l4 = Label(top, text="user_lname", width=15, padx=5, pady=3,font=("times new roman", 15, "bold"),fg="grey")
    l4.place(x=750, y=245)
    text3 = Entry(top, width=15,font="comicsansms 19 bold")
    text3.place(x=750, y=280)
    l5 = Label(top, text="user_contact", width=15, padx=5, pady=3,font=("times new roman", 15, "bold"),fg="grey")
    l5.place(x=370, y=350)
    text4 = Entry(top, width=15,font="comicsansms 19 bold")
    text4.place(x=350, y=380)
    l6 = Label(top, text="user_email", width=15, padx=5, pady=3,font=("times new roman", 15, "bold"),fg="grey")
    l6.place(x=750, y=350)
    text5 = Entry(top, width=15,font="comicsansms 19 bold")
    text5.place(x=750, y=380)
    l7 = Label(top, text="user_address", width=15, padx=5, pady=3,font=("times new roman", 15, "bold"),fg="grey")
    l7.place(x=375, y=445)
    text6 = Entry(top, width=15,font="comicsansms 19 bold")
    text6.place(x=350, y=475)
    l8 = Label(top, text="user_city", width=15, padx=5, pady=33,font=("times new roman", 15, "bold"),fg="grey")
    l8.place(x=740, y=415)
    text7 = Entry(top, width=15,font="comicsansms 19 bold")
    text7.place(x=753, y=475)
    l9 = Label(top, text="user_sec_ques", width=15, padx=5, pady=33,font=("times new roman", 15, "bold"),fg="grey")
    l9.place(x=380, y=510)
    cmb = ttk.Combobox(top, width=15,font=("comicsansms 19 bold"),state='readonly',justify=CENTER)
    cmb['values']=("Select","Your Fav Colour","Your Birth Place","Your Best Friend")
    cmb.place(x=350, y=570)
    cmb.current(0)
    l10 = Label(top, text="user_sec_ans", width=15, padx=5, pady=3,font=("times new roman", 15, "bold"),fg="grey")
    l10.place(x=750, y=540)
    text9=Entry(top, width=15,font="comicsansms 19 bold")
    text9.place(x=750, y=575)
    btn = Button(top, padx=4, pady=5, text="Register Now", font="comicsansms 19 bold",command=show)
    btn.place(x=565,y=650)
    top.mainloop()
def log():
    top=Toplevel()
    top.geometry("655x400+0+0")
    top.title("Login Window")
    global text10;
    global text11
    title = Label(top, text="Login Screen", font=("times new roman", 30, "bold"), fg="green", bd=12, relief=SUNKEN,bg="yellow")
    title.place(x=0, y=0, relwidth=1)
    l1 = Label(top, text="user_id", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
    l1.place(x=550, y=150)
    text10 = Entry(top, width=15, font=("comicsansms 19 bold"),bd=12,relief=SUNKEN)
    text10.place(x=550, y=190)
    l2 = Label(top, text="user_pass", width=15, padx=5, pady=3, font=("times new roman", 15, "bold"), fg="Black")
    l2.place(x=550, y=260)
    text11 = Entry(top, width=15, font=("comicsansms 19 bold"),bd=12,relief=SUNKEN)
    text11.place(x=550, y=300)
    btn = Button(top, padx=6, pady=3, text="Login", font="comicsansms 19 bold",command=showlog,bg="Black",fg="White")
    btn.place(x=610,y=400)
    top.mainloop()
if __name__=="__main__":
    b1=Button(root,padx=3,pady=5,font="comicsansms 19 bold",command=log)
    b1.place(relx=0.5,rely=0.3,anchor="center")
    b2=Button(root,padx=4,pady=5,font="comicsansms 19 bold",command=reg)
    b2.place(relx=0.5,rely=0.5,anchor="center")
    b3=Button(root,padx=15,pady=5,font="comicsansms 19 bold",command=abt)
    b3.place(relx=0.5,rely=0.7,anchor="center")
    load = Image.open("C:\\Users\\PC\\Documents\\login3 image.jpg")
    render = ImageTk.PhotoImage(load)
    b1.config(image=render)
    load1 = Image.open("C:\\Users\\PC\\Documents\\register image.jpg")
    render1 = ImageTk.PhotoImage(load1)
    b2.config(image=render1)
    load2 = Image.open("C:\\Users\\PC\Documents\\about us.jpg")
    render2 = ImageTk.PhotoImage(load2)
    b3.config(image=render2)

    root.mainloop()

























