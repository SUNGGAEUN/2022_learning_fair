from tkinter import *
import tkinter.messagebox
import turtle
#messagebox설정
price_topping = {'올리브': 300, '페퍼로니': 500,'치즈': 1500,'피망': 800, '파프리카': 800, '파인애플': 300, '감자': 1000, '고구마': 2000,'베이컨': 1000, '닭고기': 2000, '돼지고기': 2000, '소고기': 2000}
order_topping = {}
price_crust = {'일반': 0, '고구마': 4000, '치즈': 3000}
order_crust = {}
total_price = int(15000)
#가격 설정
window = Tk()
window.title('셀프 피자 가게')
window.geometry('640x300+650+300')
window.resizable(False,False)
root = Tk()
root.title('셀프 피자 가게')
root.geometry('640x400+650+300')
root.resizable(False, False )
root.withdraw()
price = Tk()
price.title('토핑')
price.geometry('150x400+1300+300')
price.resizable(False, False)
price.withdraw()
crust = Tk()
crust.title('셀프 피자 가게')
crust.geometry('640x400+650+300')
crust.resizable(False, False)
crust.withdraw()
od_crust = Tk()
od_crust.title('크러스트')
od_crust.geometry('150x100+1460+300')
od_crust.resizable(False, False)
od_crust.withdraw()
cash = Tk()
cash.title('셀프 피자 가게')
cash.geometry('640x400+650+300')
cash.resizable(False, False)
cash.withdraw()
#False는 창 크기 못늘리게 고정, title 창 제목

hello = Label(window, text='어서오세요! 셀프 피자 가게 입니다')
hello.place(x = 225, y= 70)
question = Label(window, text='주문하시겠습니까?')
question.place(x= 265, y = 90)
#시작화면

def close():
    message = tkinter.messagebox.showinfo('셀프 피자 가게', '안녕히가세요')
    window.destroy()
#아니오>창닫기
def yes():
    window.destroy()
    root.deiconify()
    price.deiconify()
    od_crust.deiconify()
#deiconify 안보이게 창 띄우기
y = Button(window, text = '예',padx = 6, pady = 6, command = yes)
y.place(x= 250, y = 120)
n = Button(window, text = '아니오', padx = 6, pady = 6, command = close)
n.place(x = 340, y = 120)

def add(i):
    global order_topping, price_topping,total_price
    if i not in price_topping:
        nop = tkinter.messagebox.showinfo('셀프 피자 가게','주문하신 토핑이 없습니다')
    this_price = price_topping.get(i)
    total_price += this_price
    if i in order_topping:
        order_topping[i] = order_topping.get(i) + 1
    else:
        order_topping[i] = 1
    print_orber()
    print_price()
def print_orber():
    tp = ''
    for j in order_topping:
        tp = tp + j + 'X' + str(order_topping.get(j)) + '\n'
    textarea.delete('1.0',END)
    textarea.insert(INSERT, tp)
def go():
    root.withdraw()
    crust.deiconify()

topping = Label(root, text = '토핑을 선택해주세요', font = 'Arial 20')
topping.pack()
x = Label(root, text = '기본 가격은 15000원 입니다', font = 'Arial 10')
x.place(x = 240, y = 290)
topping1 = Button(root, text = '올리브\n300원', width = 12, height =4, command =lambda: add('올리브'))
topping1.place(x = 125, y = 50)
topping2 = Button(root, text = '페퍼로니\n500원', width = 12, height = 4, command = lambda: add('페퍼로니'))
topping2.place(x = 225, y = 50)
topping3 = Button(root, text = '치즈\n1500원', width = 12, height = 4, command = lambda: add('치즈'))
topping3.place(x = 325, y= 50)
topping4 = Button(root, text = '피망\n800원', width = 12, height = 4, command = lambda: add('피망'))
topping4.place(x = 425, y = 50)
topping5 = Button(root, text = '파프리카\n800원',width = 12, height = 4,command = lambda: add('파프리카'))
topping5.place(x = 125, y = 130)
topping6 = Button(root, text = '파인애플\n300원', width = 12, height = 4, command = lambda: add('파인애플'))
topping6.place(x = 225, y = 130)
topping7 = Button(root, text = '감자\n1000원', width = 12, height = 4, command = lambda: add('감자'))
topping7.place(x = 325, y = 130)
topping8 = Button(root, text = '고구마\n2000원', width = 12, height = 4, command = lambda: add('고구마'))
topping8.place(x = 425, y = 130)
topping9 = Button(root, text = '베이컨\n1000원', width = 12, height = 4, command = lambda: add('베이컨'))
topping9.place(x = 125, y = 210)
topping10 = Button(root, text = '닭고기\n2000원', width = 12, height = 4, command = lambda: add('닭고기'))
topping10.place(x = 225, y = 210)
topping11 = Button(root, text = '돼지고기\n2000원', width = 12, height = 4, command = lambda: add('돼지고기'))
topping11.place(x = 325, y = 210)
topping12 = Button(root, text = '소고기\n2000원', width = 12, height = 4, command = lambda: add('소고기'))
topping12.place(x = 425, y = 210)
c = Button(root, text = '다음으로', padx = 5, pady = 5, command = go)
c.place(x = 550, y = 300)
topping_price = Label(root, text = '0원', font = 'Arial 20')
topping_price.place( x = 300, y = 310)
#토핑 버튼 넓이 높이 폰트
def trun():
    crust.withdraw()
    root.deiconify()
def go2():
    crust.withdraw()
    cash.deiconify()
def cru(st):
    global price_crust, order_crust, total_price
    if st not in price_crust:
        noc = tkinter.messagebox.showinfo('셀프 피자 가게', '주문하신 크러스트가 없습니다')
    this_price = price_crust.get(st)
    total_price += this_price
    
    order_crust[st] = order_crust.get(st)
    order_crust[st] = 1
    print_crust_order()
    print_price()
def print_crust_order():
    global cru
    cs = ''
    for q in order_crust:
        cs = q
    crust_text.delete('1.0',END)
    crust_text.insert(INSERT, cs)

cr = Label(crust, text = '크러스트를 선택해주세요',font = 'Arial 20')
cr.place(x = 170, y = 50)
cr1 = Button(crust, text = '일반\n0원', width = 12, height = 4, command = lambda: cru('일반'))
cr1.place(x = 155, y = 150)
cr2 = Button(crust, text = '치즈\n3000원', width = 12, height = 4, command = lambda: cru('치즈'))
cr2.place(x = 275, y = 150)
cr3 = Button(crust, text = '고구마\n4000원', width = 12, height = 4, command = lambda: cru('고구마'))
cr3.place(x = 400, y = 150)
re = Button(crust, text = '이전으로', command = trun)
re.place(x = 30, y = 300)
crust_price = Label(crust, text = '0원', font = 'Arial 20')
crust_price.place(x = 300, y = 300)
c2 = Button(crust, text = '다음으로', command = go2)
c2.place(x = 550, y = 300)
w = Label(crust, text = '한 번만 눌러주세요', font = 'Arial 15')
w.place(x = 240, y = 100)
#크러스트 선택
def trun2():
    cash.withdraw()
    crust.deiconify()
def pay2(event):
    global jan, total_price
    don = int(cash_text.get())
    if don >= total_price:
        jan.configure(text = '거스름돈 '+ str(don - total_price)+'원입니다')
        u2()
    else:
        lock = tkinter.messagebox.showinfo('셀프 피자 가게', '금액이 부족합니다')
def u2():
    end = Button(cash, text = '주문 마치기',command = cook)
    end.place(x = 550, y = 300)
def pay():
    global jan, total_price
    don = int(cash_text.get())
    if don >= total_price:
        jan.configure(text = '거스름돈 ' + str(don - total_price) +'원입니다')
        u()
    else:
        lock2 = tkinter.messagebox.showinfo('셀프 피자 가게', '금액이 부족합니다')
#결제
def u():
    end = Button(cash, text = '주문 마치기',command = cook)
    end.place(x = 550, y = 300)
#주문 마치고 cook실행->터틀
def cook():
    price.destroy()
    od_crust.destroy()
    cash.destroy()
    root.destroy()
    crust.destroy()
    turtle.setup(width = 700, height = 500)
    t = turtle.Turtle()
    t.ht()
    t.pensize(10)
    t.penup()
    t.goto(0,-200)
    t.color('brown')
    t.pendown()
    t.circle(200)
    t.seth(90)
    t.penup()
    t.forward(400)
    t.pendown()
    t.backward(400)
    t.penup()
    t.forward(200)
    t.seth(135)
    t.forward(200)
    t.pendown()
    t.backward(400)
    t.penup()
    t.forward(200)
    t.seth(180)
    t.forward(200)
    t.pendown()
    t.backward(400)
    t.penup()
    t.forward(200)
    t.seth(225)
    t.forward(200)
    t.pendown()
    t.backward(400)
    fi = tkinter.messagebox.showinfo('셀프 피자 가게', '주문하신 피자가 나왔습니다.\n        안녕히가세요')
    turtle.bye()
#터틀
re2 = Button(cash, text = '이전으로', command = trun2)
re2.place( x = 30, y = 300)
cash_price = Label(cash, text = '결제하실 금액은 0원입니다', font = 'Arial 20')
cash_price.place(x = 150, y = 100)
please = Label(cash, text = '금액을 입력해주세요')
please.place(x = 260, y=170)
go_cash = Button(cash, text = '결제하기', command = pay)
go_cash.place( x = 375, y = 195)
jan = Label(cash, text = '')
jan.place(x = 260, y = 240)
#이전으로->trun

def print_price():
    global total_price
    topping_price.configure(text = str(total_price)+'원')
    crust_price.configure(text = str(total_price)+'원')
    cash_price.configure(text = '결제하실 금액은 '+ str(total_price) + '원입니다')

textarea = Text(price)
textarea.pack()
crust_text = Text(od_crust)
crust_text.pack()
cash_text = Entry(cash, width = 12)
cash_text.place(x = 275, y = 200)
cash_text.bind('<Return>', pay2)
