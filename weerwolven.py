import random
from tkinter import *
from tkinter import ttk
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

    menubar = Menu(scherm)
    menu.add_cascade(label='Informatie')
    menubar.add_cascade(label="File", menu=menu)
    scherm.config(menu=menubar)

    frame = Frame(scherm, bg='#E2E2E2')
    frame.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

    info_label = Label(frame, text="Druk op Speel weerwolven om te spelen", bg="#E2E2E2", font=('bold', 14))
    info_label.place(relx=0.0, rely=0.5)

    speelbutton = ttk.Button(frame, text="Speel weerwolven", command=lambda:invoeren_spelers(scherm))
    speelbutton.place(relx=0.433, rely=0.5)

    afsluitbutton = ttk.Button(frame, text="Afsluiten", command=sys.exit)
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

    entry = ttk.Entry(frame)
    entry.focus_force()
    entry.place(relx=0.37, rely=0.23)
    submit_button = ttk.Button(frame, text="Voeg de speler toe",
                           command=lambda: definieer_speler(entry.get()))
    submit_button.place(relx=0.52, rely=0.2, width=120)

    verwijder_button = ttk.Button(frame, text="Verwijder speler", command=lambda: verwijder_speler(entry.get()))
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

    x = 0
    volgendebutton = ttk.Button(frame, text="volgende", command=lambda:initialiseren_spel(scherm, x))
    volgendebutton.place(relx=0.9, rely=0.2)

    borderframe = Frame(scherm, bg="#808487")
    borderframe.place(relx=0.25, rely=0.245, relwidth=0.205, relheight=0.51, anchor='n')
    frame1 = Frame(scherm, bg="#808487")
    frame1.place(relx=0.25, rely=0.25, relwidth=0.2, relheight=0.5, anchor='n')

    spelerlabel = Label(frame1, text="Deze spelers doen mee", bg='#808487', font=('bolt', 12))
    spelerlabel.pack(side=TOP)
    spelerbox = Listbox(frame1, width=40, height=20,bg="#E2E2E2")
    spelerbox.pack()
    checkbutton = ttk.Button(frame, text='Welke spelers doen er mee?',
                         command=lambda: check_spelers(spelerbox, spelerlabel))
    checkbutton.place(relx=0.1, rely=0.2)
    borderframe = Frame(scherm, bg="#808487")
    borderframe.place(relx=0.5, rely=0.245, relwidth=0.205, relheight=0.51, anchor='n')
    frame2 = Frame(scherm, bg="#808487")
    frame2.place(relx=0.5, rely=0.25, relwidth=0.2, relheight=0.5, anchor='n')

    listboxborder = Frame(scherm, bg='#808487')
    listboxborder.place(relx=0.75, rely=0.245, relwidth=0.205, relheight=0.51, anchor='n')
    listboxframe = Frame(scherm, bg='#808487')
    listboxframe.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.5, anchor='n')

    infolabel_toevoegen_rol = Label(listboxframe, text="Rollen toevoegen", bg='#808487', font=('bolt', 12))
    infolabel_toevoegen_rol.pack(side=TOP)
    l = Listbox(listboxframe, selectmode='multiple', width=40, height=30, bg="#E2E2E2")
    x = 0
    for i in rollen:
        l.insert(x, i)
        x += x
    l.pack()

    infolabel_toegevoegde_rollen = Label(frame2, text="Deze rollen doen mee", bg='#808487', font=('bolt', 12))
    infolabel_toegevoegde_rollen.pack(side=TOP)
    listboxrollen = Listbox(frame2, height=40, width=40, bg="#E2E2E2")
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

    voeg_rol_toe_button = ttk.Button(frame, text="Voeg de rollen toe",
                                 command=voeg_rollen_toe, width=20)
    voeg_rol_toe_button.place(relx=0.7, rely=0.2)

    verwijder_rollen_button = ttk.Button(frame, text="Leeg lijst",
                                     command=lambda: rollen_verwijderen(listboxrollen), width=20)
    verwijder_rollen_button.place(relx=0.7, rely=0.6)

    check_rollen_button = ttk.Button(frame,
                                 text="Welke rollen doen mee?",
                                 command=lambda: check_rollen(listboxrollen, infolabel_toegevoegde_rollen)
                                   , width=24)
    check_rollen_button.place(relx=0.1, rely=0.6)


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


def initialiseren_spel(scherm, x):
    rollen = lees_uit_bestand('rollen.txt')
    spelers = lees_uit_bestand('weerwolf.txt')
    if x == 0:
        combinatie = combineer_rol_speler(spelers, rollen)
        sla_rol_speler_op(combinatie)
    else:
        combinatie = lees_combinatie_uit_bestand()

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
                else:
                    pass

        if waarde == 'Weerwolf':
            x = 1
            for widget in scherm.winfo_children():
                widget.destroy()

            foto1 = Image.open("images-weerwolves/weerwolf.jpg")
            foto1 = ImageTk.PhotoImage(foto1)

            label1 = Label(scherm, image=foto1)
            label1.pack()
            label1.image = foto1
            terugbutton = ttk.Button(scherm, text='ok', command=lambda: initialiseren_spel(scherm, x))
            terugbutton.pack()
        elif waarde == 'Burger':
            x = 1
            for widget in scherm.winfo_children():
                widget.destroy()

            foto1 = Image.open("images-weerwolves/burger.jpg")
            foto1 = ImageTk.PhotoImage(foto1)

            label1 = Label(scherm, image=foto1)
            label1.pack()
            label1.image = foto1
            terugbutton = ttk.Button(scherm, text='ok', command=lambda: initialiseren_spel(scherm, x))
            terugbutton.pack()
        elif waarde == 'Heks':
            x = 1
            for widget in scherm.winfo_children():
                widget.destroy()

            foto1 = Image.open("images-weerwolves/heks.jpg")
            foto1 = ImageTk.PhotoImage(foto1)

            label1 = Label(scherm, image=foto1)
            label1.pack()
            label1.image = foto1
            terugbutton = ttk.Button(scherm, text='ok', command=lambda: initialiseren_spel(scherm, x))
            terugbutton.pack()
        elif waarde == 'Ziener':
            x = 1
            for widget in scherm.winfo_children():
                widget.destroy()

            foto1 = Image.open("images-weerwolves/ziener.jpg")
            foto1 = ImageTk.PhotoImage(foto1)

            label1 = Label(scherm, image=foto1)
            label1.pack()
            label1.image = foto1
            terugbutton = ttk.Button(scherm, text='ok', command=lambda:initialiseren_spel(scherm, x))
            terugbutton.pack()
        elif waarde == 'Jager':
            x = 1
            for widget in scherm.winfo_children():
                widget.destroy()

            foto1 = Image.open("images-weerwolves/jager.jpg")
            foto1 = ImageTk.PhotoImage(foto1)

            label1 = Label(scherm, image=foto1)
            label1.pack()
            label1.image = foto1
            terugbutton = ttk.Button(scherm, text='ok', command=lambda: initialiseren_spel(scherm, x))
            terugbutton.pack()
        elif waarde == 'Cupido':
            x = 1
            for widget in scherm.winfo_children():
                widget.destroy()

            foto1 = Image.open("images-weerwolves/cupido.jpg")
            foto1 = ImageTk.PhotoImage(foto1)

            label1 = Label(scherm, image=foto1)
            label1.pack()
            label1.image = foto1
            terugbutton = ttk.Button(scherm, text='ok', command=lambda: initialiseren_spel(scherm, x))
            terugbutton.pack()
        elif waarde == 'Het onschuldige meisje':
            x = 1
            for widget in scherm.winfo_children():
                widget.destroy()

            foto1 = Image.open("images-weerwolves/onschuldigmeisje.jpg")
            foto1 = ImageTk.PhotoImage(foto1)

            label1 = Label(scherm, image=foto1)
            label1.pack()
            label1.image = foto1
            terugbutton = ttk.Button(scherm, text='ok', command=lambda: initialiseren_spel(scherm, x))
            terugbutton.pack()

    wiedoenermeelabel = Label(frame1, text="Spelers", bg='white')
    wiedoenermeelabel.pack(side=TOP, anchor='w')

    x = 1
    for speler in spelers:
        spelerlabel = Label(frame1, text=str(x) + ' ' + speler, bg='white')
        spelerlabel.pack(side=TOP, anchor='w')
        x+=1

    controle_knop = ttk.Button(frame1, text="Bevestig",
                               command=lambda: check_speler_rol(combinatie, speler_entry.get()))
    controle_knop.pack(side=BOTTOM, anchor='s')
    speler_entry = ttk.Entry(frame1, text="Voer de speler in")
    speler_entry.pack(side=BOTTOM)


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
    print(spelers_rollen)
    return spelers_rollen


def sla_rol_speler_op(combinatie):
    with open('combinatie.txt', 'w') as file:
        for comb in combinatie:
            for i in comb:
                file.write(i + ',' + comb[i] + ';')


def lees_combinatie_uit_bestand():
    combinatie = []
    with open('combinatie.txt', 'r') as file:
        data = file.read()
        data = data[0:-1]
        combinatielijst = data.split(';')
        for combinaties in combinatielijst:
            combi_lst = combinaties.split(',')
            combi_dct = {combi_lst[0]:combi_lst[1]}
            combinatie.append(combi_dct)
    return combinatie


def main():
    hoofdmenu()


if __name__ == '__main__':
    main()
