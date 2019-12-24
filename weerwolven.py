import random
from tkinter import *
from PIL import ImageTk, Image
import sys

height = 677
width = 1200

def hoofdmenu():
    scherm = Tk()
    scherm.title("Weerwolven")
    menubar = Menu(scherm)
    canv = Canvas(scherm, width=width, height=height)
    canv.pack()
    menu = Menu(menubar, tearoff=0)
    menu.add_cascade(label='Informatie')
    menubar.add_cascade(label="File", menu=menu)

    foto = Image.open("weerwolven.jpg")
    foto = ImageTk.PhotoImage(foto)
    label = Label(scherm, image=foto)
    label.place(relwidth=1, relheight=1)

    frame = Frame(scherm, bg='#E2E2E2')
    frame.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

    info_label = Label(frame, text="Druk op Speel weerwolven om te spelen", bg="#E2E2E2", font=('bold', 14))
    info_label.place(relx=0.0, rely=0.5)

    speelbutton = Button(frame, text="Speel weerwolven", command=lambda:invoeren_spelers(scherm))
    speelbutton.place(relx=0.433, rely=0.5)

    afsluitbutton = Button(frame, text="Afsluiten", command=sys.exit)
    afsluitbutton.place(relx=0.6, rely=0.5)
    scherm.config(menu=menubar)
    scherm.mainloop()



def invoeren_spelers(scherm):
    rollen = ["Weerwolf", "Weerwolf", "Weerwolf", "Weerwolf", "Weerwolf", "Burger", "Burger", "Burger", "Burger",
              "Burger", "Burger", "Burger", "Burger", "Ziener", "Heks", "Jager", "Cupido",
              "Het onschuldige meisje", "Dief"]

    for widget in scherm.winfo_children():
        widget.destroy()

    canv = Canvas(scherm, width=width, height=height, bg="#2fcc4e")
    canv.pack()

    foto1 = Image.open("weerwolven.jpg")
    foto1 = ImageTk.PhotoImage(foto1)

    label = Label(scherm, image=foto1)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.image = foto1

    #frameborder = Frame(scherm, bg='black')
    #frameborder.place(relx=0.5, rely=0.846, relwidth=0.755, relheight=0.11, anchor='n')
    frame = Frame(scherm, bg='#E2E2E2')
    frame.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

    entry = Entry(frame, bd=5)
    entry.place(relx=0.37, rely=0.2)
    submit_button = Button(frame, text="Voeg de speler toe",
                           command=lambda: definieer_speler(entry.get()))
    submit_button.place(relx=0.52, rely=0.2, width=120)

    verwijder_button = Button(frame, text="Verwijder speler", command=lambda: verwijder_speler(entry.get()))
    verwijder_button.place(relx=0.52, rely=0.6, width=120)

    def check_spelers(spelerbox, spelerlabel):
        haal_rollen_uit_lijst(spelerbox)
        lijst = lees_uit_bestand('weerwolf.txt')
        lengte = len(lijst)
        spelerlabel['text'] = "Welke spelers doen er mee" + '(' + str(lengte) + ')'
        x = 0
        for i in lijst:
            spelerbox.insert(x, i)
            x = x + 1

    volgendebutton = Button(frame, text="volgende", command=lambda:initialiseren_spel(scherm))
    volgendebutton.place(relx=0.8, rely=0.2)

    borderframe = Frame(scherm, bg="red")
    borderframe.place(relx=0.25, rely=0.245, relwidth=0.205, relheight=0.51, anchor='n')
    frame1 = Frame(scherm, bg="red")
    frame1.place(relx=0.25, rely=0.25, relwidth=0.2, relheight=0.5, anchor='n')

    spelerlabel = Label(frame1, text="Deze spelers doen mee", bg='red', font=('bolt', 12))
    spelerlabel.pack(side=TOP)
    spelerbox = Listbox(frame1, width=40, height=20,bg="#ffa196")
    spelerbox.pack()
    checkbutton = Button(frame, text='Welke spelers doen er mee?',
                         command=lambda: check_spelers(spelerbox, spelerlabel))
    checkbutton.place(relx=0.1, rely=0.2)
    borderframe = Frame(scherm, bg="yellow")
    borderframe.place(relx=0.5, rely=0.245, relwidth=0.205, relheight=0.51, anchor='n')
    frame2 = Frame(scherm, bg="yellow")
    frame2.place(relx=0.5, rely=0.25, relwidth=0.2, relheight=0.5, anchor='n')

    listboxborder = Frame(scherm, bg='blue')
    listboxborder.place(relx=0.75, rely=0.245, relwidth=0.205, relheight=0.51, anchor='n')
    listboxframe = Frame(scherm, bg='blue')
    listboxframe.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.5, anchor='n')

    infolabel_toevoegen_rol = Label(listboxframe, text="Rollen toevoegen", bg='blue', font=('bolt', 12))
    infolabel_toevoegen_rol.pack(side=TOP)
    l = Listbox(listboxframe, selectmode='multiple', width=40, height=15, bg="#969fff")
    x = 0
    for i in rollen:
        l.insert(x, i)
        x += x
    l.pack()

    infolabel_toegevoegde_rollen = Label(frame2, text="Deze rollen doen mee", bg='yellow', font=('bolt', 12))
    infolabel_toegevoegde_rollen.pack(side=TOP)
    listboxrollen = Listbox(frame2, height=20, width=40, bg="#fdff91")
    listboxrollen.pack()

    def voeg_rollen_toe():
        rollen = lees_uit_bestand('rollen.txt')
        clicked_items = l.curselection()
        for item in clicked_items:
            rollen.append(l.get(item))
        sla_rollen_op(rollen)

    def verwijder_rollen():
        rollen = []
        sla_rollen_op(rollen)

    def check_rollen(listboxrollen, infolabel_toegevoegde_rollen):

        haal_rollen_uit_lijst(listboxrollen)
        lijst = lees_uit_bestand('rollen.txt')
        lengte = len(lijst)
        infolabel_toegevoegde_rollen['text'] = "Deze rollen doen mee" + '(' + str(lengte) + ')'
        x = 0
        for i in lijst:
            listboxrollen.insert(x, i)
            x = x + 1

    voeg_rol_toe_button = Button(listboxframe, text="Voeg de rollen toe",
                                 command=voeg_rollen_toe, width=40, bg="#969fff")
    voeg_rol_toe_button.pack(side=TOP)

    verwijder_rollen_button = Button(listboxframe, text="Start opnieuw met toevoegen",
                                     command=lambda: rollen_verwijderen(listboxrollen), width=40, bg="#969fff")
    verwijder_rollen_button.pack(side=TOP)

    check_rollen_button = Button(listboxframe,
                                 text="Welke rollen doen er mee",
                                 command=lambda: check_rollen(listboxrollen, infolabel_toegevoegde_rollen)
                                 , width=40, bg="#969fff")
    check_rollen_button.pack(side=TOP)

    def haal_rollen_uit_lijst(listboxrollen):
        listboxrollen.delete(0, END)


    def rollen_verwijderen(listboxrollen):
        haal_rollen_uit_lijst(listboxrollen)
        verwijder_rollen()

    def verwijder_speler(speler):
        speler = speler.capitalize()
        lijst = lees_uit_bestand('weerwolf.txt')
        lijst.remove(speler)
        sla_lijst_op(lijst)

def initialiseren_spel(scherm):
    rollen = lees_uit_bestand('rollen.txt')
    spelers = lees_uit_bestand('weerwolf.txt')
    combinatie = combineer_rol_speler(spelers, rollen)

    for widget in scherm.winfo_children():
        widget.destroy()

    canv = Canvas(scherm, width=width, height=height, bg="#2fcc4e")
    canv.pack()

    foto1 = Image.open("weerwolven.jpg")
    foto1 = ImageTk.PhotoImage(foto1)

    label = Label(scherm, image=foto1)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.image = foto1

    frameborder = Frame(scherm, bg="green")
    frameborder.place(relx=0.5, rely=0.095, relheight=0.81, relwidth=0.505, anchor='n')
    frame1 = Frame(scherm, bg="white")
    frame1.place(relx=0.5, rely=0.1, relheight=0.8, relwidth=0.5, anchor='n')

    def check_speler_rol(combinatie, knoptext):
        for comb in combinatie:
            for key in comb:
                if key == knoptext:
                    waarde = comb[key]
                    speler_bevestiging(waarde)

    def speler_bevestiging(waarde):
        spelerscherm = Tk()
        spelerscherm.title(waarde)


        if waarde == 'Burger':
            label = Label(spelerscherm, text=waarde)
            label.pack()
        elif waarde == 'Weerwolf':
            weerwolflabel.pack(x=0, y=0, relwidth=1, relheight=1)

        elif waarde == 'Heks':
            label = Label(spelerscherm, text=waarde)
            label.pack()
        elif waarde == 'Ziener':
            label = Label(spelerscherm, text=waarde)
            label.pack()
        elif waarde == 'Jager':
            label = Label(spelerscherm, text=waarde)
            label.pack()
        elif waarde == 'Cupido':
            label = Label(spelerscherm, text=waarde)
            label.pack()
        elif waarde == 'Het onschuldige meisje':
            label = Label(spelerscherm, text=waarde)
            label.pack()


    def toon_burger():
        pass


    #def toon_weerwolf(weerwolflabel):
       # weerwolflabel.place(x=0, y=0, relwidth=1, relheight=1)



    def toon_heks():
        heksenscherm = Tk()
        foto1 = Image.open("weerwolven.jpg")
        foto1 = ImageTk.PhotoImage(foto1)

        label = Label(heksenscherm, image=foto1)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.image = foto1

    def toon_ziener():
        zienerscherm = Tk()
        foto1 = Image.open("weerwolven.jpg")
        foto1 = ImageTk.PhotoImage(foto1)

        label = Label(zienerscherm, image=foto1)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.image = foto1

    def toon_jager():
        jagerscherm = Tk()
        foto1 = Image.open("weerwolven.jpg")
        foto1 = ImageTk.PhotoImage(foto1)

        label = Label(jagerscherm, image=foto1)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.image = foto1

    def toon_cupido():
        cupidoscherm = Tk()
        foto1 = Image.open("weerwolven.jpg")
        foto1 = ImageTk.PhotoImage(foto1)

        label = Label(cupidoscherm, image=foto1)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.image = foto1

    def toon_meisje():
        meisjescherm = Tk()
        foto1 = Image.open("weerwolven.jpg")
        foto1 = ImageTk.PhotoImage(foto1)

        label = Label(meisjescherm, image=foto1)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.image = foto1

    x = 1
    for speler in spelers:
        spelerlabel = Label(frame1, text=str(x) + ' ' + speler, bg='white')
        spelerlabel.pack()
        x+=1

    speler_entry = Entry(frame1, text="Voer de speler in")
    speler_entry.pack(side=LEFT, anchor='s')
    controle_knop = Button(frame1, text="Bevestig", command=lambda: check_speler_rol(combinatie, speler_entry.get()))
    controle_knop.pack(side=LEFT, anchor='s')

def definieer_speler(speler):
    speler = speler.capitalize()
    spelerlijst = lees_uit_bestand("weerwolf.txt")
    spelerlijst.append(speler)
    sla_lijst_op(spelerlijst)

def lees_uit_bestand(bestand):
    spelerlijst = []
    with open(bestand, "r") as file:
        data = file.read()
        data = data.split(',')
        for i in data:
            if i != '':
                spelerlijst.append(i)
    return spelerlijst

def sla_lijst_op(spelerlijst):
    with open("weerwolf.txt", "w") as file:
        for speler in spelerlijst:
            file.write(speler + ",")

def sla_rollen_op(spelerlijst):
    with open("rollen.txt", "w") as file:
        for speler in spelerlijst:
            file.write(speler + ",")

def combineer_rol_speler(spelers, rollen):
    spelers_rollen = []
    rollen = random.sample(rollen, len(rollen))
    i = 0
    for speler in spelers:
        dict = {speler: rollen[i]}
        spelers_rollen.append(dict)
        i = i + 1
    return spelers_rollen

def main():
    hoofdmenu()

if __name__ == '__main__':
    main()
