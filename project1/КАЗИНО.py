
from random import*
from tkinter import messagebox
import time

root = Tk()
#Переменные для подсчета денег

actuall_money = 1000
stavka_money = 10
s = None



#Раздел функций
def money10():
    global stavka_money , actuall_money
    stavka_money = stavka_money + 10
    stavka['text'] = stavka_money
def money100():
    global stavka_money , actuall_money
    stavka_money = stavka_money + 100
    stavka['text'] = stavka_money
def money1000():
    global stavka_money , actuall_money
    stavka_money = stavka_money + 1000
    stavka['text'] = stavka_money
def moneyx2():
    global stavka_money , actuall_money
    stavka_money = stavka_money * 2
    stavka['text'] = stavka_money
def moneyd2():
    global stavka_money , actuall_money
    stavka_money = stavka_money / 2
    stavka['text'] = stavka_money
def all_in():
    global stavka_money , actuall_money
    stavka_money = actuall_money
    stavka['text'] = stavka_money

    







def broll(event):
    global s , stavka_money , actuall_money
    time.sleep(0.33333333)
    rolling1 = randint(1 , 4)
    rolling2 = randint(1 , 4)
    rolling3 = randint(1 , 4)
    rolling4 = randint(1 , 4)
    if rolling1 == 1:
        lab_1slot['image'] = img_apple
    elif rolling1 == 2:
        lab_1slot['image'] = img_pear
    elif rolling1 == 3:
        lab_1slot['image'] = img_blackberry
    else:
        lab_1slot['image'] = img_banan
    if rolling2 == 1:
        lab_2slot['image'] = img_apple
    elif rolling2 == 2:
        lab_2slot['image'] = img_pear
    elif rolling2 == 3:
        lab_2slot['image'] = img_blackberry
    else:
        lab_2slot['image'] = img_banan
    if rolling3 == 1:
        lab_3slot['image'] = img_apple
    elif rolling3 == 2:
        lab_3slot['image'] = img_pear
    elif rolling3 == 3:
        lab_3slot['image'] = img_blackberry
    else:
        lab_3slot['image'] = img_banan
    if rolling4 == 1:
        lab_4slot['image'] = img_apple
    elif rolling4 == 2:
        lab_4slot['image'] = img_pear
    elif rolling4 == 3:
        lab_4slot['image'] = img_blackberry
    else:
        lab_4slot['image'] = img_banan

    if rolling1 == rolling2 == rolling3 == rolling4:                                                                            #win
        actuall_money = actuall_money + stavka_money * 10 + stavka_money
        actuallmoney1['text'] = actuall_money
        x = str(stavka_money * 10)
        s = str(s)
        f = open('results.txt', 'a')
        f.write(x)
        f.write(' rub win: ')
        f.write(s)
        f.write('\n')
        print("файл изменен")
        if s == None:
            f = open('results.txt', 'a')
            f.write(x)
            f.write(' rub win: ')
            f.write('NoName')
            f.write('\n')
            print("файл изменен")
    elif stavka_money > actuall_money:
        stavka['text'] = 'недостаточно средств'
        stavka_money = 0
    else:
        actuall_money = actuall_money - stavka_money
        actuallmoney1['text'] = actuall_money
    if rolling1 == rolling2 or rolling2 == rolling3 or rolling3 == rolling4:
        actuall_money = actuall_money + stavka_money
        actuallmoney1['text'] = actuall_money
    if rolling1 == rolling2 == rolling3 or rolling2 == rolling3 == rolling4:
        actuall_money = actuall_money + stavka_money * 2 + stavka_money
        actuallmoney1['text'] = actuall_money
#Регистрация
def regist():
    global s
    global reg2
    registr = Tk()
    registr.title("Регистрация")
    registr.geometry('600x500+220+100')
    registr.resizable(False, False)
    registr['bg'] = '#E0FFFF'
    reg1 = (Label(registr , bg = '#E0FFFF' , text = "Введите имя:", font = ('times_new_roman' , 18 , 'bold')))
    reg1.place(x = 100 , y = 100)
    reg2 = (Entry(registr, bg = '#E0FFFF' , fg = '#4169E1' , font = ('times_new_roman' , 24 , 'bold')))
    reg2.place(x = 100 , y = 150)
    reg3 = Button(registr, bg = "#4169E1", text = 'close: ' , width = 8 , height = 2 , font = ('times_new_roman' , 16 , 'bold'), command = lambda:registr.destroy())
    reg3.place(x = 110, y = 250)
    reg4 = Button(registr, bg = "#4169E1", text = 'confirm: ' , width = 8 , height = 2 , font = ('times_new_roman' , 16 , 'bold'), command = getname)
    reg4.place(x = 360, y = 250)
def getname():
    global reg2
    global s
    s = reg2.get()
    player['text'] = s
    
#Главное окно

root.title("")
#root.attributes('-fullscreen', True)
root.geometry('1000x800+220+100')
root.resizable(False, False)
root['bg'] = '#E0FFFF'


#Импорт картинок
img_apple = PhotoImage(file = 'Image\pple.png')
img_pear = PhotoImage(file = 'Image\pear.png')
img_banan = PhotoImage(file = 'Image\scl.png')
img_blackberry = PhotoImage(file = 'Image\i.png')

#Кнопки/картинки

lab_1slot = (Label(root, image = img_apple, bg = '#E0FFFF'))
lab_1slot.place(x = 350, y = 400)
lab_2slot = (Label(root, image = img_pear, bg = '#E0FFFF'))
lab_2slot.place(x = 150, y = 400)
lab_3slot = (Label(root, image = img_banan, bg = '#E0FFFF'))
lab_3slot.place(x = 550, y = 400)
lab_4slot = (Label(root , image = img_blackberry, bg = '#E0FFFF'))
lab_4slot.place(x = 750, y = 400)
btn_roll = Button(root, bg = "#4169E1", text = 'ROLL' , width = 0 , height = 0 , font = ('times_new_roman' , 16 , 'bold'))
btn_roll.place(x = 435 , y = 665)
btn_regist = Button(root, bg = "#4169E1", text = 'registration: ' , width = 12 , height = 2 , font = ('times_new_roman' , 16 , 'bold') , command = regist)
btn_regist.place(x = 750 , y = 35)
info = (Label(root, text = 'press tab ONCE and space to roll:       ' , bg = '#E0FFFF' , fg = '#4169E1' , font = ('times_new_roman' , 24 , 'bold')))
info.place(x = 275 , y = 665)
player = (Label(root , bg = '#E0FFFF' , text = 'NoName' , font = ('times_new_roman' , 18 , 'bold')))
player.place(x = 50 , y = 35)
stavka = (Label(root , bg = '#E0FFFF' , text = 'Ставка:   10' , font = ('times_new_roman' , 24 , 'bold')))
stavka.place(x = 375 , y = 135)
actuallmoney = (Label(root , bg = '#E0FFFF' , text = 'Ваши деньги: ',  font = ('times_new_roman' , 24 , 'bold')))
actuallmoney.place(x = 50 , y = 150)
actuallmoney1 = (Label(root , bg = '#E0FFFF' , text = actuall_money ,  font = ('times_new_roman' , 18)))
actuallmoney1.place(x = 100 , y = 200)
#Кнопки ставок
btn_mon10 = Button(root, bg = "#4169E1", text = '+10' , width = 5 , height = 1 , font = ('times_new_roman' , 20 , 'bold') , command = money10)
btn_mon10.place(x = 200 , y = 250)
btn_mon100 = Button(root, bg = "#4169E1", text = '+100' , width = 5 , height = 1 , font = ('times_new_roman' , 20 , 'bold') , command = money100)
btn_mon100.place(x = 300 , y = 250)
btn_mon1000 = Button(root, bg = "#4169E1", text = '+1000' , width = 5 , height = 1 , font = ('times_new_roman' , 20 , 'bold') , command = money1000)
btn_mon1000.place(x = 400 , y = 250)
btn_x2 = Button(root, bg = "#4169E1", text = 'x2' , width = 5 , height = 1 , font = ('times_new_roman' , 20 , 'bold') , command = moneyx2)
btn_x2.place(x = 500 , y = 250)
btn_d2 = Button(root, bg = "#4169E1", text = '%2' , width = 5 , height = 1 , font = ('times_new_roman' , 20 , 'bold') , command = moneyd2)
btn_d2.place(x = 600 , y = 250)
btn_all_in = Button(root, bg = "#4169E1", text = 'max' , width = 5 , height = 1 , font = ('times_new_roman' , 20 , 'bold') , command = all_in)
btn_all_in.place(x = 700 , y = 250)

btn_roll.bind('<space>' , broll)

btn_roll.pack_forget() 

root.mainloop()


