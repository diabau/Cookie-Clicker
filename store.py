import os
from tkinter import *

root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)
imagemamie = PhotoImage(file="assets/mamie.png")
root.title("Store")
root.iconbitmap("assets/cookie.ico")


fichier = open("save/data.txt", "a+")
fichier.seek(0)  # place le curseur au début du fichier
cookie = int(fichier.read())




fichier_mamie = open("save/mamie.txt", "a+")
fichier_mamie.seek(0)
data_mamie = fichier_mamie.read()
data_mamie = int(data_mamie)

def mamie(): 
    global cookie
    cookieseconde = 1 * int(data_mamie)
    cookie += cookieseconde
    counter.config(text='Nombre de cookies : ' + str(cookie))
    root.after(1000, mamie)

def achat():
    global cookie
    global data_mamie
    if cookie >= 500:
        cookie -= 500
        data_mamie += 1
        counter.config(text='Nombre de cookies : ' + str(cookie))
        counter_mamie.config(text='Nombre de mamie : ' + str(data_mamie))

def save():
    fichier_mamie = open("save/mamie.txt", "a+")
    fichier = open("save/data.txt", "a+")
    fichier.seek(0) 
    fichier.truncate()  # permet d'arrondir la valeur
    fichier.write(str(cookie))
    fichier_mamie.seek(0) 
    fichier_mamie.truncate()  # permet d'arrondir la valeur
    fichier_mamie.write(str(data_mamie))
    fichier.close()
    fichier_mamie.close()
    root.destroy()
    os.system('python3 main.py')
    
root.protocol("WM_DELETE_WINDOW", save) # permet d'executer la fonction quitandsave lors de la fermeture de la fenetre



counter = Label(root, text='Nombre de cookies : ' + str(cookie))
counter.pack()

counter_mamie = Label(root, text='Nombre de mamie : ' + str(data_mamie))
counter_mamie.pack()    

button_mamie=Button(root, image=imagemamie, command=achat)
Label(root, text='Acheté une mamie qui vous fera 1 cookie par seconde\n 500 cookie').pack()
button_mamie.pack()



root.after(1000, mamie)
fichier.close()
fichier_mamie.close()
root.mainloop()