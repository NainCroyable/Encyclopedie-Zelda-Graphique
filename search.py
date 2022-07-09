from functools import partial
import tkinter as tk
import requests

class page_search:

    def __init__(self):
        self.list_result = []

        self.color = "#FFFFFF"

        # on créeeeeeez la fenetre tkinter
        self.fenetre = tk.Tk()
        self.fenetre.geometry("300x600")
        self.fenetre.title("Zelda Encyclopedia - Search")
        self.fenetre.resizable(width=True, height=True)
        self.fenetre.config(bg=self.color)

        # boite pour txt et bouton valider
        self.frame_search = tk.Frame(self.fenetre, background=self.color)
        self.frame_search.pack(expand=True)


        # ajouter une entrée pour ecrire
        self.entree_recherche = tk.Entry(self.frame_search)
        self.entree_recherche.bind('<Return>', self.rechercher)
        self.entree_recherche.focus()
        self.entree_recherche.pack()

        # bouton pour valider
        bouton = tk.Button(self.frame_search, text="Valider", command=partial(self.rechercher, "idsqohcuhcq"))
        bouton.pack()

        self.afficher()


    def afficher(self):

        # boite
        self.frame = tk.Frame(self.fenetre, background=self.color)
        self.frame.pack(expand=True)

        result_label = []
        for t in range(len(self.list_result)):
            result_label.append(tk.Button(self.frame, text=self.list_result[t], command=partial(self.ouvrir, self.list_result[t])))
            print(self.list_result[t])
            result_label[t].pack()

        self.fenetre.mainloop()
    
    def rechercher(self, recherche=None):
        if recherche != None:

            searched = self.entree_recherche.get()

            all = requests.get("https://botw-compendium.herokuapp.com/api/v2/all").json()
            list_result = []
            
            creatures = all["data"]["creatures"]
            for u in range(len(creatures["food"])):
                if searched in creatures["food"][u]["name"]:
                    list_result.append(creatures["food"][u]["name"])
            
            for u in range(len(creatures["non_food"])):
                if searched in creatures["non_food"][u]["name"]:
                    list_result.append(creatures["non_food"][u]["name"])
            
            equipment = all["data"]["equipment"]
            for u in range(len(equipment)):
                if searched in equipment[u]["name"]:
                    list_result.append(equipment[u]["name"])
            
            material = all["data"]["materials"]
            for u in range(len(material)):
                if searched in material[u]["name"]:
                    list_result.append(material[u]["name"])
                    
            
            monster = all["data"]["monsters"]
            for u in range(len(monster)):
                if searched in monster[u]["name"]:
                    list_result.append(monster[u]["name"])
            
            treasure = all["data"]["treasure"]
            for u in range(len(treasure)):
                if searched in treasure[u]["name"]:
                    list_result.append(treasure[u]["name"])

            self.list_result = list_result
            print(self.list_result)
            self.afficher()

    
    def ouvrir(self, nom):
        from see import page_see
        self.page = []
        self.page.append(page_see(nom))
