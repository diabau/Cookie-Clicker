from tkinter import * 

fenetre = Tk()

fichier = open("save/data.txt", "a+")

imagecookie = PhotoImage(file="assets/cookie.png")

fenetre.geometry("500x500")


fichier.seek(0)  # place le curseur au début du fichier

data = fichier.read()
if data: 
    cookie = int(data) 

def onclick():
    global cookie
    cookie += 1
    print(cookie)
    counter.config(text='Nombre de cookies : ' + str(cookie))

def quitandsave():
    fichier.seek(0) 
    fichier.truncate()  # permet d'arrondir la valeur
    fichier.write(str(cookie))
    fenetre.destroy()

fenetre.protocol("WM_DELETE_WINDOW", quitandsave) # permet d'executer la fonction quitandsave lors de la fermeture de la fenetre

counter = Label(fenetre, text='Nombre de cookies : ' + str(cookie))
counter.pack()    

bouttoncookie=Button(fenetre, image=imagecookie, command=onclick)
bouttoncookie.pack()

fenetre.mainloop()
fichier.close()
