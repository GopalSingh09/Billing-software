from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="black"
        title=Label(self.root,text="Billing Software",bd=10,relief=GROOVE,bg=bg_color,fg="white", font=("times new roman",30,"bold"),pady=2).pack(fill=X)
                                 #======================Variables========================================
        # ======================cosmatics========================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.oil=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()

        # ======================Grocery========================================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ======================Cold dring========================================

        self.coca = IntVar()
        self.fanta = IntVar()
        self.maaza = IntVar()
        self.sprite = IntVar()
        self.appie = IntVar()
        self.red_bull = IntVar()

        # ======================Grocery========================================

        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ======================Customer========================================

        self.c_name=StringVar()
        self.c_phone= StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

                                 #==============customer detail frame====================================
        F1=LabelFrame(self.root,text="Customer Details",bd=8,relief=GROOVE, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0, y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 15").grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone no.", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(   row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20,textvariable=self.c_phone, font="arial 15").grid(row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="Bill no.", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid( row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=20,textvariable=self.search_bill, font="arial 15").grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="search",width=10,command=self.find_bill,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10, pady=10)

        #========================Cosmetics=================
        F2=LabelFrame(self.root,text="Cosmetics",bd=8,relief=GROOVE, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5, y=175,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Hair_oil_lbl = Label(F2, text="Hair oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_oil_txt = Entry(F2, width=10,textvariable=self.oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_l_lbl = Label(F2, text="Body lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_l_txt = Entry(F2, width=10,textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # ========================Grocery Frame=================

        F3 = LabelFrame(self.root, text="Grocery", bd=8, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=340, y=175, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=0, column=1, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=2,padx=10, pady=10)

        g2_lbl = Label(F3, text="Food oil", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=1, column=1, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=2, padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=2, column=1, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=2,padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=3, column=1, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=4, column=1, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=2,padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=5, column=1, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=2, padx=10,pady=10)

        # ========================Cold drink Frame=================

        F4 = LabelFrame(self.root, text="Cold drink", bd=8, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=670, y=175, width=325, height=380)

        k1_lbl = Label(F4, text="Coca cola", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=0, column=1, padx=10, pady=10, sticky="w")
        k1_txt = Entry(F4, width=10,textvariable=self.coca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=2,padx=10, pady=10)

        k2_cream_lbl = Label(F4, text="fanta", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=1, column=1, padx=10, pady=10, sticky="w")
        k2_cream_txt = Entry(F4, width=10,textvariable=self.fanta, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=2, padx=10, pady=10)

        k3_w_lbl = Label(F4, text="maaza", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=2, column=1, padx=10, pady=10, sticky="w")
        k3_w_txt = Entry(F4, width=10,textvariable=self.maaza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=2, padx=10,pady=10)

        k4_lbl = Label(F4, text="red bull", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid( row=3, column=1, padx=10, pady=10, sticky="w")
        k4_txt = Entry(F4, width=10,textvariable=self.red_bull, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=2,padx=10, pady=10)

        k5_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=4, column=1, padx=10, pady=10, sticky="w")
        k5_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=2, padx=10, pady=10)

        k6_lbl = Label(F4, text="Appie", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=5, column=1, padx=10, pady=10, sticky="w")
        k6_txt = Entry(F4, width=10,textvariable=self.appie, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,  column=2,padx=10,pady=10)

        #============ Bill area========

        F5 = Frame(self.root,  bd=8, relief=GROOVE)
        F5.place(x=1000, y=175, width=350, height=380)
        bill_title=Label(F5,text="bill area",font="arial 15 bold", bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcomman=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=========button frame======
        F6 = LabelFrame(self.root, text="bill manu", bd=8, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1=Label(F6,text="total cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2 = Label(F6, text="total Grocery Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid( row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="total Cold drinks Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid( row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        t1 = Label(F6, text=" cosmetic tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid( row=0, column=2, padx=20, pady=1, sticky="w")
        t1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        t2 = Label(F6, text=" Grocery tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid( row=1, column=2, padx=20, pady=1, sticky="w")
        t2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        t3 = Label(F6, text=" Cold drinks tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        t3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=740,width=585,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",pady=12,width=9,bd=5,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)

        gbill_btn = Button(btn_f, text="Generate bill",command=self.bill_area, bg="cadetblue", fg="white", pady=12, width=9, bd=5,font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, text="Clear",command=self.clear_data, bg="cadetblue", fg="white", pady=12, width=9, bd=5, font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, text="Exit",command=self.Exit_app, bg="cadetblue", fg="white", pady=12, width=9, bd=5, font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get() * 150
        self.c_fw_p=self.face_wash.get() * 89
        self.c_o_p=self.oil.get() * 200
        self.c_g_p=self.gell.get() * 489
        self.c_l_p=self.lotion.get() * 780

        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                     self.c_fc_p+
                                     self.c_fw_p+
                                     self.c_o_p+
                                     self.c_g_p+
                                    self.c_l_p

                                    )
        self.cosmetic_price.set("Rs.  "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs.  "+str(self.c_tax))

        self.g_r_p=self.rice.get() * 180
        self.g_fo_p=self.food_oil.get() * 180
        self.g_d_p=self.daal.get() * 60
        self.g_w_p=self.wheat.get() * 240
        self.g_s_p=self.sugar.get() * 459
        self.g_t_p=self.tea.get() * 150

        self.total_grocery_price = float(
                                     self.g_r_p+
                                     self.g_fo_p+
                                     self.g_d_p+
                                     self.g_w_p+
                                     self.g_s_p+
                                    self.g_t_p
                                  )
        self.grocery_price.set("Rs.  "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set("Rs.  " + str(self.g_tax))

        self.cd_m_p=self.maaza.get() * 60
        self.cd_c_p=self.coca.get() * 60
        self.cd_a_p=self.appie.get() * 60
        self.cd_s_p=self.sprite.get() * 60
        self.cd_rb_p=self.red_bull.get() * 60
        self.cd_f_p=self.fanta.get() * 60

        self.total_cold_drink_price = float(
                                        self.cd_m_p +
                                        self.cd_c_p+
                                        self.cd_a_p +
                                        self.cd_s_p +
                                        self.cd_rb_p +
                                        self.cd_f_p
                                  )
        self.cold_drink_price.set("Rs.  "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price * 0.05), 2)
        self.cold_drink_tax.set("Rs.  " + str(self.cd_tax))

        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.cd_tax
                                )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\twelcome webxode retail\n")
        self.txtarea.insert(END,f"\n Bill number :{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer name :{self.c_name.get()} ")
        self.txtarea.insert(END,f"\n Phone number :{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=======================================")
        self.txtarea.insert(END, f"\nProducts\t\tQuantity\t\tprice")
        self.txtarea.insert(END, f"\n=======================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cosmetic_price.get()=="Rs. 0.0" :
            messagebox.showerror("error","No product purchased please add some product in your cart")
        else:
            self.welcome_bill()
            #=========================================cosmetics=============================

            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n Oil\t\t{self.oil.get()}\t\t{self.c_o_p}")

            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Gell\t\t{self.gell.get()}\t\t{self.c_g_p}")

            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Lotion\t\t{self.lotion.get()}\t\t{self.c_l_p}")

                # =========================================grocery=============================

            if self.rice.get() != 0:
                    self.txtarea.insert(END, f"\n Rice\t\t{self.lotion.get()}\t\t{self.g_r_p}")

            if self.food_oil.get() != 0:
                    self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")

            if self.daal.get() != 0:
                    self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.wheat.get() != 0:
                    self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get() != 0:
                    self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get() != 0:
                    self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

                # =========================================Cold drink=============================

            if self.maaza.get() != 0:
                self.txtarea.insert(END, f"\n Maaza\t\t{self.maaza.get()}\t\t{self.cd_m_p}")

            if self.coca.get() != 0:
                self.txtarea.insert(END, f"\n Coca Cola\t\t{self.coca.get()}\t\t{self.cd_c_p}")

            if self.appie.get() != 0:
                self.txtarea.insert(END, f"\n Appie\t\t{self.appie.get()}\t\t{self.cd_a_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.cd_s_p}")

            if self.red_bull.get() != 0:
                self.txtarea.insert(END, f"\n Red bull\t\t{self.red_bull.get()}\t\t{self.cd_rb_p}")

            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.cd_f_p}")

            self.txtarea.insert(END, f"\n---------------------------------------")
            if self.cosmetic_tax.get()!="Rs.  0.0":
                   self.txtarea.insert(END,f"\nCosmetic tax\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Rs.  0.0":
                   self.txtarea.insert(END,f"\nGrocery tax tax\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!="Rs. /; 0.0":
                   self.txtarea.insert(END,f"\nCold drink tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\nTotal bill : \t\t\tRs. {str(self.Total_bill)}")

            self.txtarea.insert(END, f"\n---------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save the bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("billls/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved succesfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("billls/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"billls/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                     self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Exit", "Do you really want to clear the bill")
        if op > 0:

            # ======================cosmatics========================================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.oil.set(0)
            self.gell.set(0)
            self.lotion.set(0)

            # ======================Grocery========================================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ======================Cold dring========================================

            self.coca.set(0)
            self.fanta.set(0)
            self.maaza.set(0)
            self.sprite.set(0)
            self.appie.set(0)
            self.red_bull.set(0)

            # ======================Grocery========================================

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ======================Customer========================================

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no = StringVar()
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()