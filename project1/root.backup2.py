from tkinter import*
from random import*
from tkinter import messagebox
import time

root = Tk()
#переменные монет
money = 1000

#Раздел функций









def broll(event):
    global s
    time.sleep(0.155)
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

    if rolling1 == rolling2 == rolling3 == rolling4:
        s = str(s)
        f = open('results.txt', 'a')
        f.write('Победитель: ')
        f.write(s)
        f.write('\n')
        print("файл изменен")

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

root.title("КАЗИНО ОФФЛАЙН (НЕ СКАМ)))))")
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



btn_roll.bind('<space>' , broll)

btn_roll.pack_forget() 









root.mainloop()


