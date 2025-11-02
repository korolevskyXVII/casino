from tkinter import *
from random import *
from tkinter import messagebox

root = Tk()

# Раздел функций


def rolling():
    rolling1 = randint(1, 4)
    rolling2 = randint(1, 4)
    rolling3 = randint(1, 4)
    rolling4 = randint(1, 4)
    if rolling1 == 1:
        lab_1slot["image"] = img_apple
    elif rolling1 == 2:
        lab_1slot["image"] = img_pear
    elif rolling1 == 3:
        lab_1slot["image"] = img_blackberry
    else:
        lab_1slot["image"] = img_banan
    if rolling2 == 1:
        lab_2slot["image"] = img_apple
    elif rolling2 == 2:
        lab_2slot["image"] = img_pear
    elif rolling2 == 3:
        lab_2slot["image"] = img_blackberry
    else:
        lab_2slot["image"] = img_banan
    if rolling3 == 1:
        lab_3slot["image"] = img_apple
    elif rolling3 == 2:
        lab_3slot["image"] = img_pear
    elif rolling3 == 3:
        lab_3slot["image"] = img_blackberry
    else:
        lab_3slot["image"] = img_banan
    if rolling4 == 1:
        lab_4slot["image"] = img_apple
    elif rolling4 == 2:
        lab_4slot["image"] = img_pear
    elif rolling4 == 3:
        lab_4slot["image"] = img_blackberry
    else:
        lab_4slot["image"] = img_banan


# Главное окно

root.title("КАЗИНО ОФФЛАЙН (НЕ СКАМ)))))")
# root.attributes('-fullscreen', True)
root.geometry("1000x800+220+100")
root.resizable(False, False)
root["bg"] = "#E0FFFF"


# Импорт картинок
img_apple = PhotoImage(file="Image\pple.png")
img_pear = PhotoImage(file="Image\pear.png")
img_banan = PhotoImage(file="Image\scl.png")
img_blackberry = PhotoImage(file="Image\i.png")

# Кнопки/картинки
lab_1slot = Label(root, image=img_apple, bg="#E0FFFF")
lab_1slot.place(x=350, y=400)
lab_2slot = Label(root, image=img_pear, bg="#E0FFFF")
lab_2slot.place(x=150, y=400)
lab_3slot = Label(root, image=img_banan, bg="#E0FFFF")
lab_3slot.place(x=550, y=400)
lab_4slot = Label(root, image=img_blackberry, bg="#E0FFFF")
lab_4slot.place(x=750, y=400)
btn_roll = Button(
    root,
    bg="#4169E1",
    text="ROLL",
    width=11,
    height=2,
    font=("times_new_roman", 16, "bold"),
    command=rolling,
)
btn_roll.place(x=435, y=650)
