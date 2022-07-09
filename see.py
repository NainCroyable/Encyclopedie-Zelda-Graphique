import tkinter as tk
import requests

class page_see:

    def __init__(self, name):
        self.color = "#FFFFFF"

        self.obtenir_infos(name)

        # on créeeeeeez la fenetre tkinter
        self.fenetre = tk.Toplevel()
        self.fenetre.geometry("800x400")
        self.fenetre.title("Zelda Encyclopedia - "+self.name)
        self.fenetre.resizable(width=True, height=True)
        self.fenetre.config(bg=self.color)

        # boite principale
        self.main_frame = tk.Frame(self.fenetre, background=self.color)

        # boite droite
        self.frame = tk.Frame(self.main_frame, background=self.color)

        label_name = tk.Label(self.frame, text=self.name+" :", background=self.color, font=('Times', '40', 'bold'))
        label_name.pack()

        label_category = tk.Label(self.frame, text="category : "+self.category, background=self.color, justify="left")
        label_category.pack()

        if self.locations != None:
            label_locations = tk.Label(self.frame, text="common locations : "+self.locations, background=self.color, justify="left")
            label_locations.pack()
        
        if self.drops != None:
            label_drops = tk.Label(self.frame, text="drops : "+self.drops, background=self.color, justify="left")
            label_drops.pack()

        if self.attack != None:
            label_attack = tk.Label(self.frame, text="attack : "+str(self.attack), background=self.color, justify="left")
            label_attack.pack()
        
        if self.defense != None:
            label_defense = tk.Label(self.frame, text="defense : "+str(self.defense), background=self.color, justify="left")
            label_defense.pack()
        
        if self.hearts != None:
            label_hearts = tk.Label(self.frame, text="hearts : "+str(self.hearts), background=self.color, justify="left")
            label_hearts.pack()
        
        if self.effect != None:
            label_effect = tk.Label(self.frame, text="effects : "+str(self.effect), background=self.color, justify="left")
            label_effect.pack()

        # image
        self.download_image()
        self.img_width = 300
        self.img_height = 300
        self.image = tk.PhotoImage(file="image.png").zoom(35).subsample(32)
        self.canvas = tk.Canvas(self.main_frame, width=self.img_width, height=self.img_height, bg='#4065A4', bd=0, highlightthickness=0)
        self.canvas.create_image(self.img_width/2, self.img_height/2, image=self.image)
        self.canvas.grid(row=0, column=0)

        # afficher
        self.main_frame.pack(expand=True)
        self.frame.grid(row=0, column=1)
        self.fenetre.mainloop()
    
    def obtenir_infos(self, searched):
        one = requests.get(f"https://botw-compendium.herokuapp.com/api/v2/entry/{searched}")

        f = one.json()

        if f["data"] != {}:
            data = f["data"]

            self.name = searched
            category = data["category"]
            locations_text = None
            drops_text = None
            attack = None
            defense = None
            effect = None
            hearts = None

            if category == "creatures" or category == "monster":

                try: 
                    f = data["common_locations"] 
                except KeyError: 
                    data["common_locations"] = None

                if data["common_locations"] != None:
                    locations = list(data["common_locations"])
                else:
                    locations = ["None"]
                locations_text = ""

                try: 
                    f = data["drops"] 
                except KeyError: 
                    data["drops"] = None

                if data["drops"] != None:
                    drops = list(data["drops"])
                else:
                    drops = ["None"]
                drops_text = None

                url_image = data["image"]

                for y in range(len(locations)):
                    locations_text += locations[y]
                    locations_text += ", "
                
                drops_text = ""
                for y in range(len(drops)):
                    drops_text += drops[y]
                    drops_text += ", "

                
            elif category == "equipment":
                try: 
                    locations = list(data["common_locations"])
                except TypeError: 
                    locations = []
                locations_text = ""
                url_image = data["image"]
                attack = data["attack"]
                defense = data["defense"]

                for y in range(len(locations)):
                    locations_text += locations[y]
                    locations_text += ", "
                
            elif category == "materials":
                locations = list(data["common_locations"])
                locations_text = ""
                url_image = data["image"]
                effect = data["cooking_effect"]
                hearts = data["hearts_recovered"]

                for y in range(len(locations)):
                    locations_text += locations[y]
                    locations_text += ", "
                
                
            else:
                if data["common_locations"] != None:
                    locations = list(data["common_locations"])
                else:
                    locations = []
                locations_text = ""
                url_image = data["image"]
                drops = list(data["drops"])
                drops_text = ""
                
                for y in range(len(drops)):
                    drops_text += drops[y]
                    drops_text += ", "

                for y in range(len(locations)):
                    locations_text += locations[y]
                    locations_text += ", "
                
            self.url = url_image
            self.category = category
            self.locations = locations_text
            self.drops = drops_text
            self.attack = attack
            self.defense = defense
            self.effect = effect
            self.hearts = hearts
            
            if self.drops == "" or self.drops == " ":
                self.drops = None

            print(self.url)
    
    def download_image(self):
        print("download ...")

        img_data = requests.get(self.url).content
        with open('image.png', 'wb') as handler:
            handler.write(img_data)
