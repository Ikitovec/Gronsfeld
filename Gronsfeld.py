from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox

def clicked():
    txt_original = txt.get("1.0", 'end-1c')
    txt2.delete(1.0, END)
    eng_upp_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rus_upp_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    signs='0123456789'
    temp_flag=0
    step=txt3.get("1.0", 'end-1c')
    for i in step:
        if signs.find(i,0)==-1:
            temp_flag=1
            messagebox.showinfo('Ошибка!', f'В графе сдвиг должны быть только числа!')
            break

    if temp_flag==0:
        if len(step)!=0:
            e=0
            for i in txt_original:
                index = -5
                for j in range(0, 1):
                    index = eng_upp_alphabet.find(i, 0)
                    if (index != -1):
                        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        alphabet_size = 26
                        break
                    if (index == -1):
                        index = eng_low_alphabet.find(i, 0)
                        if (index != -1):
                            alphabet = 'abcdefghijklmnopqrstuvwxyz'
                            alphabet_size = 26
                            break
                        if (index == -1):
                            index = rus_upp_alphabet.find(i, 0)
                            if (index != -1):
                                alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                                alphabet_size = 33
                                break
                            if (index == -1):
                                index = rus_low_alphabet.find(i, 0)
                                if (index != -1):
                                    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                    alphabet_size = 33
                                    break
                                # if (index != '/n'):
                                #    messagebox.showinfo('Ошибка!', f'Вы ввели неизвестный символ!)')
                if index == -1:
                    txt2.insert(INSERT, i)

                else:
                    if ((combo2.get()=='Зашифровать') | (combo2.get()=='Расшифровать')):

                        if combo2.get()=='Зашифровать':

                            txt2.insert(INSERT, alphabet[(index + (int(step[e% len(step)]) )) % alphabet_size])
                            e+=1
                        if combo2.get() == 'Расшифровать':
                            txt2.insert(INSERT, alphabet[(index - (int(step[e% len(step)]) )) % alphabet_size])
                            e += 1
                    else:
                        messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')
        else:
            messagebox.showinfo('Ошибка!', f'Сдвиг не должен быть пустым!')

def swap():
    temp = txt2.get("1.0", 'end-1c')
    txt.delete(1.0, END)
    txt.insert(INSERT, temp)
    txt2.delete(1.0, END)

window = Tk()
window.title("Шифр Гронсфельда")
window.geometry('500x250')

lbl = Label(window, text="Сдвиг")
lbl.grid(column=0, row=2)

txt3 = scrolledtext.ScrolledText(window, width=40, height=1)
txt3.grid(column=2, row=2)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=4)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=5)
lbl = Label(window)


btn = Button(window, text="Поменять значения", command=swap)
btn.grid(column=2, row=4)
lbl = Label(window)

lbl = Label(window, text="Ваше сообщение")
lbl.grid(column=0, row=0)

txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)


lbl = Label(window, text="Результат:")
lbl.grid(column=0, row=6)


txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=6)


window.mainloop()

