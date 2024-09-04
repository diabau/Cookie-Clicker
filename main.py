from tkinter import *
import os
import time
fenetre = Tk()
fenetre.title("Cookie Clicker")
fichier = open("save/data.txt", "a+")
fichier_mamie = open("save/mamie.txt", "a+")
imagecookie = PhotoImage(file="assets/cookie.png")
fenetre.iconbitmap("assets/cookie.ico")
fenetre.geometry("500x500")
fenetre.resizable(width=False, height=False)


fichier.seek(0)  # place le curseur au début du fichier
fichier_mamie.seek(0)

data = fichier.read()
cookie = int(data)
data_mamie = fichier_mamie.read()

def mamie(): 
    global cookie
    cookieseconde = 10 * int(data_mamie)
    cookie += cookieseconde
    counter.config(text='Nombre de cookies : ' + str(cookie))
    fenetre.after(10000, mamie)
    

def onclick():
    global cookie
    cookie += 1
    print(cookie)
    counter.config(text='Nombre de cookies : ' + str(cookie))

def quitandsave():
    fichier.seek(0) 
    fichier.truncate()  # permet d'arrondir la valeur
    fichier.write(str(cookie))
    fichier.close()
    fichier_mamie.close()
    fenetre.destroy()
    

def store():
    quitandsave()
    os.system('python store.py')


fenetre.protocol("WM_DELETE_WINDOW", quitandsave) # permet d'executer la fonction quitandsave lors de la fermeture de la fenetre

counter = Label(fenetre, text='Nombre de cookies : ' + str(cookie))
counter.pack()    

bouttoncookie=Button(fenetre, image=imagecookie, command=onclick)
bouttoncookie.pack()

counter_mamie = Label(fenetre, text='Nombre de mamie : ' + str(data_mamie))
counter_mamie.pack()
counter_mamie.place(x=0, y=475)

bouttonstore=Button(fenetre, text="store", command=store)
bouttonstore.pack()
bouttonstore.place(x=463, y=475)

fenetre.after(10000, mamie)
fenetre.mainloop()
fichier.close()
fichier_mamie.close()
