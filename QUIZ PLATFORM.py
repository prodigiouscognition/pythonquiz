from tkinter import *
import mysql.connector
conn=mysql.connector.connect(user='root',password='Mathematics2001@',host='localhost',port=3306,database='quiz')
window1=Tk()
window1.geometry("650x435+500+150")
window1.maxsize(650,435)
window1.minsize(650,435)
window1.title("LETS EXPERIMENT")
def one():
    window1.destroy()
    window2=Tk()
    window2.title("FORM")
    window2.geometry("400x380+600+150")
    window2.maxsize(400, 380)
    window2.minsize(400, 380)
    window2.configure(bg="#11afed")
    label3 = Label(window2, text="ENTER YOUR DETAILS:", font="lucida 15 bold underline",bg="black",fg="orange").grid(row=0, column=3,pady=15)
    name = Label(window2, text="Name",bg="#11afed",fg="black",font="lucida 15 bold")
    phone = Label(window2, text="Phone no.",bg="#11afed",fg="black",font="lucida 15 bold")
    gender = Label(window2, text="Gender",bg="#11afed",fg="black",font="lucida 15 bold")
    age = Label(window2, text="Age",bg="#11afed",fg="black",font="lucida 15 bold")
    address = Label(window2, text="Address",bg="#11afed",fg="black",font="lucida 15 bold")
    email = Label(window2, text="Email Id",bg="#11afed",fg="black",font="lucida 15 bold")
    name.grid(row=1, column=1)
    phone.grid(row=2, column=1)
    gender.grid(row=3, column=1)
    age.grid(row=5, column=1)
    address.grid(row=6, column=1)
    email.grid(row=7, column=1)
    namevalue = StringVar()
    phonevalue = IntVar()
    gendervalue = IntVar()
    agevalue = IntVar()
    addressvalue = StringVar()
    emailvalue = StringVar()
    nameentry = Entry(window2, textvariable=namevalue,bg="orange",fg="black",font="lucida 15")
    phoneentry = Entry(window2, textvariable=phonevalue,bg="orange",fg="black",font="lucida 15")
    genderentry1 = Radiobutton(window2, text="MALE",bg="orange",fg="black",font="lucida 9",variable=gendervalue,value=1)
    genderentry2 = Radiobutton(window2, text="FEMALE", bg="orange", fg="black", font="lucida 9", variable=gendervalue,value=2)
    ageentry = Entry(window2, textvariable=agevalue,bg="orange",fg="black",font="lucida 15")
    addressentry = Entry(window2, textvariable=addressvalue,bg="orange",fg="black",font="lucida 15")
    emailentry = Entry(window2, textvariable=emailvalue,bg="orange",fg="black",font="lucida 15")
    nameentry.grid(row=1, column=3,pady=5)
    phoneentry.grid(row=2, column=3,pady=5)
    genderentry1.grid(row=3, column=3,pady=5)
    genderentry2.grid(row=4,column=3)
    ageentry.grid(row=5, column=3,pady=5)
    addressentry.grid(row=6, column=3,pady=5)
    emailentry.grid(row=7, column=3,pady=5)
    button1 = Button(window2, text="TAKE TEST",bg="black",fg="orange",font="lucida 15 bold",relief=RIDGE,command=lambda :[des1(window2),two(namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue)])
    button1.grid(column=3,pady=10)
    window2.mainloop()
def two(namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue):
    window3=Tk()
    window3.geometry("550x800+500+10")
    window3.title("ENGLISH")
    window3.config(bg="#de1296")
    window3.maxsize(550,800)
    window3.minsize(550,800)
    frame1=Frame(window3)
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    label1 = Label(frame1, text="LANGUAGE", fg="#de1296", bg="black", font="helveica 20 bold italic underline").pack(pady=10)
    label2=Label(frame1,text="What is the meaning of idiom CALL IN?",fg="#de1296",font="lucida 15 italic bold").pack()
    radio1 = Radiobutton(frame1, text="TO JOIN", padx=14, font="lucida 10 italic bold", variable=var1, value=1).pack()
    radio2 = Radiobutton(frame1, text="SUMMON", padx=14, font="lucida 10 italic bold", variable=var1, value=2).pack()
    radio3 = Radiobutton(frame1, text="RECOLLECT", padx=14, font="lucida 10 italic bold", variable=var1, value=3).pack()
    radio4 = Radiobutton(frame1, text="DEMANDED", padx=14, font="lucida 10 italic bold", variable=var1, value=4).pack()
    label3 = Label(frame1, text="Her thinking leans ____ democracy.",fg="#de1296", font="lucida 15 italic bold").pack()
    radio5 = Radiobutton(frame1, text="WITH", padx=14, font="lucida 10 italic bold", variable=var2, value=1).pack()
    radio6 = Radiobutton(frame1, text="TOWARDS", padx=14, font="lucida 10 italic bold", variable=var2, value=2).pack()
    radio7 = Radiobutton(frame1, text="FOR", padx=14, font="lucida 10 italic bold", variable=var2,
                         value=3).pack()
    radio8 = Radiobutton(frame1, text="NONE OF THESE", padx=14, font="lucida 10 italic bold", variable=var2, value=4).pack()
    label4 = Label(frame1, text="_____ his principles, he has to be very careful.",fg="#de1296",font="lucida 15 italic bold").pack()
    radio9 = Radiobutton(frame1, text="WITH REGARD OF", padx=14, font="lucida 10 italic bold", variable=var3, value=1).pack()
    radio10 = Radiobutton(frame1, text="WITH REGARD ON", padx=14, font="lucida 10 italic bold", variable=var3, value=2).pack()
    radio11 = Radiobutton(frame1, text="WITH REGARD TO", padx=14, font="lucida 10 italic bold", variable=var3,
                         value=3).pack()
    radio12 = Radiobutton(frame1, text="NONE OF THESE", padx=14, font="lucida 10 italic bold", variable=var3, value=4).pack()
    label5 = Label(frame1, text="They didn't reach an agreement ___ their differences.",fg="#de1296", font="lucida 15 italic bold").pack()
    radio13 = Radiobutton(frame1, text="ON ACCOUNT OF", padx=14, font="lucida 10 italic bold", variable=var4, value=1).pack()
    radio14 = Radiobutton(frame1, text="DUE", padx=14, font="lucida 10 italic bold", variable=var4, value=2).pack()
    radio15 = Radiobutton(frame1, text="BECAUSE", padx=14, font="lucida 10 italic bold", variable=var4,
                         value=3).pack()
    radio16 = Radiobutton(frame1, text="OWING", padx=14, font="lucida 10 italic bold", variable=var4, value=4).pack()
    label6 = Label(frame1, text="He's still sleeping, ____",fg="#de1296", font="lucida 15 italic bold").pack()
    radio17 = Radiobutton(frame1, text="IS NOT HE?", padx=14, font="lucida 10 italic bold", variable=var5, value=1).pack()
    radio18 = Radiobutton(frame1, text="ISN'T HE?", padx=14, font="lucida 10 italic bold", variable=var5, value=2).pack()
    radio19 = Radiobutton(frame1, text="WASN'T HE?", padx=14, font="lucida 10 italic bold", variable=var5,
                         value=3).pack()
    radio20 = Radiobutton(frame1, text="NONE OF THESE", padx=14, font="lucida 10 italic bold", variable=var5, value=4).pack()
    window3.after(600000, lambda :[des1(window3),three(var1,var2,var3,var4,var5,namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue)])
    button1=Button(frame1,text="NEXT",fg="black",bg="#de1296",font="lucida 14 bold",relief=RIDGE,command=lambda :[des1(window3),three(var1,var2,var3,var4,var5,namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue)]).pack(pady=10)
    frame1.pack()
    window3.mainloop()
def three(var1,var2,var3,var4,var5,namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue):
    sum=0
    if (var1.get() == 2):
        sum = sum + 2
    elif (var1.get() == 1 or var1.get() == 3 or var1.get() == 4):
        sum = sum - 0.5
    if (var2.get() == 2):
        sum = sum + 2
    elif (var2.get() == 1 or var2.get() == 3 or var2.get() == 4):
        sum = sum - 0.5
    if (var3.get() == 3):
        sum = sum + 2
    elif (var3.get() == 1 or var3.get() == 2 or var3.get() == 4):
        sum = sum - 0.5
    if (var4.get() == 1):
        sum = sum + 2
    elif (var4.get() == 2 or var4.get() == 3 or var4.get() == 4):
        sum = sum - 0.5
    if (var5.get() == 2):
        sum = sum + 2
    elif (var5.get() == 1 or var5.get() == 3 or var5.get() == 4):
        sum = sum - 0.5
    window4 = Tk()
    window4.title("VERBAL REASONING")
    window4.config(bg="orange")
    window4.geometry("560x820+500+5")
    window4.maxsize(560, 820)
    window4.minsize(560, 820)
    frame1 = Frame(window4)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    label1 = Label(frame1, text="VERBAL REASONING", fg="orange", bg="black", font="helveica 20 bold italic").pack(pady=10)
    label2 = Label(frame1, text=" If MADRAS is to NBESBT, then BOMBAY is to", fg="orange", font="lucida 15 italic bold").pack()
    radio1 = Radiobutton(frame1, text="CPNCBX", padx=14, font="lucida 10 italic bold", variable=var1, value=1).pack()
    radio2 = Radiobutton(frame1, text="CPNCBZ", padx=14, font="lucida 10 italic bold", variable=var1, value=2).pack()
    radio3 = Radiobutton(frame1, text="CPNCBY", padx=14, font="lucida 10 italic bold", variable=var1, value=3).pack()
    radio4 = Radiobutton(frame1, text="CQOCBZ", padx=14, font="lucida 10 italic bold", variable=var1, value=4).pack()
    label3 = Label(frame1, text="If TRIPPLE is to SQHOOKD,then DISPOSE is to",fg="orange", font="lucida 15 italic bold").pack()
    radio5 = Radiobutton(frame1, text="CHRONRD", padx=14, font="lucida 10 italic bold", variable=var2, value=1).pack()
    radio6 = Radiobutton(frame1, text="DSOESPI", padx=14, font="lucida 10 italic bold", variable=var2, value=2).pack()
    radio7 = Radiobutton(frame1, text="ESJTPTF", padx=14, font="lucida 10 italic bold", variable=var2,
                         value=3).pack()
    radio8 = Radiobutton(frame1, text="ESOPSID", padx=14, font="lucida 10 italic bold", variable=var2, value=4).pack()
    label4 = Label(frame1, text="If COULD is to BNTKC and MARGIN is to\n LZQFHM, then MOULDING is to", fg="orange" ,font="lucida 15 italic bold").pack()
    radio9 = Radiobutton(frame1, text="CHMFINTK", padx=14, font="lucida 10 italic bold", variable=var3, value=1).pack()
    radio10 = Radiobutton(frame1, text="LNKTCHMF", padx=14, font="lucida 10 italic bold", variable=var3, value=2).pack()
    radio11 = Radiobutton(frame1, text="LNTKCHMF", padx=14, font="lucida 10 italic bold", variable=var3,
                          value=3).pack()
    radio12 = Radiobutton(frame1, text="NITKHCMF", padx=14, font="lucida 10 italic bold", variable=var3, value=4).pack()
    label5 = Label(frame1, text="If  MONKEY is to XDJMNL, then TIGER is to", fg="orange", font="lucida 15 italic bold").pack()
    radio13 = Radiobutton(frame1, text="QDFHS", padx=14, font="lucida 10 italic bold", variable=var4, value=1).pack()
    radio14 = Radiobutton(frame1, text="SDFHS", padx=14, font="lucida 10 italic bold", variable=var4, value=2).pack()
    radio15 = Radiobutton(frame1, text="SHFDQ", padx=14, font="lucida 10 italic bold", variable=var4,
                          value=3).pack()
    radio16 = Radiobutton(frame1, text="UJHFS", padx=14, font="lucida 10 italic bold", variable=var4, value=4).pack()
    label6 = Label(frame1, text="If FRAGRANCE is to SBHSBODFG, then IMPOSING is to", fg="orange", font="lucida 15 italic bold").pack()
    radio17 = Radiobutton(frame1, text="NQPTJHOJ", padx=14, font="lucida 10 italic bold", variable=var5, value=1).pack()
    radio18 = Radiobutton(frame1, text="NQPTJOHI", padx=14, font="lucida 10 italic bold", variable=var5, value=2).pack()
    radio19 = Radiobutton(frame1, text="NQTPJOHJ", padx=14, font="lucida 10 italic bold", variable=var5,
                          value=3).pack()
    radio20 = Radiobutton(frame1, text="NQPTJOHJ", padx=14, font="lucida 10 italic bold", variable=var5, value=4).pack()
    window4.after(600000, lambda: [des1(window4),
                                   four(var1, var2, var3, var4, var5, sum, namevalue, phonevalue, gendervalue, agevalue,
                                         addressvalue, emailvalue)])
    button1 = Button(frame1, text="NEXT", fg="black", bg="orange", font="lucida 14 bold", relief=RIDGE,command=lambda :[des1(window4),four(var1,var2,var3,var4,var5,sum,namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue)]).pack(pady=10)
    frame1.pack()
    window4.mainloop()
def four(var1,var2,var3,var4,var5,sum,namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue):
    if (var1.get() == 2):
        sum = sum + 2
    elif (var1.get() == 1 or var1.get() == 3 or var1.get() == 4):
        sum = sum - 0.5
    if (var2.get() == 1):
        sum = sum + 2
    elif (var2.get() == 2 or var2.get() == 3 or var2.get() == 4):
        sum = sum - 0.5
    if (var3.get() == 3):
        sum = sum + 2
    elif (var3.get() == 1 or var3.get() == 2 or var3.get() == 4):
        sum = sum - 0.5
    if (var4.get() == 1):
        sum = sum + 2
    elif (var4.get() == 2 or var4.get() == 3 or var4.get() == 4):
        sum = sum - 0.5
    if (var5.get() == 4):
        sum = sum + 2
    elif (var5.get() == 1 or var5.get() == 2 or var5.get() == 3):
        sum = sum - 0.5
    window5 = Tk()
    window5.title("MATHEMATICS")
    window5.geometry("650x800+500+10")
    window5.config(bg="blue")
    window5.maxsize(650, 800)
    window5.minsize(650, 800)
    frame1 = Frame(window5)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    label1 = Label(frame1, text="MATHEMATICS", fg="blue", bg="black", font="helveica 20 bold italic").pack(
        pady=10)
    label2 = Label(frame1, text="What is three fifth of 100", fg="blue", font="lucida 15 italic bold").pack()
    radio1 = Radiobutton(frame1, text="3", padx=14, font="lucida 10 italic bold", variable=var1, value=1).pack()
    radio2 = Radiobutton(frame1, text="5", padx=14, font="lucida 10 italic bold", variable=var1, value=2).pack()
    radio3 = Radiobutton(frame1, text="20", padx=14, font="lucida 10 italic bold", variable=var1, value=3).pack()
    radio4 = Radiobutton(frame1, text="60", padx=14, font="lucida 10 italic bold", variable=var1, value=4).pack()
    label3 = Label(frame1, text="If David’s age is 27 years old in 2011. What was his age in 2003?", fg="blue", font="lucida 15 italic bold").pack()
    radio5 = Radiobutton(frame1, text="17 years", padx=14, font="lucida 10 italic bold", variable=var2, value=1).pack()
    radio6 = Radiobutton(frame1, text="37 years", padx=14, font="lucida 10 italic bold", variable=var2, value=2).pack()
    radio7 = Radiobutton(frame1, text="20 years", padx=14, font="lucida 10 italic bold", variable=var2,
                         value=3).pack()
    radio8 = Radiobutton(frame1, text="19 years", padx=14, font="lucida 10 italic bold", variable=var2, value=4).pack()
    label4 = Label(frame1, text="What is the remainder of 21 divided by 7?",fg="blue", font="lucida 15 italic bold").pack()
    radio9 = Radiobutton(frame1, text="1", padx=14, font="lucida 10 italic bold", variable=var3, value=1).pack()
    radio10 = Radiobutton(frame1, text="-1", padx=14, font="lucida 10 italic bold", variable=var3, value=2).pack()
    radio11 = Radiobutton(frame1, text="2", padx=14, font="lucida 10 italic bold", variable=var3,
                          value=3).pack()
    radio12 = Radiobutton(frame1, text="0", padx=14, font="lucida 10 italic bold", variable=var3, value=4).pack()
    label5 = Label(frame1, text="What is 7% of 100",fg="blue", font="lucida 15 italic bold").pack()
    radio13 = Radiobutton(frame1, text="7", padx=14, font="lucida 10 italic bold", variable=var4, value=1).pack()
    radio14 = Radiobutton(frame1, text="70", padx=14, font="lucida 10 italic bold", variable=var4, value=2).pack()
    radio15 = Radiobutton(frame1, text="0.7", padx=14, font="lucida 10 italic bold", variable=var4,
                          value=3).pack()
    radio16 = Radiobutton(frame1, text="0.07", padx=14, font="lucida 10 italic bold", variable=var4, value=4).pack()
    label6 = Label(frame1, text="How many years are there in a decade?",fg="blue", font="lucida 15 italic bold").pack()
    radio17 = Radiobutton(frame1, text="1", padx=14, font="lucida 10 italic bold", variable=var5, value=1).pack()
    radio18 = Radiobutton(frame1, text="100", padx=14, font="lucida 10 italic bold", variable=var5, value=2).pack()
    radio19 = Radiobutton(frame1, text="10", padx=14, font="lucida 10 italic bold", variable=var5,
                          value=3).pack()
    radio20 = Radiobutton(frame1, text="20", padx=14, font="lucida 10 italic bold", variable=var5, value=4).pack()
    window5.after(600000, lambda: [des1(window5),
                                   five(var1, var2, var3, var4, var5, sum, namevalue, phonevalue, gendervalue, agevalue,
                                         addressvalue, emailvalue)])
    button1 = Button(frame1, text="END TEST", font="lucida 14 bold", relief=RIDGE, bg="blue",fg="black",
                     command=lambda: [des1(window5), five(var1,var2,var3,var4,var5,sum,namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue)]).pack(pady=10)
    frame1.pack()
    window5.mainloop()
def five(var1,var2,var3,var4,var5,sum,namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue):
    if (var1.get() == 4):
        sum = sum + 2
    elif (var1.get() == 1 or var1.get() == 2 or var1.get() == 3):
        sum = sum - 0.5
    if (var2.get() == 4):
        sum = sum + 2
    elif (var2.get() == 1 or var2.get() == 2 or var2.get() == 3):
        sum = sum - 0.5
    if (var3.get() == 4):
        sum = sum + 2
    elif (var3.get() == 1 or var3.get() == 2 or var3.get() == 3):
        sum = sum - 0.5
    if (var4.get() == 1):
        sum = sum + 2
    elif (var4.get() == 2 or var4.get() == 3 or var4.get() == 4):
        sum = sum - 0.5
    if (var5.get() == 3):
        sum = sum + 2
    elif (var5.get() == 1 or var5.get() == 2 or var5.get() == 4):
        sum = sum - 0.5
    window6=Tk()
    window6.title("RESULT")
    window6.geometry("400x380+600+150")
    window6.config(bg="black")
    window6.maxsize(400, 380)
    window6.minsize(400, 380)
    label1=Label(text=sum,bg="black",fg="green",font="helvetica 15 bold").pack()
    label2=Label(text="Is your score",fg="green",bg="black",font="helvetics 15 bold").pack()
    button1=Button(text="EXIT",fg="black",bg="green",relief=GROOVE,font="helvetica 15 bold",command=lambda: [des1(window6),des2(namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue,sum)]).pack(side=BOTTOM)
    window6.mainloop()
def des1(window):
    window.destroy()
def des2(namevalue,phonevalue,gendervalue,agevalue,addressvalue,emailvalue,sum):
    cur = conn.cursor()
    sql = 'insert into quiz1(name,phone,gender,age,address,email,marks) values(%s,%s,%s,%s,%s,%s,%s)'
    name=namevalue.get()
    phone=phonevalue.get()
    gender=gendervalue.get()
    age=agevalue.get()
    address=addressvalue.get()
    email=emailvalue.get()
    values = (name,phone,gender,age,address,email,sum)
    cur.execute(sql, values)
    cur.execute('commit')
    cur.close()
    conn.close()
label1=Label(window1,text="LETS EXPERIMENT PRESENTS THE MOST LOGICAL QUIZ",fg="blue",bg="black",font="helveica 13 bold italic").pack()
pic=PhotoImage(file="quiz.PNG")
pic_label=Label(image=pic,relief=SUNKEN)
pic_label.pack(pady=10)
button1=Button(text="PROCEED ->",bg="#eb09b6",fg="blue",font="helvetica 12 bold",relief=GROOVE,command=one).pack(pady=20)
label2=Label(window1,text="There will be three sections in the quiz. Each section will consist of 5 questions.\n"
                          "The first section consists of language based questions, second verbal reasoning \n"
                          "and the third section will consist mathematics based questions.\n"
                          "Each correct answer will award you 2 marks and for every wrong answer 0.5 marks\n"
                          "will be deducted. You have 10 min to solve each section.",fg="orange",bg="black",font="helveica 13 bold italic").pack()
window1.mainloop()

