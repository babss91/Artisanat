from django.db import models

class Artisanat():
    ARTISANATS = [
        {
            "id": 1, "category": "bois", "img_category":"bois",
            "description":"je suis dans la ville de 1....",
            "produits":[
                {
                    "id":1, "nom":"chombo", "img_nom":"chombo", "prix": 33,
                    "description":"blabala balab alabalan anla  nabala ablaba ablaba labalaa"
                }
            ]
        },
        {
            "id": 2, "category": "drap ", "img_category":"drap",
            "description":"je suis dans la ville de 2...."
            
        },
        {
            "id": 3, "category": "accessoires", "img_category":"accessoires", 
            "description":"je suis dans la ville de 3...."
        },
        {
            "id": 4, "category": "decoration", "img_category":"decoration", 
            "description":"je suis dans la ...."
        }
   
    ]

    @classmethod
    def all(cls):
        return cls.ARTISANATS

    @classmethod
    def find(cls, id):
        return cls.ARTISANATS[int(id) - 1]
    