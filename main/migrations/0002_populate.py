from django.db import migrations


def populate_tables(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Quantity = apps.get_model("main", "Quantity")
    Unit = apps.get_model("main", "Unit")
    Ingredient = apps.get_model("main", "Ingredient")
    Tag = apps.get_model("main", "Tag")
    Cocktail = apps.get_model("main", "Cocktail")
    CocktailIngredient = apps.get_model("main", "CocktailIngredient")
    user = User.objects.first()
    quantities = [
        # fmt: off
        # quantity_type, label, value, min_value, max_value, step
        (1, "1", 1, None, None, None,),  # float
        (1, "10", 10, None, None, None,),  # float
        (1, "11", 11, None, None, None,),  # float
        (1, "12", 12, None, None, None,),  # float
        (1, "13", 13, None, None, None,),  # float
        (1, "14", 14, None, None, None,),  # float
        (1, "17", 17, None, None, None,),  # float
        (1, "18", 18, None, None, None,),  # float
        (1, "2", 2, None, None, None,),  # float
        (1, "20", 20, None, None, None,),  # float
        (1, "22", 22, None, None, None,),  # float
        (1, "25", 25, None, None, None,),  # float
        (1, "3", 3, None, None, None,),  # float
        (1, "4", 4, None, None, None,),  # float
        (1, "5", 5, None, None, None,),  # float
        (1, "50", 50, None, None, None,),  # float
        (1, "6", 6, None, None, None,),  # float
        (1, "7", 7, None, None, None,),  # float
        (1, "75", 75, None, None, None,),  # float
        (1, "8", 8, None, None, None,),  # float
        (1, "9", 9, None, None, None,),  # float
        (1, "0,5", 0.5, None, None, None,),  # float
        (1, "1,5", 1.5, None, None, None,),  # float
        (1, "2,5", 2.5, None, None, None,),  # float
        (1, "un", 1, None, None, None,),  # float
        (1, "1 demi", 0.5, None, None, None,),  # float
        (1, "3,5", 3.5, None, None, None,),  # float
        (1, "4,5", 4.5, None, None, None,),  # float
        (1, "5,5", 5.5, None, None, None,),  # float
        (1, "demi", 0.5, None, None, None,),  # float
        (1, "1 ou 2", 1, 2, 1, None,),  # float
        (2, "2-3", None, 2, 3, None,),  # either
        (2, "2 ou 3", None, 2, 3, None,),  # either
        (2, "3 ou 4", None, 3, 4, None,),  # either
        (2, "4 ou 5", None, 4, None, None,),  # either
        (2, "7 ou 8", None, 7, 8, None,),  # either
        (3, "5 à 7", None, 5, 7, 1.0,),  # interval
        (3, "7 à 10", None, 7, 10, 1.0,),  # interval
        (3, "7 à 8", None, 7, 8, 1.0,),  # interval
        (4, "quelques", None, None, None, None,),  # not measurable
        (4, None, None, None, None, None,),
        # fmt: on
    ]
    units = [
        (
            None,
            None,
        ),  # immeasurable ingredient like "1 egg"
        (
            "cl",
            None,
        ),
        (
            "l",
            None,
        ),
        (
            "%",
            None,
        ),
        (
            "/10",
            None,
        ),
        (
            "/2",
            None,
        ),
        (
            "/3",
            None,
        ),
        (
            "/4",
            None,
        ),
        (
            "/5",
            None,
        ),
        (
            "/8",
            None,
        ),
        (
            "boule",
            "boules",
        ),
        (
            "brin",
            "brins",
        ),
        (
            "cube",
            "cubes",
        ),
        (
            "cuillère à café",
            "cuillères à café",
        ),
        (
            "cuillère à soupe",
            "cuillères à soupe",
        ),
        (
            "demi-tranche",
            "demi-tranches",
        ),
        (
            "feuille",
            "feuilles",
        ),
        (
            "goutte",
            "gouttes",
        ),
        (
            "litre",
            "litres",
        ),
        (
            "morceau",
            "morceaux",
        ),
        (
            "part",
            "parts",
        ),
        (
            "pincée",
            "pincées",
        ),
        (
            "quartier",
            "quartiers",
        ),
        (
            "rondelle",
            "rondelles",
        ),
        (
            "shooter",
            "shooters",
        ),
        (
            "trait",
            "traits",
        ),
        (
            "tranche",
            "tranches",
        ),
        (
            "verre",
            "verres",
        ),
    ]
    ingredients = [
        "(Kina) Lillet *",
        "7up",
        "Absinthe",
        "Amaretto",
        "Amaro (Amaro Nonino...)",
        "Angostura bitters",
        "Applejack (à substituer par du Calvados en France)",
        "Apricot Brandy",
        "Apérol",
        "Baileys",
        "Bourbon",
        "Bourgogne aligoté",
        "Bénedictine",
        "Bénédictine",
        "Cachaça",
        "Calvados",
        "Campari",
        "Cannelle en poudre",
        "Cannelle râpée ou en poudre",
        "Champagne",
        "Chantilly / Crème fouettée",
        "Cognac",
        "Cointreau",
        "Cola",
        "Crème fouettée / chantilly",
        "Crème fouettée/chantilly",
        "Curaçao Bleu",
        "Curaçao blanc",
        "Drambuie",
        "Dry Gin",
        "Dubonnet rouge",
        "Fernet-Branca",
        "Fruits selon votre envie (citrons, oranges, bananes, pommes, fraises...)",
        "Gin",
        "Ginger Ale (Canada Dry)",
        "Ginger Beer",
        "Jack Daniel's no.7",
        "Kahlua",
        "Lillet blanc",
        "Lime Cordial",
        "Liqueur de pêche (Peach schnapps...)",
        "Malibu Coco",
        "Marasquin",
        "Noix de muscade en poudre",
        "Noix de muscade râpée",
        "noix de muscade râpée",
        "Old Tom Gin",
        "Orange Bitters",
        "Passoã",
        "Peach Schnapps (liqueur de pêche)",
        "Pernod",
        "Peychaud's Bitters",
        "Pineau des Charentes",
        "Pisco",
        "Pisco (brandy)",
        "Porto",
        "Poudre de cacao",
        "Prosecco",
        "Rhum",
        "Rhum blanc",
        "Rhum cubain",
        "Scotch whisky",
        "Sel et/ou sel de céleri et/ou poivre",
        "Sirop de grenadine",
        "Sloe Gin",
        "Sloe Gin *",
        "Soho",
        "Southern Comfort",
        "Sprite",
        "Sucre fin en poudre",
        "Tabasco",
        "Tequila",
        "Tonic (Schweppes...)",
        "Venezzio Bitter",
        "Vermouth rouge",
        "Vin rouge",
        "Vodka",
        "Whisky Bourbon",
        "Xérès",
        "absinthe",
        "ananas",
        "ananas coupées en morceaux",
        "anisé (Pernod, pastis)",
        "banane coupée en rondelles",
        "banane pelée",
        "beurre non salé (1 cuillère à café)",
        "bière",
        'bière "stout" (Guinness...)',
        "bière blonde",
        "bière brune",
        "bière cervoise",
        "bière stout (Guinness...)",
        "blanc d'oeuf",
        "blanc d'œuf",
        "bouillon de bœuf en marmite",
        "glace au citron vert",
        "glace à la menthe",
        "brandy (Cognac) ou rhum jamaïcain au choix",
        "brandy (Singani ou Pisco)",
        "brin de menthe fraîche",
        "cachaça",
        "café",
        "café chaud",
        "café fraîchement préparé",
        "cassonade",
        "cerise",
        "chartreuse",
        "chocolat au lait chaud",
        "chocolat chaud",
        "cidre",
        "cidre sans alcool *",
        "citron",
        "citron (vert ou jaune selon votre préférence)",
        "citron coupé en quartiers",
        "citron pressé et filtré",
        "citron vert",
        "citron vert pressé et filtré",
        "cola",
        "colorant alimentaire liquide bleu",
        "concombre",
        "crème de banane",
        "crème de cacao",
        "crème de cacao blanc",
        "crème de cacao blanc (Marie Brizard...)",
        "crème de cacao brun",
        "crème de cacao noir",
        "crème de cassis",
        "crème de coco",
        "crème de coco Lopez",
        "crème de menthe",
        "crème de menthe blanche",
        "crème de noix de coco",
        "crème de pêche",
        "crème fouettée",
        "crème fouettée / chantilly",
        "crème fraîche",
        "crème fraîche liquide",
        "crème fraîche ou liquide",
        "crème liquide",
        "crème légère",
        "crème ou lait de coco",
        "crème ou liqueur de menthe blanche",
        "crème ou liqueur de violette",
        "crème épaisse",
        "cuillère à café de sucre en poudre",
        "eau bouillante",
        "eau chaude",
        "eau fraîche",
        "eau gazeuse",
        "eau plate chaude",
        "extrait de vanille",
        "fraises",
        "framboises fraîches",
        "fruit de la passion",
        "gin",
        "gin (Plymouth)",
        "gin ou vodka",
        "ginger ale (Canada Dry)",
        "ginger ale (Canada Dry) ou 7up.",
        "ginger ale (Canada Dry...)",
        "ginger ale (Canada Dry®)",
        "jaune d'oeuf",
        "jaune d'œuf",
        "jus d'ananas",
        "jus d'ananas (ou jus de pomme)*",
        "jus d'orange",
        "jus de betterave",
        "jus de canneberge",
        "jus de canneberge (cranberry)",
        "jus de citron",
        "jus de citron filtré et pressé",
        "jus de citron jaune",
        "jus de citron jaune pressé",
        "jus de citron jaune pressé et filtré",
        "jus de citron pressé",
        "jus de citron pressé et filtré",
        "jus de citron vert",
        "jus de citron vert et filtré",
        "jus de citron vert filtré et pressé",
        "jus de citron vert pressé",
        "jus de citron vert pressé et filtré",
        "jus de fruits de la passion",
        "jus de limonade",
        "jus de mangue",
        "jus de pamplemousse",
        "jus de pamplemousse pressé",
        "jus de pomme",
        "jus de pomme (optionnel)",
        "jus de pomme frais",
        "jus de raisin",
        "jus de raisin rouge",
        "jus de tomate",
        "jus ou saumure d'olive",
        "kirsch",
        "lait",
        "lait chaud",
        "lait concentré sucré",
        "lait de coco",
        "lait entier",
        "lemon bitter (Schweppes lemon bitter...)",
        "lemon/lime soda (Sprite ou 7up)",
        "lime cordial",
        "limonade",
        "limonade de citron vert",
        "limonade ou 7up",
        "limonade ou ginger ale (Canada Dry)",
        "liqueur Advocaat",
        "liqueur Galliano",
        "liqueur d'abricot (Apricot Brandy)",
        "liqueur d'abricot (Apricot brandy)",
        "liqueur de banane",
        "liqueur de café",
        "liqueur de café (Kalhua...)",
        "liqueur de café Tia Maria",
        'liqueur de carvi/cumin "Kummel"',
        "liqueur de cerise (Cherry brandy)",
        "liqueur de cerises",
        "liqueur de cerises (Cherry Brandy)",
        "liqueur de fraise",
        "liqueur de framboise",
        "liqueur de melon",
        "liqueur de melon (Midori)",
        "liqueur de menthe verte (Get 27...)",
        "liqueur de mûre",
        "liqueur de noisette (Frangelico)",
        "liqueur de noisettes Frangelico",
        "liqueur de pomme (Manzana, Apple Schnapps...)",
        "liqueur de pomme (Manzana, Apple Shnapps...)",
        "liqueur de pêche",
        "liqueur de pêche (Peach Schnapps)",
        "liqueur de pêche (Peach schnapps...)",
        "liqueur de vanille",
        "liqueur de violette",
        "liqueur ou crème de cacao",
        "liqueur ou crème de menthe verte (Get 27...)",
        "liqueur ou crème de mûre",
        "liqueur/crème de menthe blanche",
        "mangue",
        "mangue découpée en petits morceaux",
        "marasquin",
        "melon",
        "menthe",
        "menthe fraîche",
        "menthe verte",
        "menthe verte fraîche",
        "miel",
        "mélasse",
        "mûres",
        "nectar de pêche",
        "noix de coco",
        "noix de muscade râpée / en poudre",
        "oeuf",
        "orange",
        "orange coupée en quartier",
        "purée de fruit de la passion",
        "purée de pêche blanche",
        "racine de gingembre",
        "rhum",
        "rhum (151 Proof / Overproof)",
        "rhum (jamaïcain, porto-ricain)",
        "rhum (portoricain)",
        "rhum Bacardi",
        "rhum Demerara",
        "rhum ambré",
        "rhum blanc",
        "rhum blanc agricole",
        "rhum brun",
        "rhum cubain",
        "rhum jamaïcain",
        "rhum léger",
        "rhum vieilli",
        "rhum vieux",
        "rhum épicé",
        "rondelle d'orange",
        "rondelle de citron",
        "sauce Worchestershire",
        "sauce worcestershire",
        "schnapps à la cannelle (Goldschlager)",
        "schnapps à la pomme",
        "scotch whisky",
        "sel",
        "sherry (Xérès)",
        "Jägermeister",
        "sirop d'agave",
        "sirop d'ananas",
        "sirop d'orgeat",
        "sirop de banane",
        "sirop de cassis",
        "sirop de citron",
        "sirop de falernum",
        "sirop de falernum (sinon grenadine)",
        "sirop de fraise",
        "sirop de framboise",
        "sirop de fruits de la passion",
        "sirop de gomme",
        "sirop de grenadine",
        "sirop de kiwi",
        "sirop de miel *",
        "sirop de sucre",
        "sirop de sucre (1 cuillère à café)",
        "sirop de sucre de canne",
        "sirop de vanille",
        "sirop saveur rhum",
        "sirop saveur tequila",
        "soda 7Up®",
        "sucre",
        "sucre / cassonade",
        "sucre de canne",
        "sucre en poudre",
        "sucre ou cassonade",
        "tabasco",
        "tequila",
        "thé chaud",
        "tonic (Schweppes)",
        "triple sec (Curaçao blanc)",
        "triple sec (Curaçao orange)",
        "triple sec (Curaçao)",
        "triple sec (Curaçao, Marie Brizard...)",
        "triple sec (Grand Marnier)",
        "vermouth blanc",
        "vermouth blanc (Martini, Noilly Prat...)",
        "vermouth blanc (Martini...)",
        "vermouth dry (Martini extra dry, Noilly Prat dry)",
        "vermouth rouge",
        "vermouth rouge (Martini rosso, Noilly Prat rouge)",
        "vermouth rouge (Martini...)",
        "boisson énergisante (Red Bull...)",
        "vin blanc",
        "vin blanc pétillant sans alcool",
        "vin de liqueur (Madère voire Porto)",
        "vin de liqueur (Porto)",
        "vin de liqueur rouge (Porto)",
        "vin mousseux / crémant de Loire",
        "vin rouge",
        "vin rouge (1 bouteille classique)",
        "vin rouge de Bourgogne",
        "vodka",
        "vodka à l'herbe de bison (Zubrowka)",
        "whiskey (irlandais ou américain)",
        "whisky",
        "whisky (Bourbon ou Rye Whiskey)",
        "whisky (Scotch)",
        "whisky (Seagram's Seven Crown®)",
        "whisky Bourbon",
        "whisky canadien",
        "whisky de seigle (Rye whiskey, etc.)",
        "whisky irlandais (Jameson, etc.)",
        "whisky écossais (Scotch, etc.)",
    ]
    tags = [
        (
            0,
            "B&B",
            "siroter",
            "digestif",
            "cocktails",
            "simples",
            "réaliser",
        ),
        (
            1,
            "cocktail",
            "Baltimore",
            "Egg",
            "Nogg",
            "grog",
            "personnes",
            "affaiblies",
            "tuberculeux",
        ),
        (
            2,
            "Banana",
            "Bliss",
            "cocktail",
            "Cognac",
            "liqueur",
            "banane",
            "siroter",
            "digestif",
        ),
        (
            3,
            "Brandy",
            "Alexander",
            "cocktail",
            "onctueux",
            "chocolaté",
            "déguster",
            "digestif",
        ),
        (
            4,
            "cocktail",
            "Brandy",
            "soda",
            "B&S",
            "recette",
            "aventures",
            "valet",
            "Jeeves",
        ),
        (
            5,
            "Brandy",
            "Champerelle",
            "cocktail",
            "origine",
            "française",
            "déguster",
            "digestif",
        ),
        (
            6,
            "Brandy",
            "Egg",
            "Nog",
            "Trinquer",
            "cocktail",
            "œuf",
        ),
        (
            7,
            "Brandy",
            "Julep",
            "cocktail",
            "famille",
            "juleps",
            "version",
            "digestif",
        ),
        (
            8,
            "Brandy",
            "Scaffa",
            "cocktail",
            "étages",
            "digestif",
        ),
        (
            9,
            "café",
            "royal",
            "recettes",
            "techniques",
            "cocktail",
        ),
        (
            10,
            "cocktail",
            "Egg",
            "Nogg",
            "Lait",
            "poule",
            "XVIIème siècle",
            "nombreuses",
            "variantes",
        ),
        (
            11,
            "French",
            "Connection",
            "cocktail",
            "subtil",
            "goût",
            "amande",
            "après-repas",
        ),
        (
            12,
            "cocktail",
            "French",
            "Mule",
            "variante",
            "française",
            "Moscow",
            "Mule",
        ),
        (
            13,
            "Hot",
            "Brandy",
            "Alexander",
            "version",
            "chaude",
            "Brandy",
            "Alexander",
        ),
        (
            14,
            "Metropolitan",
            "cocktails",
            "recettes",
            "distinctes",
            "Metropolitan",
        ),
        (
            15,
            "cocktail",
            "Pisco",
            "Sour",
            "boisson",
            "nationale",
            "pays",
            "sud-américains",
        ),
        (
            16,
            "cocktail",
            "Piscola",
            "boissons",
            "emblématiques",
            "Chili",
        ),
        (
            17,
            "cocktail",
            "Sazerac",
            "technique",
            "réalisation",
            "tradition",
            "respecter",
            "Sazerac",
        ),
        (
            18,
            "Side",
            "Car",
            "cocktail",
            "puissant",
            "couleur",
            "jaune",
            "or",
        ),
        (
            19,
            "Stinger",
            "cocktail",
            "bonnet",
            "nuit",
            "soirées",
            "new yorkaises",
            "XXème siècle",
        ),
        (
            20,
            "Yungueño",
            "cocktail",
            "traditionnel",
            "Bolivie",
        ),
        (
            21,
            "cocktail",
            "Air",
            "mail",
            "recette",
            "champagne",
            "fêtes",
            "fin d'année",
        ),
        (
            22,
            "Barbotage",
            "cocktail",
            "douceur",
            "fraîcheur",
            "finesse",
            "champagne",
        ),
        (
            23,
            "cocktail",
            "Bellini",
            "recette",
            "italienne",
            "1948",
            "Venise",
        ),
        (
            24,
            "cocktail",
            "Black",
            "Velvet",
            "recette",
            "bière",
            "champagne",
        ),
        (
            25,
            "Buck's",
            "Fizz",
            "cocktail",
            "fêtes",
            "fin d'année",
            "outre-Manche",
        ),
        (
            26,
            "cocktail",
            "Cardinal",
            "variante",
            "kir",
            "vin",
            "rouge",
        ),
        (
            27,
            "Champagne",
            "cocktail",
            "cocktails",
            "prestige",
            "grandes",
            "occasions",
        ),
        (
            28,
            "champagne",
            "Julep",
            "variante",
            "mint",
            "julep",
        ),
        (
            29,
            "cocktail",
            "Communard",
            "recette",
            "kir",
            "crème",
            "cassis",
            "vin",
            "rouge",
        ),
        (
            30,
            "cocktail",
            "Death",
            "afternoon",
            "recette",
            "mort",
            "après-midi",
        ),
        (
            31,
            "embuscade",
            "cocktail",
            "origine",
            "caennaise",
            "escapade",
            "Normandie",
        ),
        (
            32,
            "cocktail",
            "Jacuzzi",
            "recette",
            "Champagne",
            "saveurs",
        ),
        (
            33,
            "cocktail",
            "Kalimotxo",
            "Calimocho",
            "recette",
            "espagnole",
            "Vin",
            "rouge",
            "Cola",
        ),
        (
            34,
            "Kir",
            "recette",
            "apéritif",
            "vin",
            "blanc",
        ),
        (
            35,
            "cocktail",
            "Kir",
            "royal",
            "champagne",
            "kir",
        ),
        (
            36,
            "cocktail",
            "Mimosa",
            "champagne",
            "orange",
            "jus",
            "orange",
            "pressé",
        ),
        (
            37,
            "cocktail",
            "Pick",
            "me",
            "up",
            "recette",
            "douce",
            "fruitée",
            "réception",
        ),
        (
            38,
            "cocktail",
            "Poor",
            "man's",
            "Black",
            "Velvet",
            "dérivé",
            "Black",
            "Velvet",
            "homme",
            "pauvre",
        ),
        (
            39,
            "Sangria",
            "recette",
            "fruitée",
            "originaire",
            "Espagne",
        ),
        (
            40,
            "soupe",
            "angevine",
            "recette",
            "originaire",
            "Anjou",
            "Noël",
            "nouvel an",
            "fête",
        ),
        (
            41,
            "Spritz",
            "recette",
            "cocktail",
            "classique",
            "italien",
            "Apérol",
            "Prosecco",
        ),
        (
            42,
            "cocktail",
            "Tinto",
            "de",
            "Verano",
            "recette",
            "emblématique",
            "espagnole",
            "vin",
            "rouge",
            "été",
        ),
        (
            43,
            "vin",
            "chaud",
            "classique",
            "saison",
            "hivernale",
        ),
        (
            44,
            "Acapulco",
            "Gold",
            "cocktail",
            "sans alcool",
            "onctueux",
        ),
        (
            45,
            "cocktail",
            "sans alcool",
            "Afterglow",
            "recette",
            "simples",
        ),
        (
            46,
            "cocktail",
            "Alice",
            "recette",
            "sans alcool",
            "onctueuse",
            "fruitée",
        ),
        (
            47,
            "cocktail",
            "Amazonas",
            "recette",
            "rafraîchissante",
            "sans alcool",
            "mangues",
        ),
        (
            48,
            "cocktail",
            "Apple",
            "cobbler",
            "recette",
            "sans alcool",
            "fruitée",
            "rafraîchissante",
        ),
        (
            49,
            "cocktail",
            "Apple",
            "rose",
            "recette",
            "lemon",
            "bitter",
        ),
        (
            50,
            "cocktail",
            "Apple",
            "shot",
            "recette",
            "sans alcool",
            "désaltérante",
            "simple",
        ),
        (
            51,
            "cocktail",
            "Baby",
            "Bellini",
            "sans alcool",
            "Bellini",
        ),
        (
            52,
            "cocktail",
            "Batman",
            "recette",
            "sans alcool",
            "simple",
            "enfants",
        ),
        (
            53,
            "cocktail",
            "Bloody",
            "Orange",
            "variante",
            "Bloody",
            "Mary",
        ),
        (
            54,
            "cocktail",
            "Bora",
            "bora",
            "recette",
            "exotique",
            "rafraîchissante",
            "déguster",
            "modération",
        ),
        (
            55,
            "Bora",
            "Bora",
            "Brew",
            "cocktail",
            "sans alcool",
            "jus",
            "ananas",
        ),
        (
            56,
            "café",
            "frappé",
            "boisson",
            "chaude",
            "français",
            "version",
            "glacée",
        ),
        (
            57,
            "cocktail",
            "Cendrillon",
            "Cinderella",
            "recette",
            "sans alcool",
            "fruitée",
            "rafraîchissante",
        ),
        (
            58,
            "cocktail",
            "DBK",
            "diabolo",
            "banane-kiwi",
            "boisson",
            "bars",
            "France",
        ),
        (
            59,
            "cocktail",
            "Florida",
            "recette",
            "douce",
            "fruitée",
            "rafraîchissante",
            "été",
        ),
        (
            60,
            "cocktail",
            "Ginger",
            "Mick",
            "recette",
            "hommage",
            "héros",
            "roman",
            "australien",
            "1916",
        ),
        (
            61,
            "version",
            "sans alcool",
            "kir",
            "pétillant",
            "enfants",
        ),
        (
            62,
            "Milk-Shake",
            "Mojito",
            "cocktail",
            "français",
            "version",
            "milkshake",
        ),
        (
            63,
            "Port",
            "au",
            "prince",
            "cocktail",
            "sans alcool",
            "capitale",
            "haïtienne",
        ),
        (
            64,
            "Punch sans alcool pour enfants",
            "sans alcool",
            "enfants",
            "anniversaire",
            "fête",
        ),
        (
            65,
            "Pussyfoot",
            "cocktail classique",
            "sans alcool",
            "militant",
        ),
        (
            66,
            "Virgin Rainbow Cocktail",
            "sans alcool",
            "arc-en-ciel",
        ),
        (
            67,
            "Roy Rogers",
            "simple",
            "Coca",
            "Grenadine",
        ),
        (
            68,
            "Sangria sans alcool",
            "sans alcool",
            "enfants",
            "adultes",
            "rapide",
            "simple",
        ),
        (
            69,
            "Sangrita",
            "Mexique",
            "shooter",
            "tequila",
        ),
        (
            70,
            "Shirley Temple",
            "célèbre",
            "enfant-star",
        ),
        (
            71,
            "Virgin Bloody Mary",
            "sans alcool",
            "vodka",
        ),
        (
            72,
            "Virgin Caipirinha",
            "sans alcool",
            "Caipirinha",
        ),
        (
            73,
            "Virgin Margarita",
            "sans alcool",
            "Margarita",
            "mexicaine",
        ),
        (
            74,
            "Virgin Mojito",
            "sans alcool",
            "mojito",
            "rhum",
        ),
        (
            75,
            "Virgin Pina colada",
            "sans alcool",
            "Piña Colada",
            "onctueuse",
            "savoureuse",
        ),
        (
            76,
            "Virgin Planteur",
            "sans alcool",
            "planter's punch",
        ),
        (
            77,
            "Virgin Spritz",
            "sans alcool",
            "Spritz",
            "italien",
        ),
        (
            78,
            "Addington",
            "vintage",
            "1930",
        ),
        (
            79,
            "Agincourt",
            "bataille",
            "Pas-de-Calais",
        ),
        (
            80,
            "Alabama Slammer",
            "Sloe Comfy Screw",
        ),
        (
            81,
            "Ale sangaree",
            "cervoise",
        ),
        (
            82,
            "Almond Joy",
            "douce",
            "crèmeuse",
        ),
        (
            83,
            "Amaretto Sour",
            "liqueur italienne",
            "acidulée",
            "sours",
        ),
        (
            84,
            "Amaretto Sunrise",
            "Tequila Sunrise",
            "Amaretto",
            "tequila",
        ),
        (
            85,
            "Americano",
            "apéritif",
            "amers",
        ),
        (
            86,
            "Andalusia",
            "corsée",
            "Andalousie",
        ),
        (
            87,
            "Angel's Tip",
            "onctueuse",
            "crème de cacao",
            "crème fraîche",
        ),
        (
            88,
            "Angel's Tit",
            "onctueuse",
            "marasques",
        ),
        (
            89,
            "Apple Colada",
            "douce",
            "fruitée",
            "pomme",
            "noix de coco",
        ),
        (
            90,
            "Apple Jack",
            "originale",
            "Robert Vermeire",
            "1922",
        ),
        (
            91,
            "Apple Sunrise",
            "douce",
            "fruitée",
            "années 80",
        ),
        (
            92,
            "Baileys Irish Coffee",
            "café irlandais",
            "doux",
            "digestif",
        ),
        (
            93,
            "Banshee",
            "crèmeuse",
            "banane",
            "cacao",
        ),
        (
            94,
            "Batida de coco",
            "batidas",
            "brésilien",
        ),
        (
            95,
            "Bentley",
            "inchangée",
            "Applejack",
            "Dubonnet",
        ),
        (
            96,
            "Black & Tan",
            "cocktail à étages",
            "punch",
        ),
        (
            97,
            "Brain Duster",
            "absinthe",
            "1895",
        ),
        (
            98,
            "Café Calypso",
            "café",
            "Tia Maria",
        ),
        (
            99,
            "Café italien",
            "café chaud",
            "Amaretto",
            "chantilly",
        ),
        (
            100,
            "Caipirinha",
            "Brésil",
        ),
        (
            101,
            "Dizzy Blonde",
            "audacieuse",
            "Advocaat",
            "Pernod",
        ),
        (
            102,
            "Fernandito",
            "Fernet Coca",
            "Amérique du Sud",
        ),
        (
            103,
            "Frangelico Luau",
            "douce",
            "noisettes",
        ),
        (
            104,
            "Fuzzy Navel",
            "pêche",
            "orange",
        ),
        (
            105,
            "Garibaldi",
            "campari orange",
        ),
        (
            106,
            "General Harrison's Egg Nogg",
            "9ème président des États-Unis",
        ),
        (
            107,
            "Grasshopper",
            "crème",
            "pousse-café",
        ),
        (
            108,
            "Jack Rose",
            "doux",
            "fruité",
        ),
        (
            109,
            "Litchi Sunrise",
            "Soho",
            "sunrise",
        ),
        (
            110,
            "Monaco",
            "France",
        ),
        (
            111,
            "Nutty Irishman",
            "apéritif",
            "liqueur de noisette",
            "italien",
        ),
        (
            112,
            "Orgasme",
            "onctueux",
            "savoureux",
        ),
        (
            113,
            "Peach & Love",
            "fruitée",
            "cidre",
        ),
        (
            114,
            "Pineau Colada",
            "Pina Colada",
            "charentaise",
        ),
        (
            115,
            "Port wine sangaree",
            "Porto",
            "sangarees",
        ),
        (
            116,
            "Porto Flip",
            "raffiné",
            "digestif",
        ),
        (
            117,
            "Pousse l'amour",
            "long drink",
            "français",
        ),
        (
            118,
            "Cerise",
            "Vermouth",
        ),
        (
            119,
            "Andalous",
            "Vin",
            "Xérès",
        ),
        (
            120,
            "Xérès",
        ),
        (
            121,
            "Cidre",
            "Bière",
            "Étages",
        ),
        (
            122,
            "Bière",
            "Grenadine",
            "Simple",
        ),
        (
            123,
            "Amaretto",
            "Thé",
            "Hiver",
            "Chaud",
        ),
        (
            124,
            "Xérès",
            "Espagne",
            "Vin",
        ),
        (
            125,
            "Train",
            "XXe siècle",
        ),
        (
            126,
            "Suggestif",
        ),
        (
            127,
            "Kina Lillet",
            "Disparition",
        ),
        (
            128,
            "Long Island Iced Tea",
            "Dérivé",
        ),
        (
            129,
            "Fizz",
            "Rafraîchissant",
        ),
        (
            130,
            "Classique",
            "Onctueux",
            "Savoureux",
        ),
        (
            131,
            "Kummel",
        ),
        (
            132,
            "Corsé",
            "Visage d'ange",
        ),
        (
            133,
            "Avertissement",
        ),
        (
            134,
            "Bleuté",
            "Grand Cocktail",
        ),
        (
            135,
            "Années 1930",
            "Bleu",
        ),
        (
            136,
            "Pink Lady",
            "White Lady",
            "Sœur",
        ),
        (
            137,
            "Unique",
            "Décennie",
            "Inchangeable",
        ),
        (
            138,
            "Orange",
            "Jus pressé",
        ),
        (
            139,
            "Plus d'un siècle",
        ),
        (
            140,
            "Old Tom Gin",
            "Très sec",
        ),
        (
            141,
            "Ressuscité",
            "Décennies",
        ),
        (
            142,
            "Manhattan",
            "Hôtel Astoria",
        ),
        (
            143,
            "Première Guerre Mondiale",
        ),
        (
            144,
            "Roosevelt",
            "Churchill",
            "James Bond",
            "Référence",
        ),
        (
            145,
            "Ambre",
            "Rouge",
            "Simple",
        ),
        (
            146,
            "Tom Bullock",
            "1917",
        ),
        (
            147,
            "Artillerie",
            "Française",
            "75mm",
        ),
        (
            148,
            "Gin",
            "Vermouth Dry",
            "Sec",
        ),
        (
            149,
            "Marine britannique",
            "Élixir",
        ),
        (
            150,
            "Rafraîchissant",
            "Doux",
            "Gin",
            "Citron",
            "Eau gazeuse",
        ),
        (
            151,
            "Eau de vie",
            "Grain",
            "Juleps",
        ),
        (
            152,
            "Gin Fizz",
            "Américaine",
            "1880",
        ),
        (
            153,
            "Sours",
            "Gin",
        ),
        (
            154,
            "Chaud",
            "Économique",
        ),
        (
            155,
            "Scorbut",
            "Malaria",
            "Historique",
        ),
        (
            156,
            "Impôt sur le revenu",
        ),
        (
            157,
            "Paul McCartney",
            "Surnom",
        ),
        (
            158,
            "Greffe",
            "Testicules de singe",
            "Homme",
        ),
        (
            159,
            "Plus d'un siècle",
            "Créateur",
        ),
        (
            160,
            "Simple",
            "Fleur d'oranger",
        ),
        (
            161,
            "Fruité",
            "Apéritif",
            "Short Drink",
        ),
        (
            162,
            "Mal de mer",
            "XIXe siècle",
        ),
        (
            163,
            "Doux",
            "Fruité",
            "Rafraîchissant",
            "Féminin",
        ),
        (
            164,
            "Royal Automobile Club",
            "1914",
        ),
        (
            165,
            "Fruité",
            "Framboises",
            "Collins",
        ),
        (
            166,
            "Agrumes",
            "1er Prix",
            "Concours",
        ),
        (
            167,
            "Bloody Mary",
            "Gin",
            "Vodka",
        ),
        (
            168,
            "Gin",
            "Ginger Ale",
            "Cooler",
        ),
        (
            169,
            "Complexe",
            "Singapour",
            "Emblématique",
        ),
        (
            170,
            "Prohibition",
            "21 Club",
            "New-York",
        ),
        (
            171,
            "Bâtard souffrant",
        ),
        (
            172,
            "Canular",
            "Légendaire",
        ),
        (
            173,
            "Audacieux",
            "Subtil",
        ),
        (
            174,
            "James Bond",
            "Casino Royale",
            "Ian Fleming",
        ),
        (
            175,
            "Agrumes",
            "Dame Blanche",
        ),
        (
            176,
            "Gin",
            "Liqueur de menthe",
        ),
        (
            177,
            "Dick Bradsell",
            "Plymouth Gin",
            "Défi",
        ),
        (
            178,
            "Facile",
            "Savoureux",
        ),
        (
            179,
            "Acapulco",
            "Mexique",
            "Balnéaire",
        ),
        (
            180,
            "Riche en arômes",
            "Récent",
        ),
        (
            181,
            "Pomme",
            "Mojito",
        ),
        (
            182,
            "Exotique",
            "Rafraîchissant",
            "Malibu",
        ),
        (
            183,
            "Fruité",
            "Rafraîchissant",
            "Bacardi",
        ),
        (
            184,
            "Exotique",
            "Tiki",
            "Estivale",
        ),
        (
            185,
            "Pina Colada",
            "Ancêtre",
        ),
        (
            186,
            "Banane",
            "Pina Colada",
        ),
        (
            187,
            "Banane",
            "Daiquiri",
        ),
        (
            188,
            "Classique",
            "Italien",
            "Années 50",
        ),
        (
            189,
            "Chaud",
            "Riche en saveurs",
        ),
        (
            190,
            "Rhum",
            "Entre les draps",
        ),
        (
            191,
            "Diable Noir",
            "Rude",
        ),
        (
            192,
            "Grog",
            "Miel",
            "Mélasse",
        ),
        (
            193,
            "Tiki",
            "Agréable",
            "Blue Hawaiian",
        ),
        (
            194,
            "Mojito",
            "Curaçao bleu",
        ),
        (
            195,
            "Fruitée",
            "Deux versions",
        ),
        (
            196,
            "Chaud",
            "Saveurs jamaïcaines",
        ),
        (
            197,
            "Variante",
            "Caipirinha",
        ),
        (
            198,
            "Rhum",
            "Crème de banane",
            "Lime Cordial",
        ),
        (
            199,
            "Chaud",
            "Cacao",
        ),
        (
            200,
            "Agrumes",
        ),
        (
            201,
            "Exotique",
            "Noix de coco",
        ),
        (
            202,
            "Rhum",
            "Citron",
            "Cola",
        ),
        (
            203,
            "Origine cubaine",
            "Plage",
        ),
        (
            204,
            "Boisson nationale",
            "Bermudes",
        ),
        (
            205,
            "Couleur",
            "Diable",
        ),
        (
            206,
            "Tiki",
            "Nom du créateur",
        ),
        (
            207,
            "Origine cubaine",
            "Multiples saveurs",
        ),
        (
            208,
            "Fruitée",
            "Rhum",
            "Désaltérante",
        ),
        (
            209,
            "Comédie musicale",
            "1908",
        ),
        (
            210,
            "Recette de 1954",
            "Aube glaciale",
        ),
        (
            211,
            "Hommage",
            "Écrivain",
        ),
        (
            212,
            "Rhum",
            "Citron",
            "Miel",
        ),
        (
            213,
            "Grog beurré",
        ),
        (
            214,
            "Tiki",
            "Années 40",
            "Ouragan",
        ),
        (
            215,
            "Variante",
            "Moscow Mule",
            "Rhum",
        ),
        (
            216,
            "Pavillon pirate noir",
        ),
        (
            217,
            "Tiki",
            "Bitter",
        ),
        (
            218,
            "Recette ancienne",
            "1862",
        ),
        (
            219,
            "Très fruitée",
        ),
        (
            220,
            "Bartender Trader Vic",
            "Très connu",
        ),
        (
            221,
            "Variante",
            "Tequila Sunrise",
        ),
        (
            222,
            "Rhum",
            "Riche en saveurs",
        ),
        (
            223,
            "Hommage",
            "Star de cinéma",
        ),
        (
            224,
            "Onctueuse",
            "Nom évocateur",
        ),
        (
            225,
            "Recette originale",
            "Mojito",
            "Préféré des français",
        ),
        (
            226,
            "Mojito",
            "Fraise",
        ),
        (
            227,
            "Mojito",
            "Champagne",
            "Royal",
        ),
        (
            228,
            "Tiki",
            "Trois types de rhum",
        ),
        (
            229,
            "Tiki",
            "Rhum",
            "Crème de coco",
            "Doux",
            "Exotique",
        ),
        (
            230,
            "Rhum",
            "Crème de coco",
            "Jus d'ananas",
        ),
        (
            231,
            "Tiki",
            "Fruitée",
            "Rafraîchissante",
            "Punch Planteur",
        ),
        (
            232,
            "Équilibrée",
            "Harry Craddock",
            "1930",
        ),
        (
            233,
            "Bermudes",
            "Stick",
        ),
        (
            234,
            "Tiki",
            "Hawaï",
            "Bartender Trader Vic",
        ),
        (
            235,
            "Saveurs douces",
            "Appréciable",
        ),
        (
            236,
            "Antillais",
            "Rhum agricole",
        ),
        (
            237,
            "Fruitée",
            "Vermouth",
        ),
        (
            238,
            "Doux",
            "Offensif",
            "Lion blanc",
        ),
        (
            239,
            "Jaune",
            "Short drink",
            "Rafraîchissant",
        ),
        (
            240,
            "Tiki",
            "Don the Beachcomber",
        ),
        (
            241,
            "Flambé",
            "À avaler cul-sec",
            "Avec modération",
        ),
        (
            242,
            "Nom de bande dessinée",
        ),
        (
            243,
            "Shooter",
            "À boire sans les mains",
        ),
        (
            244,
            "Variante",
            "Kamikaze",
            "Curaçao bleu",
        ),
        (
            245,
            "Couleurs rasta",
            "Hommage à Bob Marley",
        ),
        (
            246,
            "Schnapps à la cannelle",
        ),
        (
            247,
            "B-52",
            "Pet de canard",
        ),
        (
            248,
            "Couleurs du Mexique",
        ),
        (
            249,
            "Bombe",
            "Shooter",
            "Bière",
        ),
        (
            250,
            "Jägermeister",
            "Boisson énergisante",
        ),
        (
            251,
            "Couleurs du drapeau mexicain",
        ),
        (
            252,
            "Accrocheur",
            "Succès à l'étranger",
        ),
        (
            253,
            "Parisien",
            "Chartreuse",
        ),
        (
            254,
            "Ancien",
            "Nouvelle Orléans",
        ),
        (
            255,
            "Tequila",
            "Gin",
            "Vodka",
        ),
        (
            256,
            "Doux",
            "Rafraîchissant",
            "Facile à réaliser",
        ),
        (
            257,
            "Mémoire des aztèques",
        ),
        (
            258,
            "Aire de Cuba Libre",
        ),
        (
            259,
            "Bouillon",
            "Boeuf",
            "Original",
        ),
        (
            260,
            "Margarita",
            "Mexicaine",
            "Bleue",
        ),
        (
            261,
            "Sec",
            "Tequila",
            "Kahlua",
        ),
        (
            262,
            "Doux",
            "Cactus",
        ),
        (
            263,
            "Unique",
            "Tequila",
            "Vermouth",
        ),
        (
            264,
            "Simple",
            "Tequila",
            "Pamplemousse",
        ),
        (
            265,
            "Rafraîchissant",
            "Nouveau-Mexique",
        ),
        (
            266,
            "Couleurs",
            "Diable",
        ),
        (
            267,
            "Traduction",
        ),
        (
            268,
            "Riche",
            "Saveurs",
            "Hiver",
        ),
        (
            269,
            "Fruité",
            "Rafraîchissant",
            "Tequila",
        ),
        (
            270,
            "Doux",
            "Fruité",
            "Coloré",
        ),
        (
            271,
            "Viril",
            "Fort",
        ),
        (
            272,
            "Mexicaine",
            "Tequila",
            "Cointreau",
            "Citron vert",
        ),
        (
            273,
            "Fraise",
            "Mexicaine",
        ),
        (
            274,
            "Tequila",
            "Moscow Mule",
        ),
        (
            275,
            "Mexicain",
            "Favori",
        ),
        (
            276,
            "Soleil",
            "Inspiré",
        ),
        (
            277,
            "Tequila Martini",
        ),
        (
            278,
            "Tequila",
            "Tonic",
        ),
        (
            279,
            "Doux",
            "Fruité",
            "Tequila",
            "Curaçao",
        ),
        (
            280,
            "Doux",
            "Margarita",
        ),
        (
            281,
            "Vampirique",
            "Rouge",
            "Pimenté",
        ),
        (
            282,
            "Doux",
            "Orange",
            "Digestif",
        ),
        (
            283,
            "Française",
            "Amertume",
            "Acidité",
        ),
        (
            284,
            "Vodka-Orange",
            "Crème de Banane",
        ),
        (
            285,
            "Appletini",
        ),
        (
            286,
            "Décoller",
        ),
        (
            287,
            "Kamikaze",
        ),
        (
            288,
            "Douceur",
            "Fraîcheur",
            "Caractère",
        ),
        (
            289,
            "Brise",
            "Baie",
        ),
        (
            290,
            "Vodka",
            "Bière",
        ),
        (
            291,
            "Martini",
            "Dégradé",
        ),
        (
            292,
            "Digestif",
            "Simple",
            "Russe noir",
        ),
        (
            293,
            "Originale",
            "Légende",
        ),
        (
            294,
            "Fraîche",
            "Attrayante",
        ),
        (
            295,
            "Bleu",
            "Vodka",
            "Curaçao bleu",
        ),
        (
            296,
            "Rafraîchissant",
            "Citron",
        ),
        (
            297,
            "Caipiroska",
            "Vodka",
            "Cachaça",
        ),
        (
            298,
            "Vodka",
            "Cranberry",
            "Cape Cod",
        ),
        (
            299,
            "Pina Colada",
        ),
        (
            300,
            "Banane",
        ),
        (
            301,
            "Chocolat",
            "Martini",
        ),
        (
            302,
            "Onctueux",
            "Savoureux",
        ),
        (
            303,
            "Sex and the city",
        ),
        (
            304,
            "Concombre",
            "Frais",
        ),
        (
            305,
            "Saumure d'olive",
        ),
        (
            306,
            "Stimulant",
        ),
        (
            307,
            "Liqueur de Fraise",
        ),
        (
            308,
            "Française",
            "Martini",
        ),
        (
            309,
            "Digestif",
            "Amandes",
        ),
        (
            310,
            "Amandes",
            "Digestif",
        ),
        (
            311,
            "Lévrier",
            "Levrette",
        ),
        (
            312,
            "Fruitée",
            "Nombril poilu",
        ),
        (
            313,
            "Harvey",
            "Mur",
        ),
        (
            314,
            "Vent divin",
            "Japonais",
        ),
        (
            315,
            "Fruité",
        ),
        (
            316,
            "Puissant",
            "Doux",
            "Femme",
        ),
        (
            317,
            "Doux",
            "Vodka",
            "Cranberry",
            "Orange",
        ),
        (
            318,
            "Martini",
            "Fraise",
        ),
        (
            319,
            "Melon",
            "Frais",
        ),
        (
            320,
            "Fruitée",
            "Vodka",
            "Bison",
        ),
        (
            321,
            1942,
            "Ginger beer",
            "Vodka",
        ),
        (
            322,
            "Gingembre",
            "Ananas",
            "Frais",
        ),
        (
            323,
            "Exotique",
            "Fruit de la passion",
        ),
        (
            324,
            "Rafraîchissant",
            "Sirène violette",
        ),
        (
            325,
            "Arc-en-ciel",
        ),
        (
            326,
            "Menthe",
            "Framboises",
            "Fraîches",
        ),
        (
            327,
            "Jus de Pomme",
        ),
        (
            328,
            "Classique",
            "Nouvelle génération",
        ),
        (
            329,
            "Vodka",
            "Pamplemousse",
        ),
        (
            330,
            "Doux",
            "Fruité",
            "Sunrise",
        ),
        (
            331,
            "Tournevis",
            "Vodka",
            "Orange",
        ),
        (
            332,
            "Doux",
            "Été",
            "Brise de mer",
        ),
        (
            333,
            "Bleue",
            "Sex On The Beach",
        ),
        (
            334,
            "Évocateur",
        ),
        (
            335,
            "Southern Comfort",
        ),
        (
            336,
            "Screwdriver",
        ),
        (
            337,
            "Screwdriver",
        ),
        (
            338,
            "Screwdriver",
        ),
        (
            339,
            "Black Russian",
            "Cola",
        ),
        (
            340,
            "Ferrari",
        ),
        (
            341,
            "Caractère",
        ),
        (
            342,
            "Vodka-Menthe",
            "Apéritif",
        ),
        (
            343,
            "Vodka Martini",
            "James Bond",
        ),
        (
            344,
            "The Big Lebowski",
        ),
        (
            345,
            "Sex on The Beach",
        ),
        (
            346,
            "7Up®",
        ),
        (
            347,
            "Vintage",
            "XXème siècle",
        ),
        (
            348,
            "Manhattan",
        ),
        (
            349,
            "Nevada",
            "1940",
            "Histoire",
        ),
        (
            350,
            "Tom Bullock",
            "1917",
            "Histoire",
        ),
        (
            351,
            "Mint Julep",
            "Mûre",
            "Dérivé",
        ),
        (
            352,
            "Las Vegas",
            "Cocktail",
        ),
        (
            353,
            "Savoy Cocktail Book",
            "1930",
            "Vintage",
        ),
        (
            354,
            "Enflammé",
            "Spectacle visuel",
        ),
        (
            355,
            "Chaudronnier",
            "Unique",
            "Français",
        ),
        (
            356,
            "Classique",
            "Whisky",
            "Campari",
            "Vermouth rouge",
            "Sec",
        ),
        (
            357,
            "Canadien",
            "Fruits frais",
            "Saveurs riches",
        ),
        (
            358,
            "Sec",
            "Chancelier",
            "Français",
        ),
        (
            359,
            "Hommage",
            "Winston Churchill",
        ),
        (
            360,
            "Francophone",
            "Système mécanique",
        ),
        (
            361,
            "Bourbon",
            "Bénédictine",
            "Alliance",
        ),
        (
            362,
            "Digestif",
            "Amandes",
            "Doux",
        ),
        (
            363,
            "Crémeux",
            "Filleul",
        ),
        (
            364,
            "Zeste de citron",
            "Long",
            "Epais",
        ),
        (
            365,
            "Chaud",
            "Whisky",
            "Café",
            "Crème liquide",
            "Irlandais",
        ),
        (
            366,
            "Chaud",
            "Doux",
            "Vache irlandaise",
        ),
        (
            367,
            "Gin Rickey",
            "Dérivé",
            "Irlandais",
        ),
        (
            368,
            "Désaltérant",
            "Jack Daniel's",
            "Lemonade",
        ),
        (
            369,
            "Digestif",
            "Amérisé",
            "Américain",
        ),
        (
            370,
            "Ancien",
            "Mint Julep",
        ),
        (
            371,
            "Classique",
            "Ancien",
            "Old Fashioned",
        ),
        (
            372,
            "Nouveau",
            "Classique",
            "Apérol",
            "Avion en papier",
        ),
        (
            373,
            "Ecossais",
            "Manhattan",
            "Hors-la-loi",
            "Rob Roy",
        ),
        (
            374,
            "Caractère",
            "Clou rouillé",
        ),
        (
            375,
            "Sec",
            "Années 1930",
            "Vieux Carré",
        ),
        (
            376,
            "Whiskey Julep",
            "Mint Julep",
            "Identique",
        ),
        (
            377,
            "Célèbre",
            "Sours",
            "Whisky Sour",
        ),
    ]
    cocktails = [
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à dégustation</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail B&amp;B (B and B) tient son nom "
            "des ingrédients qui le composent : Brandy et Bénedictine. Le "
            "&quot;B &amp; B&quot; est attribué au &quot;Club 21&quot; de "
            "New York mais la recette aurait été publiée auparavant dans "
            "les années 1910.</p>",
            "ingredients": ["4 cl de Cognac", "4 cl de Bénédictine"],
            "summary": "Le B&amp;B : à siroter en digestif, il est l&#x27;un des "
            "cocktails les plus simples à réaliser.",
            "title": "Cocktail B&B",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Baltimore Egg Nogg est une "
            "variante du cocktail classique Egg Nogg, ils apparaîssent "
            "tous les deux pour la première fois en 1862 dans &quot;How "
            "to mix drinks&quot; de Jerry Thomas. Comme indiqué "
            "ci-dessus, la recette appelle à l&#x27;origine à choisir "
            "entre le brandy et le rhum, comme beaucoup le font vous "
            "pouvez tout à fait intégrer les 2 ingrédients en les "
            "partageant à parts égales.</p><p>Jerry Thomas nous y indique "
            "que la recette du Baltimore Egg Nogg est une excellente "
            "boisson pour les personnes affaiblies et un régime "
            "nourrissant pour les tuberculeux.</p>",
            "ingredients": [
                "1 cuillère à café de sucre en poudre",
                "1 oeuf",
                "3 cl de vin de liqueur (Madère voire Porto)",
                "3 cl de brandy (Cognac) ou rhum jamaïcain au choix",
                "5 cl de lait",
                "1 pincée de noix de muscade râpée",
            ],
            "summary": "Le cocktail Baltimore Egg Nogg : un excellent grog pour les "
            "personnes affaiblies et les tuberculeux.",
            "title": "Cocktail Baltimore Egg Nogg",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à martini</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>D&#x27;origine inconnue, le cocktail Banana "
            "Bliss est composé à parts égales de cognac et de liqueur de "
            "banane. &quot;Bliss&quot; signifie bonheur en français, et "
            "&quot;Banana&quot; nous vous laissons deviner :)</p><p>La "
            "recette du Banana Bliss est apparu pour la première fois "
            "dans &quot;Café royal Cocktail book&quot; de W. J. "
            "Tarling&#x27;s en 1937 qui attribue l&#x27;invention du "
            "cocktail à E. Angerosa.</p>",
            "ingredients": ["4 cl de Cognac", "4 cl de liqueur de banane"],
            "summary": "Le Banana Bliss : un cocktail à base de Cognac et liqueur de "
            "banane à siroter en digestif.",
            "title": "Cocktail Banana Bliss",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Brandy Alexander est un dérivé de "
            "l&#x27;Alexander. Ici le cognac remplace le gin "
            "d&#x27;origine, et la crème de cacao brun remplace la crème "
            "de cacao blanc.</p>",
            "ingredients": [
                "3 cl de Cognac",
                "3 cl de crème de cacao brun",
                "3 cl de crème légère",
                "Noix de muscade râpée",
            ],
            "summary": "Le Brandy Alexander : un cocktail onctueux et chocolaté à "
            "déguster en digestif.",
            "title": "Cocktail Brandy Alexander",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Brandy and soda , abrégé B&amp;S, "
            "est publié pour la première fois en 1862 dans &quot;How to "
            "mix drinks&quot; de Jerry Thomas.</p><p>Ce cocktail et sa "
            "recette apparaîssent dans les romans de P.G. Wodehouse et "
            "notamment en 1923 dans &quot;The Inimitable Jeeves&quot; où "
            "Bertrie Wooster commande à son valet Jeeves un &quot;brandy "
            "and soda&quot; avec pas trop de soda.</p>",
            "ingredients": ["8 cl de Cognac", "12 cl d'eau gazeuse"],
            "summary": "Le cocktail Brandy and soda (B&amp;S) : une recette qui apparaît "
            "dans les aventures du célèbre valet Jeeves.",
            "title": "Cocktail Brandy and soda (B&S)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned ou à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Brandy Champerelle est "
            "apparue en 1862 dans &quot;How to mix drinks&quot; de Jerry "
            "Thomas qui y indique qu&#x27;il s&#x27;agit d&#x27;un "
            "cocktail français. Dans cet ouvrage, la recette appelle à "
            "1/3 de brandy + 1/3 de curaçao + 1/3 de Bogart&#x27;s "
            "Bitter. En réalité il y a eu une erreur à l&#x27;impression, "
            "il ne devait pas s&#x27;agir de &quot;Bogart&#x27;s "
            "Bitter&quot; mais de &quot;Boker&#x27;s Bitter&quot;. "
            "Quoiqu&#x27;il en soit le Boker&#x27;s Bitter n&#x27;est "
            "plus produit depuis semble-t-il les années 1890, on le "
            "remplace donc par de l&#x27;Angostura bitters pour lequel "
            "quelques gouttes suffisent.</p>",
            "ingredients": [
                "4 cl de Cognac",
                "4 cl de Curaçao blanc",
                "Quelques gouttes d'Angostura bitters",
            ],
            "summary": "Le Brandy Champerelle : un cocktail d&#x27;origine française à "
            "déguster en digestif.",
            "title": "Cocktail Brandy Champerelle",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Brandy Egg Nog est une version "
            "simplifiée du grand cocktail classique Egg Nogg (Lait de "
            "poule) avec ici le blanc d&#x27;oeuf et le rhum en "
            "moins.</p>",
            "ingredients": [
                "4 cl de Cognac",
                "1 jaune d'œuf",
                "1 cl de sirop de sucre",
                "5 cl de lait",
                "Noix de muscade en poudre",
            ],
            "summary": "Le Brandy Egg Nog : Trinquer sans à priori avec un très bon "
            "cocktail à base d&#x27;œuf.",
            "title": "Cocktail Brandy Egg Nog",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Brandy Julep fait partie de la "
            "famille des &quot;juleps&quot; dont la consommation "
            "remonterait au 17ème ou 18ème siècle et dont le cocktail le "
            "plus connu est le Mint Julep. Le Brandy Julep est publié "
            "pour la première fois sous ce nom en 1862 dans &quot;How to "
            "mix drinks&quot; de Jerry Thomas.</p>",
            "ingredients": [
                "5 cl de Cognac",
                "1 cuillère à café de sucre en poudre",
                "5 à 7 feuilles de menthe fraîche",
            ],
            "summary": "Le Brandy Julep : un cocktail de la famille des juleps en "
            "version digestif.",
            "title": "Cocktail Brandy Julep",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: verre à dégustation ou à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Brandy Scaffa est apparu en 1862 "
            "dans &quot;Bartenders Guide : How to mix drinks&quot; de "
            "Jerry Thomas, aucune information quant à l&#x27;origine de "
            "cette recette.</p>",
            "ingredients": [
                "5/10 de Cognac",
                "5/10 de marasquin",
                "2 traits d'Angostura bitters",
            ],
            "summary": "Le Brandy Scaffa : un cocktail à étages en digestif !",
            "title": "Cocktail Brandy Scaffa",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>2ème version</h2><p>Faire "
            "une tasse de café chaud. Poser une cuillère à café au dessus "
            "de la tasse. Insérer dans la cuillère le morceau de sucre "
            "puis le brandy. Faire flamber le brandy avec le morceau de "
            "sucre. Servir ainsi ou insérer le contenu de la cuillère "
            "dans la tasse quand la flamme s&#x27;éteint.</p>",
            "ingredients": [
                "6 cl de Cognac",
                "12 cl de café chaud",
                "1 cuillère à café de sucre en poudre",
                "6 cl de crème liquide",
            ],
            "summary": "Le café royal : deux recettes et deux techniques existent pour "
            "ce cocktail.",
            "title": "Cocktail Café royal",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Egg Nogg (aussi appelé Lait de "
            "poule ) apparaît dès 1862 dans &quot;How to mix drinks&quot; "
            "de Jerry Thomas. Jerry Thomas nous y indique que les eggs "
            "noggs sont d&#x27;origine américaine, qu&#x27;ils sont "
            "consommés pendant Noël dans le nord de l&#x27;Amérique et en "
            "toutes saisons dans le sud. Le Egg Nogg était appelé en "
            "Écosse &quot;Auld man&#x27;s milk&quot;.</p><p>La naissance "
            "du Egg Nogg fait encore débat mais il semble qu&#x27;il "
            "était déjà utilisé au 17ème siècle pour porter un toast. Le "
            "lait et les œufs n&#x27;étant pas à la portée de tous à "
            "cette époque, cette boisson s&#x27;adressait plutôt aux "
            "classes aisées ou aux fermiers.</p><p>Notez que le nom de ce "
            "cocktail peut se trouver sous différentes orthographes "
            "(eggnog, egg nog...), en réalité la bonne orthographe telle "
            "qu&#x27;elle a été écrite pour la première fois en 1862 est "
            "&quot;Egg Nogg&quot;.</p><h2>Variantes du Egg Nogg</h2><p>• "
            "Baltimore Egg Nogg</p><p>• General Harrison&#x27;s Egg "
            "Nogg</p><p>• Sherry Egg Nogg</p><p>• Brandy Egg Nog</p>",
            "ingredients": [
                "1 cuillère à café de sucre en poudre",
                "2 cl d'eau fraîche",
                "1 oeuf",
                "4 cl de Cognac",
                "2 cl de rhum brun",
                "5 cl de lait",
                "1 pincée de noix de muscade râpée",
            ],
            "summary": "Le cocktail Egg Nogg (Lait de poule) : né vers le XVIIème siècle "
            "il dispose de nombreuses variantes.",
            "title": "Cocktail Egg Nogg (Lait de poule)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail French Connection est un digestif "
            "dont la recette se réalise à parts égales de Cognac et "
            "d&#x27;Amaretto, il a été appelé ainsi d&#x27;après le film "
            "américan de 1971 du même nom The French Connection .</p>",
            "ingredients": ["4 cl de Cognac", "4 cl de Amaretto"],
            "summary": "Le French Connection : Un cocktail au subtil goût d&#x27;amande "
            "pour l&#x27;après-repas.",
            "title": "Cocktail French Connection",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tasse en cuivre</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail French Mule est la variante française du Moscow "
            "Mule, la seule diffrence réside dans l&#x27;eau-de-vie "
            "utilisée, ici du Cognac à la place de la vodka.</p><p>Tout "
            "comme son ascendant, le French Mule se sert par tradition "
            "dans une tasse en cuivre.</p>",
            "ingredients": [
                "5 cl de Cognac",
                "2 cl de jus de citron vert",
                "8 cl de Ginger Beer",
            ],
            "summary": "Le cocktail French Mule : la variante française du Moscow Mule !",
            "title": "Cocktail French Mule",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: grande tasse à café</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Hot Brandy Alexander est une "
            "variante du célèbre Brandy Alexander à base de brandy, crème "
            "de cacao et crème fraîche.</p>",
            "ingredients": [
                "3 cl de Cognac",
                "3 cl de liqueur ou crème de cacao",
                "12 cl de lait chaud",
                "Crème fouettée / chantilly",
            ],
            "summary": "Le Hot Brandy Alexander : la version chaude du fameux Brandy "
            "Alexander.",
            "title": "Cocktail Hot Brandy Alexander",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>2ème "
            "version</h2><p>Frapper tous les ingrédients au shaker puis "
            "verser dans les verres en filtrant la glace.</p><h2>Histoire "
            "et origine</h2><p>Le cocktail Metropolitan (métropolitain en "
            "français) dispose aujourd&#x27;hui de deux recettes bien "
            "différentes. Il est difficile de définir l&#x27;inventeur de "
            "la version originale (la 1ère ci-dessus), en effet la "
            "recette serait apparue pour la première fois en 1884 dans "
            "&quot;Modern Bartender&#x27;s Guide&quot; de O. H. Byron, la "
            "recette aurait aussi été imprimée en 1935 dans &quot;The Old "
            "Waldorf-Astoria Bar Book&quot;.</p><p>Pour la version plus "
            "moderne qui est un dérivé du Cosmopolitan, on dit que la "
            "recette aurait été créée par Chuck Coggins en 1993, barman "
            "au &quot;Marion&#x27;s Continental Restaurant and "
            "Lounge&quot; à Manhattan (New York).</p>",
            "ingredients": [
                "4 cl de Cognac",
                "2 cl de vermouth rouge (Martini...)",
                "1 cl de sirop de sucre",
                "Quelques traits d'Angostura bitters",
            ],
            "summary": "Le Metropolitan : deux cocktails aux recettes bien distinctes "
            "portent le nom de Metropolitan.",
            "title": "Cocktail Metropolitan",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre rocks</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Pisco Sour est un symbole "
            "national revendiqué à la fois par le Pérou et le Chili. Tous "
            "deux prétendent que le Pisco (eau-de-vin de raisin) a été "
            "créé dans leur pays respectif.</p><p>Le Pisco Sour serait né "
            "peu dans les années 1920 à Lima, capitale du Pérou. Le "
            "créateur du cocktail serait Victor Morris, alias &quot;Le "
            "Gringo&quot; et propritaire du Morris Bar. Le whisky sour "
            "aurait été pris comme modèle pour élaborer un pisco sour qui "
            "aurait été à base de pisco, de jus de citron et de sirop de "
            "sucre. En 1928-1929 le livre &quot;Lima, the City of Kings "
            "1928-29&quot; aurait mentionné le Morris Bar en indiquant le "
            "pisco sour comme une spécialité du lieu. On dit que "
            "c&#x27;est l&#x27;hôtel Maury qui aurait établi la version "
            "finale du Pisco Sour, celle que nous connaissons "
            "aujourd&#x27;hui avec notamment le blanc d&#x27;oeuf en "
            "plus. Très vite, le pisco sour s&#x27;est invité sur les "
            "cartes de tous les bars du coin et notamment le Country Club "
            "dans lequel on trouve les meilleurs piscos sours, ainsi que "
            "l&#x27;hôtel Bolivar qui est à l&#x27;origine du cocktail "
            "&quot;Cathedral&quot;, un pisco sour avec une double dose de "
            "pisco.</p><p>Chaque année au Pérou un jour férié est dédié "
            "au pisco sour, il s&#x27;agit du deuxième samedi de chaque "
            "mois de février.</p>",
            "ingredients": [
                "4 cl de Pisco (brandy)",
                "2 cl de jus de citron vert pressé et filtré",
                "1 cl de sirop de sucre",
                "Le blanc d'un petit oeuf",
                "1 trait d'Angostura bitters",
            ],
            "summary": "Le cocktail Pisco Sour : la boisson nationale revendiquée par "
            "deux pays sud-américains.",
            "title": "Cocktail Pisco Sour",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Piscola est un cocktail natif et "
            "emblématique du Chili, depuis le début des années 2000 il a "
            "été mis en place au Chili la journée du Piscola qui a lieu "
            "tous les 8 février.</p><p>Les Piscolas sont réalisés avec du "
            "Coca Cola ou du Pepsi ainsi que du Pisco qui est un Brandy "
            "comme le Cognac.</p>",
            "ingredients": ["5 cl de Pisco", "10 cl de Cola"],
            "summary": "Le cocktail Piscola : l&#x27;une des boissons emblématiques du "
            "Chili.",
            "title": "Cocktail Piscola",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><p>* Si vous n&#x27;avez pas "
            "le matériel pour pulvériser dans le verre, faites tourner la "
            "glace et l&#x27;absinthe avec une cuillère à mélange pour "
            "imprégner tout l&#x27;intérieur du verre.</p><h2>Histoire et "
            "origine</h2><p>Le cocktail Sazerac aurait été créé vers "
            "1850, il tient son nom du Cognac du même nom avec lequel le "
            "cocktail était réalisé à l&#x27;origine. Quelques années "
            "plus tard, le Cognac a été contraint d&#x27;être remplacé "
            "par du rhye whiskey à cause du phylloxera qui détruisait les "
            "vignes (nb : le cognac est une eau-de-vie de vin). La "
            "recette originale du Sazerac est donc bien avec du "
            "Cognac.</p><p>La technique de réalisation du Sazerac est "
            "unique. C&#x27;est une tradition et une histoire à "
            "respecter, on ne réalise pas cette recette comme "
            "n&#x27;importe quel cocktail se réalisant directement au "
            "verre ! Suivez donc bien les instructions "
            "ci-dessus.</p><p>Certains servent les Sazeracs sur de la "
            "glace pilée, nous le déconseillons fortement afin que les "
            "arômes ne soient pas noyés.</p><p>Le Sazerac est un vieu "
            "cocktail, mais contrairement à certaines idées reçues ce "
            "n&#x27;est pas le plus ancien.</p>",
            "ingredients": [
                "5 cl de Cognac",
                "1 cl d'Absinthe",
                "1 cl de sirop de sucre",
                "2 ou 3 trait de Peychaud's Bitters",
            ],
            "summary": "Le cocktail Sazerac : une technique de réalisation et une "
            "tradition à respecter sans laquelle un Sazerac n&#x27;en serait "
            "pas un.",
            "title": "Cocktail Sazerac",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Comme beaucoup de cocktails classiques, "
            "l&#x27;origine du cocktail Side Car n&#x27;est pas "
            "officiellement définie. Le Side car aurait vraisemblablement "
            "vu le jour au Buck&#x27;s Club à Londres au début des années "
            "1920, son créateur serait Pat MacGarry, l&#x27;un des "
            "barmen. Une seconde version moins probable attribuerait ce "
            "cocktail à Franck Meier du Ritz à Paris vers 1923. Une autre "
            "hypothèse attribuait le cocktail Side car à Harry Mac Elhone "
            "du New York&#x27;s Bar / Harry&#x27;s Bar à Paris, mais ce "
            "n&#x27;est pas le cas car en 1922 il aurait lui-même "
            "attribué ce cocktail au Buck&#x27;s Club de "
            "Londres.</p><p>Robert Vermeire publie pour la première fois "
            "la recette en 1922 dans &quot;How to mix them&quot;, la "
            "recette était alors réalisée à parts égales de brandy "
            "(cognac), triple sec (cointreau) et jus de "
            "citron.</p><p>Concernant l&#x27;origine du nom que porte ce "
            "cocktail, les versions sont toutes aussi nombreuses. La "
            "version majoritairement retenue nous indique que le nom "
            "rendrait hommage à un officier de l&#x27;armée qui avait "
            "l&#x27;habitude de se rendre au bar en side car.</p><p>Son "
            "origine étant contestée, les dosages dans la recette font "
            "débat et personne ne peut affirmer aujourd&#x27;hui quelle "
            "est la proportionalité authentique des ingrédients, il ne "
            "s&#x27;agit que d&#x27;une question de goût propre à chacun. "
            "Certains préférerent en effet le cocktail Side car avec des "
            "ingrédients à doses égales mais cette option est très loin "
            "de faire l&#x27;unanimité, pour beaucoup l&#x27;équilibre du "
            "cocktail est entièrement rompu dans ce cas. À vous de "
            "tester...</p>",
            "ingredients": [
                "4 cl de Cognac",
                "2 cl de Cointreau",
                "1 cl de jus de citron jaune pressé et filtré",
            ],
            "summary": "Le Side Car : un cocktail puissant dissimulé sous une douce "
            "couleur jaune d&#x27;or.",
            "title": "Cocktail Side car",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre au cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Stinger a été publié pour la "
            "première fois en 1917 dans &quot;The idéal Bartender&quot; "
            "(Le barman idéal) de Tom Bullock. Attribué à personne en "
            "particulier, le Stinger est considéré à cette époque comme "
            "le &quot;night cap&quot; (bonnet de nuit) des soirées à New "
            "York : c&#x27;est le dernier cocktail que l&#x27;on sirote "
            "avant d&#x27;aller se coucher.</p><p>Traditionnellement "
            "réalisé avec du cognac et bu en digestif, le Stinger est "
            "parfois aussi considéré comme un &quot;type&quot; de "
            "cocktail dans lequel on associe la crème de menthe blanche à "
            "tout spiritueux ou brandy. Dans cet esprit, un stinger "
            "serait alors consommé en fin de repas et associé avec un "
            "dessert au chocolat.</p><p>Certains barmen réalise le "
            "Stinger directement au verre et sur de la glace pilée.</p>",
            "ingredients": [
                "7 cl de Cognac",
                "3 cl de crème de menthe blanche",
            ],
            "summary": "Le Stinger : le cocktail qui fût le bonnet de nuit des soirées "
            "new yorkaises au début du XXème siècle.",
            "title": "Cocktail Stinger",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler, sling ou verre tulipe</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Yungueño est le cocktail traditionnel "
            "bolivien, il se compose de Singani qui est une eau-de-vie de "
            "vin fabriquée en Bolivie (à substituer par du pisco à défaut "
            "d&#x27;en avoir), de jus d&#x27;orange, et de sucre en "
            "poudre.</p>",
            "ingredients": [
                "7 cl de brandy (Singani ou Pisco)",
                "13 cl de jus d'orange",
                "2 cuillères à café de cassonade",
            ],
            "summary": "Le Yungueño : le cocktail traditionnel de Bolivie.",
            "title": "Cocktail Yungueño",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: flûte à champagne</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Aucune information quant à l&#x27;origine du "
            "cocktail Air Mail (écrit aussi parfois airmail) qui porte le "
            "nom d&#x27;une société de transport aérien de courrier, "
            "c&#x27;est une recette à base de Champagne qui trouvera "
            "idéalement sa place lors des fêtes de Noël ou du Nouvel "
            "An.</p>",
            "ingredients": [
                "4 cl de rhum ambré",
                "2 cl de jus de citron vert pressé et filtré",
                "1 cuillère à café de miel",
                "5 à 7 cl de Champagne",
            ],
            "summary": "Le cocktail Air mail : une recette au champagne à servir "
            "idéalement lors des fêtes de fin d&#x27;année.",
            "title": "Cocktail Air mail",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>D&#x27;origine pas réellement connue, le "
            "cocktail Barbotage est à choisir pour ravir avec certitude "
            "vos invités lors de grandes réceptions et autres moments "
            "festifs. Le champagne, idéal dans ces moments-là, se verra "
            "additionner d&#x27;ingrédients qui rendront ce cocktail très "
            "fruité et rafraîchissant, de quoi régaler avec élégance vos "
            "conviés.</p>",
            "ingredients": [
                "1 cl de sirop de grenadine",
                "2 cl de jus de citron pressé et filtré",
                "4 cl de jus d'orange",
                "5 cl de Champagne",
            ],
            "summary": "Le Barbotage : un cocktail qui allie douceur et fraîcheur à la "
            "finesse du champagne.",
            "title": "Cocktail Barbotage",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Bellini est un cocktail "
            "&quot;classique&quot;, ceci est la recette officielle de "
            "l&#x27;IBA (International Bartender Association).</p><p>Le "
            "Bellini a été créé par Giuseppe Cipriani en 1948 au "
            "Harry&#x27;s Bar de Venise, Giuseppe a appelé son cocktail "
            "ainsi en l&#x27;honneur du peintre Giovanni "
            "Bellini.</p><p>Le Harry&#x27;s Bar de Venise est un "
            "établissement très réputé créé en 1931, de nombreuses "
            "célébrités y sont venus, on parle de Ernest Hemingway, Orson "
            "Welles, Maria Callas ou encore Charly Chaplin.</p><p>À "
            "l&#x27;origine, les bellinis tels qu&#x27;ils avaient "
            "initialement été inventés par leur créateur se faisaient "
            "avec de la purée de pêche blanche mariné dans le vin et un "
            "trait de jus de framboise que l&#x27;on complète avec le "
            "mousseux italien &quot;Prosecco&quot;.</p>",
            "ingredients": [
                "5 cl de purée de pêche blanche",
                "10 cl de Prosecco",
            ],
            "summary": "Le cocktail Bellini : une recette italienne créée en 1948 à "
            "Venise.",
            "title": "Cocktail Bellini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte ou pilsner</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Black Velvet est un cocktail qui "
            "offre une combinaison originale entre la bière brune et le "
            "champagne à parts égales.</p><p>Il aurait été créé par le "
            "barman du Brooks&#x27;s Club de Londres à la mi-décembre "
            "1861, il aurait été servi alors que le pays était en deuil "
            "suite à la mort du prince Albert, consort de la Reine "
            "Victoria. Le barman avait décidé que même le champagne "
            "devait porter le deuil, ce mélange improbable est devenu par "
            "la suite très célèbre, et bien au-delà des frontières.</p>",
            "ingredients": ["50% de bière brune", "50% de Champagne"],
            "summary": "Le cocktail Black Velvet : une recette osée qui marie la bière "
            "et le champagne.",
            "title": "Cocktail Black Velvet",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Buck&#x27;s Fizz aurait été créé "
            "en 1921 par Pat McGarry au Buck&#x27;s Club à Londres, "
            "d&#x27;où le nom du cocktail.</p><p>Vous pourrez croiser des "
            "recettes du Buck&#x27;s Fizz avec du sirop de grenadine mail "
            "il n&#x27;en est rien. La recette originale appelle à 2 "
            "parts de champagne pour 1 part de jus d&#x27;orange, et les "
            "trois premières publication de la recette en 1930 "
            "(&quot;Savoy Cocktail Book&quot; de Harry Craddock), 1936 "
            "(&quot;Artistry of Mixing Drinks&quot; de Frank Meier) puis "
            "1937 (&quot;Cafe Royal Cocktail Book&quot; de W. J. Tarling) "
            "n&#x27;inclut en aucun cas du sirop de grenadine.</p><p>La "
            "composition du Buck&#x27;s Fizz est identique à celle du "
            "cocktail Mimosa qui pour sa part est fait à parts égales de "
            "Champagne et de jus d&#x27;orange.</p>",
            "ingredients": [
                "5 cl de jus d'orange",
                "7 cl de Champagne",
            ],
            "summary": "Le Buck&#x27;s Fizz : un cocktail utilisé pour les fêtes de fin "
            "d&#x27;année outre-Manche.",
            "title": "Cocktail Buck's Fizz",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à vin</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 1 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Cardinal est un descendant du "
            "kir, fameux apéritif d&#x27;origine bourguignonne. Le "
            "cardinal s&#x27;appellerait ainsi pour sa robe pourpre, il "
            "accepterait donc tout vin rouge de Bourgogne (ou proche) ne "
            "compromettant pas cette robe.</p><p>Selon la qualité des "
            "crèmes de cassis utilisées, il faut parfois en adapter la "
            "quantité pour conserver l&#x27;équilibre des "
            "&quot;cardinaux&quot;.</p>",
            "ingredients": [
                "2 cl de crème de cassis",
                "10 cl de vin rouge de Bourgogne",
            ],
            "summary": "Le cocktail Cardinal : une variante du célèbre kir mais avec du "
            "vin rouge.",
            "title": "Cocktail Cardinal",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>D&#x27;origine pas réellement connue, la "
            "recette du Champagne cocktail a été publiée pour la première "
            "fois en 1862 dans &quot;The Bartender&#x27;s Guide : How To "
            "Mix Drinks&quot; de Jerry Thomas.</p><p>Depuis la recette a "
            "bien évoluée puisque dans cette version de 1862 il n&#x27;y "
            "avait pas de cognac, le sucre était en poudre, le vin était "
            "versé dans un tumbler rempli au tiers de glace pilée, et le "
            "cocktail était réalisé au shaker !</p><p>Le champagne "
            "cocktail est idéal pour les fêtes et célébrations les plus "
            "prestigieuses, les petites touches d&#x27;amertume et de "
            "finesse adoucies par le sucre rendent ce cocktail tout à "
            "fait exquis.</p>",
            "ingredients": [
                "1 cl de Cognac",
                "9 cl de Champagne",
                "1 morceau de sucre",
                "2-3 traits d'Angostura bitters",
            ],
            "summary": "Le Champagne cocktail : l&#x27;un des plus grands cocktails de "
            "prestige, idéal pour les grandes occasions.",
            "title": "Cocktail Champagne cocktail",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old fashioned ou flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Champagne Julep fait "
            "partie de la famille des juleps, c&#x27;est une variante du "
            "célèbre Mint Julep.</p>",
            "ingredients": [
                "4 cl de Cognac",
                "1 cl de sirop de sucre de canne",
                "6 cl de Champagne",
                "4 feuilles de menthe",
            ],
            "summary": "Le champagne Julep : une variante du grand classique mint julep.",
            "title": "Cocktail Champagne Julep",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à vin</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 1 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Communard est l&#x27;un des "
            "nombreux dérivés du célèbre kir. L&#x27;histoire du "
            "communard n&#x27;est pas précisément connue même si cette "
            "recette trouve son origine en Bourgogne.</p><p>Le mystère "
            "subsiste effectivement quant au nom donné à ce cocktail, on "
            "dit que sa couleur rouge sang évoquerait probablement les "
            "évènements sanglants de la Commune de Paris en 1871 et la "
            "couleur du drapeau. Les cocktails communards se "
            "réaliseraient donc avec des vins rouges de Bourgogne (ou "
            "proche) et dont la robe se rapproche du rouge sang.</p>",
            "ingredients": ["2 cl de crème de cassis", "10 cl de vin rouge"],
            "summary": "Le cocktail Communard : une recette dérivée du kir, à base de "
            "crème de cassis et vin rouge.",
            "title": "Cocktail Communard",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Death in the afternoon est "
            "attribué à Ernest Hemingway qui vers 1935 invite à ajouter "
            "du champagne glacé jusqu&#x27;à ce qu&#x27;il atteigne une "
            "&quot;bonne opacification opalescente&quot;.</p>",
            "ingredients": ["3 cl d'absinthe", "9 cl de Champagne"],
            "summary": "Le cocktail Death in the afternoon : une recette signifiant "
            "&quot;mort en après-midi&quot;.",
            "title": "Cocktail Death in the afternoon",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à bière</li>\n"
            "<li>Type&nbsp;: long drink (25cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Embuscade est originaire de la "
            "Basse Normandie et a été créé dans l&#x27;un des bars du "
            "centre historique de Caen. L&#x27;embuscade est un cocktail "
            "prisé des étudiants caennais.</p>",
            "ingredients": [
                "7 cl de vin blanc",
                "3 cl de Calvados",
                "3 cl de sirop de cassis",
                "2 cl de sirop de citron",
                "10 cl de bière",
            ],
            "summary": "L&#x27;embuscade : un cocktail d&#x27;origine caennaise à "
            "essayer lors d&#x27;une escapade en Normandie.",
            "title": "Cocktail Embuscade",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Jacuzzi est une recette au Champagne riche et "
            "fruitée, un peu à cheval entre le Mimosa, le Bellini et le "
            "French 75 puisqu&#x27;il comporte les ingrédients de ces 3 "
            "cocktails.</p>",
            "ingredients": [
                "2 cl de gin",
                "3 cl de liqueur de pêche",
                "3 cl de jus d'orange",
                "5 cl de Champagne",
            ],
            "summary": "Le cocktail Jacuzzi : une recette au Champagne riche en saveurs.",
            "title": "Cocktail Jacuzzi",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned ou tumbler</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Kalimotxo (écrit Calimocho en "
            "français) est un cocktail très populaire en Espagne, il est "
            "consommé dans de nombreux bars mais surtout lors du Botellón "
            ".</p><p>Le Botellón est une fête traditionnelle pendant "
            "laquelle les jeunes espagnols se rassemblent dans la rue "
            "pour consommer de l&#x27;alcool, fumer et écouter de la "
            "musique. Cette fête est née au pays basque espagnol mais "
            "s&#x27;est répandue plus tard dans tout le pays.</p><p>La "
            "recette du Kalimotxo est très simple à réaliser, rapide et à "
            "la portée de tous, d&#x27;où son succés en Espagne même face "
            "à la sangria.</p>",
            "ingredients": ["50% de Vin rouge", "50% de Cola"],
            "summary": "Le cocktail Kalimotxo (ou Calimocho) : une recette espagnole à "
            "base de Vin rouge et Cola.",
            "title": "Cocktail Kalimotxo",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Kir est sans doute l&#x27;apéritif le plus "
            "consommé en France, c&#x27;est un cocktail dont on a "
            "généralisé à tort la composition, beaucoup de personnes "
            "croient qu&#x27;il est composé d&#x27;un simple vin blanc "
            "accompagné de crème de cassis. Non, un kir n&#x27;est pas "
            "fait avec n&#x27;importe quel vin blanc mais avec du "
            "Bourgogne aligoté.</p><p>Pourtant les kirs s&#x27;appelaient "
            "jadis des &quot;blancs cassis&quot; jusqu&#x27;à ce que le "
            "chanoine Félix Kir donne son nom au cocktail. Félix Kir est "
            "né en 1876, a été ordonné prêtre en 1901, et a reçu la "
            "légion d&#x27;honneur en 1946, cette même année il est "
            "devenu maire de Dijon.</p><p>Dès l&#x27;élection de Félix "
            "Kir en 1946, les &quot;Kirs&quot; sont servis dans chaque "
            "évènement dijonnais et se font connaître sous ce nouveau "
            "nom, le kir a alors commencé à devenir célèbre.</p><p>La "
            "recette originale du kir se réalisait avec 1/3 de crème de "
            "cassis et 2/3 de Bourgogne aligoté. La présence de tant de "
            "crème était faite pour dissimuler le goût alors acide du "
            "Bourgogne aligoté.</p><p>Plus tard, la maison liquoriste "
            "Lejay-Lagoutte a l&#x27;autorisation du maire pour "
            "commercialiser les blancs-cassis sous le nom de "
            "&quot;kir&quot;. 12 ans après d&#x27;autres liquoristes "
            "possèdent l&#x27;accord du maire pour commercialiser le kir "
            "mais la marque est déjà déposée par Lejay-Lagoutte. De "
            "nombreux procès eurent lieu, mais la cour de cassation "
            "décide en 1992 que seule la maison Lejay-Lagoutte peut être "
            "titulaire de la marque &quot;Un kir&quot;.</p>",
            "ingredients": [
                "2 cl de crème de cassis",
                "10 cl de Bourgogne aligoté",
            ],
            "summary": "Le Kir : la recette d&#x27;un apéritif qui ne se réalise pas "
            "avec n&#x27;importe quel vin blanc.",
            "title": "Cocktail Kir",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Kir royal est un cocktail dérivé du "
            "célèbre Kir , le champagne remplace ici le vin blanc de "
            "Bourgogne utilisé pour les kirs simples.</p>",
            "ingredients": ["2 cl de crème de cassis", "10 cl de Champagne"],
            "summary": "Le cocktail Kir royal : quand le champagne s&#x27;invite dans un "
            "kir...",
            "title": "Cocktail Kir royal",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Mimosa (champagne orange) aurait "
            "été créé vers 1925 par un barman du Ritz à Paris. Ce "
            "cocktail consiste en 2 part égales de champagne et de jus "
            "d&#x27;orange frais.</p><p>On attribue souvent le Mimosa à "
            "Frank Meier mais dans son livre de 1933 &quot;The Artistry "
            "of Mixing Drinks&quot; il publie la recette sans la "
            "signer.</p><p>La recette du cocktail Buck&#x27;s Fizz est la "
            "même que le Mimosa à la différence près que les ingrédients "
            "ne sont pas à parts égales.</p>",
            "ingredients": [
                "6 cl de jus d'orange",
                "6 cl de Champagne",
            ],
            "summary": "Le cocktail Mimosa : un &quot;champagne orange&quot; à réaliser "
            "avec du jus d&#x27;orange fraîchement pressé.",
            "title": "Cocktail Mimosa",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Parfois appelé &quot;Harry&#x27;s Pick me "
            "Up&quot;, le cocktail Pick me Up aurait été créé par Bob "
            "Card, barman au &quot;Harry&#x27;s New York Bar&quot; à "
            "Paris dans les années 1920.</p><p>La première publication "
            "d&#x27;un cocktail &quot;Pick me Up&quot; remonte à 1927 "
            "dans &quot;Barflies and Cocktails&quot; de Harry McElhone. "
            "La recette ayant totalement changé, on trouve souvent ce "
            "coktail avec du jus de citron à la place du jus "
            "d&#x27;orange.</p>",
            "ingredients": [
                "3,5 cl de Cognac",
                "2,5 cl de jus d'orange",
                "1 cl de sirop de grenadine",
                "5 cl de Champagne",
            ],
            "summary": "Le cocktail Pick me up : une recette douce et fruitée idéale "
            "pour une réception.",
            "title": "Cocktail Pick me up",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à cidre ou pilsner</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Poor man&#x27;s Black Velvet est "
            "une variante du célèbre Black Velvet. Cette version dans "
            "lequel on remplace le champagne par du cidre se traduit en "
            "français par &quot;Black Velvet d&#x27;homme "
            "pauvre&quot;.</p>",
            "ingredients": ["5/10 de bière brune", "5/10 de cidre"],
            "summary": "Le cocktail Poor man&#x27;s Black Velvet : un dérivé du fameux "
            "Black Velvet mais en version &quot;homme pauvre&quot;.",
            "title": "Cocktail Poor man's Black Velvet",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à punch</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette de la Sangria basique est "
            "celle-ci, l&#x27;esprit de base se caractérise au minimum "
            "par la présence de vin rouge, de brandy, de fruits frais, de "
            "soda et parfois de sucre. Chacun est bien entendu libre "
            "d&#x27;y rajouter par exemple des fruits en morceaux "
            "(banane, pomme, pêche...), de la liqueur (porto, triple "
            "sec...), et/ou de la cannelle très courante dans les "
            "sangrias.</p><p>Le nom Sangria vient du mot espagnol "
            "&quot;sangre&quot; qui signifie en français "
            "&quot;sang&quot;, c&#x27;est la couleur du cocktail qui est "
            "à l&#x27;origine de son nom. Les ingrédients qui composent "
            "la recette de la sangria la rendent très fruitée et "
            "rafraîchissante, ce qui masque la teneur en alcool et donne "
            "à la sangria son petit côté sournois.</p>",
            "ingredients": [
                "75 cl de vin rouge (1 bouteille classique)",
                "8 cl de Cognac",
                "1 citron coupé en quartiers",
                "1 orange coupée en quartier",
                "20 cl de limonade ou ginger ale (Canada Dry)",
            ],
            "summary": "La Sangria : une recette fruitée originaire d&#x27;Espagne.",
            "title": "Cocktail Sangria",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Vous "
            "pouvez aussi réaliser la soupe angevine pour plusieurs "
            "personnes dans un grand récipient ou bol à punch, les "
            "proportions seront alors de 18 cl de Cointreau, 10 cl de jus "
            "de citron, 10 cl de sirop de sucre et 1 bouteille de 75 cl "
            "de vin mousseux.</p>",
            "ingredients": [
                "2 cl de Cointreau",
                "1 cl de jus de citron",
                "1 cl de sirop de sucre de canne",
                "8 cl de vin mousseux / crémant de Loire",
            ],
            "summary": "La soupe angevine : une recette originaire de l&#x27;Anjou "
            "idéale pour Noël, nouvel an ou autre fête.",
            "title": "Cocktail Soupe angevine",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à dégustation</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>Le Spritz fait partie des nouveaux cocktails "
            "classiques IBA, il est originaire d&#x27;Italie. La vraie "
            "recette du Spritz est toujours composé de Prosecco, Aperol "
            "et eau gazeuse.</p><p>L&#x27;Apérol est né peu après 1912, "
            "lorsque les frères Luigi et Silvio Barbieri reprirent la "
            "société d&#x27;alcool familiale à Padoue, une ville "
            "italienne située à côté de Venise. Le terme "
            "&quot;Apérol&quot; est par ailleurs tiré du mot français "
            "&quot;Apéro&quot;.</p><p>Vers les années 1950, la recette du "
            "Spritz commence à voir le jour, la renommée de cet Apéritif "
            "à Base de Vin (ABV) a ensuite été très vite grandissante en "
            "Italie.</p>",
            "ingredients": [
                "6 cl de Prosecco",
                "4 cl de Apérol",
                "2 cl d'eau gazeuse",
            ],
            "summary": "Le Spritz : la vraie recette d&#x27;un grand cocktail classique "
            "italien fait d&#x27;Apérol et de Prosecco.",
            "title": "Cocktail Spritz",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Tinto de Verano fait partie des cocktails "
            "les plus populaires en Espagne, il se réalise toujours avec "
            "du vin rouge, de la limonade et des agrumes.</p><p>Le Tinto "
            "de Verano signifie vin rouge d&#x27;été et pour cause, les "
            "espagnols ont trouvé le moyen à travers ce cocktail de "
            "pouvoir boire du vin rouge de manière plus cohérente pendant "
            "la période estivale, grâce à la limonade qui a "
            "l&#x27;avantage d&#x27;être très rafraîchissante.</p><p>Le "
            "Tinto de verano a commencé à devenir populaire en Espagne "
            "dans les années 1960 mais son origine remonte aux années "
            "1920. Le créateur des tintos de verano serait Federico "
            "Vargas Madero , propriétaire de l&#x27;auberge Venta de las "
            "Vargas à El Brillante , un quartier de Cordoue (Córdoba). "
            "C&#x27;est pour cette raison que cette boisson porte aussi "
            "le nom de Vargas .</p>",
            "ingredients": ["50% de vin rouge", "50% de limonade"],
            "summary": "Le cocktail Tinto de Verano : une recette emblématique espagnole "
            "signifiant vin rouge d&#x27;été.",
            "title": "Cocktail Tinto de Verano",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy ou tasse</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Vin chaud dispose de nombreuses recettes "
            "toutes différentes les unes des autres, en effet ce cocktail "
            "remonte à plusieurs siècles et il est donc difficile de "
            "s&#x27;en tenir à une recette d&#x27;origine.</p><p>Il "
            "s&#x27;agit de la plus simple et rapide des recettes de vins "
            "chauds que Cocktail Mag vous publie ici, vous pouvez "
            "rajouter selon votre goût du jus de citron, des clous de "
            "girofle et/ou de l&#x27;anis étoilé.</p><p>Outre-manche le "
            "vin chaud est appelé mulled wine ou spiced wine , sachez "
            "qu&#x27;ici ou ailleurs c&#x27;est généralement du vin "
            "français (souvent du Bordeaux) que l&#x27;on recommande "
            "d&#x27;utiliser.</p>",
            "ingredients": [
                "9 cl de vin rouge",
                "2 cl d'eau bouillante",
                "1 cl de sirop de sucre",
                "1 rondelle d'orange",
                "Cannelle en poudre",
            ],
            "summary": "Le vin chaud : un grand classique de la saison hivernale.",
            "title": "Cocktail Vin Chaud",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Acapulco Gold est un cocktail "
            "sans alcool dont on ne dispose pas d&#x27;information quant "
            "à l&#x27;origine de sa recette.</p>",
            "ingredients": [
                "6 cl de jus d'ananas",
                "2 cl de jus de raisin",
                "2 cl de crème ou lait de coco",
                "2 cl de crème fouettée",
            ],
            "summary": "Le Acapulco Gold : un cocktail sans alcool très onctueux.",
            "title": "Cocktail Acapulco Gold",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Afterglow est un cocktail sans alcool aux "
            "ingrédients basiques, parfait pour les enfants.</p>",
            "ingredients": [
                "5 cl de jus d'orange",
                "5 cl de jus d'ananas",
                "2 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail sans alcool Afterglow : une recette des plus simples "
            "à réaliser.",
            "title": "Cocktail Afterglow",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Alice n&#x27;a pas d&#x27;origine "
            "connue, c&#x27;est une recette qui plaira à celles et ceux "
            "qui apprécient les cocktails onctueux et fruités, et très "
            "adaptée pour les enfants.</p>",
            "ingredients": [
                "4 cl de sirop de grenadine",
                "6 cl de jus d'orange",
                "6 cl de jus d'ananas",
                "4 cl de crème liquide",
            ],
            "summary": "Le cocktail Alice : une recette sans alcool onctueuse et "
            "fruitée.",
            "title": "Cocktail Alice",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre tulipe</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Aucune information quant à l&#x27;origine du "
            "cocktail Amazonas qui est aussi le nom d&#x27;un État du "
            "Brésil ayant pour capitale Manaus .</p><p>Les Amazonas se "
            "veulent quoiqu&#x27;il en soit très rafraîchissants grâce au "
            "jus de citron, l&#x27;Angostura bitters apporte en plus une "
            "petite pointe d&#x27;amertume très appréciable rendant par "
            "la même occasion cette recette un peu plus riche en "
            "saveurs.</p>",
            "ingredients": [
                "10 cl de jus de mangue",
                "2 cl de jus de citron pressé et filtré",
                "Quelques gouttes d'Angostura bitters",
                "1 mangue",
            ],
            "summary": "Le cocktail Amazonas : une recette rafraîchissante et sans "
            "alcool à base de mangues.",
            "title": "Cocktail Amazonas",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (25cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Apple cobbler n&#x27;a pas d&#x27;origine précise, "
            "il fait partie de la famille des cobblers qui sont un type "
            "de long drink.</p>",
            "ingredients": [
                "18 cl de jus de pomme",
                "6 cl de jus de citron pressé et filtré",
                "4 traits d'extrait de vanille",
            ],
            "summary": "Le cocktail Apple cobbler : une recette sans alcool fruitée et "
            "rafraîchissante.",
            "title": "Cocktail Apple Cobbler",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le Apple "
            "Rose est un cocktail désaltérant sans alcool que vous pouvez "
            "décorer avec des fruits de votre choix : quartier de pomme, "
            "quartier de citron, fraise, feuille de menthe....</p>",
            "ingredients": [
                "5/10 de jus de pomme",
                "5/10 de lemon bitter (Schweppes lemon bitter...)",
                "un trait de sirop de framboise",
            ],
            "summary": "Le cocktail Apple rose : un recette qui met à l&#x27;honneur le "
            "&quot;lemon bitter&quot;.",
            "title": "Cocktail Apple Rose",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (25cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le Apple "
            "Shot est un cocktail qui porte plutôt mal son nom "
            "puisqu&#x27;il n&#x27;est pas un "
            "&quot;shot&quot;.</p><p>Recette sans alcool plutôt "
            "désaltérante, sa réalisation est à la portée de tous "
            "puisqu&#x27;elle ne comporte que des ingrédients basiques et "
            "que le cocktail est réalisé directement au verre.</p>",
            "ingredients": [
                "12 cl de jus de pomme",
                "12 cl de jus de limonade",
                "2 traits d'Angostura bitters",
            ],
            "summary": "Le cocktail Apple shot : une recette sans alcool désaltérante et "
            "simple à réaliser.",
            "title": "Cocktail Apple Shot",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Baby Bellini est la variante sans alcool du Bellini "
            "classique.</p><p>* À défaut de trouver du cidre sans alcool "
            "vous pouvez opter pour du vin blanc pétillant sans alcool, "
            "ou du ginger ale (Canada Dry).</p>",
            "ingredients": [
                "4 cl de nectar de pêche",
                "2 cl de jus de citron pressé et filtré",
                "6 cl de cidre sans alcool *",
            ],
            "summary": "Le cocktail Baby Bellini : la version sans alcool du célèbre "
            "Bellini.",
            "title": "Cocktail Baby Bellini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le Batman "
            "est un cocktail sans alcool très simple à réaliser et fait "
            "d&#x27;ingrédients très basiques, c&#x27;est une recette "
            "largement destinée aux enfants.</p>",
            "ingredients": [
                "2 cl de sirop de grenadine",
                "12 cl de jus d'orange",
                "6 cl de limonade",
            ],
            "summary": "Le cocktail Batman : une recette sans alcool très simple, "
            "destinée aux enfants.",
            "title": "Cocktail Batman",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Bloody Orange est une variante sans alcool du "
            "célèbre Bloody Mary. Le jus de betterave vient apporter "
            "l&#x27;aspect sanglant au cocktail (&quot; Bloody &quot;), "
            "sa présence a d&#x27;ailleurs la particularité d&#x27;allier "
            "jus de fruits et de légumes dans une même recette.</p>",
            "ingredients": [
                "7 cl de jus d'orange",
                "7 cl de jus de pomme",
                "6 cl de jus de betterave",
            ],
            "summary": "Le cocktail Bloody Orange : une variante du célèbre Bloody Mary.",
            "title": "Cocktail Bloody Orange",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: hurricane ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Bora bora est un cocktail qui se veut très "
            "fruité et rafraîchissant. La célèbre île de Polynésie "
            "française située dans le pacifique sud a donné son nom à "
            "cette recette qui, avec ses saveurs exotiques, se "
            "dégusterait effectivement volontiers dans ce genre de petit "
            "coin de paradis.</p>",
            "ingredients": [
                "2 cl de jus de citron",
                "2 cl de sirop de grenadine",
                "8 cl de jus de fruits de la passion",
                "8 cl de jus d'ananas",
            ],
            "summary": "Le cocktail Bora bora : une recette exotique et rafraîchissante "
            "à déguster sans modération.",
            "title": "Cocktail Bora bora",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le Bora "
            "Bora Brew est un cocktail sans alcool toujours réalisé avec "
            "du jus d&#x27;ananas 100% pur jus, du ginger ale et 1 trait "
            "de sirop de grenadine, à décorer théoriquement avec un "
            "quartier d&#x27;ananas.</p>",
            "ingredients": [
                "12 cl de jus d'ananas",
                "6 cl de ginger ale (Canada Dry)",
                "2 cl de sirop de grenadine",
            ],
            "summary": "Le Bora Bora Brew : un cocktail sans alcool à base de jus "
            "d&#x27;ananas.",
            "title": "Cocktail Bora Bora Brew",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: sling</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le café "
            "frappé est une recette assez simple uniquement composée de "
            "café et sucre de canne.</p><p>Comme son nom l&#x27;indique "
            "c&#x27;est un café qui est frappé au shaker, ce qui va "
            "d&#x27;ailleurs lui offrir une jolie mousse. Les cafés "
            "frappés sont généralement servis dans des verres sling.</p>",
            "ingredients": ["10 cl de café", "2 cl de sirop de sucre de canne"],
            "summary": "Le café frappé : la boisson chaude préférée des français en "
            "version glacée.",
            "title": "Cocktail Café frappé",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Cendrillon , plus connu sous son nom anglissime "
            "&quot;Cinderella&quot;, est un cocktail sans alcool que "
            "l&#x27;on recommande souvent de réaliser avec des jus de "
            "fruits fraîchement pressés.</p><p>Cette recette est la "
            "version simplifiée, la limonade remplace effectivement ici "
            "le jus de citron et l&#x27;eau gazeuse généralement utilisés "
            "dans les Cendrillons .</p><p>Le Cendrillon est un délicieux "
            "cocktail très fruité, rafraîchissant, et très polyvalent. En "
            "effet, il séduit petits et grands et sait s&#x27;inviter "
            "dans de nombreuses occasions : fêtes et anniversaires "
            "notamment d&#x27;enfants, sur une plage, en apéritif, en "
            "brunch...</p>",
            "ingredients": [
                "7 cl de jus d'orange",
                "6 cl de jus d'ananas",
                "2 cl de sirop de grenadine",
                "5 cl de limonade",
            ],
            "summary": "Le cocktail Cendrillon (Cinderella) : une recette sans alcool "
            "fruitée et rafraîchissante.",
            "title": "Cocktail Cendrillon (Cinderella)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>DBK est "
            "le nom donné aux Diabolos Banane-Kiwi, célèbres boissons "
            "sans alcool et très rafraîchissantes que tous les barmen "
            "connaissent.</p>",
            "ingredients": [
                "1,5 cl de sirop de banane",
                "1,5 cl de sirop de kiwi",
                "17 cl de limonade",
            ],
            "summary": "Le cocktail DBK : la recette du diabolo banane-kiwi, célèbre "
            "boisson connue dans tous les bars de France.",
            "title": "Cocktail DBK",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: hurricane ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Avec son nom qui évoque la Floride, le "
            "cocktail Florida est un cocktail fruité et rafraîchissant "
            "qui existe aujourd&#x27;hui sous de multiples recettes "
            "toutes différentes les unes des autres, avec et sans alcool. "
            "La recette la plus courante à ce jour est celle "
            "ci-dessus.</p><p>Il est probable que le Florida ait été créé "
            "par le bartender historique Robert Vermeire, car c&#x27;est "
            "dans sa publication de 1922 &quot;Cocktails : How to mix "
            "them&quot; que l&#x27;on retrouve les premières traces de ce "
            "cocktail. Dans cette recette originale les floridas sont à "
            "servir dans un petit verre de vin, se réalisent au shaker et "
            "sont composés du jus d&#x27;un citron, du jus d&#x27;une "
            "demi-orange, 3 traits d&#x27;Angostura bitters, et 1 ou 2 "
            "traits de sirop de gomme.</p>",
            "ingredients": [
                "6 cl de jus d'orange",
                "6 cl de jus d'ananas",
                "5 cl de jus de citron pressé",
                "3 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Florida : une recette douce, fruitée et "
            "rafraîchissante idéale en été.",
            "title": "Cocktail Florida",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Ginger Mick rend hommage à Ginger "
            "Mick, personnage du roman australien de C.J. Dennis datant "
            "de 1916 &quot;The moods of Ginger Mick&quot; .</p><p>Plus "
            "tard en 1920, le film muet Ginger Mick basé sur le roman "
            "sort sur les écrans, il est réalisé par Raymond "
            "Longford.</p>",
            "ingredients": [
                "7 cl de jus de pomme",
                "3 cl de jus de citron pressé et filtré",
                "3 cl de tonic (Schweppes)",
                "7 cl de ginger ale (Canada Dry)",
            ],
            "summary": "Le cocktail Ginger Mick : une recette en hommage au héros "
            "d&#x27;un roman australien de 1916.",
            "title": "Cocktail Ginger Mick",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Voici la "
            "recette du kir pétillant sans alcool signé Cocktail Mag, "
            "idéal pour les anniversaires et autres fêtes de vos "
            "enfants.</p><p>Très simple à réaliser, il se compose "
            "uniquement de sirop de cassis et de vin blanc sans alcool, "
            "très facile à trouver en grande surface !</p>",
            "ingredients": [
                "2 cl de sirop de cassis",
                "10 cl de vin blanc pétillant sans alcool",
            ],
            "summary": "La version sans alcool du kir pétillant, idéal pour vos enfants "
            "!",
            "title": "Cocktail Kir pétillant sans alcool",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tulipe ou sling</li>\n"
            "<li>Type&nbsp;: long drink (25cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Ce Milk-Shake Mojito signé Cocktail Mag "
            "retrouve toutes les saveurs des vrais mojitos !</p>",
            "ingredients": [
                "1 boule de glace à la menthe",
                "1 boule de glace au citron vert",
                "3 cl de sirop saveur rhum",
                "20 cl de lait",
            ],
            "summary": "Le Milk-Shake Mojito : le cocktail préféré des français en "
            "version milkshake !",
            "title": "Cocktail Milk-Shake Mojito",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: hurricane</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Aucune information sur l&#x27;origine de la "
            "recette du cocktail Port au Prince .</p><p>Rappelons que "
            "Port au Prince est la capitale de Haïti, elle compte presque "
            "2.500.000 habitants que l&#x27;on appelle les "
            "&quot;port-au-princiens&quot; ou "
            "&quot;port-au-princiennes&quot;. On se rappelle que le 12 "
            "janvier 2010, un tremblement de terre de magitude 7 sur "
            "l&#x27;échelle de Richter a causé la mort d&#x27;environ "
            "230.000 personnes et fait environ 300.000 blessés.</p>",
            "ingredients": [
                "8 cl de jus d'ananas",
                "4 cl de jus de mangue",
                "4 cl de jus d'orange",
                "2 cl de jus de citron vert pressé et filtré",
                "2 cl de sirop de fraise",
            ],
            "summary": "Le Port au prince : un cocktail sans alcool en l&#x27;honneur de "
            "la capitale haïtienne.",
            "title": "Cocktail Port au Prince",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: bol ou saladier à punch</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À "
            "propos</h2><p>C&#x27;est donc une recette super facile "
            "d&#x27;un Punch sans alcool que Cocktail Mag vous propose, "
            "un punch idéal pour les fêtes de vos enfants !</p><p>Rien de "
            "plus simple, rien de plus rapide, même pas besoin de doser, "
            "et pas besoin non plus de laisser reposer le punch au frigo "
            "!</p><p>Vous verrez vos enfants vont adorer ... et vous "
            "aussi ;)</p>",
            "ingredients": [
                "1 litre de jus d'orange",
                "1 litre de jus d'ananas",
                "1 litre de jus de pamplemousse",
                "1 litre de limonade",
                "0,5 litre de sirop de grenadine",
            ],
            "summary": "La recette d&#x27;un punch sans alcool facile et rapide pour les "
            "enfants, parfait pour leurs anniversaires et autres fêtes !",
            "title": "Cocktail Punch sans alcool pour les enfants",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (16cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Pussyfoot (parfois écrit Pussy "
            "Foot) est un cocktail sans alcool avec jaune d&#x27;oeuf, un "
            "détail qui pourrait en rebuter plus d&#x27;un mais à "
            "tort...</p><p>Ce cocktail a été créé dans les années 1920 "
            "par Robert Vermeire du &quot;Embassy Club&quot; à Londres, "
            "c&#x27;est dans la publication &quot; Cocktails : how to mix "
            "them &quot; de 1922 dont il est l&#x27;auteur que l&#x27;on "
            "retrouve la recette du pussyfoot.</p><p>C&#x27;est aussi "
            "dans cette publication que l&#x27;on apprends que ce "
            "cocktail a été nommé ainsi en hommage à "
            "&quot;Pussyfoot&quot; Johnson, le &quot;champion du monde "
            "des abstentionnistes&quot; pour reprendre les mêmes termes. "
            "Effectivement, William Eugene Johnson (1862-1945) était un "
            "avocat et agent des services répressifs américain qui "
            "voulait faire interdire toute boisson enivrante.</p><p>La "
            "recette des pussyfoots a bien évolué, puisqu&#x27;à "
            "l&#x27;origine Robert Vermeire réalise ce cocktail avec le "
            "jus d&#x27;un citron, le jus d&#x27;une orange, un trait de "
            "sirop d&#x27;abricot, 3 brins de menthe et un petit blanc "
            "d&#x27;oeuf, le tout frappé au shaker.</p>",
            "ingredients": [
                "10 cl de jus d'orange",
                "3 cl de jus de citron pressé",
                "1 jaune d'œuf",
                "1,5 cl de sirop de grenadine",
            ],
            "summary": "Le Pussyfoot : un cocktail classique en hommage à un militant du "
            "sans-alcool.",
            "title": "Cocktail Pussyfoot",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball ou hurricane</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><p>Le Rainbow cocktail sans "
            "alcool , ou Virgin Rainbow Cocktail , est un cocktail à "
            "étages aux couleurs de l&#x27;arc-en-ciel, idéal pour les "
            "enfants. Il s&#x27;agit de la version sans alcool du vrai "
            "Rainbow Cocktail réalisé à l&#x27;origine avec de la vodka "
            "et du curaçao bleu.</p>",
            "ingredients": [
                "2 cl de sirop de grenadine",
                "13 cl de jus d'orange",
                "5 cl de limonade",
                "3 gouttes de colorant alimentaire liquide bleu",
            ],
            "summary": "Le Virgin Rainbow Cocktail : une recette sans alcool couleur "
            "arc-en-ciel !",
            "title": "Cocktail Rainbow cocktail sans alcool",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 1 mn</li></ul><h2>À propos</h2><p>Le Roy "
            "Rogers est un cocktail très simple à réaliser, c&#x27;est "
            "une boisson réalisée ni plus ni moins qu&#x27;avec du Coca "
            "et de la Grenadine. Roy Rogers (1911-1998) était un cow-boy "
            "et chanteur américain.</p>",
            "ingredients": ["2 cl de Sirop de grenadine", "18 cl de Cola"],
            "summary": "Le cocktail Roy Rogers : la recette d&#x27;un &quot;Coca "
            "Grenadine&quot; très simple à réaliser.",
            "title": "Cocktail Roy Rogers",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: bol à punch</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Voici la "
            "vraie recette de la Sangria sans alcool , on remplace le vin "
            "d&#x27;origine par du jus de raisin rouge, aucun intérêt se "
            "rajouter d&#x27;autres jus de fruits sinon ce n&#x27;est "
            "plus tellement une Sangria sans alcool !</p><p>On vous "
            "laisse choisir dans cette recette les fruits que vous "
            "souhaitez inclure, donc faites vous plaisir :) !</p>",
            "ingredients": [
                "3 litres de jus de raisin rouge",
                "1 litre de limonade",
                "0,5 litre de sirop de grenadine",
                "Fruits selon votre envie (citrons, oranges, bananes, "
                "pommes, fraises...)",
            ],
            "summary": "La vraie recette de la Sangria sans alcool, simple et rapide, "
            "pour les enfants et les adultes !",
            "title": "Cocktail Sangria sans alcool",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Dans la tradition mexicaine, le cocktail "
            "Sangrita se boit accompagné d&#x27;un shooter de tequila. La "
            "sangrita existe préparée en bouteille.</p><p>La recette "
            "intègre parfois du piment et de l&#x27;oignon, dans ce cas "
            "l&#x27;idéal est de réaliser plusieurs sangritas à la fois "
            "et les passer au blender. Ajoutez 1 petit oignon et 1 petit "
            "piment rouge pour environ 6 sangritas.</p><p>En mélangeant "
            "la tequila avec la sangrita on obtient le cocktail "
            "Vampiro.</p>",
            "ingredients": [
                "5 cl de jus de tomate",
                "2,5 cl de jus d'orange",
                "1 cl de jus de citron vert pressé et filtré",
                "2 ou 3 gouttes de tabasco",
                "2 ou 3 traits de sauce Worchestershire",
                "1 pincée de sel",
            ],
            "summary": "La sangrita : un cocktail qui se consomme accompagné d&#x27;un "
            "shooter de tequila au Mexique.",
            "title": "Cocktail Sangrita",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: hurricane ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Shirley Temple est un cocktail sans alcool "
            "né vraisemblablement dans les années 1930 à "
            "Hollywood.</p><p>Shirley Temple (1928-2014) a été la "
            "première enfant-star mondialement célèbre avant de devenir "
            "diplomate. Elle a donné son nom à ce cocktail spécialement "
            "conçu pour les enfants.</p>",
            "ingredients": [
                "3 cl de Sirop de grenadine",
                "17 cl de ginger ale (Canada Dry) ou 7up.",
                "1 cerise",
            ],
            "summary": "Le Shirley Temple : un cocktail qui porte le nom de la célèbre "
            "ancienne enfant-star.",
            "title": "Cocktail Shirley Temple",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Virgin Bloody Mary , généralement abrégé "
            "&quot;Virgin Mary&quot;, est la version sans alcool du "
            "célèbre Bloody Mary duquel on a simplement retirer la "
            "vodka.</p>",
            "ingredients": [
                "9 cl de jus de tomate",
                "Quelques gouttes de tabasco",
                "0,5 cl de sauce worcestershire",
                "2 cl de jus de citron pressé et filtré",
                "Sel et/ou sel de céleri et/ou poivre",
            ],
            "summary": "Le Virgin Bloody Mary : la version sans alcool du fameux Bloody "
            "Mary à la vodka.",
            "title": "Cocktail Virgin Bloody Mary",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (≈12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>La Virgin "
            "Caipirinha est la version sans alcool de la célèbre "
            "Caipirinha à base de Cachaça.</p>",
            "ingredients": [
                "1 citron vert",
                "2 cuillères à café de cassonade",
                "Tonic (Schweppes...)",
            ],
            "summary": "Le cocktail Virgin Caipirinha : la recette de la fameuse "
            "Caipirinha en version sans alcool.",
            "title": "Cocktail Virgin Caïpirinha",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à margarita</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Virgin Margarita est la version "
            "sans alcool de l&#x27;authentique Margarita qui aurait été "
            "créée par Margaret Sames vers 1948 à Acapulco (Mexique), et "
            "réalisée avec de la tequila, du triple sec et du jus de "
            "citron.</p><p>Tout comme la Margarita originale, on retrouve "
            "ici les saveurs de tequila, d&#x27;orange et de citron ainsi "
            "que l&#x27;étonnante alliance entre le sel, le sucre et "
            "l&#x27;acidité.</p>",
            "ingredients": [
                "12 cl de jus d'orange",
                "4 cl de jus de citron pressé et filtré",
                "4 cl de sirop saveur tequila",
            ],
            "summary": "Le cocktail Virgin Margarita : la recette sans alcool de la "
            "célèbre Margarita mexicaine.",
            "title": "Cocktail Virgin Margarita",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball ≥30cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><p>Contrairement à ce "
            "qu&#x27;on peut malheureusement voir quelques fois, jamais "
            "de &quot;sirop saveur mojito&quot; dans un virgin mojito ! "
            "Il n&#x27;y a aucun intérêt à cela puisqu&#x27;une fois que "
            "votre sirop saveur rhum remplace le rhum, votre virgin "
            "mojito a le goût d&#x27;un vrai mojito et n&#x27;a donc en "
            "aucun cas besoin d&#x27;un &quot;sirop saveur "
            "mojito&quot;.</p><h2>Histoire et origine</h2><p>Le cocktail "
            "Virgin Mojito a été créé à partir du célèbre Mojito à base "
            "de rhum que l&#x27;on attribue souvent à Francis Drake. Le "
            "Virgin Mojito est la version sans alcool et peut donc être "
            "consommé par tous. Les virgins mojitos sont des cocktails "
            "très rafraîchissants qui ont un grand succès, ils sont "
            "idéaux pendant la saison estivale.</p><p>Depuis "
            "l&#x27;apparition du sirop saveur rhum, le virgin mojito a "
            "un goût quasi identique à sa version alcoolisée, ce sirop "
            "saveur rhum remplace donc logiquement le rhum et le sucre en "
            "poudre.</p><p>Le virgin mojito existait déjà avant la sortie "
            "du sirop saveur rhum grâce auquel aujourd&#x27;hui les "
            "virgins mojitos ont le même goût que la version alcoolisée. "
            "La recette était alors composée de 3cl de jus de citron "
            "vert, quelques feuilles de menthe, 1 cuillère à café de "
            "sucre et 8cl de ginger ale.</p>",
            "ingredients": [
                "3 cl de sirop saveur rhum",
                "4 cl de jus de citron vert",
                "7 ou 8 feuilles de menthe verte",
                "4 ou 5 quartiers de citron vert",
                "8 cl d'eau gazeuse",
            ],
            "summary": "Le Virgin Mojito : la vraie recette en version sans alcool du "
            "très célèbre mojito à base de rhum.",
            "title": "Cocktail Virgin Mojito",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Virgin Pina Colada est la version sans alcool de la "
            "fameuse Piña Colada. Par conséquent et contrairement à ce "
            "que l&#x27;on peut malheureusement trouver sur certains "
            "sites de recettes, les Virgins Piñas Coladas doivent "
            "absolument garder les saveurs de leur version alcoolisée et "
            "donc inclure jus d&#x27;ananas et crème ou lait de coco, "
            "sans quoi bien entendu ce ne serait pas une vraie Virgin "
            "Pina Colada.</p><p>À l&#x27;origine la recette courante de "
            "la virgin pina colada se composait simplement de jus "
            "d&#x27;ananas et lait de coco, mais maintenant que l&#x27;on "
            "peut trouver du sirop saveur rhum, cette nouvelle version "
            "incluant ce sirop a le grand avantage de donner aux Virgins "
            "Pinas Coladas le même goût que la version alcoolisé et les "
            "mêmes saveurs exotiques.</p>",
            "ingredients": [
                "3 cl de sirop saveur rhum",
                "12 cl de jus d'ananas",
                "5 cl de lait de coco",
            ],
            "summary": "Le cocktail Virgin Pina colada : la recette sans alcool de la "
            "célèbre Piña Colada, tout aussi onctueuse et savoureuse.",
            "title": "Cocktail Virgin Pina Colada",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Virgin Planteur est la version sans alcool du "
            "fameux Planter&#x27;s Punch .</p><p>Le sirop saveur rhum "
            "vient remplacer le rhum brun d&#x27;origine, rendant le "
            "cocktail plus sucré.</p>",
            "ingredients": [
                "2 cl de sirop saveur rhum",
                "1 cl de sirop de grenadine",
                "5 cl de jus d'orange",
                "5 cl de jus d'ananas",
                "2 cl de jus de citron",
            ],
            "summary": "Le Virgin Planteur : la version sans alcool du célèbre "
            "planter&#x27;s punch.",
            "title": "Cocktail Virgin Planteur",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: à vin</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Virgin Spritz est la version sans alcool du fameux "
            "Spritz. Le Venezzio Bitter avec sa petite amertume vient "
            "remplacer l&#x27;Apérol d&#x27;origine, et le vin blanc "
            "pétillant sans alcool (que l&#x27;on trouve facilement en "
            "grande surface) vient quant à lui remplacer le "
            "Prosecco.</p><p>Très simple à réaliser et à la portée de "
            "tous, il se prépare directement au verre, dans un grand "
            "verre à vin.</p>",
            "ingredients": [
                "6 cl de Venezzio Bitter",
                "6 cl de vin blanc pétillant sans alcool",
            ],
            "summary": "Le cocktail Virgin Spritz : la version sans alcool du célèbre "
            "Spritz italien.",
            "title": "Cocktail Virgin Spritz (sans alcool)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: double verre à cocktail</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Ceci est la recette originale du Addington "
            "Cocktail telle qu&#x27;elle a été publiée par Harry Craddock "
            "en 1930 dans son célèbre livre de recettes The Savoy "
            "Cocktail Book .</p>",
            "ingredients": [
                "3,5 cl de vermouth blanc (Martini...)",
                "3,5 cl de vermouth rouge (Martini...)",
                "5 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Addington : une recette vintage datant de 1930.",
            "title": "Cocktail Addington",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Agincourt est le nom anglo-saxon de la "
            "commune française d&#x27;Azincourt située dans le "
            "Pas-de-Calais. Le nom donné à la recette du cocktail "
            "Agincourt fait très certainement référence à la bataille qui "
            "a eue lieu dans cette ville d&#x27;azincourt (Battle of "
            "Agincourt) en 1514 pendant la guerre de 100 ans.</p>",
            "ingredients": [
                "3 cl de vermouth dry (Martini extra dry, Noilly Prat dry)",
                "3 cl de vermouth doux (Martini...)",
                "1,5 cl de Amaretto",
                "0,5 cl de jus de citron pressé et filtré",
            ],
            "summary": "Le cocktail Agincourt : une recette en souvenir d&#x27;une "
            "bataille qui s&#x27;est déroulée dans le Pas-de-Calais.",
            "title": "Cocktail Agincourt",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Alabama Slammer est "
            "toujours composée à minima des ingrédients ci-dessus, "
            "parfois complétée de vodka ou de jus de citron. Pour des "
            "Alabama Slammers plus corsés, vous pouvez réduire la "
            "quantité de jus d&#x27;orange pour en mettre seulement la "
            "même dose que les autres ingrédients.</p><p>L&#x27;inventeur "
            "de l&#x27;Alabama Slammer reste inconnu mais on dit que le "
            "cocktail aurait vu le jour à l&#x27;Université de "
            "l&#x27;Alabama en 1975. L&#x27;Alabama est pour rappel un "
            "État sud-américain situé à proximité de la Floride.</p>",
            "ingredients": [
                "4 cl de Southern Comfort",
                "4 cl de Amaretto",
                "4 cl de Sloe Gin",
                "8 cl de jus d'orange",
            ],
            "summary": "Le cocktail Alabama Slammer : une recette aux airs de Sloe Comfy "
            "Screw.",
            "title": "Cocktail Alabama Slammer",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Ale Sangaree fait partie de la "
            "famille des &quot;sangarees&quot;. Parfois traduit par "
            "sangria, le sangaree est totalement différent. Les sangarees "
            "dateraint en effet des années 1770 alors que les sangrias "
            "datent des années 1960, les ingrédients qui les composent "
            "sont aussi complètement différents.</p><p>Le cocktail ale "
            "sangaree pourrait donc remonter au XVIIIème siècle, "
            "c&#x27;est en 1862 qu&#x27;est publiée pour la première fois "
            "la recette dans &quot;Bartender&#x27;s guide : How to mix "
            "drinks&quot; de Jerry Thomas.</p><p>&quot;Ale&quot; est un "
            "terme qui à l&#x27;origine désignait la Cervoise, ancêtre de "
            "la bière arrivée au cours du XVIIIème sièce et fabriquée "
            "avec du houblon.</p>",
            "ingredients": [
                "10 cl de bière cervoise",
                "1 cuillère à soupe de sucre",
                "Noix de muscade râpée",
            ],
            "summary": "Ale sangaree : une recette de cocktail qui met à l&#x27;honneur "
            "la cervoise.",
            "title": "Cocktail Ale Sangaree",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Informations "
            "supplémentaires</h2><p>Le cocktail Almond Joy peut aussi se "
            "réaliser au blender.</p>",
            "ingredients": [
                "1 part de Amaretto",
                "1 part de crème de cacao blanc (Marie Brizard...)",
                "4 parts de crème fraîche liquide",
            ],
            "summary": "Le cocktail Almond Joy : une recette douce et particulièrement "
            "crèmeuse.",
            "title": "Cocktail Almond Joy",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Amaretto Sour fait partie comme "
            "son nom l&#x27;indique de la famille des &quot;sours&quot; "
            "introduit par Jerry Thomas en 1862 et qui consiste à "
            "mélanger un spiritueux avec du citron et du sucre, rendant "
            "les cocktails acides et doux à la fois. Quant à la fameuse "
            "liqueur italienne Amaretto, elle a été créée en 1851 et "
            "n&#x27;a commencé à être importée au États-Unis que vers "
            "1960. Très difficile donc de trouver qui a eu l&#x27;idée en "
            "premier de rendre l&#x27;Amaretto "
            "&quot;sour&quot;.</p><p>Pour la garnison, le choix est "
            "souvent offert entre un zeste de citron, un zeste "
            "d&#x27;orange, ou une cerise accompagnée d&#x27;une "
            "demi-tranche de citron. L&#x27;Amaretto Sour étant sans "
            "origine connue, Cocktail Mag invite de ce fait au zeste de "
            "citron comme l&#x27;implique à l&#x27;origine la famille des "
            "&quot;sours&quot; introduite par Jerry Thomas.</p>",
            "ingredients": [
                "4 cl de Amaretto",
                "2 cl de jus de citron pressé et filtré",
                "1 cuillère à café de sucre en poudre",
            ],
            "summary": "Le cocktail Amaretto Sour : la fameuse liqueur italienne dans la "
            "douceur acidulée des &quot;sours&quot;.",
            "title": "Cocktail Amaretto Sour",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Amaretto Sunrise est une variante de la célèbre "
            "Tequila Sunrise, la liqueur d&#x27;amande italienne Amaretto "
            "vient ici remplacer la tequila d&#x27;origine.</p><p>Cette "
            "recette, qui sera très largement appréciée de celles et ceux "
            "qui aiment les cocktails doux et fruités, inspire de par sa "
            "couleur un lever de soleil et ce n&#x27;est pas un hasard. "
            "La Tequila Sunrise aurait été inventée très exactement dans "
            "ce but !</p>",
            "ingredients": [
                "6 cl de Amaretto",
                "12 cl de jus d'orange",
                "2 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Amaretto Sunrise : une variante de la Tequila "
            "Sunrise où l&#x27;Amaretto remplace la tequila.",
            "title": "Cocktail Amaretto Sunrise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (14cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Americano a vu le jour en 1861 au "
            "bar de Gaspare Campari (1828-1882). Le campari provenant de "
            "milan et le vermouth de Turin, le cocktail avait été "
            "initialement appelé le &quot;milano-torino&quot;.</p><p>En "
            "1919 commence la prohibition aux États-Unis, les américains "
            "profitent de leur séjour en Italie pour consommer des "
            "boissons alcoolisées. Le cocktail fût alors rebaptisé "
            "&quot;Américano&quot; en l&#x27;honneur des touristes "
            "américains qui appréciaient la boisson lors de leur séjour "
            "en Italie. La recette s&#x27;exporte alors aux États-Unis, "
            "le cocktail commence alors à devenir populaire.</p><p>Depuis "
            "l&#x27;Americano est un peu entré en concurrence avec le "
            "cocktail negroni, lui aussi à base de Campari mais plus "
            "viril (le gin remplace l&#x27;eau gazeuse). La popularité de "
            "l&#x27;Américano vascille donc selon les régions dans le "
            "monde.</p><p>Les americanos se consomment selon les "
            "habitudes et préférences de chacun. Certains suppriment "
            "l&#x27;eau gazeuse, certains ajoutent quelques gouttes "
            "d&#x27;angostura, quand d&#x27;autres diminuent ou "
            "augmentent la proportion de campari pour plus ou moins "
            "d&#x27;amertume.</p>",
            "ingredients": [
                "4 cl de Campari",
                "4 cl de vermouth rouge",
                "6 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Americano : un grand classique des amers à déguster "
            "en apéritif.",
            "title": "Cocktail Americano",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (&gt;7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Intenses "
            "et fortement parfumés, les cocktails andalusias "
            "s&#x27;apprécient en les dégustant doucement, idéalement à "
            "la fin d&#x27;un repas aux saveurs andalousiennes.</p>",
            "ingredients": [
                "4,5 cl de sherry (Xérès)",
                "1,5 cl de rhum blanc",
                "1,5 cl de Cognac",
            ],
            "summary": "Le cocktail Andalusia : une recette corsée aux parfums "
            "d&#x27;Andalousie.",
            "title": "Cocktail Andalusia",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à liqueur</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Angel&#x27;s Tip est une recette qui se réalise "
            "avec de la liqueur ou crème de cacao foncée ainsi que de la "
            "crème fraîche, c&#x27;est une recette semblable au cocktail "
            "Angel&#x27;s Tit .</p>",
            "ingredients": [
                "2/3 de crème de cacao",
                "1/3 de crème fraîche ou liquide",
                "1 cerise",
            ],
            "summary": "Le cocktail Angel&#x27;s Tip : une recette onctueuse à base de "
            "crème de cacao et crème fraîche.",
            "title": "Cocktail Angel's Tip",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à liqueur</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Angel&#x27;s Tit est une recette qui se réalise "
            "avec du marasquin qui est une liqueur de cerise ou de "
            "marasque qui est une variété de griotte.</p><p>Angel&#x27;s "
            "Tit signifie téton d&#x27;ange , c&#x27;est un cocktail à ne "
            "pas confondre avec le Angel&#x27;s Tip , qui lui est fait "
            "avec de la liqueur de cacao à la place du marasquin.</p>",
            "ingredients": [
                "2/3 de Marasquin",
                "1/3 de crème fraîche ou liquide",
                "1 cerise",
            ],
            "summary": "Le cocktail Angel&#x27;s Tit : une recette onctueuse aux saveurs "
            "de marasques.",
            "title": "Cocktail Angel's Tit",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: sling ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Apple Colada est une variante de "
            "la célèbre Pina Colada dans laquelle on ajoute des saveurs "
            "de pomme aux saveurs déjà présentes de coco. Il est à noter "
            "que le rhum d&#x27;origine est supprimé car associé aux "
            "saveurs déjà très présentes de noix de coco il masque trop "
            "les saveurs de pommes.</p>",
            "ingredients": [
                "6 cl de schnapps à la pomme",
                "3 cl de crème de coco",
                "3 cl de lait entier",
            ],
            "summary": "Le cocktail Apple Colada : une recette douce et fruitée qui "
            "allie la pomme avec la noix de coco.",
            "title": "Cocktail Apple Colada",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Apple Jack est apparu pour la première "
            "fois en 1922 dans l&#x27;ouvrage de Robert Vermeire "
            "&quot;Cocktails : How to mix them&quot;, ce cocktail "
            "s&#x27;appelle ainsi car on appelle le Calvados du Apple "
            "Jack Brandy à l&#x27;étranger.</p><p>C&#x27;est la vraie "
            "recette originale telle qu&#x27;elle a été publiée en 1922 "
            "que nous vous proposons ici avec ni plus ni moins que du "
            "Calvados, du sirop de gomme et de l&#x27;Angostura "
            "Bitter.</p>",
            "ingredients": [
                "6 cl de Calvados",
                "2 cl de sirop de gomme",
                "1 ou 2 traits d'Angostura bitters",
            ],
            "summary": "Le cocktail Apple Jack : la vraie recette originale de Robert "
            "Vermeire datant de 1922.",
            "title": "Cocktail Apple Jack",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Apple Sunrise est une variante de la célèbre "
            "Tequila Sunrise où la crème de cassis et le Calvados "
            "viennent remplacer la grenadine et la tequila "
            "d&#x27;origine.</p><p>Créé dans les années 80 c&#x27;est un "
            "cocktail doux et fruité qu&#x27;apprécieront un bon nombre "
            "d&#x27;entre vous et qui est de surcroît réalisé avec des "
            "ingrédients d&#x27;origine française même à l&#x27;étranger "
            "(Calvados biensûr mais crème de cassis aussi).</p>",
            "ingredients": [
                "2 cl de crème de cassis",
                "5 cl de Calvados",
                "8 cl de jus d'orange",
            ],
            "summary": "Le cocktail Apple Sunrise : une recette douce et fruitée créée "
            "dans les années 80.",
            "title": "Cocktail Apple Sunrise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Baileys Irish Coffee , aussi "
            "appelé &quot;Café irlandais au Baileys&quot;, est une "
            "variante du célèbre Irish Coffee . Le Baileys remplace dans "
            "cette recette le whisky irlandais d&#x27;origine.</p>",
            "ingredients": [
                "4 cl de Baileys",
                "12 cl de café chaud",
                "2 cuillère à café de sucre en poudre",
                "5 cl de crème fouettée / chantilly",
            ],
            "summary": "Le Baileys Irish Coffee : le fameux café irlandais dans une "
            "version plus douce, idéal en digestif.",
            "title": "Cocktail Baileys Irish Coffee",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Cette recette de Banana Banshee est celle de "
            "base, comme certains établissements le font vous pouvez "
            "enrichir cette recette en ajoutant dans le blender par "
            "exemple quelques morceaux d&#x27;une banane, du malibu "
            "banane, un brun de rhum ou autre.</p><p>Les banshees sont "
            "des singes hurleurs d&#x27;Australie, ce serait en leur "
            "honneur que ce cocktail aurait été nommé.</p>",
            "ingredients": [
                "1/2 part de liqueur de banane",
                "1/2 part de crème de cacao blanc (Marie Brizard...)",
                "2 parts de crème épaisse",
            ],
            "summary": "Le cocktail Banshee : une recette très crèmeuse aux saveurs de "
            "banane et cacao.",
            "title": "Cocktail Banana Banshee",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La Batida de coco est la plus connue des "
            "recettes de &quot;batidas&quot;, célèbres cocktails "
            "brésiliens dont le style ont tendance à se rapprocher du "
            "smoothie ou milkshake.</p>",
            "ingredients": [
                "5 cl de Cachaça",
                "5 cl de lait de coco",
                "2 cl de lait concentré sucré",
            ],
            "summary": "Le Batida de coco : le plus célèbre cocktail de la famille des "
            "&quot;batidas&quot; brésiliennes.",
            "title": "Cocktail Batida de Coco",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail ou old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Bentley est un cocktail sec dont la "
            "recette n&#x27;a strictement jamais évoluée, il a toujours "
            "été composé d&#x27;Applejack (que l&#x27;on substitue à "
            "défaut d&#x27;en avoir en France par du Calvados) et surtout "
            "de Dubonnet rouge.</p>",
            "ingredients": [
                "5 cl de Applejack (à substituer par du Calvados en France)",
                "5 cl de Dubonnet rouge",
            ],
            "summary": "Le cocktail Bentley : une recette restée inchangée à base "
            "d&#x27;Applejack et de Dubonnet.",
            "title": "Cocktail Bentley",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à bière</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Black &amp; Tan est apparu pour "
            "la première fois en 1917 dans &quot;The Ideal "
            "Bartender&quot; de Tom Bullock. La recette a bien évoluée "
            "depuis sa première apparition, à l&#x27;origine le Black "
            "&amp; Tan était un punch à base de sucre en poudre, citrons "
            "pressés, bière stout et champagne.</p>",
            "ingredients": [
                "50% de bière blonde",
                "50% de bière stout (Guinness...)",
            ],
            "summary": "Le Black &amp; Tan : un cocktail à étages qui était un punch à "
            "l&#x27;origine.",
            "title": "Cocktail Black & Tan",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Cette recette du cocktail Brain Duster est "
            "apparue en 1895 dans &quot;Modern American Drinks&quot; de "
            "George Kappeler. L&#x27;eau gazeuse et le sirop de gomme "
            "contenus dans cette recette originale sont aujourd&#x27;hui "
            "couramment remplacés par 2 traits d&#x27;Angostura bitters, "
            "dans ce cas le cocktail devient un short drink de 7cl et est "
            "servi dans un verre à cocktail.</p>",
            "ingredients": [
                "3 cl d'absinthe",
                "1,5 cl de whisky",
                "1,5 de vermouth rouge (Martini...)",
                "2 cl de sirop de gomme",
                "4 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Brain Duster : une recette à base d&#x27;absinthe "
            "parue en 1895.",
            "title": "Cocktail Brain Duster",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le Café "
            "Calypso est un cocktail qui a la particularité de contenir "
            "du Tia Maria, une liqueur de café jamaïcaine avec des "
            "saveurs vanillées. Titrant 20°, le Tia Maria est aussi "
            "appelé &quot;Dark Spirit&quot;.</p>",
            "ingredients": [
                "2/10 de liqueur de café Tia Maria",
                "8/10 de café chaud",
                "Crème fouettée / chantilly",
            ],
            "summary": "Le Café Calypso : une recette qui honore la liqueur de café Tia "
            "Maria.",
            "title": "Cocktail Café Calypso",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre toddy ou mug</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>La "
            "recette du Café italien peut aussi se réaliser avec de la "
            "liqueur galliano ou un autre alcool de base d&#x27;origine "
            "italienne que l&#x27;amaretto.</p>",
            "ingredients": [
                "2,5 cl de Amaretto",
                "1,5 cl de sirop de sucre",
                "8 cl de café chaud",
                "Crème fouettée / chantilly",
            ],
            "summary": "Le Café italien : une recette de café chaud enrichi "
            "d&#x27;Amaretto et de chantilly.",
            "title": "Cocktail Café italien",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>L&#x27;origine du cocktail Caipirinha doit "
            "remonter aussi loin que la création du cachaça lui-même. "
            "&quot;Caipirinha&quot; vient du mot &quot;caipira&quot; qui "
            "désigne une personne de la campagne.</p><p>Le cachaça est "
            "une eau-de-vie brésilienne réalisée directement à partir du "
            "vesou, le jus de canne à sucre. C&#x27;est un cousin du rhum "
            "qui lui est obtenu à partir de la mélasse : sirop obtenu "
            "après raffinage du sucre de canne à sucre.</p><p>Alcool le "
            "plus populaire du Brésil, le cachaça remonterait au début "
            "des années 1800. Les travailleurs dans les champs de cannes "
            "à sucre consommaient le &quot;garapa&quot;, du jus de canne "
            "à sucre qu&#x27;ils portaient juste à ébullition pour "
            "chasser bactéries ou autres parasites.</p><p>Devenus les "
            "cocktails emblématiques du Brésil, les caipirinhas ont "
            "l&#x27;avantage d&#x27;avoir une recette unique qui met tout "
            "le monde d&#x27;accord.</p><p>En remplaçant la Cachaça par "
            "de la vodka, on obtient le cocktail Caïpiroska.</p>",
            "ingredients": [
                "5 cl de cachaça",
                "1/2 citron vert",
                "2 cuillères à café de sucre ou cassonade",
            ],
            "summary": "Le cocktail Caipirinha : une recette unique qui vient tout droit "
            "du Brésil.",
            "title": "Cocktail Caïpirinha",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Dizzy Blonde (blonde vertigineuse) est à base "
            "d&#x27;advocaat, une liqueur onctueuse originaire des "
            "Pays-Bas et fabriquée à partir de jaune d&#x27;œuf, de sucre "
            "et d&#x27;alcool.</p>",
            "ingredients": [
                "3 cl de liqueur Advocaat",
                "2 cl de Pernod",
                "3 cl de jus d'orange",
                "4 cl de limonade",
            ],
            "summary": "Le cocktail Dizzy Blonde : une recette audacieuse à base "
            "d&#x27;Advocaat et de Pernod.",
            "title": "Cocktail Dizzy Blonde",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (14cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>Le Fernandito est un tout nouveau cocktail "
            "classique IBA, c&#x27;est une recette très simple à réaliser "
            "qui se compose uniquement de Fernet Branca et "
            "Cola.</p><p>L&#x27;histoire du Fernet Branca commence dans "
            "les années 1840 lorsque le Dr Fernet mit au point un mélange "
            "de presque 30 plantes, herbes et épices pour venir à bout "
            "des soucis digestifs de ses patients. Branca qui était alors "
            "apothicaire décida de s&#x27;associer à Fernet pour faire de "
            "son médicament une liqueur destinée à combattre le Choléra. "
            "Le Fernet-Branca est né, les vertus de cette boisson se sont "
            "par la suite révélés plus nombreuses que prévu, guérissant "
            "les problèmes nerveux, de fièvre ou de digestion.</p><p>Peu "
            "connus en France, les cocktails Fernanditos sont très "
            "consommés dans les pays d&#x27;Amérique du Sud et notamment "
            "en Argentine.</p>",
            "ingredients": ["7 cl de Fernet-Branca", "7 cl de Cola"],
            "summary": "Le cocktail Fernandito : la recette d&#x27;un &quot;Fernet "
            "Coca&quot; très consommé en Amérique du Sud.",
            "title": "Cocktail Fernandito (Fernet-Coca)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Frangelico Luau est comme son nom l&#x27;indique "
            "une recette à base de Frangelico, une liqueur italienne de "
            "noisette fabriquée à Canale dans le Piémont.</p>",
            "ingredients": [
                "5 cl de liqueur de noisettes Frangelico",
                "9 cl de jus d'ananas",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Frangelico Luau : une recette douce aux saveurs de "
            "noisettes.",
            "title": "Cocktail Frangelico Luau",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler ou old fashioned</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Fuzzy Navel est toujours réalisé "
            "avec du Peach Schnapps (liqueur de pêche) et du jus "
            "d&#x27;orange, mais la proportion des 2 ingrédients peut "
            "varier. La variante la plus proche de ce cocktail est le "
            "Hairy Navel dans lequel on trouve de la vodka en "
            "plus.</p><p>Le Fuzzy Navel fait partie des cocktails "
            "modernes qui, dès les années 1980 avec la commercialisation "
            "du Peachtree schnapps, a fait partie des plus populaires de "
            "ceux-là. Cocktail alcoolisé doux et fruité à la fois, il a "
            "beaucoup plu à une clientèle de jeunes adultes à ses débuts, "
            "et c&#x27;est grâce à ça que le Fuzzy Navel a vite gagné en "
            "célébrité.</p><p>Si l&#x27;origine du cocktail n&#x27;est "
            "pas connu avec certitude, on sait que Navel se réfère à une "
            "variété d&#x27;orange, et que Fuzzy se réfère au Schnapps "
            "aux pêches présent dans ce cocktail (peach fuzz signifie "
            "duvet de pêche).</p><p>Notez que les cocktails Fuzzy Navels "
            "sont parfois réalisés dans des verres old fashioned, et "
            "qu&#x27;il est conseillé d&#x27;utiliser du jus "
            "d&#x27;orange fraîchement pressé.</p>",
            "ingredients": [
                "5 cl de liqueur de pêche (Peach Schnapps)",
                "10 cl de jus d'orange",
            ],
            "summary": "Le cocktail Fuzzy Navel : une recette aux saveurs de pêche et "
            "d&#x27;orange.",
            "title": "Cocktail Fuzzy Navel",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Garibaldi est aussi appelé "
            "campari orange. L&#x27;origine de ce cocktail très simple à "
            "réaliser n&#x27;est pas certaine, il est en tout cas fort "
            "problable que son nom rende hommage à Giuseppe Garibaldi "
            "(1807-1882), un général italien né à Nice.</p>",
            "ingredients": ["5 cl de Campari", "10 cl de jus d'orange"],
            "summary": "Le cocktail Garibaldi : Un campari orange qui se déguste à tout "
            "moment de la journée.",
            "title": "Cocktail Garibaldi (campari orange)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail General Harrison&#x27;s Egg Nogg "
            "est une variante du cocktail classique Egg Nogg, il apparaît "
            "pour la première fois en 1862 dans &quot;How to mix "
            "drinks&quot; de Jerry Thomas qui nous indique que ce "
            "cocktail est le préféré du Général Harrison et que cette "
            "boisson est très populaire du côté du Mississipi.</p><p>Le "
            "Général William Henry Harrison (1773-1841) est devenu en "
            "1840 le neuvième président des USA après avoir passé une "
            "carrière militaire et politique dans l&#x27;Ohio.</p>",
            "ingredients": [
                "1 oeuf",
                "1,5 cuillère à café de sucre en poudre",
                "5 cl de cidre",
            ],
            "summary": "Le General Harrison&#x27;s Egg Nogg : le cocktail préféré du "
            "9ème président des États-Unis.",
            "title": "Cocktail General Harrison's Egg Nogg",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Grasshopper se réalise à doses "
            "égales de crème fraîche, de crème de cacao blanc et de crème "
            "de menthe, ce dernier ingrédient lui conférant sa couleur "
            "verte.</p><p>À défaut de crème vous pouvez bien entendu "
            "utiliser de la liqueur (seul le taux de sucre contenu "
            "diffère).</p>",
            "ingredients": [
                "3 cl de crème de menthe",
                "3 cl de crème de cacao blanc",
                "3 cl de crème fraîche liquide",
                "Poudre de cacao",
            ],
            "summary": "Le cocktail Grasshopper : un trio de crème à siroter idéalement "
            "en pousse-café.",
            "title": "Cocktail Grasshopper",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>L&#x27;origine du cocktail Jack Rose est "
            "floue, il existe une multitude de versions.</p><p>La "
            "première version raconte que le Jack Rose aurait été inventé "
            "vers 1910 par Jacob Rosensweig (1876-1947), un gangster "
            "américain surnommé &quot;Bald Jack Rose&quot;.</p><p>La "
            "seconde version attribue ce cocktail à Frank May, un barman "
            "américain dont le surnom était &quot;Jack "
            "Rose&quot;.</p><p>Une autre version qui semble "
            "aujourd&#x27;hui être écartée raconte que ce cocktail aurait "
            "été créé vers 1920 ou 1930 à l&#x27;auberge Colts Neck par "
            "Lisa Laird, ancêtre de la famille écossaise Laird. Lisa "
            "Laird était la compagne d&#x27;un certain Jack Rose, "
            "c&#x27;est pour lui qu&#x27;elle aurait créé ce cocktail. Le "
            "barman de l&#x27;auberge, Nelson Fastige, aurait créé le "
            "cocktail Apple Jack, une version plus corsée du &quot;Jack "
            "Rose&quot;.</p><p>Encore une autre version raconte que ce "
            "cocktail a été inventé au début des années 1800 par un M. "
            "Rose dont le cocktail préféré était le Apple "
            "Jack.</p><p>Enfin, Albert Stevens Crockett publie en 1934 "
            "&quot;The Old Waldorf Astoria Bar Book&quot;, pour lui le "
            "nom du cocktail évoquerait la couleur d’une variété de rose "
            ": la rose jacqueminot.</p>",
            "ingredients": [
                "4 cl de Calvados",
                "2 cl de jus de citron pressé",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le Jack Rose : un cocktail doux et fruité aux multiples "
            "origines.",
            "title": "Cocktail Jack Rose",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Litchi Sunrise est la variante au Soho de la "
            "célèbre Tequila Sunrise.</p><p>Comme tous les cocktails de "
            "la famille des &quot;sunrises&quot;, le Litchi Sunrise est "
            "allongé au jus d&#x27;orange et au sirop de "
            "grenadine.</p><p>Les litchis dont le Soho est une liqueur, "
            "sont des fruits originaires de Chine mais aujourd&#x27;hui "
            "cultivé dans une vingtaine de pays, notamment en Chine, "
            "Inde, Vietnam, où encore La Réunion. Il y a aussi une grosse "
            "production à Madagascar, c&#x27;est ceux-là qui sont "
            "généralement exportés en France.</p>",
            "ingredients": [
                "6 cl de Soho",
                "8 cl de jus d'orange",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le Litchi Sunrise : Quand le Soho vient s&#x27;inviter dans un "
            "cocktail &quot;sunrise&quot; !",
            "title": "Cocktail Litchi Sunrise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à bière</li>\n"
            "<li>Type&nbsp;: long drink (25cl)</li>\n"
            "<li>Temps&nbsp;: 1 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Monaco , cocktail parfois appelé tango "
            "panaché puiqu&#x27;il est à cheval entre les deux, est une "
            "boisson incontournable des bars français, suisses, belges, "
            "luxembourgeois et bien sûr dans la principauté monégasque. "
            "La vraie recette du monaco se réalise avec du sirop de "
            "grenadine, ainsi que de la limonade et de la bière à parts "
            "égales.</p><p>La grenadine et la limonade rendent les "
            "Monacos très doux et rafraîchissants, inégalable dans la "
            "catégorie des cocktails à base de bière.</p>",
            "ingredients": [
                "3 cl de sirop de grenadine",
                "11 cl de limonade",
                "11 cl de bière blonde",
            ],
            "summary": "Le cocktail Monaco : la recette d&#x27;une des boissons les plus "
            "connues de France.",
            "title": "Cocktail Monaco",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Nutty Irishman est parfois "
            "réalisé avec un peu de lait ou crème légère en plus. Aucune "
            "information sur l&#x27;origine de ce cocktail mais une chose "
            "est certaine, il se réalise avec du &quot;Frangelico&quot;, "
            "une liqueur de noisette italienne.</p><p>Fabriquée dans le "
            "Piémont (nord-ouest de l&#x27;Italie), le Frangelico est "
            "obtenu par infusion du distillat de noisette avec notamment "
            "du cacao, de la vanille et des herbes. Très bien conçue, la "
            "forme de la bouteille évoque la silhouette d&#x27;un "
            "moine.</p>",
            "ingredients": [
                "4 cl de Baileys",
                "4 cl de liqueur de noisette (Frangelico)",
            ],
            "summary": "Le cocktail Nutty Irishman : un apéritif qui met à "
            "l&#x27;honneur une savoureuse liqueur de noisette italienne.",
            "title": "Cocktail Nutty Irishman",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Orgasme (&quot;orgasm&quot; à "
            "l&#x27;étranger) n&#x27;a pas d&#x27;origine connue. "
            "Quelques recettes légèrement différentes existent sous ce "
            "même nom mais elles ont généralement toutes en commun la "
            "liqueur d&#x27;amandes et le Baileys. Mais c&#x27;est cette "
            "recette qui est la plus commune.</p><p>Une version semblable "
            "existe en shooter, voir la recette du Shooter Orgasme .</p>",
            "ingredients": [
                "3 cl de Baileys",
                "3 cl de Kahlua",
                "3 cl de Amaretto",
            ],
            "summary": "Le cocktail Orgasme : un short drink onctueux et très savoureux "
            "!",
            "title": "Cocktail Orgasme",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte ou verre à cidre</li>\n"
            "<li>Type&nbsp;: long drink (≈12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Peu d&#x27;information sur l&#x27;origine du "
            "cocktail Peach and Love même s&#x27;il est probable "
            "qu&#x27;il soit d&#x27;origine bretonne.</p>",
            "ingredients": [
                "2 cl de jus de citron pressé et filtré",
                "6 cl de nectar de pêche",
                "5 cl de cidre",
            ],
            "summary": "Le cocktail Peach &amp; Love : une recette fruitée à base de "
            "cidre.",
            "title": "Cocktail Peach & Love",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler ou apéritif</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Pineau Colada est une variante de la célèbre Piña "
            "Colada.</p>",
            "ingredients": [
                "4 cl de Pineau des Charentes",
                "3 cl de lait de coco",
                "6 cl de jus d'ananas",
                "1 cl de jus de citron vert pressé",
                "1 trait de sirop de fraise",
            ],
            "summary": "Le cocktail Pineau Colada : la version charentaise de la Pina "
            "Colada.",
            "title": "Cocktail Pineau Colada",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Port wine Sangaree fait partie "
            "des &quot;sangarees&quot;. Bien que les sangarees se "
            "traduisent parfois par sangrias, ces deux types de cocktails "
            "sont différents. Les sangarees dateraint des années 1770 "
            "alors que les sangrias datent des années 1960, et leurs "
            "compositions diffèrent totalement.</p><p>Le port wine "
            "sangaree daterait donc probablement du XVIIIème siècle, il a "
            "été publié pour la première en 1862 dans "
            "&quot;Bartender&#x27;s guide : How to mix drinks&quot; de "
            "Jerry Thomas.</p>",
            "ingredients": [
                "5 cl de vin de liqueur rouge (Porto)",
                "1 cuillère à café de sucre",
                "Noix de muscade râpée",
            ],
            "summary": "Le cocktail Port wine sangaree : une recette à base de Porto de "
            "la famille des sangarees.",
            "title": "Cocktail Port wine sangaree",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Porto Flip fait partie de la "
            "catégorie des flips, il aurait été créé en 1695 qui est "
            "aussi l&#x27;année d&#x27;apparition du mot &quot;flip&quot; "
            "le dictionnaire Oxford. À l&#x27;époque le flip était un "
            "mélange à base de sucre, de bière, rhum ou autre "
            "spiritueux.</p>",
            "ingredients": [
                "4 cl de Porto",
                "2 cl de Cognac",
                "1 jaune d'œuf",
                "1 cuillère à café de sucre en poudre",
                "Noix de muscade râpée",
            ],
            "summary": "Le Porto Flip : un cocktail très raffiné et servi idéalement en "
            "digestif.",
            "title": "Cocktail Porto Flip",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Pousse l&#x27;Amour est publié en "
            "1862 dans &quot;Bartenders guide : How to mix drinks&quot; "
            "de Jerry Thomas, il y indique qu&#x27;il s&#x27;agit "
            "d&#x27;un cocktail français.</p>",
            "ingredients": [
                "4 cl de marasquin",
                "1 jaune d'oeuf",
                "3 cl de liqueur de vanille",
                "2 cl de Cognac",
            ],
            "summary": "Le cocktail Pousse l&#x27;amour : un délicieux long drink à "
            "étages d&#x27;origine française.",
            "title": "Cocktail Pousse l'Amour",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Rose a été pendant un temps un cocktail classique "
            "IBA mais ne l&#x27;ai plus.</p>",
            "ingredients": [
                "4 cl de vermouth rouge",
                "2 cl de kirsch",
                "1 cl de liqueur de cerises",
            ],
            "summary": "Le Rose : un cocktail qui marie la cerise et le vermouth.",
            "title": "Cocktail Rose",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sherry Egg Nogg est une variante "
            "du grand cocktail classique Egg Nogg , il apparaît pour la "
            "première fois en 1862 dans &quot;How to mix drinks&quot; de "
            "Jerry Thomas. Le Xérès (plus connu en Angleterre sous le nom "
            "de Sherry et à ne pas confondre avec cherry qui signifie "
            "cerise) est un vin blanc originaire de la région de "
            "l&#x27;Andalousie.</p>",
            "ingredients": [
                "1 oeuf",
                "1,5 cuillère à café de sucre en poudre",
                "6 cl de sherry (Xérès)",
                "5 cl de lait",
                "1 pincée de noix de muscade râpée / en poudre",
            ],
            "summary": "Le Sherry Egg Nogg : un cocktail qui met à l&#x27;honneur le "
            "célèbre vin andalousien de Xérès.",
            "title": "Cocktail Sherry Egg Nogg",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sherry Sangaree fait partie de la "
            "famille des &quot;sangarees&quot;. Bien que le nom de cette "
            "famille se traduise parfois par sangria, ils n&#x27;ont rien "
            "à voir l&#x27;un avec l&#x27;autre. Les sangarees dateraint "
            "des années 1770 alors que les sangrias datent des années "
            "1960, leurs ingrédients sont aussi complètement "
            "différents.</p><p>Le cocktail sherry sangaree pourrait "
            "remonter au XVIIIème siècle, la recette a été publiée pour "
            "la première fois en 1862 dans &quot;Bartender&#x27;s guide : "
            "How to mix drinks&quot; de Jerry Thomas.</p><p>Le Xérès plus "
            "connu en Angleterre sous le nom de Sherry (et à ne pas "
            "confondre avec cherry signifiant cerise) est un vin blanc "
            "andalousien.</p>",
            "ingredients": [
                "5 cl de sherry (Xérès)",
                "1 cuillère à café de sucre",
                "Noix de muscade râpée",
            ],
            "summary": "Le cocktail Sherry Sangaree : le Xérès mis à l&#x27;honneur dans "
            "cette recette.",
            "title": "Cocktail Sherry Sangaree",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: à bière</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Snakebite se réalise généralement avec de la bière "
            "&quot;stout&quot;, qui est une bière de fermentation haute, "
            "d&#x27;où sa saveur prononcé et son degré "
            "d&#x27;alcool.</p><p>Caractérisée entre autres par sa "
            "couleur sombre, la stout est brassée avec de l&#x27;orge "
            "torréfié. La plus célèbre des stouts est la "
            "Guinness.</p><p>Les Snakebites ont plutôt tendance à être "
            "réalisés avec de la stout en Amérique, et de la Lager en "
            "Grande-Bretagne.</p><p>&quot;Snakebite&quot; signifie "
            "&quot;morsure de serpent&quot;.</p>",
            "ingredients": ["50% de cidre", "50% de bière stout (Guinness...)"],
            "summary": "Le Snakebite : un cocktail à étages à base de cidre et de bière.",
            "title": "Cocktail Snakebite",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à bière</li>\n"
            "<li>Type&nbsp;: long drink (25cl)</li>\n"
            "<li>Temps&nbsp;: 1 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Tango est la recette très simple d&#x27;une "
            "&quot;bière grenadine&quot;, boisson servie très couramment "
            "dans les bars/brasseries.</p>",
            "ingredients": [
                "3 cl de sirop de grenadine",
                "22 cl de bière blonde",
            ],
            "summary": "Le cocktail Tango : la recette ultra simple de la &quot;bière "
            "grenadine&quot;.",
            "title": "Cocktail Tango",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy ou pousse-café</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Si vous "
            "utilisez une verrerie fragile et sensible à la contenance de "
            "boisson chaude pour faire par exemple cette recette du Thé à "
            "l&#x27;Amaretto , vous pouvez insérer en amont une longue "
            "cuillère (comme une cuillère à mélange) dans le verre. "
            "C&#x27;est une technique très simple pour éviter au verre de "
            "se fissurer sous la chaleur du liquide.</p>",
            "ingredients": [
                "7/10 de thé chaud",
                "3/10 de Amaretto",
                "Crème fouettée/chantilly",
            ],
            "summary": "Le Thé à l&#x27;Amaretto (Amaretto Tea) : un cocktail chaud dont "
            "vous ne pourrez plus vous passer en hiver.",
            "title": "Cocktail Thé à l'Amaretto",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Xérès cocktail met en avant le Xérès, fameux vin "
            "espagnol élaboré en Andalousie et aussi appelé Jerez (en "
            "Espagne) ou sherry (dénomination anglaise).</p>",
            "ingredients": [
                "7 cl de Xérès",
                "Quelques gouttes d'Orange Bitters",
            ],
            "summary": "Le Xérès cocktail : la recette qui honore le célèbre vin "
            "espagnol du même nom.",
            "title": "Cocktail Xérès cocktail",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail 20th century est apparu en 1937 "
            "dans le livre &quot;Cafe Royal Cocktail Book&quot; de "
            "William J. Tarling qui était barman au Café Royal (Londres) "
            "et président du &quot;United Kingdom Bartenders&#x27; "
            "Guild&quot;.</p><p>Ce cocktail aurait été baptisé ainsi en "
            "l&#x27;honneur du train &quot;20th (twentieth) century "
            "limited&quot; qui a relié New York à Chicago entre 1902 et "
            "1967, on l&#x27;appelait jadis &quot;le train le plus "
            "célèbre du monde&quot;.</p><p>* À l&#x27;origine, le "
            "cocktail 20th century appelle à utiliser du Kina Lillet, "
            "maintenant disparu. Beaucoup le remplace aujourd&#x27;hui "
            "par du Lillet Blanc, d&#x27;autres utilisent du &quot;Cocchi "
            "Americano&quot; plus proche du Kina Lillet original.</p>",
            "ingredients": [
                "4 cl de gin",
                "2 cl de (Kina) Lillet *",
                "2 cl de crème de cacao blanc",
                "2 cl de jus de citron pressé et filtré",
            ],
            "summary": "Le 20th century : un cocktail en l&#x27;honneur du train qui fût "
            "le plus célèbre du monde pendant le vingtième siècle.",
            "title": "Cocktail 20th century",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>La "
            "recette du cocktail 69 Special est très proche du Rickey, à "
            "la différence près que le 7up remplace l&#x27;eau "
            "pétillante.</p><p>Il est à noter qu&#x27;il n&#x27;est pas "
            "rare que certains préfèrent opter pour la limonade à la "
            "place du 7up dans les 69 Spéciaux.</p><p>Avec son nom plutôt "
            "coquin, le 69 Special est un cocktail qui s&#x27;inviterait "
            "idéalement à la Saint-Valentin ou lors d&#x27;une soirée "
            "entre amoureux.</p>",
            "ingredients": [
                "4,5 cl de gin",
                "1,5 cl de jus de citron",
                "9 cl de 7up",
            ],
            "summary": "Le cocktail 69 Special : Seriez-vous tenté par un petit 69 ??",
            "title": "Cocktail 69 Special",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Abbey est publié pour la première "
            "fois en 1930 dans &quot;The Savoy cocktail book&quot; de "
            "Harry Craddock. La recette originale est celle-ci avec plus "
            "exactement les proportions suivantes : 50% de gin, 25% de "
            "Kina Lillet et 25% de jus d&#x27;orange (sans oublier le "
            "trait d&#x27;Angostura bitters).</p><p>* Le Kina Lillet "
            "n&#x27;existant plus, vous pouvez le remplacer par du Lillet "
            "&quot;normal&quot;. Le Lillet ne contient pas de quinine et "
            "adoucit donc radicalement le cocktail, l&#x27;esprit "
            "d&#x27;origine n&#x27;est plus véritablement là mais "
            "c&#x27;est la meilleure solution au jour "
            "d&#x27;aujourd&#x27;hui.</p><p>C&#x27;est aussi pour cette "
            "raison que vous pourrez trouver des recettes d&#x27;Abbey "
            "arrangées dans lesquelles le Kina Lillet est remplacé par du "
            "vermouth. Dans tous les cas, déguster des abbeys sonnera "
            "toujours un peu faux en l&#x27;absence de Kina Lillet.</p>",
            "ingredients": [
                "3,5 cl de gin",
                "1,5 cl de (Kina) Lillet *",
                "1,5 cl de jus d'orange",
                "1 trait d'Angostura bitters",
            ],
            "summary": "Le cocktail Abbey : un mélange qui sonne un peu faux depuis la "
            "disparition du Kina Lillet.",
            "title": "Cocktail Abbey",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Adios Motherfucker (abrégé AMF) "
            "est une variante du célèbre Long island Iced Tea à la "
            "différence que le triple sec utilisé ici est du Caraçao bleu "
            "et non pas du Cointreau ou Grand Marnier, et que la limonade "
            "remplace le coca d&#x27;origine.</p>",
            "ingredients": [
                "2 cl de tequila",
                "2 cl de rhum brun",
                "2 cl de gin",
                "2 cl de vodka",
                "1 cl de Curaçao Bleu",
                "1 cl de jus de citron pressé et filtré",
                "5 cl de limonade",
            ],
            "summary": "Le cocktail Adios Motherfucker : une recette dérivée du Long "
            "Island Iced Tea.",
            "title": "Cocktail Adios MotherFucker",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Albemarle Fizz est apparu dans le "
            "célèbre &quot;Savoy Cocktail Book&quot; de Harry Craddock "
            "paru pour la première fois en 1930, mais ce cocktail "
            "n&#x27;est apparu que dans une édition ultérieure du livre, "
            "vers 1976.</p><p>La recette du Albemarle Fizz a légèrement "
            "évoluée avec le temps, voici la recette d&#x27;origine "
            ":</p><p>&quot; Albemarle &quot; est pour information "
            "l&#x27;ancien nom de la Caroline du Nord (USA), et aussi le "
            "nom d&#x27;une ville de ce même État.</p>",
            "ingredients": [
                "4 cl de gin",
                "1,5 cl de jus de citron pressé et filtré",
                "1,5 cl de sirop de framboise",
                "5 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Albemarle Fizz : une recette rafraîchissante de la "
            "famille des fizzes.",
            "title": "Cocktail Albemarle Fizz",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (6cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Alexander est à ne pas confondre "
            "avec le &quot;Brandy Alexander&quot; qui est fait à base de "
            "cognac.</p><p>L&#x27;alexander a été publié pour la première "
            "fois en 1916 dans le livre &quot;Recipes for Mixed "
            "Drinks&quot; de Hugo Ensslin&#x27;s. Il est réalisé à parts "
            "égales de gin, de crème de cacao et de crème "
            "fraîche.</p><p>Plusieurs versions existent sur "
            "l&#x27;origine de l&#x27;Alexander. Son origine réelle reste "
            "donc très incertaine mais il semblerait que l&#x27;Alexander "
            "aurait été créé à New York avant la prohibition, dans les "
            "années 1910, par le barman Troy Alexander. Ce cocktail de "
            "couleur blanche aurait été créé à l&#x27;occasion d&#x27;un "
            "dîner célébrant Phoebe Snow, personnage de publicité pour "
            "les chemins de fer qui était toujours vêtu d&#x27;une robe "
            "blanche.</p>",
            "ingredients": [
                "2 cl de gin",
                "2 cl de crème de cacao blanc",
                "2 cl de crème légère",
                "Noix de muscade râpée",
            ],
            "summary": "L&#x27;Alexander : un cocktail onctueux et savoureux "
            "aujourd&#x27;hui devenu un grand classique.",
            "title": "Cocktail Alexander",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Allies apparaît pour "
            "la première fois en 1916 dans &quot;Recipes for mixed "
            "drinks&quot; de Hugo Ensslin. La recette n&#x27;a jamais "
            "changée, elle a toujours été composée de gin, de vermouth "
            "dry et surtout d&#x27;un trait de Kummel.</p><p>Le Kummel, "
            "qui a toujours fait tout le charme de ce cocktail, est une "
            "liqueur à base de carvi principalement (aussi appelé cumin "
            "des près), d&#x27;épices et herbes.</p>",
            "ingredients": [
                "4 cl de gin",
                "4 cl de vermouth blanc",
                '2 cl de liqueur de carvi/cumin "Kummel"',
            ],
            "summary": "Le cocktail Allies : une recette célèbre pour sa présence de "
            "Kummel.",
            "title": "Cocktail Allies",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Angel Face est d&#x27;origine "
            "française, il daterait de la seçonde guerre mondiale sans "
            "plus de précision. Vers les années 1950, on trouve des "
            "recettes du Angel Face avec des ingrédients différents, il "
            "s&#x27;agit ici de la recette classique avec 1/3 de gin, 1/3 "
            "d&#x27;Apricot Brandy et 1/3 de Calvados.</p>",
            "ingredients": [
                "3 cl de Gin",
                "3 cl d'Apricot Brandy",
                "3 cl de Calvados",
            ],
            "summary": "Le cocktail Angel Face : une recette signifiant &quot;visage "
            "d&#x27;ange&quot; mais plutôt corsée.",
            "title": "Cocktail Angel Face",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Attention qui daterait "
            "des années 1940 appelle à l&#x27;orgine à 4 parts égales des "
            "4 premiers ingrédients. Nous vous laissons ici la recette "
            "originale mais beaucoup pensent qu&#x27;elle est très "
            "déséquilibrée et qu&#x27;il faudrait plus de gin pour le "
            "rééquilibrer, à vous de tester et de vous faire votre propre "
            "opinion.</p>",
            "ingredients": [
                "2 cl de gin",
                "2 cl de vermouth blanc (Martini...)",
                "2 cl de liqueur de violette",
                "2 cl d'absinthe",
                "2 traits d'Orange Bitters",
            ],
            "summary": "Le cocktail Attention : une recette dont le nom vous met en "
            "garde...",
            "title": "Cocktail Attention",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Aviation a été publié pour la "
            "première fois en 1916 dans &quot;Recipes for mixed "
            "drinks&quot; de Hugo Ensslin, chef barman au Wallick Hôtel "
            "Times Square à New York. L&#x27;origine du cocktail "
            "n&#x27;est pas connue, la recette originale sont avec les "
            "ingrédients ci-dessus.</p><p>Il existe une version plus "
            "classique du cocktail Aviation dans lequel la crème de "
            "violette est supprimée : 4 cl de Gin + 1,5 cl de jus de "
            "citron pressé + 1,5 cl de marasquin. En 1930, Harry Craddock "
            "publie &quot;Savoy Cocktail Book&quot; dans lequel la crème "
            "de violette était déjà supprimée car contraignante à trouver "
            "et pas très courante.</p>",
            "ingredients": [
                "3 cl de Gin",
                "1,5 cl de jus de citron pressé",
                "1,5 cl de marasquin",
                "1 cl de crème ou liqueur de violette",
            ],
            "summary": "Aviation : sous sa couleur bleutée se dissimule un grand "
            "cocktail.",
            "title": "Cocktail Aviation",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: long drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Blue Devil (diable bleu en "
            "français) est apparu pour la première fois dans un ouvrage "
            "en 1935 dans le livre Old Mr. Boston DeLuxe Official "
            "Bartender&#x27;s Guide .</p><p>À l&#x27;origine, la recette "
            "du Blue Devil était composée de gin, jus de citron, "
            "maraschino et de Crème Yvette. La Crème Yvette ayant été "
            "décommercialisée, le curaçao bleu est venu la "
            "remplacer.</p><p>La couleur des Blue Devils tournent entre "
            "le bleu et le vert, le choix du curaçao bleu utilisé peut "
            "influencer la couleur de ce cocktail.</p>",
            "ingredients": [
                "4 cl de gin",
                "2 cl de Curaçao Bleu",
                "2 cl de jus de citron pressé et filtré",
                "1 cl de sirop de sucre",
            ],
            "summary": "Le Blue Devil : un cocktail bleu datant des années 1930.",
            "title": "Cocktail Blue Devil",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Blue Lady est une variante des "
            "célèbres White Lady et Pink Lady . Tout comme ses deux "
            "consœurs, les Blue Ladies ne sont pas plus réservés aux "
            "femmes qu&#x27;aux hommes comme leur nom pourrait nous le "
            "faire croire.</p>",
            "ingredients": [
                "2 cl de Curaçao Bleu",
                "4 cl de gin",
                "4 cl de jus de citron pressé et filtré",
            ],
            "summary": "Blue Lady : la petite sœur des cocktails Pink Lady et White "
            "Lady.",
            "title": "Cocktail Blue Lady",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Bramble aurait été créé en 1984 "
            "par Dick Bradsell au Fred&#x27;s Club de Londres, il est "
            "très populaire en Angleterre. Sa recette n&#x27;a jamais "
            "évoluée et il n&#x27;existe qu&#x27;une seule version, elle "
            "contient toujours du gin, jus de citron, sirop de sucre et "
            "liqueur de mûre.</p><p>C&#x27;est l&#x27;un des rares "
            "cocktails dans lesquels on trouve des saveurs de mûre.</p>",
            "ingredients": [
                "3,5 cl de gin",
                "1,5 cl de jus de citron pressé et filtré",
                "1 cl de sirop de sucre",
                "1,5 cl de liqueur ou crème de mûre",
            ],
            "summary": "Le cocktail Bramble : une recette unique qui n&#x27;a jamais "
            "changée depuis plusieurs décennie.",
            "title": "Cocktail Bramble",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Rappelons avant tout que le cocktail Bronx "
            "c&#x27;est une tradition et une légende à respecter : un "
            "Bronx se réalise avec du jus d&#x27;orange pressé !</p><p>Le "
            "Bronx a très propablement été créé par Johnnie Solon, un "
            "barman réputé qui arrive à l&#x27;hôtel Waldorf Astoria de "
            "New York en 1899. C&#x27;est dans les quelques années qui "
            "suivèrent son arrivée à l&#x27;hôtel que Johnnie Solon "
            "aurait créé le Bronx.</p><p>L&#x27;historien Albert S. "
            "Crockett publie en 1934 &quot;TheOld Waldorf-Astoria Bar "
            "Book&quot; dans lequel il raconte l&#x27;histoire de la "
            "création du Bronx. Un jour où Johnnie Solon faisait un "
            "cocktail nommé &quot;Duplex&quot; pour un client, son maître "
            "d&#x27;hôtel nommé &quot;Traverson&quot; est arrivé en lui "
            "proposant de créer un nouveau cocktail et en lui indiquant "
            "qu&#x27;un client avait estimé qu&#x27;il (Johnnie) en était "
            "incapable. Johnnie aurait alors réalisé un cocktail venu "
            "d&#x27;une idée subite : mélanger 2 tiers de gin pour 1 "
            "tiers de jus d&#x27;orange, puis finir avec 2 doses égales "
            "de vermouth blanc et rouge. Johnnie aurait alors versé sa "
            "nouvelle recette dans un verre à cocktail et tendu celui-ci "
            "à Traverson qui aurait alors bu le verre d&#x27;un "
            "trait.</p><p>Le Bronx est un quartier de New York, mais le "
            "nom du cocktail ne viendrait pas d&#x27;ici. Johnnie Solon "
            "aurait constaté des bêtes étranges et inconnues au zoo, ce "
            "qu&#x27;avait déjà remarqué certains de ses clients qui "
            "avaient bu auparavant un peu trop de cocktails. Quand "
            "Traverson demanda à Johnnie quel nom il voulait donné à son "
            "cocktail, c&#x27;est en se rappelant de cette histoire de "
            "bêtes étranges qu&#x27;il nomma son cocktail le "
            "&quot;Bronx&quot;.</p><p>Le cocktail fût aussitôt un succès, "
            "l&#x27;hôtel liquidait une à plusieurs caisses "
            "d&#x27;oranges à presser par jour.</p>",
            "ingredients": [
                "3 cl de gin",
                "2 cl de vermouth rouge",
                "2 cl de vermouth blanc",
                "3 cl de jus d'orange",
            ],
            "summary": "Le cocktail Bronx : une recette qui doit être réalisée avec du "
            "jus d&#x27;orange pressé.",
            "title": "Cocktail Bronx",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>Le cocktail Bulldog est apparu pour la "
            "première fois en 1922 dans le livre &quot;Cocktails : How to "
            "mix them&quot; de Robert Vermeire , très célèbre bartender "
            "du XXème siècle et l&#x27;une des plus grande personnalités "
            "du monde des cocktails.</p><p>Ceci est la vraie recette "
            "originale telle qu&#x27;elle a été publiée par Robert "
            "Vermeire en 1922, les Bulldogs sont ni plus ni moins "
            "composés de gin, jus de citron jaune, sirop de sucre de "
            "canne et ginger ale.</p>",
            "ingredients": [
                "7 cl de gin",
                "4 cl de jus de citron jaune pressé",
                "2 cl de sirop de sucre de canne",
                "7 cl de ginger ale (Canada Dry...)",
            ],
            "summary": "Le cocktail Bulldog : une recette qui date de plus d&#x27;un "
            "siècle.",
            "title": "Cocktail Bulldog",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Casino a été publié la première "
            "fois en 1916 dans &quot;Recipes for Mixed Drinks&quot; de "
            "Hugo R. Ensslin, puis en 1930 dans &quot;The Savoy Cocktail "
            "Book&quot; de Harry Craddock. Dans ces deux premières "
            "publications, le cocktail Casino se réalise avec un gin "
            "spécifique : le &quot;Old Tom Gin&quot;.</p>",
            "ingredients": [
                "4 cl de Old Tom Gin",
                "1 cl de Marasquin",
                "1 cl de jus de citron pressé et filtré",
                "2 traits d'Orange Bitters",
            ],
            "summary": "Le Casino : un cocktail très sec qui met à l&#x27;honneur le Old "
            "Tom Gin.",
            "title": "Cocktail Casino",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Clover Club aurait été créé vers "
            "1911, il porte le nom d&#x27;un club d&#x27;hommes de "
            "Philadelphie composé de businesssmen, avocats ou "
            "journalistes. Ils avaient l&#x27;habitude de se regrouper "
            "dans l&#x27;hôtel Bellevue-Stratford, c&#x27;est ici "
            "qu&#x27;un jeune barman Ambrose Burnside Lincoln Hoffman "
            "aurait inventé le cocktail vers 1880.</p><p>En 1934 un "
            "magazine cite ce cocktail dans les 12 pires cocktails de la "
            "decennie, et vers 1950 le cocktail n&#x27;était plus "
            "qu&#x27;un lointain souvenir.</p><p>Récemment s&#x27;est "
            "construit un restaurant à Brooklyn qui porte le nom de "
            "&quot;Clover Club&quot; et ressuscite ce bon vieu cocktail "
            "pour en faire l&#x27;un de leurs cocktails phare. À "
            "l&#x27;heure où ce texte est écrit, la recette du cocktail "
            "Clover Club est réalisée dans ce restaurant avec du vermouth "
            "dry en plus.</p>",
            "ingredients": [
                "4 cl de gin",
                "2 cl de jus de citron pressé et filtré",
                "1 cl de sirop de grenadine",
                "1 blanc d'œuf",
            ],
            "summary": "Le Clover Club : un cocktail qui a ressuscité après des "
            "décennies d&#x27;oubli.",
            "title": "Cocktail Clover Club",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Astoria est publiée en "
            "1931 dans &quot;The Old Waldorf-Astoria Bar Book&quot; de "
            "Stevens Crockett&#x27;s qui édite les recettes d&#x27;un "
            "l&#x27;hôtel familial new-yorkais : le "
            "Waldorf-Astoria.</p><p>Le Old Waldorf-Astoria était un hôtel "
            "familial de New-York au départ divisé en 2 hôtels : le "
            "Waldorf (créé en 1893 par William Waldorf Astor) et "
            "l&#x27;Astoria (créé en 1897 par l&#x27;intermédiaire deJohn "
            "Jacob Astor). En 1929 les 2 hôtels ont été détruits, mais le "
            "&quot;nouveau&quot; Waldorf-Astoria a été reconstruit en "
            "1931 à Manhattan sur Park Avenue, il devient cette année-là "
            "l&#x27;un des plus grands hôtels du monde. C&#x27;est aussi "
            "en 1931 qu&#x27;en lieu et place de l&#x27;ancien "
            "Waldorf-Astoria, l&#x27;empire State Building a été "
            "construit.</p>",
            "ingredients": [
                "1/3 de gin",
                "2/3 de vermouth blanc extra dry (Martini...)",
                "2 ou 3 traits d'Orange Bitters",
            ],
            "summary": "Le Astoria : le cocktail phare de l&#x27;hôtel du même nom situé "
            "à Manhattan.",
            "title": "Cocktail Astoria",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Cornell est publiée "
            "pour la première fois en 1916 dans &quot;Recipes for Mixed "
            "Drinks&quot; de Hugo R. Ensslin, la recette appelle à "
            "utiliser du London Dry Gin.</p>",
            "ingredients": [
                "4 cl de gin",
                "5 cl de marasquin",
                "1 blanc d'oeuf",
            ],
            "summary": "Le cocktail Cornell : une recette apparue pendant la première "
            "guerre mondiale.",
            "title": "Cocktail Cornell",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (6cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Dry Martini est un grand "
            "classique et très certainement l&#x27;un des cocktails les "
            "plus célèbres à base de vermouth. La tradition veut que la "
            "recette du Dry Martini soit composée de 5 parts de gin pour "
            "1 part de vermouth, c&#x27;est pour cette raison que ce "
            "short drink fait 6 cl au lieu de 7.</p><p>L&#x27;origine de "
            "ce cocktail remonte à très loin et est donc très incertaine. "
            "On dit que le Dry martini pourrait remonter à 1849 et aurait "
            "été créé dans la ville de Martinez en Californie. On dit "
            "aussi que la marque Martini &amp; Rossi serait à "
            "l&#x27;origine du Dry martini, d&#x27;où le nom du cocktail. "
            "Quoiqu&#x27;il en soit ce n&#x27;est qu&#x27;à partir de la "
            "période de la prohibition aux États-Unis, de 1920 à 1933, "
            "que le succès du cocktail Dry martini a commencé grâce au "
            "succès du gin.</p><p>En remplaçant le gin par de la tequila "
            "ou de la vodka, on obtiendra respectivement les cocktails "
            "tequini et vodkatini.</p><p>Le Dry Martini est le cocktail "
            "favori de James Bond, arrangé à sa manière il préfère "
            "notamment ce cocktail frappé au shaker. On associe aussi le "
            "cocktail Dry Martini à quelques personnalités comme "
            "notamment Franklin Roosevelt ou Winston Churchill.</p>",
            "ingredients": [
                "5 cl de gin",
                "1 cl de vermouth blanc (Martini, Noilly prat...)",
            ],
            "summary": "Le Dry Martini : un cocktail qui fût une référence pour "
            "Roosevelt, Churchill et James Bond !",
            "title": "Cocktail Dry Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Dubonnet cocktail , aussi appelé "
            "&quot;Zaza&quot; serait l&#x27;un des cocktails favoris de "
            "la reine Élizabeth 2, il a fait son apparition dans les "
            "années 1900. Le cocktail est composé à dose égale de gin et "
            "de Dubonnet, fameux apéritif français créé en 1846 de la "
            "famille des &quot;ABV&quot; (apéritif à base de vin) composé "
            "de mistelles et au goût subtil de plantes et "
            "d&#x27;épices.</p><p>Harry Craddock a été le premier à "
            "imprimer cette recette dans son célèbre ouvrage The savoy "
            "cocktail book en 1930. À l&#x27;origine sans décoration, le "
            "Dubonnet cocktail se sert de plus en plus accompagné "
            "d&#x27;un zeste de citron.</p>",
            "ingredients": ["3,5 cl de gin", "3,5 cl de Dubonnet rouge"],
            "summary": "Le Dubonnet cocktail : sa couleur ambre rouge renferme une "
            "recette simple mais plaisante.",
            "title": "Cocktail Dubonnet cocktail",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Fog Horn a été publié par Tom "
            "Bullock en 1917 dans &quot; The Ideal Bartender &quot; qui "
            "invitait à utiliser dans sa recette du Old Tom Gin.</p><p>La "
            "recette ci-dessus est la recette courante réalisée par les "
            "barmen aujourd&#x27;hui, ci-après la recette d&#x27;origine "
            "telle qu&#x27;elle a été publiée en 1917 et qui était un peu "
            "plus complexe.</p><p>Mélanger dans un verre à mélange à "
            "moitié rempli de glace :</p><p>Verser dans un verre en "
            "filtrant la glace, puis compléter avec le ginger ale.</p>",
            "ingredients": ["6 cl de gin", "14 cl de ginger ale (Canada Dry®)"],
            "summary": "Le cocktail Fog Horn : une recette publiée en 1917 par Tom "
            "Bullock.",
            "title": "Cocktail Fog Horn",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail French 75 est publié "
            "pour la première fois sous ce nom dans &quot;The Savoy "
            "Cocktail Book&quot; de Harry Craddock en 1930, mais on "
            "retrouve une recette similaire dès 1927 dans "
            "&quot;Here&#x27;s How&quot; de Judge Jr. Ce cocktail est "
            "globalement un Tom Collins mais avec du champagne à la place "
            "de l&#x27;eau gazeuse.</p><p>Le &quot;French 75&quot; est le "
            "nom que portait un canon français utilisé pendant la "
            "première guerre mondiale, c&#x27;était de arme de 75 mm.</p>",
            "ingredients": [
                "3 cl de gin",
                "1,5 cl de jus de citron",
                "1,5 cl de sirop de sucre de canne",
                "6 cl de Champagne",
            ],
            "summary": "Le French 75 : un cocktail portant le nom d&#x27;une arme "
            "d&#x27;artillerie française de 75mm.",
            "title": "Cocktail French 75",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 1 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Les premières traces du cocktail Gibson se "
            "trouvent dans un article de Edward Townsend dans le New York "
            "World en 1898.</p><p>C&#x27;est dans le Bohemian Club de San "
            "Francisco que dirigeait Edward Townsend que le Gibson aurait "
            "été inventé, par l&#x27;un des membres du Club, donnant son "
            "nom au cocktail. Le premier livre à faire paraître la "
            "recette complète du Gibson est en 1908, dans The "
            "World&#x27;s Drinks and How to Mix Them de William Boothby "
            ".</p>",
            "ingredients": [
                "5 cl de gin",
                "2 cl de vermouth dry (Martini extra dry, Noilly Prat dry)",
            ],
            "summary": "Le Gibson : un cocktail sec au gin et vermouth dry.",
            "title": "Cocktail Gibson",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Plusieurs histoires se contredisent sur "
            "l&#x27;origine du cocktail Gimlet mais on a plus tendance à "
            "l&#x27;attribuer à Thomas Desmond Gimlette (1857–1943), "
            "amiral et medecin du &quot;Royal Navy&quot; de l&#x27;armée "
            "britanique. Le citron avait le pouvoir de lutter contre le "
            "scorbut, et le gin permettait de conserver la vitamine C "
            "présente dans le citron.</p><p>Le cocktail aurait été "
            "initialement composé de gin et de jus de citron vert mais "
            "depuis bien longtemps, beaucoup de barmen se sont accordés à "
            "dire que le jus de citron devait être remplacé par du lime "
            "cordial pour adoucir le cocktail.</p><p>Si vous n&#x27;avez "
            "pas de lime cordial, vous pouvez le remplacer par 1 cl de "
            "jus de citron vert et 1 cl du sirop de sucre.</p>",
            "ingredients": ["5 cl de gin", "2 cl de lime cordial"],
            "summary": "Le Gimlet : un cocktail qui fût l&#x27;elixir magique de la "
            "marine britannique.",
            "title": "Cocktail Gimlet",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Gin Fizz a été publiée "
            "pour la première fois en 1862 dans &quot;How to Mix "
            "Drinks&quot; de Jerry Thomas sous le nom de Gin Fix. Le Gin "
            "Fizz est une variante du célèbre cocktail Gin Tonic, on le "
            "concoctait dès 1750 pour lutter contre la malaria grâce à la "
            "vertu de la quinine se trouvant dans le tonic.</p><p>Recette "
            "simple et équilibrée, on apporte simplement au gin la "
            "fraîcheur du citron et la douceur du sucre, c&#x27;est "
            "l&#x27;objectif des fizzes. Avec les mêmes proportions, nous "
            "pourrions donc faire de même avec toute autre "
            "eau-de-vie.</p><p>Plusieurs cocktails sont dérivés du Gin "
            "Fizz : Silver Fizz (avec un blanc d&#x27;œuf), Golden Fizz "
            "(avec un jaune d&#x27;œuf), Royal Fizz (avec un œuf entier) "
            "ou Ramos Gin Fizz.</p><p>Le Gin Fizz n&#x27;est pas à "
            "confondre avec le cocktail Tom Collins, la principale "
            "différence réside dans le fait que le Gin Fizz est servi "
            "sans glace au contraire du Tom Collins.</p>",
            "ingredients": [
                "4 cl de gin",
                "3 cl de jus de citron pressé et filtré",
                "1 cuillère à café de sucre",
                "5 cl d'eau gazeuse",
            ],
            "summary": "Le Gin Fizz : un cocktail doux et rafraîchissant fait de gin, "
            "jus de citron et eau gazeuse.",
            "title": "Cocktail Gin Fizz",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Gin Julep fait partie de la "
            "famille des &quot;juleps&quot; dont la consommation "
            "remonterait au XVIIème ou XVIIIème siècle, le cocktail le "
            "plus célèbre de cette famille est le Mint Julep . Le Gin "
            "Julep est publié pour la première fois dans "
            "&quot;Bar-tenders Guide : How to mix drinks&quot; en 1862 "
            "par Jerry Thomas.</p>",
            "ingredients": [
                "5 cl de gin",
                "1 cuillère à café de sucre en poudre",
                "5 à 7 feuilles de menthe fraîche",
            ],
            "summary": "Le Gin Julep : la célèbre eau de vie de grain à l&#x27;honneur "
            "dans ce cocktail de la famille des juleps.",
            "title": "Cocktail Gin Julep",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Gin Rickey apparaît pour la "
            "première fois en 1882 dans &quot;Bartenders Manual&quot; de "
            "Harry Johnson&#x27;s. Le Gin Rickey aurait été créé par le "
            "barman George Williamson en 1880 au &quot;Shoomaker&#x27;s "
            "Bar&quot; à Washington, en l&#x27;honneur du colonel Joe "
            "Rickey qui est devenu par la suite un grand importateur de "
            "citrons.</p><p>Les Gin Rickeys sont globalement des gin fizz "
            "avec le sucre en moins.</p><p>Il n&#x27;y a pas de "
            "décoration dans la recette originale du Gin Rickey mais rien "
            "n&#x27;empêche d&#x27;embellir avec une tranche ou un zeste "
            "de citron vert.</p>",
            "ingredients": [
                "7 cl de gin",
                "4 cl de jus de citron vert pressé et filtré",
                "9 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Gin Rickey : une recette américaine créée en 1880 "
            "proche du gin fizz.",
            "title": "Cocktail Gin Rickey",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le Gin "
            "Sour fait partie des &quot;Sours&quot;, célèbre famille de "
            "cocktails qui sont toujours réalisés avec une eau-de-vie, du "
            "jus de citron et du sucre.</p><p>Il est possible de rajouter "
            "ou non selon votre convenance dans un Gin Sour un blanc "
            "d&#x27;oeuf et 2 ou 3 traits d&#x27;Angostura bitters, vous "
            "pouvez aussi mettre plus de sirop de sucre pour obtenir un "
            "Gin Sour plus sucré.</p>",
            "ingredients": [
                "6 cl de Gin",
                "3 cl de jus de citron vert",
                "1 cl de sirop de sucre",
            ],
            "summary": "Le Gin Sour : une recette de la famille des &quot;Sours&quot; en "
            "version Gin.",
            "title": "Cocktail Gin Sour",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: Toddy</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Gin Toddy est paru pour la "
            "première fois en 1862 dans B artenders Guide : How to mix "
            "drinks de Jerry Thomas.</p><p>La recette se réalise de "
            "différentes manières en fonction des préférences de chacun. "
            "Certains préfèrent en effet insérer 1 ou 2 cl de jus de "
            "citron à la place de la rondelle pour avoir un goût plus "
            "prononcé d&#x27;acidité, quand d&#x27;autres préfèreront "
            "diminuer la quantité d&#x27;eau chaude.</p>",
            "ingredients": [
                "6 cl de gin",
                "12 cl d'eau chaude",
                "1 cuillère à café de sucre en poudre",
                "1 rondelle de citron",
            ],
            "summary": "Le Gin Toddy : une recette peu onéreuse pour se réchauffer avec "
            "un cocktail chaud.",
            "title": "Cocktail Gin Toddy",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Gin Tonic remonterait aux "
            "environs de 1750 et aurait commencé à être consommé par des "
            "officiers de la marine anglo-saxonne. À cette époque, la "
            "malaria et le scorbut faisaient des ravages, les officiers "
            "auraient décidé d&#x27;ajouter au gin du tonic et du citron "
            "pour leurs vertus. Le mélange était magique, le tonic à base "
            "de quinine aidait à lutter contre la malaria, le citron "
            "aidait à lutter contre le scorbut, tandis que l&#x27;alcool "
            "préservait la vitamine C.</p><p>De retour sur leurs terres, "
            "les anglais ont gardé leurs habitudes à consommer le gin "
            "tonic, y ont rajouté du sucre et de l&#x27;eau gazeuse pour "
            "adoucir le mélange, le cocktail Gin Fizz est alors né.</p>",
            "ingredients": ["4 cl de gin", "Tonic (Schweppes...)"],
            "summary": "Gin Tonic : un cocktail autrefois utilisé pour combattre le "
            "scorbut et la malaria !",
            "title": "Cocktail Gin Tonic",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Income tax (impôt sur le revenu) "
            "et une variante très proche du Bronx et aurait été créé vers "
            "1906 par Johnny Solon, barman au Waldorf-Astoria Hotel de "
            "New York.</p>",
            "ingredients": [
                "3 cl de gin",
                "1 cl de vermouth blanc",
                "1 cl de vermouth rouge",
                "2 cl de jus d'orange",
                "2 traits d'Angostura bitters",
            ],
            "summary": "Le cocktail Income tax : l&#x27;impôt sur le revenu a sa propre "
            "recette !",
            "title": "Cocktail Income Tax",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Macca est un cocktail qui semble être "
            "d&#x27;origine française, mais qui ne dispose de peu "
            "d&#x27;informations supplémentaires quant à son "
            "origine.</p><p>&quot;Macca&quot; est aussi le surnom de Paul "
            "McCartney, mais aucun lien avec les cocktails Maccas.</p>",
            "ingredients": [
                "1 cl de crème de cassis",
                "2 cl de vermouth dry (Martini extra dry, Noilly Prat dry)",
                "2 cl de vermouth rouge (Martini...)",
                "2 cl de gin",
                "5 cl d'eau gazeuse",
            ],
            "summary": "La recette du cocktail Macca qui est aussi le surnom de Paul "
            "McCartney.",
            "title": "Cocktail Macca",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: martini</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Monkey Gland a été publié pour la "
            "première fois dans le &quot;Washington Post&quot;, "
            "attribuant la création du cocktail à Frank Meier du Ritz à "
            "Paris. La recette originale veut qu&#x27;il y ait autant de "
            "gin que de jus d&#x27;orange. Le doute s&#x27;est installé "
            "plus tard quant au véritable inventeur de ce cocktail, quand "
            "le nom de Harry MacElhone a commencé à circuler.</p><p>Pour "
            "des raisons de disponibilité, l&#x27;absinthe est parfois "
            "remplacée par de l&#x27;anisé ou de la bénédictine.</p>",
            "ingredients": [
                "2,5 cl de gin",
                "1 cl d'absinthe",
                "3 cl de jus d'orange",
                "0,5 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Monkey Gland : un nom qui évoque la greffe des "
            "testicules de singe pratiquée sur l&#x27;homme.",
            "title": "Cocktail Monkey Gland",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Apéritif incontestable, le cocktail Negroni a "
            "vu sa recette évoluer avec le temps. Longtemps réalisé avec "
            "1/3 de gin, 1/3 de vermouth et 1/3 de bitter, il se réalise "
            "de plus en plus avec plus de gin pour un meilleur "
            "équilibre.</p><p>Son origine n&#x27;est pas réellement "
            "certaine mais le cocktail aurait vu le jour dans les années "
            "1900 grâce au comte Camillo Negroni, un aristocrate de "
            "Florence dont le cocktail préféré était l&#x27;Americano. Un "
            "peu lassé, le comte aurait demandé à son barman habituel "
            "Fosco Scarelli de remplacer l&#x27;eau gazeuse par du gin. "
            "Le célèbre cocktail Negroni est né, il est devenu "
            "aujourd&#x27;hui un grand classique de l&#x27;apéritif.</p>",
            "ingredients": [
                "3 cl de vermouth rouge (Martini...)",
                "3 cl de Campari",
                "4 cl de gin",
            ],
            "summary": "Le cocktail Negroni : une recette de plus d&#x27;un siècle qui "
            "porte le nom de son créateur.",
            "title": "Cocktail Negroni",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Orange Blossom est né au tout "
            "début voire avant la période de prohibition aux États-Unis "
            "(1919-1933), il est simplement composé de gin et de jus "
            "d&#x27;orange.</p><p>Le Orange Blossom a été publié pour la "
            "première fois en 1922 dans le livre de recettes de Robert "
            "Vermeire qui invite à ajouter un &quot;petit trait&quot; "
            "d&#x27;Orange Bitters, voire un trait de sirop de "
            "grenadine pour ceux qui souhaitent adoucir ce "
            "cocktail.</p><p>Robert y indique par ailleurs que cette "
            "recette provient d&#x27;un certain &quot;Malloy&quot; de "
            "Pittsburg, qui serait donc le créateur de ce cocktail.</p>",
            "ingredients": ["4 cl de gin", "6 cl de jus d'orange"],
            "summary": "Le cocktail Orange Blossom : une recette très simple signifiant "
            "&quot;Fleur d&#x27;oranger&quot; en français.",
            "title": "Cocktail Orange Blossom",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Paradise est apparue "
            "pour la première fois en 1930 dans &quot;The Savoy cocktail "
            "book&quot; de Harry Craddock, c&#x27;est l&#x27;auteur de "
            "cet ouvrage qui est le créateur de ce cocktail.</p><p>Harry "
            "Craddock était barman à New York, puis durant la prohibition "
            "aux USA, il est parti au &quot;American Bar&quot; du luxueux "
            "&quot;Savoy Hôtel&quot; de Londres dont il devient le chef "
            "barman en 1924. Il est le créateur de pas moins de 250 "
            "cocktails dont l&#x27;un d&#x27;eux est le désormais "
            "classique &quot;Paradise&quot;.</p>",
            "ingredients": [
                "4 cl de gin",
                "2 cl de liqueur d'abricot (Apricot Brandy)",
                "1 cl de jus d'orange",
            ],
            "summary": "Le cocktail Paradise : un short drink fruité à siroter "
            "idéalement en apéritif.",
            "title": "Cocktail Paradise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Pink Gin est originaire "
            "d&#x27;Angleterre, là où il est aussi connu sous le nom "
            "&quot;Gin &amp; Bitters&quot;. Traditionnellement, ce "
            "cocktail british est réalisé avec du Plymouth Gin qui a "
            "l&#x27;avantage d&#x27;être plus doux et donc de rendre ce "
            "cocktail plus agréable pour certains.</p><p>À partir des "
            "années 1830, l&#x27;Angostura bitters a commencé à être "
            "exporté vers l&#x27;Angleterre, le Pink Gin fût alors "
            "concocté sur le &quot;Royal Navy&quot; de la marine "
            "britannique pour les vertus médicales de l&#x27;angostura à "
            "guérir le mal de mer.</p><p>Le Pink Gin a été introduit plus "
            "tard dans les bars britanniques et est devenu très populaire "
            "à partir de 1870.</p><p>Il est de plus en plus fréquent de "
            "voir des &quot;Pinks Gins&quot; réalisés avec un zeste de "
            "citron inséré dans le verre.</p>",
            "ingredients": ["4 cl de gin", "3 traits d'Angostura bitters"],
            "summary": "Le Pink Gin : le cocktail elixir contre le mal de mer pendant le "
            "19ème siècle.",
            "title": "Cocktail Pink Gin",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>D&#x27;origine pas réellement connue, le "
            "cocktail Pink Lady aurait vu le jour dans les années 1930. "
            "Certains attribuent l&#x27;invention à Lady Mendl en "
            "1933.</p><p>Dès sa création, le Pink Lady a l&#x27;image du "
            "cocktail idéal pour les femmes à cause de son nom, sa "
            "douceur, sa couleur et ses saveurs fruitées.</p>",
            "ingredients": [
                "4 cl de gin",
                "2 cl de jus de citron pressé et filtré",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le Pink Lady : un cocktail doux, fruité et rafraîchissant qui a "
            "l&#x27;image du cocktail féminin.",
            "title": "Cocktail Pink Lady",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail RAC (ou R.A.C.) a été publié pour "
            "la première fois dans &quot; Cocktails : How to mix them "
            "&quot; de 1922 par le célèbre bartender Robert Vermeire "
            ".</p><p>L&#x27;auteur y indique que les initiales R.A.C. "
            "signifient Royal Automobile Club (Londres) et que la recette "
            "a été créée en 1914 par Fred Faecks.</p>",
            "ingredients": [
                "5 cl de Dry Gin",
                "2,5 cl de vermouth blanc",
                "2,5 cl de vermouth rouge",
                "1 trait de sirop de grenadine",
                "1 trait d'Orange Bitters",
            ],
            "summary": "Le RAC cocktail : une recette datant de 1914 qui provient du "
            "Royal Automobile Club.",
            "title": "Cocktail RAC",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Raspberry Collins est un &quot;Collins&quot; (type "
            "de long drink) dans une version aux framboises, vous pouvez "
            "si vous le souhaitez rajouter un peu de liqueur ou sirop de "
            "framboise pour des saveurs plus prononcées du fruit.</p>",
            "ingredients": [
                "4 cl de gin",
                "1,5 cl de jus de citron pressé",
                "1,5 cl de sirop de sucre de canne",
                "6 cl d'eau gazeuse",
                "10 framboises fraîches",
            ],
            "summary": "Le Raspberry Collins : la recette fruitée d&#x27;un collins aux "
            "framboises.",
            "title": "Cocktail Raspberry Collins",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Red Lion aurait été créé en 1933 "
            "par le barman britannique Arthur A. Tarling. Sa recette lui "
            "a valu cette année-là le premier prix d&#x27;un concours "
            "britannique de cocktails, la &quot;British Empire Cocktail "
            "Competition&quot;.</p><p>Cette compétition était organisée "
            "par la marque de gin &quot;Booth&#x27;s Gin&quot; créée vers "
            "1740. À ce jour, ce gin est encore produit et commercialisé. "
            "Red Lion est le nom que portait la plus ancienne distillerie "
            "de Booth&#x27;s gin.</p>",
            "ingredients": [
                "3 cl de gin",
                "3 cl de triple sec (Grand Marnier)",
                "2 cl de jus de citron pressé et filtré",
                "2 cl de jus d'orange",
            ],
            "summary": "Le Red Lion : un cocktail riche en agrumes qui remporta le 1er "
            "prix d&#x27;un célèbre concours.",
            "title": "Cocktail Red Lion",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Red Snapper est un dérivé du "
            "célèbre cocktail Bloody Mary , le gin remplace ici la vodka "
            "initiale.</p><p>Fernand Petiot, qui serait le créateur du "
            "Bloody Mary, aurait été contraint de remplacer la vodka par "
            "du gin dans sa création et d&#x27;appeler son cocktail le "
            "&quot;Red Snapper&quot; en arrivant au King Cole Bar à New "
            "York au milieu des années 1930.</p>",
            "ingredients": [
                "Quelques gouttes de tabasco",
                "1 cl de sauce worcestershire",
                "2 cl de jus de citron pressé et filtré",
                "6 cl de gin",
                "11 cl de jus de tomate",
            ],
            "summary": "Le cocktail Red Snapper : un Booldy Mary avec du gin à la place "
            "de la vodka.",
            "title": "Cocktail Red Snapper",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Shady Grove , aussi appelé Shady Grove Cooler , est "
            "un cocktail de la famille des &quot;coolers&quot;, et comme "
            "tous les cocktails de cette famille il est donc toujours "
            "composé d&#x27;une eau-de-vie, de jus de citron, de sirop de "
            "sucre (à ne jamais oublier pour un cocktail de cette famille "
            "contrairement à ce qu&#x27;on peut voir quelques fois) et "
            "d&#x27;un soda.</p><p>Le Shady Grove un cocktail doux, sucré "
            "et rafraîchissant encore plus savoureux qu&#x27;un gin fizz "
            "ou un tom collins.</p>",
            "ingredients": [
                "6 cl de gin",
                "3 cl de jus de citron vert pressé",
                "1 cl de sirop de sucre de canne",
                "5 cl de ginger ale (Canada Dry...)",
            ],
            "summary": "Le cocktail Shady Grove : la recette d&#x27;un cooler au gin et "
            "ginger ale.",
            "title": "Cocktail Shady Grove",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler ou hurricane</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Singapore Sling ne fait "
            "malheureusement pas partie des cocktails desquels on connaît "
            "l&#x27;origine avec certitude, mais il existe quelques "
            "théories dont la suivante...</p><p>Certains disent que ce "
            "cocktail aurait été créé vers 1915 au Long Bar de "
            "l&#x27;Hôtel Raffles à Singapour par le barman M. Tong Boon "
            "Ngiam, mais...</p><p>La recette apparaît pour la première "
            "fois sous le nom de &quot;Straits Sling&quot; en 1922 dans "
            "&quot;Cocktails and How to Mix Them&quot; de Robert "
            "Vermeire. Dans cette version de Robert Vermeire, le cocktail "
            "n&#x27;a ni cointreau, ni jus d&#x27;ananas, ni de sirop de "
            "grenadine, mais contient 2 bitters et est complété avec du "
            "soda.</p><p>Ted Haigh, alias Dr Cocktail, a fait des "
            "recherches poussées sur l&#x27;origine du Singapore Sling et "
            "indique que même l&#x27;hôtel Raffles ne disposerait pas de "
            "la recette originale. La recette actuelle daterait de 1970 "
            "et aurait été mise au point par le neveu de Ngiam Tong "
            "Boon.</p><p>Toujours est-il qu&#x27;un siècle après, le "
            "cocktail est devenu une grande îcone dans l&#x27;hôtel et à "
            "Singapour où un repas sans &quot;Singapore Sling&quot; "
            "laisserait presque un goût d&#x27;inachevé et de déshonneur. "
            "À l&#x27;origine, le cocktail était plutôt destiné aux "
            "femmes, ses ingrédients alcoolisés se faisant effectivement "
            "bien oublié sous une douce couleur rosée.</p><p>De "
            "composition assez complexe, le cocktail Singapore Sling est "
            "ici rallongé à 20cl pour garder avec précision "
            "l&#x27;équilibre des ingrédients.</p><p>Un peu complexe, la "
            "recette du Singapore Sling est aussi connue dans une version "
            "très simplifiée dans laquelle on ne garde que le gin (3cl), "
            "la liqueur de cerise (3cl), le jus de citron (1cl) et "
            "l&#x27;eau gazeuse (5cl).</p>",
            "ingredients": [
                "4 cl de gin",
                "2 cl de liqueur de cerises (Cherry Brandy)",
                "0,5 cl de Cointreau",
                "0,5 cl de Bénédictine",
                "1 cl de sirop de grenadine",
                "8 cl de jus d'ananas",
                "3 cl de jus de citron pressé et filtré",
                "1 trait d'Angostura bitters",
            ],
            "summary": "Le Singapore Sling : un cocktail à la recette complexe devenu la "
            "boisson emblématique de Singapour.",
            "title": "Cocktail Singapore Sling",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Southside aurait vu le jour au 21 "
            "Club à New York, durant la Prohibition "
            "(1919-1933).</p><p>Les premières traces écrites de cette "
            "recette se trouvent dans le célèbre Savoy Cocktail Book de "
            "Harry Craddock en 1930. Plus tard, en 1946, Lucius Beebe le "
            "publie à son tour dans Stork Club Bar Book .</p>",
            "ingredients": [
                "3 cl de gin",
                "2 cl de jus de citron",
                "5 cl d'eau gazeuse",
                "1 cuillère à café de sucre",
                "1 ou 2 feuilles de menthe",
            ],
            "summary": "Le cocktail Southside : une recette née durant la Prohibition au "
            "21 Club à New-York.",
            "title": "Cocktail Southside",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Suffering Bastard aurait été créé "
            "par Joe Scialom au Shepherd&#x27;s Hotel au Caire (Égypte) "
            "avant 1950. La recette ci-dessus est l&#x27;originale telle "
            "qu&#x27;elle a été retrouvée dans des papiers privés de Joe "
            "Scialom.</p><p>La première référence écrite de ce cocktail "
            "date du 1er mai 1950, il s&#x27;agit du Time Magazine qui "
            "indiquait que le Suffering Bastard était la boisson préférée "
            "des égyptiens.</p><p>Pourquoi la recette a été nommée "
            "&quot;Bâtard souffrant&quot; est par contre un "
            "mystère.</p><p>Le Suffering Bastard compte depuis peu parmi "
            "les nouveaux cocktails classiques IBA.</p>",
            "ingredients": [
                "2 cl de gin",
                "2 cl de Cognac",
                "1 cl de Lime Cordial",
                "Quelques gouttes d'Angostura bitters",
                "7 cl de Ginger Beer",
            ],
            "summary": "Le cocktail Suffering Bastard : une recette qui signifie "
            "&quot;Bâtard souffrant&quot;.",
            "title": "Cocktail Suffering Bastard",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Très populaire en Amérique, le cocktail Tom "
            "Collins a une composition identique au Gin Fizz, à la "
            "différence principale qu&#x27;il est servi sur glace et "
            "réalisé directement au verre. La recette du Tom Collins a "
            "été publiée la première fois en 1876 sous le nom de Gin Fix "
            "dans &quot;Bartender&#x27;s Guide&quot; de Jerry Thomas, "
            "barman américain et père de la mixologie.</p><p>Les "
            "&quot;collins&quot; sont un type de long drinks qui remonte "
            "à 1850 et qu&#x27;on attribuerait à Vincent Collins, un "
            "barman de New York qui avait alors 23 ans. Il réalisait le "
            "Tom Collins à partir de &quot;Old Tom Gin&quot;, un gin plus "
            "doux et sucré mais aujourd&#x27;hui difficilement trouvable, "
            "d&#x27;où peut-être l&#x27;origine du nom &quot;Tom "
            "Collins&quot;. Le Tom Collins fût un tel succès que Vincent "
            "Collins aurait créé vers 1970 le &quot;John Collins&quot; en "
            "hommage à son frère en remplaçant le gin par du bourbon. "
            "Cette origine du John Collins reste malgré tout plus "
            "qu&#x27;incertaine, David Wondrich écrit dans "
            "&quot;Imbibe!&quot; que le John Collins aurait vu le jour en "
            "Angleterre vers 1830, et encore une autre version raconte "
            "que ce serait un &quot;John Collins&quot; qui aurait inventé "
            "le cocktail du même nom dans les années 1800. Ces deux "
            "dernières versions restent plus probable, le Tom Collins "
            "tiendrait alors son nom d&#x27;un énorme canular réellement "
            "survenu à l&#x27;été 1974.</p><p>La blague consistait à "
            "croiser un ami ou un parfait inconnu dans la rue, et lui "
            "faire croire qu&#x27;un certain Tom Collins tenait des "
            "propos injurieux sur lui et que ce fameux Tom Collins se "
            "trouvait dans le bar du coin. Lorsque cette personne se "
            "rendait alors dans le bar pour régler ses comptes, un "
            "complice se trouvant dans le bar expliquait alors que Tom "
            "Collins était parti dans un autre bar. La victime finissait "
            "par vadrouiller de bar en bar pour retrouver Tom Collins. "
            "Les boucs émissaires de plus en plus nombreux, les grands "
            "journaux ont fait état du phénomène. Le &quot;Daily "
            "Republican&quot; publie en juin 1974 &quot;Tom Collins Still "
            "Among Us&quot; (Tom Collins toujours parmi nous) en "
            "indiquant que l&#x27;individu avait encore toute la journée "
            "d&#x27;hier continué son projet néfaste de diffamation "
            "envers les citoyens et qu&#x27;il avait réussi à garder la "
            "distance sur ses poursuivants. Le quotidien continue en "
            "écrivant qu&#x27;à certains moments Tom Collins était à 2 "
            "doigts d&#x27;être capturé par ses poursuivants, ses "
            "déplacements sont surveillés avec la plus grande "
            "vigilance.</p><p>Lorsque la presse s&#x27;est rendu compte "
            "qu&#x27;il s&#x27;agissait d&#x27;un canular, elle aurait "
            "continué à jouer le jeu déclarant même que Collins aurait "
            "été repéré en Californie sur la route de l&#x27;Arizona, et "
            "qu&#x27;au printemps d&#x27;après il sera entré en "
            "république sud-américaine.</p><p>Cette histoire a vu grandir "
            "la popularité du cocktail, les boucs émissaires se voyant "
            "faire réaliser des cocktails nommés &quot;Tom Collins&quot; "
            "lorsqu&#x27;il entraient dans les bars. Nous pourrions bien "
            "imaginer qu&#x27;à l&#x27;origine le canular ait été lancé "
            "dans un projet purement marketing, quoiqu&#x27;il en soit le "
            "cocktail est devenu très célèbre en Amérique après cette "
            "histoire. Après la farce, le Tom Collins est vite devenu le "
            "cocktail le plus servi dans les salles de jeux de New York, "
            "O.H. Byron l&#x27;honore comme le cocktail le plus populaire "
            "dans &quot;The Modern Bartender’s Guide&quot; en "
            "1884.</p><p>En 1891, le médecin britannique Sir Morell "
            "Mackenzie veut attribuer l&#x27;origine du cocktail Tom "
            "Collins à l&#x27;Angleterre dans un article de magazine, et "
            "plus particulièrement à un certain John Collins. Il indique "
            "également que le cocktail est lié à une chanson du même nom, "
            "chose réfutée peu de temps après par un autre magazine qui "
            "fait remarquer que la chanson s&#x27;appelle en réalité "
            "&quot;Jim Collins&quot;. En 1898, l&#x27;écrivain américain "
            "Charles Montgomery Skinner indique que le Tom Collins est un "
            "cocktail d&#x27;origine américaine qui s&#x27;est developpé "
            "en France, en Angleterre et en Allemagne.</p><p>Si "
            "l&#x27;origine du cocktail reste toujours aussi incertaine, "
            "la recette a évolué depuis 1876 avec notamment la "
            "disparition du sirop de gomme et l&#x27;utilisation "
            "d&#x27;un gin plus &quot;classique&quot; que le Old Tom "
            "Gin.</p>",
            "ingredients": [
                "5 cl de gin",
                "3 cl de jus de citron pressé et filtré",
                "2 cuillère à café de sucre en poudre",
                "7 cl d'eau gazeuse",
            ],
            "summary": "Le Tom Collins : Le cocktail rendu célèbre grâce à un canular "
            "légendaire !",
            "title": "Cocktail Tom Collins",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: martini</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Tuxedo voit sa recette publiée "
            "pour la première fois en 1882 dans une publication de Harry "
            "Johnson. Ce n&#x27;est que plus de cinquante ans plus tard "
            "qu&#x27;il se révèle quand il est publié par Harry Craddock "
            "dans &quot;The Savoy Cocktail Book&quot; "
            "(1933).</p><p>Beaucoup réalisent le cocktail Tuxedo avec du "
            "&quot;Old Tom Gin&quot; pour respecter la recette originale, "
            "pour des raisons de disponibilité l&#x27;absinthe est "
            "malheureusement parfois remplacée par de l&#x27;anisé ou "
            "autre eau-de-vie.</p>",
            "ingredients": [
                "3 cl de gin",
                "3 cl de vermouth blanc",
                "1 cl de marasquin",
                "0,5 cl d'absinthe",
                "2 traits d'Orange Bitters",
            ],
            "summary": "Le Tuxedo : une union audacieuse mais qui rend ce cocktail très "
            "subtil.",
            "title": "Cocktail Tuxedo",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Vesper est parue pour "
            "la première fois en 1953 dans le livre de James Bond "
            "&quot;Casino Royale&quot; écrit par Ian Fleming. Le cocktail "
            "y est décrit comme une invention de James Bond, et "
            "qu&#x27;il aurait baptisé &quot;Vesper&quot; à cause de son "
            "profond attachement pour Vesper Lynd, un autre personnage du "
            "roman.</p><p>Plusieurs histoires se racontent concernant "
            "l&#x27;origine du cocktail, mais l&#x27;origine réelle se "
            "trouverait dans le livre &quot;You Only Live Once&quot;, "
            "autobiography de Ian Fleming écrite par Ivar Bryce. "
            "L&#x27;auteur rappelle que dans son exemplaire de "
            "&quot;Casion Royale&quot;, Ian Fleming a écrit &quot;To "
            "Ivar, who mixed the first vesper and said the good "
            "word&quot; (À Ivar qui a mixé le premier vesper et a dit le "
            "bon mot). Ivar Bryce explique aussi que le nom "
            "&quot;Vesper&quot; vient d&#x27;une boisson déjà existante "
            "qui a été servi à la maison d&#x27;un colonel britannique "
            "vivant en Jamaïque et qui était composé de rhum, de fruits "
            "surgelés et d&#x27;herbes.</p><p>Le Lillet est un apéritif "
            "composé de 85% de vin de Bordeaux (cépages de sauvigon et "
            "sémillon) et 15% de liqueur de fruits, il en existe 2 sortes "
            ": le Lillet blanc et le rouge. À l&#x27;époque où le livre "
            "de Ian Fleming est publié, le Lillet blanc était connu sous "
            "le nom de &quot;Kina Lillet&quot;.</p>",
            "ingredients": [
                "4,5 cl de gin",
                "1,5 cl de vodka",
                "1 cl de Lillet blanc",
            ],
            "summary": "Le Vesper : un cocktail rendu célèbre grâce au livre de James "
            "Bond &quot;Casino royale&quot; par Ian Fleming.",
            "title": "Cocktail Vesper",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail White lady aurait été créé par "
            "Harry MacElhone, créateur du fameux Harry&#x27;s New York "
            "Bar à Paris. Il aurait créé ce cocktail en 1919, avant "
            "qu&#x27;il n&#x27;arrive à Paris, quand il travaillait au "
            "Ciro&#x27;s Club de Londres. Le dosage de chaque ingrédient "
            "est aujourd&#x27;hui discutable, certains réalisent la "
            "recette en égalisant le Cointreau avec le jus de "
            "citron.</p><p>Dans les premières publications de la recette "
            "et en premier lieu dans &quot;The Savoy Cocktail Book&quot; "
            "de Harry Craddock en 1930, le triple sec et le jus de citron "
            "sont à doses égales.</p>",
            "ingredients": [
                "4 cl de gin",
                "2 cl de Cointreau",
                "1 cl de jus de citron jaune pressé et filtré",
            ],
            "summary": "Le White Lady : un cocktail riche en agrumes qui signifie "
            "&quot;dame blanche&quot; en français.",
            "title": "Cocktail White lady",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail White Way , qui signifie chemin "
            "blanc en français, ne dispose d&#x27;aucune information "
            "quant à son origine.</p><p>C&#x27;est une recette simple et "
            "unique, elle est toujours composée de gin et de crème ou "
            "liqueur de menthe blanche.</p>",
            "ingredients": [
                "4,5 cl de gin",
                "2,5 cl de crème ou liqueur de menthe blanche",
            ],
            "summary": "Le cocktail White Way : une recette composée de gin et liqueur "
            "de menthe.",
            "title": "Cocktail White Way",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: double verre à cocktail</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette de cocktail Wibble a été créée il "
            "y a quelques années par le mixologiste londonnien Dick "
            "Bradsell, à la demande de l&#x27;un des représentants de la "
            "marque de gin Plymouth qui, un jour en venant dans l&#x27;un "
            "des bars tenus par Dick, lui aurait demandé d&#x27;inventer "
            "un cocktail à base de Plymouth.</p>",
            "ingredients": [
                "25% de gin (Plymouth)",
                "25% de Sloe Gin",
                "25% de jus de pamplemousse",
                "10% de liqueur de mûre",
                "10% de jus de citron pressé et filtré",
                "5% de sirop de sucre",
            ],
            "summary": "Le cocktail Wibble : une recette inventée par Dick Bradsell en "
            "réponse à un défi lancé par un représentant de Plymouth Gin.",
            "title": "Cocktail Wibble",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail 491 ne dispose d&#x27;aucune "
            "information quant à son origine, sa recette courante se "
            "compose de rhum, de gin et d&#x27;Apricot Brandy à doses "
            "égales, le tout complété de bière au gingembre. Cependant il "
            "n&#x27;est pas rare de voir cette recette de base modifiée, "
            "certains ajoutent par exemple du sirop pour adoucir le "
            "cocktail quand d&#x27;autres enlèvent la liqueur "
            "d&#x27;abricot.</p>",
            "ingredients": [
                "2 cl de rhum",
                "2 cl de gin",
                "2 cl de liqueur d'abricot (Apricot Brandy)",
                "6 cl de Ginger Beer",
            ],
            "summary": "Le cocktail 491 : une recette pleine de saveurs et facile à "
            "réaliser.",
            "title": "Cocktail 491",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Il s&#x27;agit de la recette courante et sans "
            "doute originale du cocktail Acapulco que nous vous "
            "fournissons ici, elle est en effet traditionnellement "
            "réalisée avec du rhum blanc, triple sec, jus de citron vert, "
            "blanc d&#x27;oeuf, sucre et branche de menthe "
            "fraîche.</p><p>Cette recette est de plus en plus modifiée, "
            "certains ont notamment tendance à remplacer le rhum par de "
            "la tequila sans doute parce qu&#x27;il s&#x27;agit de la "
            "boisson phare du Mexique (rappelons que Acapulco de Juárez "
            "est une ville du Mexique). En remplaçant le rhum par de la "
            "tequila, le cocktail serait plus en adéquation avec son nom. "
            "Cette recette de base étant aussi un peu corsée, il "
            "n&#x27;est pas rare de trouver du jus de fruits incorporé "
            "avec notamment du jus d&#x27;ananas et du jus de "
            "pamplemousse car ce sont des fruits exotiques.</p><p>Voilà "
            "pourquoi parfois on peut trouver des Acapulcos complètement "
            "modifiés se composant de tequila et de jus de fruits.</p>",
            "ingredients": [
                "3 cl de rhum blanc",
                "1,5 cl de triple sec (Curaçao, Marie Brizard...)",
                "1,5 cl de jus de citron vert pressé et filtré",
                "1 blanc d'œuf",
                "1 cuillère à café de sucre",
            ],
            "summary": "Le Acapulco : le cocktail qui rend hommage à la célèbre ville "
            "balnéaire mexicaine.",
            "title": "Cocktail Acapulco",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Añejo Highball aurait été créé "
            "par le célèbre mixologiste Dale DeGroff à New York dans les "
            "années 1990.</p><p>Ce cocktail rend hommage aux barmen de "
            "Cuba des années 1920 et 1930, période de la prohibition aux "
            "États-Unis pendant laquelle les américains se rendaient à "
            "Cuba pour boire notamment des cocktails.</p><p>Dale DeGroff "
            "aurait affirmé que la réalisation de añejos highballs "
            "illustre combien il est nécessaire pour un barman de "
            "comprendre le rôle que joue chaque ingrédient dans une "
            "recette, le Añejo Highball offre en effet un mélange très "
            "riche en arômes dans une parfaite adéquation.</p>",
            "ingredients": [
                "4 cl de rhum vieilli",
                "1,5 cl de triple sec (Curaçao orange)",
                "1,5 cl de jus de citron vert pressé et filtré",
                "5 cl de Ginger Beer",
                "3 ou 4 traits d'Angostura bitters",
            ],
            "summary": "Le Añejo Highball : un cocktail récent qui offre un très riche "
            "mélange d&#x27;arômes.",
            "title": "Cocktail Añejo Highball",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du Apple Mojito est une variante "
            "du grand classique Mojito auquel on a ajouté de la liqueur "
            "de pomme rendant le cocktail encore plus doux et fruité.</p>",
            "ingredients": [
                "2,5 cl de rhum cubain",
                "2,5 cl de liqueur de pomme (Manzana, Apple Schnapps...)",
                "2 cl de jus de citron vert",
                "5 cl d'eau gazeuse",
                "7 à 10 feuilles de menthe verte",
                "3 ou 4 quartiers de citron vert",
                "1 cuillère à café de sucre en poudre",
            ],
            "summary": "Le Apple Mojito : des saveurs de pomme ajoutées au célèbre "
            "Mojito.",
            "title": "Cocktail Apple Mojito (mojito pomme)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Atomic Dog (chien atomique) est une recette "
            "désaltérante et très exotique avec ses saveurs de noix de "
            "coco, de melon et d&#x27;ananas.</p>",
            "ingredients": [
                "2 cl de rhum blanc",
                "2 cl de Malibu Coco",
                "2 cl de liqueur de melon",
                "2 cl de jus de citron pressé",
                "7 cl de jus d'ananas",
            ],
            "summary": "Le cocktail Atomic Dog : une recette exotique et "
            "rafraîchisssante au Malibu.",
            "title": "Cocktail Atomic Dog",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Bacardi cocktail est apparu pour la "
            "première fois en 1922 dans &quot;Cocktails : How to mix "
            "them&quot; de Robert Vermeire. Dans la recette originale "
            "datant de 1922, il y avait du sirop de sucre en lieu et "
            "place du sirop de grenadine d&#x27;aujourd&#x27;hui.</p>",
            "ingredients": [
                "4 cl de rhum Bacardi",
                "2 cl de jus de citron vert pressé",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le Bacardi Cocktail : fruité et rafraîchissant, il se déguste à "
            "tout moment.",
            "title": "Cocktail Bacardi Cocktail",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler ou sling</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Bahama Mama fait partie de ces cocktails "
            "mystérieux dont il n&#x27;existe pas de recette originale, "
            "mais les ingrédients communs sont la plupart du temps dans "
            "la recette ci-dessus.</p><p>Quoiqu&#x27;il en soit cette "
            "recette au nom un peu atypique est très douce et exotique, "
            "la réaliser au blender lui permettra de garder sa fraîcheur "
            "plus longtemps grâce à la glace restante mais vous pouvez "
            "bien entendu la réaliser aussi au shaker.</p>",
            "ingredients": [
                "3 cl de rhum",
                "1,5 cl de Malibu Coco",
                "1,5 cl de liqueur de banane",
                "3 cl de jus d'ananas",
                "3 cl de jus d'orange",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Bahama Mama : une recette tiki exotique idéale "
            "pendant les périodes estivale.",
            "title": "Cocktail Bahama Mama",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler, collins</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Bahia daterait de la "
            "pré-prohibition et serait l&#x27;ancêtre de la Pina Colada. "
            "En 1972 il apparaît dans &quot; Trader Vic&#x27;s "
            "Bartender&#x27;s Guide &quot; et dans le monde entier on se "
            "tient à cette recette qui se réalise au blender avec du "
            "rhum, du jus d&#x27;ananas et de la crème de coco (et non "
            "pas du malibu comme malheureusement on peut le voir dans "
            "certaines fausses recettes sur le web).</p><p>Les bahias "
            "sont des cocktails très proches des célèbres Pina Colada et "
            "Chi Chi . Ce qui différencie le Bahia de la Pina est "
            "notamment le choix du rhum, dans le &quot; Trader Vic&#x27;s "
            "Bartender&#x27;s Guide &quot; on vous invite d&#x27;ailleurs "
            "à utiliser 2 rhums (jamaïcain et porto-ricain) à parts "
            "égales.</p><p>Le Bahia est une recette douce et exotique qui "
            "porte le nom d&#x27;un État du Brésil.</p>",
            "ingredients": [
                "4,5 cl de rhum (jamaïcain, porto-ricain)",
                "5,5 cl de jus d'ananas",
                "2 cl de crème de coco Lopez",
            ],
            "summary": "Le cocktail Bahia : l&#x27;ancêtre de la Pina Colada !",
            "title": "Cocktail Bahia",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler, sling ou verre tulipe</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Banana Colada est une variante de la Pina Colada "
            "dans laquelle on rajoute simplement 1 banane et de la "
            "liqueur de bananes.</p>",
            "ingredients": [
                "3 cl de rhum",
                "3 cl de crème de coco",
                "2 cl de liqueur de banane",
                "4 cl de jus d'ananas",
                "1 banane pelée",
            ],
            "summary": "Le cocktail Banana Colada : une Pina avec des saveurs de banane "
            "en plus.",
            "title": "Cocktail Banana Colada",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Banana Daiquiri , variante du "
            "grand classique Daiquiri, aurait été conçu par le capitaine "
            "George Soule en 1953 à Mountain Top, aux îles Vierges "
            "américaines.</p>",
            "ingredients": [
                "5 cl de rhum",
                "3 cl de jus de citron vert",
                "2 cl de sirop de sucre de canne",
                "1 demi banane pelée",
            ],
            "summary": "Le cocktail Banana Daïquiri : la même recette que le Daiquiri "
            "avec de la banane en plus.",
            "title": "Cocktail Banana Daiquiri",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Barracuda fait partie des "
            "nouveaux cocktails classiques IBA. La recette appelle à "
            "utiliser un rhum vieux (c&#x27;est-à-dire vieilli en fût de "
            "3 ans minimum) et du Prosecco (vin blanc pétillant "
            "italien).</p><p>Ce cocktail aurait commencé à être mis au "
            "point à partir la fin des années 1950 par Benito Cuppari, un "
            "barman italien qui oeuvrait sur des bateaux de croisière. "
            "C&#x27;est en l&#x27;honneur d&#x27;une discothèque du même "
            "nom située à Portofino et gérée par un ami à lui que Cuppari "
            "aurait baptisé sa recette le "
            "&quot;Barracuda&quot;.</p><p>Les Barracudas sont des "
            "cocktails qui se veulent fruités et rafraîchissants, le "
            "Prosecco y apporte sa petite touche italienne.</p>",
            "ingredients": [
                "4 cl de rhum vieux",
                "1 cl de liqueur Galliano",
                "5 cl de jus d'ananas",
                "1 cl de jus de citron vert",
                "4 cl de Prosecco",
            ],
            "summary": "Le Barracuda : la recette d&#x27;un cocktail classique italien "
            "des années 50.",
            "title": "Cocktail Barracuda",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À Propos</h2><p>Le "
            "cocktail Bedroom Farce signifie &quot;farce de "
            "chambre&quot;.</p>",
            "ingredients": [
                "3 cl de rhum ambré",
                "1,5 cl de whisky Bourbon",
                "1 cl de liqueur Galliano",
                "12 cl de chocolat chaud",
                "6 cl de crème fraîche",
            ],
            "summary": "Le Bedroom Farce : un cocktail chaud riche en saveurs.",
            "title": "Cocktail Bedroom Farce",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Between The Sheets n&#x27;a pas "
            "une origine certaine. D&#x27;un côté on dit que le cocktail "
            "aurait été créé dans les années 1930 par Harry MacElhone du "
            "New York&#x27;s Bar à Paris. Et d&#x27;un autre côté on dit "
            "que le cocktail aurait été inventé en 1921 par M. Polly à "
            "l&#x27;hôtel Berkeley à Londres.</p><p>Quoiqu&#x27;il en "
            "soit le &quot;Between the sheets&quot; est un cocktail "
            "parfaitement équilibré qui nous fait penser au cocktail Side "
            "Car dans lequel le cognac aurait séparé en 2 parts égales de "
            "rhum et de cognac.</p>",
            "ingredients": [
                "2 cl de rhum blanc",
                "2 cl de Cointreau",
                "2 cl de Cognac",
                "1 cl de jus de citron pressé et filtré",
            ],
            "summary": "Le Between the Sheets : un cocktail au rhum qui signifie "
            "&quot;entre les draps&quot;.",
            "title": "Cocktail Between the Sheets",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Black Devil (diable noir) est un cocktail "
            "de la famille des martinis, il reste très sec même si le "
            "vermouth adoucit très légèrement la rudesse du rhum.</p>",
            "ingredients": [
                "8/10 de rhum blanc",
                "2/10 de vermouth blanc (Martini, Noilly Prat...)",
            ],
            "summary": "Le cocktail Black devil : la recette du diable noir un peu rude "
            "à boire...",
            "title": "Cocktail Black Devil",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Black Stripe est un cocktail chaud dont la "
            "recette apparaît pour la première fois en 1862 dans "
            "&quot;How to mix drinks&quot; de Jerry Thomas. La recette "
            "d&#x27;origine ne comportait pas de miel, et la noix de "
            "muscade remplaçait la cannelle actuelle.</p>",
            "ingredients": [
                "6 cl de rhum ambré",
                "2 cuillère à café de mélasse",
                "1 cuillère à café de miel",
                "6 cl d'eau bouillante",
                "Cannelle râpée ou en poudre",
            ],
            "summary": "Le cocktail Black Stripe : un délicieux grog au miel et à la "
            "mélasse.",
            "title": "Cocktail Black Stripe",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: hurricane ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Blue Hawaiian est une variante de "
            "la Pina Colada et se réalise de la même manière au blender. "
            "C&#x27;est une recette très simple, les proportions sont "
            "toujours de 1 part de rhum + 1 part de Curaçao bleu + 1 part "
            "de crème de coco + 2 parts de jus d&#x27;ananas.</p><p>Son "
            "inventeur serait probablement Don the Beachcomber (aussi "
            "surnommé &quot;Donn Beach&quot;, Ernest Raymond Beaumont "
            "Gantt de son vrai nom - 1907-1989). Il était le fondateur de "
            "nombreux restaurants, bars et clubs.</p>",
            "ingredients": [
                "3 cl de rhum",
                "3 cl de Curaçao Bleu",
                "3 cl de crème de coco",
                "6 cl de jus d'ananas",
            ],
            "summary": "Le cocktail Blue Hawaiian : une recette tiki aussi agréable en "
            "couleur qu&#x27;en saveur.",
            "title": "Cocktail Blue Hawaiian",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à mojito</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Blue Mojito est la variante bleue du célèbre "
            "Mojito, dans lequel du Curaçao bleu vient s&#x27;inviter "
            "dans la recette.</p><p>Le Curaçao bleu apporte non seulement "
            "au cocktail une très belle couleur bleue, mais vient aussi "
            "ajouter une délicieuse saveur d&#x27;écorces d&#x27;orange "
            "aux mojitos d&#x27;origine.</p>",
            "ingredients": [
                "2 cl de rhum cubain",
                "3 cl de Curaçao Bleu",
                "2 cl de jus de citron vert",
                "5 cl d'eau gazeuse",
                "7 à 10 feuilles de menthe fraîche",
                "3 ou 4 quartiers de citron vert",
                "1 cuillère à café de sucre en poudre",
            ],
            "summary": "Le cocktail Blue Mojito : la variante au Curaçao bleu du célèbre "
            "Mojito !",
            "title": "Cocktail Blue Mojito",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (16cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Bossa nova a été nommé ainsi en honneur à la "
            "fameuse musique d&#x27;origine brésilienne.</p><p>*Il existe "
            "2 versions du cocktail Bossa Nova, une réalisée avec du jus "
            "d&#x27;ananas et l&#x27;autre avec du jus de pomme. À vous "
            "de choisir pour quel jus et donc pour quelle version vous "
            "optez...</p>",
            "ingredients": [
                "5 cl de rhum blanc",
                "2 cl de liqueur d'abricot (Apricot Brandy)",
                "2 cl de liqueur Galliano",
                "2 cl de jus de citron vert",
                "5 cl de jus d'ananas (ou jus de pomme)*",
            ],
            "summary": "Le cocktail Bossa Nova : une recette fruitée qui existe en 2 "
            "versions.",
            "title": "Cocktail Bossa Nova",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre toddy ou mug</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>La "
            "recette du Café jamaïcain peut aussi se réaliser avec du Tia "
            "Maria, une liqueur jamaïcaine à base de café rendant le "
            "cocktail plus doux.</p>",
            "ingredients": [
                "3 cl de rhum jamaïcain",
                "2 cl de sirop de sucre",
                "10 cl de café chaud",
                "Crème fouettée / chantilly",
            ],
            "summary": "Le Café jamaïcain : un cocktail chaud aux saveurs jamaïcaines.",
            "title": "Cocktail Café jamaïcain",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Caipirissima est une variante de "
            "la fameuse Caipirinha où le rhum remplace la "
            "Cachaça.</p><p>La recette de la Caipirrisima est quasiment "
            "identique à celle du Ti Punch .</p>",
            "ingredients": [
                "5 cl de rhum",
                "1 demi citron vert",
                "2 cuillères à café de sucre / cassonade",
            ],
            "summary": "Le cocktail Caipirissima : une variante de la Caipirinha.",
            "title": "Cocktail Caïpirissima",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Caribbean Breeze est une variante du Sea Breeze où "
            "le seul ingrédient commun reste le jus de canneberge.</p>",
            "ingredients": [
                "3 cl de rhum",
                "2 cl de crème de banane",
                "2 cl de Lime Cordial",
                "4 cl de jus d'ananas",
                "4 cl de jus de canneberge (cranberry)",
            ],
            "summary": "Le cocktail Caribbean Breeze : une recette à base de rhum, crème "
            "de banane et Lime Cordial.",
            "title": "Cocktail Caribbean Breeze",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul>",
            "ingredients": [
                "4,5 cl de rhum ambré",
                "1,5 cl de Whisky Bourbon",
                "1,5 cl de crème de cacao",
                "12 cl de chocolat au lait chaud",
                "6 cl de crème fouettée / chantilly",
            ],
            "summary": "Le Chocolate Vice : une recette de cocktail chaud avec des "
            "saveurs omniprésentes de cacao.",
            "title": "Cocktail Chocolate Vice",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le Citrus "
            "Cooler est un cocktail au parfum d&#x27;agrumes qui se "
            "réalise de préférence avec du jus d&#x27;orange fraîchement "
            "pressé.</p>",
            "ingredients": [
                "3 cl de rhum blanc",
                "2 cl de Cointreau",
                "6 cl de jus d'orange",
                "4 cl de lemon/lime soda (Sprite ou 7up)",
            ],
            "summary": "Le cocktail Citrus Cooler : une recette au parfum "
            "d&#x27;agrumes.",
            "title": "Cocktail Citrus Cooler",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: hurricane ou noix de coco</li>\n"
            "<li>Type&nbsp;: long drink (≥12cl)</li>\n"
            "<li>Temps&nbsp;: 10 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Coco Loco dispose de nombreuses "
            "recettes, il est réalisé différemment selon chaque région de "
            "chaque pays mais la recette qui a tendance à devenir la plus "
            "courante est celle ci-dessus.</p><p>À noter qu&#x27;une noix "
            "de coco contient environ 12cl d&#x27;eau de coco, la recette "
            "ci-dessus a donc été adaptée en fonction de cela et peut "
            "convenir en conséquence pour 2 personnes.</p><p>Voici "
            "d&#x27;autres versions :</p>",
            "ingredients": [
                "1 noix de coco",
                "3 cl de rhum",
                "3 cl de tequila",
                "3 cl de vodka",
                "8 cl de lait de coco",
                "5 cl de jus de citron vert",
            ],
            "summary": "Le Coco Loco : un cocktail exotique que vous pouvez servir dans "
            "une noix de coco.",
            "title": "Cocktail Coco Loco",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Cuba Libre aurait vu le jour "
            "juste après la seconde guerre d&#x27;indépendance qui prit "
            "fin en 1898 et qui opposait les U.S.A. à l&#x27;Espagne. "
            "Après 1898, les américains occupent toujours Cuba, et en "
            "1900 le cola y est désormais en vente. Ce serait lors de "
            "cette même année qu&#x27;un capitaine accompagné de ses "
            "troupes aurait commandé un rhum accompagné de cola et "
            "d&#x27;une tranche de citron, avant de s&#x27;écrier "
            "&quot;Por Cuba Libre !&quot;.</p><p>Cette histoire serait "
            "plus plausible mais l&#x27;origine reste toujours aussi "
            "mystérieuse et incertaine, tout comme le rhum utilisé au "
            "départ. Deux grandes marques de rhum (Bacardi et Havana "
            "Club) revendiquent bien entendu être chacune celle utilisée "
            "à l&#x27;origine.</p><p>Le Cuba Libre est parfois "
            "ironiquement appelé à Cuba &quot;mentirita&quot; ou "
            "&quot;mentiroso&quot;, signifiant &quot;petit menteur&quot; "
            "ou &quot;menteur&quot; par ceux qui ne considèrent pas Cuba "
            "comme libre, mais le Cuba Libre peut aussi être considéré "
            "comme un signe d&#x27;espoir.</p>",
            "ingredients": [
                "5 cl de rhum cubain",
                "3 ou 4 quartiers de citron vert",
                "10 cl de cola",
            ],
            "summary": "Le Cuba Libre : une recette composée de rhum, quartiers de "
            "citron et cola.",
            "title": "Cocktail Cuba Libre",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Daïquiri serait né à Cuba vers "
            "1897. Des travailleurs américains dont l&#x27;ingénieur des "
            "mines Jennings Cox exerçaient à Cuba quand un jour ils "
            "auraient décidé de concocter leur propre cocktail à "
            "l&#x27;aide des produits locaux, c&#x27;est ainsi que serait "
            "né le cocktail. Daiquiri est le nom de la plage située près "
            "de Santigo de Cuba.</p><p>Quand Robert Vermeire publie en "
            "1922 &quot;Cocktails : How to mix them&quot;, le Daïquiri "
            "est alors réalisé avec du sirop de grenadine et non pas du "
            "sirop de sucre.</p>",
            "ingredients": [
                "4 cl de rhum",
                "2 cl de jus de citron vert",
                "1 cl de sirop de sucre de canne",
            ],
            "summary": "Le cocktail Daïquiri : Né à Cuba, il porte le nom d&#x27;une "
            "plage cubaine.",
            "title": "Cocktail Daïquiri",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Dark and Stormy (écrit aussi Dark "
            "&#x27;n Stormy) est paru pour la première fois en 1990 dans "
            "le New York Times.</p><p>Le Dark and Stormy est une marque "
            "déposée par Gosling Brothers Limited, société productrice de "
            "rhum. Le cocktail se réalise donc traditionnellement avec du "
            "Gosling, plus précisément du Gosling Black Seal 80 "
            "Proof.</p>",
            "ingredients": ["6 cl de rhum ambré", "14 cl de Ginger Beer"],
            "summary": "Le Dark and Stormy : un cocktail devenu la boisson nationale des "
            "îles Bermudes.",
            "title": "Cocktail Dark and Stormy",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: flûte à champagne</li>\n"
            "<li>Type&nbsp;: long drink (≈12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Aucune "
            "information quant à l&#x27;origine de ce cocktail "
            "Devil&#x27;s Tail qui signifie en français queue du diable "
            "et dont l&#x27;originalité lui mériterait plus de "
            "célébrité.</p>",
            "ingredients": [
                "4,5 cl de rhum léger",
                "3 cl de vodka",
                "1,5 cuillère à café de liqueur d'abricot (Apricot brandy)",
                "1,5 cuillère à café de sirop de grenadine",
                "1 cuillère à café de jus de citron vert pressé et filtré",
            ],
            "summary": "Le cocktail Devil&#x27;s Tail : une recette à la couleur de la "
            "queue du diable, d&#x27;où son nom.",
            "title": "Cocktail Devil's Tail (Queue du diable)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tiki, tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Contrairement à ce que l&#x27;on peut parfois "
            "voir, le cocktail Doctor Funk n&#x27;a pas été créé par le "
            "barman Don the Beachcomber, mais par le Docteur Bernard Funk "
            "aux îles Samoa (État indépendant de Polynésie) et natif "
            "d&#x27;Allemagne.</p><p>Le cocktail Doctor Funk a été créé "
            "avant 1919 puisque cette année-là il apparaît dans le livre "
            "&quot;White Shadows in the South Seas&quot;. Dans cet "
            "ouvrage il est écrit que le cocktail (d&#x27;origine donc) "
            "est fait d&#x27;absinthe et de limonade ou lime (jus de "
            "citron vert), et qu&#x27;il est déjà bien connu dans toutes "
            "les mers du sud. On pourrait donc penser que le cocktail Dr "
            "Funk date du tout début du XXème siècle.</p><p>Quant au "
            "célèbre barman Don the Beachcomber, c&#x27;est lui qui a "
            "rendu ce cocktail célèbre en adaptant la recette à sa "
            "manière à partir des années 1930. Trader Vic participe aussi "
            "à la célébrité du Dr Funk en publiant sa recette en 1946 et "
            "1972. La recette courante est faite depuis les années 1940 "
            "avec de l&#x27;anisé (théoriquement du Pernod), du rhum brun "
            "et de l&#x27;eau gazeuse.</p>",
            "ingredients": [
                "4,5 cl de rhum ambré",
                "1,5 cl de jus de citron",
                "1,5 cl de jus de citron vert",
                "1,5 cl d'anisé (Pernod, pastis)",
                "4,5 cl d'eau gazeuse",
                "1,5 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Doctor Funk : une recette tiki qui porte le nom de "
            "son créateur.",
            "title": "Cocktail Doctor Funk",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail El Presidente a été probablement "
            "créé dans les années 1920 à La Havane à Cuba, son origine "
            "est floue. Il rendrait honneur à un président cubain, on "
            "parle de Carmen Menocal ou Gerardo Machado. Quant au "
            "créateur de ce cocktail, on parle entre autres de Eddie "
            "Woelke, barman du &quot;Jockey Club&quot; à La Havane à Cuba "
            "et potentiel créateur du cocktail classique Mary Pickford "
            ".</p>",
            "ingredients": [
                "3 cl de Rhum cubain",
                "1,5 cl de Vermouth rouge",
                "1,5 cl de Curaçao blanc",
                "1 cl de Sirop de grenadine",
            ],
            "summary": "El Presidente : un cocktail d&#x27;origine cubaine aux multiples "
            "saveurs.",
            "title": "Cocktail El Presidente",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (14,5cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "Flamingo est un cocktail fruité et rafraîchissant qui se "
            "réalise aussi en short drink avec des proportions "
            "différentes.</p>",
            "ingredients": [
                "5 cl de rhum",
                "2 cl de jus de citron vert pressé",
                "6 cl de jus d'ananas",
                "1,5 cl de sirop de grenadine",
            ],
            "summary": "Le Flamingo : une recette fruitée et désaltérante à base de "
            "rhum.",
            "title": "Cocktail Flamingo",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Fluffy Ruffles est issu du "
            "&quot;Savoy Cocktail Book&quot; de Harry Craddock publié "
            "pour la première fois en 1930, la recette invite à utiliser "
            "précisément du rhum Bacardi.</p><p>&quot;Fluffy "
            "Ruffles&quot; est un nom plutôt étrange pour un cocktail. Ce "
            "nom pourrait être tiré d&#x27;une comédie musicale de Hattie "
            "Williams qui a été lancée au Criterion Theâtre de New York à "
            "l&#x27;automne 1908, &quot;Fluffy Ruffles&quot; était aussi "
            "une composition musicale de 1919 composée par George "
            "Hamilton Green.</p>",
            "ingredients": [
                "50% de rhum Bacardi",
                "50% de vermouth rouge (Martini...)",
            ],
            "summary": "Le cocktail Fluffy Ruffles : une recette qui porte le nom "
            "d&#x27;une comédie musicale de 1908.",
            "title": "Cocktail Fluffy Ruffles",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Ceci est la recette originale et unique du "
            "cocktail Frosty Dawn telle qu&#x27;elle a été publiée par "
            "Albert Carillo en 1954 dans un journal, seules les "
            "proportions des ingrédients ont changées.</p><p>Monin et "
            "Giffard produisent du sirop de falernum, ne le remplacez pas "
            "par un autre ingrédient sans quoi ce cocktail ne serait plus "
            "un Frosty Dawn.</p>",
            "ingredients": [
                "3 cl de rhum (portoricain)",
                "1 cl de marasquin",
                "2 cl de jus d'orange",
                "1 cl de sirop de falernum",
            ],
            "summary": "Le cocktail Frosty Dawn : une recette de 1954 qui signifie "
            "&quot;aube glaciale&quot;.",
            "title": "Cocktail Frosty Dawn",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Hemingway Special est "
            "publiée pour la première fois en 1939. Après avoir changé de "
            "nom plusieurs fois, le cocktail a finalement pris le nom du "
            "célèbre écrivain Ernest Hemingway.</p><p>Selon "
            "l&#x27;histoire, le cocktail aurait vu le jour pendant la "
            "guerre civile en Espagne (1936-1939) où Hemingway décide de "
            "trouver refuge à la Havane. On raconte qu&#x27;un jour "
            "l&#x27;écrivain a décidé de se rendre dans un célèbre bar de "
            "l&#x27;île, le &quot;Floridita&quot; où travaillait "
            "Constantino Ribalaigua Vert. Hemingway, se croyant "
            "diabétique, aurait commandé un Daiquiri sans sucre. Puis les "
            "jours suivants, il aurait commandé la même chose avec une "
            "double ration de rhum, le cocktail aurait alors été nommé le "
            "&quot;Daiquiri a la Papa&quot; et &quot;Daiquiri Como "
            "Papa&quot;. Ce serait Antonio Meilan qui aurait modifié la "
            "recette en ajoutant du jus de pamplemousse, le cocktail "
            "Hemingway Special serait alors né, il est aussi appelé Papa "
            "Doble.</p>",
            "ingredients": [
                "6 cl de rhum blanc",
                "1,5 cl de marasquin",
                "1,5 cl de jus de citron vert",
                "3 cl de jus de pamplemousse",
            ],
            "summary": "Le cocktail Hemingway Special : Il est aussi appelé Papa Doble "
            "en l&#x27;honneur du célèbre écrivain.",
            "title": "Cocktail Hemingway Special",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Honey Bee se traduit par abeille en français. De "
            "couleur jaune et à base de miel les Honey Bees ont "
            "effectivement été créés en leur honneur.</p>",
            "ingredients": [
                "4 cl de rhum",
                "2 cl de jus de citron pressé et filtré",
                "1 cl de miel",
            ],
            "summary": "Le cocktail Honey Bee : une recette composée de rhum, jus de "
            "citron et de miel.",
            "title": "Cocktail Honey Bee",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre toddy ou mug</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Hot Buttered Rum (rhum chaud au beurre) "
            "est un cocktail chaud dans lequel le beurre apporte toute la "
            "richesse et la douceur de cette recette. Il remonterait à "
            "l’époque du colonialisme.</p>",
            "ingredients": [
                "6 cl de rhum ambré",
                "12 cl d'eau chaude",
                "1 cuillère à café de cassonade",
                "1 morceau de beurre non salé (1 cuillère à café)",
            ],
            "summary": "Le cocktail Hot Buttered Rum : une recette de grog beurré "
            "vraiment délicieux !",
            "title": "Cocktail Hot Buttered Rum",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Hurricane aurait vu le jour dans "
            "les années 1940 au bar Pat O&#x27;Brien situé dans le Vieux "
            "Carré Français , quartier de La Nouvelle-Orléans en "
            "Louisiane (USA). Il se dit que la recette a été inventée "
            "dans le but de se débarrasser d&#x27;un surplus de rhum. Le "
            "Hurricane est resté la boisson phare de "
            "l&#x27;établissement.</p><p>La recette a un peu évoluée avec "
            "le temps, à l&#x27;origine les Hurricanes étaient uniquement "
            "composés de rhum brun, jus de citron vert et sirop de fruit "
            "de la passion.</p>",
            "ingredients": [
                "4,5 cl de rhum ambré",
                "4 cl d'ananas",
                "4 cl de jus d'orange",
                "1,5 cl de jus de citron vert pressé et filtré",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Hurricane : une recette tiki des années 40 qui "
            "signifie ouragan.",
            "title": "Cocktail Hurricane",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: mug en cuivre</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Jamaïcan Mule est une variante du Moscow Mule où la "
            "vodka d&#x27;origine est remplacée par du rhum aux épices. "
            "Toujours aussi simple et rapide à réaliser, et toujours "
            "aussi bon et désaltérant !</p><p>Optionnellement vous pouvez "
            "ajouter quelques gouttes d&#x27;Angostura bitters.</p>",
            "ingredients": [
                "4 cl de rhum épicé",
                "2 cl de jus de citron vert",
                "9 cl de Ginger Beer",
            ],
            "summary": "Le cocktail Jamaïcan Mule : une variante du Moscow Mule avec du "
            "rhum à la place de la vodka.",
            "title": "Cocktail Jamaïcan Mule",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>rocks</li>\n"
            "<li>Type&nbsp;: long drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Jolly Roger a été créé par Robert "
            "Hess, spécialiste actuel de la mixologie, co-fondateur du "
            "&quot; Museum of the American Cocktail &quot; et auteur du "
            "livre &quot; The Essential Bartender&#x27;s Guide: How to "
            "Make Truly Great Cocktails &quot;.</p><p>Le Jolly Roger met "
            "à l&#x27;honneur le falernum, un ingrédient d&#x27;antan "
            "présent dans les cocktails tiki, de Don the Beachcomber ou "
            "Trader Vic. Le falernum se marie particulièrement bien avec "
            "les boissons à base de rhum.</p><p>Jolly Roger est le nom du "
            "célèbre pavillon pirate noir sur lequel se trouve une tête "
            "de mort et deux tibias.</p>",
            "ingredients": [
                "3 cl de rhum blanc",
                "3 cl de rhum ambré",
                "3 cl de jus d'orange",
                "1 cl de sirop de falernum",
                "1 trait d'Angostura bitters",
            ],
            "summary": "Le cocktail Jolly Roger : une recette qui porte le nom du "
            "célèbre pavillon pirate noir.",
            "title": "Cocktail Jolly Roger",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: highball ou tiki</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>Le Jungle Bird est un cocktail tiki avec un "
            "ingrédient peu commun dans cette catégorie : le Campari. La "
            "recette a vu le jour au Kuala Lumpur Hilton , un "
            "hôtel-restaurant de la ville de Kuala Lumpur en Malaisie. "
            "Les Jungle Birds ont été inventés spécialement pour "
            "l&#x27;inauguration de l&#x27;établisement en 1973.</p>",
            "ingredients": [
                "5 cl de rhum ambré",
                "2 cl de Campari",
                "5 cl de jus d'ananas",
                "2 cl de jus de citron vert",
                "1 cl de sirop de sucre",
            ],
            "summary": "Le Jungle Bird : un cocktail Tiki enrichi au bitter !",
            "title": "Cocktail Jungle Bird",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Knickerbocker apparaît pour la "
            "première fois en 1862 dans &quot;Bartenders Guide : How to "
            "mix drinks&quot; de Jerry Thomas. Les Knickerbockers sont un "
            "peu sournois, la douceur du sirop et le côté rafraîchissant "
            "apporté par le citron arrivent en effet à plutôt bien faire "
            "oublier la teneur en alcool. C&#x27;est un cocktail quasi "
            "identique au White Lion paru dans le même "
            "ouvrage.</p><p>Jerry Thomas nous invite à rajouter du sirop "
            "de framboise si le cocktail n&#x27;est pas assez doux à "
            "notre goût et nous laisse le choix du type de citron. Par "
            "ailleurs, sa recette originale de 1862 invitait à utiliser "
            "du rhum Santa Cruz.</p><p>On ne sait pas qui est "
            "l&#x27;inventeur du knickerbocker ni pourquoi ce cocktail "
            "est appelé ainsi mais il existe au moins quelques hypothèses "
            "quant à l&#x27;origine de son nom. Avant 1862 (première "
            "parution de la recette), le terme &quot;Knickerbocker&quot; "
            "apparaît en effet sous différentes formes : le Knickerbocker "
            "Boat Club créé en 1811, le Knickerbocker Base Ball Club créé "
            "en 1845, et aussi Diedrich Knickerbocker qui était un "
            "pseudonyme exploité par l&#x27;écrivain Washington Irving "
            "dès 1809.</p>",
            "ingredients": [
                "3 cl de rhum vieilli",
                "1 cl de triple sec (Curaçao)",
                "2 cl de citron (vert ou jaune selon votre préférence)",
                "1 cl de sirop de framboise",
            ],
            "summary": "Le Knickerbocker : une recette parue pour la première fois en "
            "1862 mais qui pourrait avoir 2 siècles.",
            "title": "Cocktail Knickerbocker",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: sling ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Love in the afternoon est une délicieuse recette "
            "très fruitée à tester au moins une fois, on peut trouver des "
            "recettes avec de la liqueur de fraises en plus mais cette "
            "dernière peut légèrement dénaturer les vraies saveurs de "
            "fraises fraîches déjà présentes dans le cocktail. &quot;Love "
            "in the afternoon&quot; se traduit en français par "
            "&quot;l&#x27;amour en après-midi&quot;.</p>",
            "ingredients": [
                "6 cl de rhum ambré",
                "5 cl de jus d'orange",
                "2 cl de crème de noix de coco",
                "1,5 cl de crème légère",
                "1,5 cl de sirop de sucre",
                "5 fraises",
            ],
            "summary": "Le cocktail Love in the afternoon : une recette très fruitée à "
            "goûter absolument.",
            "title": "Cocktail Love in the afternoon",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Maï-Taï a été créé en 1944 à "
            "Oakland en Californie par Victor Jules Bergeron Jr, alias "
            "&quot;Trader Vic&quot;. Il est le fondateur de la chaîne de "
            "restaurants Trader Vic&#x27;s.</p><p>Si les recettes "
            "divergent plus ou moins d&#x27;une source à l&#x27;autre, "
            "c&#x27;est d&#x27;une part parce que le créateur lui-même a "
            "modifié la recette du Mai-Tai au fil des années, et "
            "d&#x27;autre part parce que le cocktail est un peu trop fort "
            "au goût de certains barmen qui ont donc tendance à rajouter "
            "de nouveaux ingrédients sans alcool. Mais un Maï-Taï devrait "
            "toujours être composé de menthe fraîche, rhum, citron, "
            "curaçao et orgeat.</p><p>Le soir où il a créé ce cocktail, "
            "Trader Vic avait la visite de 2 amis tahitiens, Ham et "
            "Carrie Guild. Trader Vic raconte que quand Carrie a bu une "
            "gorgée elle s&#x27;est écrié &quot;Maï-Taï - Roa Ae&quot; "
            "que l&#x27;on pourrait traduire en français par "
            "extraordinairement bon. Bref, voilà pourquoi le cocktail fût "
            "baptisé &quot;Mai-Tai&quot;.</p><p>Quoiqu&#x27;il en soit, "
            "le Mai Tai est un cocktail très riche en saveurs, pour peu "
            "que l&#x27;on oublie pas le zeste de citron et surtout la "
            "menthe en décoration sans quoi un Mai-Tai n&#x27;en serait "
            "pas véritablement un.</p>",
            "ingredients": [
                "3 cl de rhum blanc",
                "3 cl de rhum ambré",
                "2 cl de triple sec (Curaçao blanc)",
                "2 cl de sirop d'orgeat",
                "2 cl de jus de citron vert pressé et filtré",
            ],
            "summary": "Le cocktail Maï-Taï : la recette la plus connue du célèbre "
            "bartender Trader Vic.",
            "title": "Cocktail Maï-Taï",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Malibu sunrise est une variante "
            "de la fameuse Tequila Sunrise que tout le monde connaît, la "
            "tequila d&#x27;origine est ici remplacée par du Malibu qui "
            "est un rhum doux aromatisé à la noix de coco.</p><p>Comme "
            "tous les cocktails de la famille &quot;Sunrise&quot; , le "
            "Malibu Sunrise doit toujours réalisé avec du jus "
            "d&#x27;orange et du sirop de grenadine, mais pas avec du jus "
            "d&#x27;ananas comme on peut parfois le voir.</p>",
            "ingredients": [
                "6 cl de Malibu Coco",
                "8 cl de jus d'orange",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Malibu Sunrise : une variante de la célèbre Tequila "
            "Sunrise.",
            "title": "Cocktail Malibu Sunrise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul>",
            "ingredients": [
                "4 cl de rhum blanc",
                "2 cl de Curaçao blanc",
                "1,5 cl de jus de citron vert pressé",
                "1,5 cl de sirop d'orgeat",
                "6 cl de lemon/lime soda (Sprite ou 7up)",
                "Quelques gouttes d'Angostura bitters",
                "1 brin de menthe fraîche",
            ],
            "summary": "Le Marama Rum Punch : un cocktail au rhum riche en saveurs.",
            "title": "Cocktail Marama Rum Punch",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: double martini</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Mary Pickford a été créé dans les "
            "années 1920 mais son inventeur n&#x27;est pas présicément "
            "connu.</p><p>Mary Pickford, star holywoodienne et femme de "
            "Douglas Fairbanks, aurait été en tournage à Cuba avec son "
            "mari et Charlie Chaplin. L&#x27;invention de ce cocktail est "
            "donc peut-être attribué à Fred Kaufman, barman à "
            "l&#x27;hôtel Sevilla de Cuba. Surnommée &quot;Little "
            "Mary&quot;, l&#x27;actrice aurait remporté l&#x27;oscar de "
            "la meilleure actrice dans &quot;Coquette&quot; en "
            "1928.</p><p>L&#x27;autre prétendent à la création de ce "
            "cocktail est Eddie Woelke, barman au Jockey Club à la Havane "
            "à Cuba et prétendent à l&#x27;invention du cocktail El "
            "Presidente .</p><p>Il s&#x27;agit ici de la version "
            "originale du cocktail Mary Pickford, la version classique "
            "intègre 1cl de marasquin et éventuellement une cerise au "
            "marasquin en décoration. Certaines recettes égalisent le "
            "rhum et le jus de pomme.</p>",
            "ingredients": [
                "4 cl de Rhum blanc",
                "7 cl de jus de pomme frais",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le Mary Pickford : un cocktail en l&#x27;honneur d&#x27;une star "
            "de cinéma hollywoodienne.",
            "title": "Cocktail Mary Pickford",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Ménage à Trois est composé comme "
            "son nom l&#x27;indique de 3 ingrédients : rhum, triple sec "
            "et crème liquide à parts égales. Les &quot;ménages à "
            "trois&quot; sont généralement réalisés avec du rhum brun "
            "mais rien n&#x27;empêche de les réaliser avec du rhum "
            "blanc.</p><p>Cette recette est connue sous ce terme français "
            "même à l&#x27;étranger, ce qui nous ferait penser que "
            "celui-ci serait d&#x27;origine française, mais sans plus "
            "d&#x27;informations malheureusement.</p>",
            "ingredients": [
                "3 cl de rhum ambré",
                "3 cl de Cointreau",
                "3 cl de crème liquide",
            ],
            "summary": "Le cocktail Ménage à Trois : une recette onctueuse au nom sans "
            "ambages.",
            "title": "Cocktail Ménage à Trois",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball 30cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><p>Une erreur courante à ne "
            "pas reproduire : les quartiers de citron ne doivent pas être "
            "pilés, seuls le sucre et la menthe sont écrasés dans du jus "
            "de citron. La menthe doit être écrasée afin d&#x27;en "
            "diffuser les arômes, la présence de quartiers de citron "
            "empêcherait ceci et rendrait votre mojito fade en menthe. Il "
            "n&#x27;y a d&#x27;ailleurs pas de quartiers de citron dans "
            "la recette originale (uniquement du jus), ils ne servent ici "
            "qu&#x27;à orner et enrichir visuellement votre "
            "mojito.</p><h2>Histoire et origine</h2><p>Le cocktail Mojito "
            "est l&#x27;un des cocktails les plus connus, et c&#x27;est "
            "aussi l&#x27;un des plus anciens. On attribue "
            "l&#x27;invention du Mojito à Francis Drake, plus connu sous "
            "le nom &quot;El Draque&quot; (le dragon). Francis Drake "
            "était un explorateur anglais qui effectua le tour du monde "
            "en 1578, il avait un repère situé à Cuba, l&#x27;île de la "
            "jeunesse (&quot;Isla de la juventud&quot;). C&#x27;est ici "
            "qu&#x27;entre 2 pillages Francis Drake dégustait "
            "l&#x27;ancêtre du Mojito qui était composé de feuilles de "
            "menthe pilées et d&#x27;aguardiente, un cocktail baptisé "
            "&quot;Drake&quot; (en hommage au capitaine de "
            "l&#x27;équipage) puis plus tard "
            "&quot;Draquecito&quot;.</p><p>Au milieu du XXème siècle, le "
            "Draquecito est rebaptisé &quot;Mojito&quot;, un mélange de "
            "&quot;mojadito&quot; signifiant humide et de "
            "&quot;mojo&quot; (sauce cubaine qui signifie &quot;jeter un "
            "sort&quot; en africain). Il est alors réalisé avec du rhum "
            "désormais raffiné par la mafia cubaine.</p><p>À Cuba, le "
            "mojito est devenu un véritable emblème national, "
            "l&#x27;écrivain Ernest Hemingway (1899-1961) joue un rôle "
            "dans la popularité du cocktail qu&#x27;il apprécie déguster "
            "dans le bar de la havane &quot;La Bodeguita del Medio&quot;. "
            "Les Mojitos ont alors commencer à s&#x27;exporter aux "
            "États-Unis puis en Europe pour enfin connaître le succès "
            "mondial qu&#x27;on lui connaît aujourd&#x27;hui.</p><p>Il "
            "est à noter que certains ajoutent un peu d&#x27;angostura "
            "bitter dans leur mojito.</p>",
            "ingredients": [
                "5 cl de rhum cubain",
                "4 cl de jus de citron vert",
                "7 à 10 feuilles de menthe verte fraîche",
                "4 ou 5 quartiers de citron vert",
                "2 cuillère à café de sucre en poudre",
                "6 cl d'eau gazeuse",
            ],
            "summary": "Le Mojito : la vraie recette originale du cocktail préféré des "
            "français !",
            "title": "Cocktail Mojito",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à mojito</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Mojito Fraise est une récente "
            "variante du célèbre Mojito dans lequel on trouve des fraises "
            "fraîches en plus.</p><p>Si vous désirez des saveurs plus "
            "prononcés de fraises, vous pouvez inclure du sirop de fraise "
            "à l&#x27;étape 2.</p>",
            "ingredients": [
                "4 cl de rhum cubain",
                "3 cl de jus de citron vert",
                "5 cl d'eau gazeuse",
                "Quelques feuilles de menthe verte",
                "Quelques fraises",
                "1 cuillère à café de sucre en poudre",
            ],
            "summary": "Le Mojito Fraise : le cocktail préféré des français dans sa "
            "version aux fraises.",
            "title": "Cocktail Mojito Fraise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à mojito</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Mojito royal est une variante du célèbre "
            "Mojito que l&#x27;on attribue à Francis Drake &quot;El "
            "Draque&quot; (le dragon). L&#x27;eau gazeuse initiale est "
            "remplacée par du champagne dans ce cocktail, d&#x27;où son "
            "nom.</p>",
            "ingredients": [],
            "summary": "Le Mojito Royal : le célèbre cocktail Mojito dans une version "
            "royale avec du champagne.",
            "title": "Cocktail Mojito Royal",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tiki, old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (11cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Navy Grog aurait été créé vers "
            "1941 par Don the Beachcomber (&quot;Donn Beach&quot;), "
            "Ernest Raymond Beaumont Gantt de son vrai nom - 1907-1989), "
            "il est l&#x27;ambassadeur des cocktails &quot;tiki&quot; "
            "dont le Navy Grog fait partie. Notez que certains barmen "
            "ajoutent à cette recette une pincée de noix de muscade "
            "râpée, d&#x27;autres réalisent les Navy Grogs au "
            "blender.</p><p>* Vous pouvez confectionner du sirop de miel "
            "en mélangeant 50% de miel et 50% d&#x27;eau chaude.</p>",
            "ingredients": [
                "2 cl de rhum blanc",
                "2 cl de rhum ambré",
                "2 cl de rhum Demerara",
                "1,5 cl de jus de citron vert filtré et pressé",
                "1,5 cl de sirop de miel *",
                "2 cl d'eau gazeuse",
            ],
            "summary": "Le Navy Grog : un cocktail tiki qui a la particularité "
            "d&#x27;être composé de 3 types de rhum.",
            "title": "Cocktail Navy Grog",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail PainKiller aurait été créé dans "
            "les années 1970 au Soggy Dollar , un bar situé à Jost Van "
            "Dyke , une île de l&#x27;archipel des îles Vierges "
            "britanniques.</p><p>La recette du Pain Killer a clairement "
            "des airs de Piña Colada, dans lequel on aurait ajouté du jus "
            "d&#x27;orange pressée.</p>",
            "ingredients": [
                "4 cl de rhum",
                "7 cl de jus d'ananas",
                "3 cl de jus d'orange",
                "3 cuillère à café de crème de coco",
            ],
            "summary": "Le PainKiller : un cocktail tiki doux et exotique à base de rhum "
            "et crème de coco.",
            "title": "Cocktail PainKiller",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le très célèbre cocktail Pina Colada a vu le "
            "jour à Cuba, il s&#x27;agissait à l&#x27;origine d&#x27;un "
            "cocktail sans alcool. La recette a totalement évoluée avec "
            "le temps, le rhum a fait son apparition dans les recettes au "
            "début des années 1920. Le coco a commencé à être intégré au "
            "milieu des années 1930, mais il faut attendre les années "
            "1950 pour voir la recette telle que nous la connaissons, "
            "c&#x27;est à dire avec le rhum, la crème de coco et le jus "
            "d&#x27;ananas réunis.</p><p>Il est à noter que les pinas "
            "coladas peuvent aussi se réaliser au shaker, et que la crème "
            "de coco peut être remplacée par du lait de "
            "coco.</p><p>L&#x27;origine réelle de la Pina Colada "
            "n&#x27;est pas exactement connue, plusieurs théories "
            "existent mais la plus crédible est la suivante. La Pina "
            "Colada aurait été inventé par Don Ramon Marrero dit "
            "&quot;Monchito&quot; le 15 aout 1954 au bar Beachcomber de "
            "l&#x27;hôtel Caribe Hilton à San Juan (Puerto Rico). Il se "
            "dit que Monchito aurait passé plus de 3 mois pour mettre au "
            "point sa pina colada, de longs mois pendant lesquels il "
            "aurait expérimenté toutes sortes d&#x27;ingrédients avec "
            "différents dosages.</p>",
            "ingredients": [
                "4 cl de rhum blanc",
                "4 cl de crème de coco",
                "7 cl de jus d'ananas",
            ],
            "summary": "La Piña Colada : un savoureux cocktail classique au rhum, crème "
            "de coco et jus d&#x27;ananas",
            "title": "Cocktail Piña Colada",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Planter&#x27;s Punch , appelé "
            "aussi &quot;Punch Planteur&quot; a été imprimé pour la "
            "première fois dans le New York Times en 1908. Dans cet "
            "article, la recette originale indiquait &quot;One of Sour, "
            "Two of Sweet, Three of Strong, Four of Weak&quot;. Comprenez "
            "1 part de citron vert, 2 parts de sucre, 3 parts de rhum "
            "ambré Myers’s, 4 parts d&#x27;eau et un trait "
            "d&#x27;Angostura bitters.</p><p>Quant à l&#x27;origine de "
            "cette recette, il existe plusieurs théories. L&#x27;une de "
            "ces théories raconte que le cocktail aurait été créé à "
            "l&#x27;hôtel &quot;Planteur&quot; de Saint-Louis. Une autre "
            "théorie raconte que ce serait la compagne d&#x27;un planteur "
            "jamaïcain qui aurait confectionné ce cocktail afin que les "
            "travailleurs se désaltèrent. Cela remonte évidemment trop "
            "loin pour en avoir une quelconque certitude.</p><p>La "
            "recette du Planter&#x27;s Punch a bien évolué et "
            "aujourd&#x27;hui les barmen s&#x27;accordent généralement à "
            "utiliser les ingrédients ci-dessus. Certains rajoutent "
            "quelques gouttes d&#x27;Angostura bitters sur le cocktail "
            "après l&#x27;avoir shaké comme dans la recette originale de "
            "1908.</p>",
            "ingredients": [
                "4 cl de rhum ambré",
                "4 cl de jus d'orange",
                "4 cl de jus d'ananas",
                "2 cl de jus de citron",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Planter&#x27;s Punch : une recette tiki fruitée et "
            "rafraîchissante aussi appelée &quot;Punch Planteur&quot;.",
            "title": "Cocktail Planter's Punch (planteur)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: technique au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Robson a été publié pour la "
            "première fois en 1930 par Harry Craddock dans son célèbre "
            "ouvrage The Savoy Cocktail Book . La recette ci-dessus est "
            "l&#x27;originale, telle qu&#x27;elle a été publiée en "
            "1930.</p><p>C&#x27;est un délicieux cocktail très équilibré, "
            "légèrement doux et rafraîchissant à la fois, avec une forte "
            "présence de rhum qui lui permet d&#x27;être un minimum "
            "dégusté puisqu&#x27;il n&#x27;est pas trop noyé.</p>",
            "ingredients": [
                "1/2 de rhum jamaïcain",
                "1/4 de jus de citron pressé et filtré",
                "1/8 de sirop de grenadine",
                "1/8 de jus d'orange",
            ],
            "summary": "Le cocktail Robson : une délicieuse recette très équilibrée, "
            "oeuvre publiée par Harry Craddock en 1930.",
            "title": "Cocktail Robson",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (≈12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Rum Swizzle apparaît dans le livre de "
            "recettes Old Mr. Boston De Luxe Official Bartender Guide "
            "(édition de 1941). C&#x27;est un cocktail emblématique des "
            "Bermudes.</p><p>La recette a un peu évoluée depuis 1941, "
            "elle était au départ composée de vieux rhum, jus de citron "
            "vert, eau gazeuse et Angostura bitters.</p><p>Certains "
            "établissements ajoutent du jus d&#x27;orange et du jus "
            "d&#x27;ananas dans le Rum Swizzle, Cocktail Mag le "
            "déconseille car l&#x27;esprit de départ est perdu, le Rum "
            "Swizzle n&#x27;en est plus tellement un dans ce "
            "cas.</p><p>Le Swizzle est le nom d&#x27;un stick servant à "
            "mélanger les ingrédients dans un verre, ce cocktail se veut "
            "donc être servi avec l&#x27;un de ces sticks swizzle .</p>",
            "ingredients": [
                "6 cl de rhum vieux",
                "2,5 cl de jus de citron vert",
                "1,5 cl de sirop de falernum (sinon grenadine)",
                "3 ou 4 traits d'Angostura bitters",
            ],
            "summary": "Le Rum Swizzle : un cocktail des Bermudes dont la particularité "
            "est son stick.",
            "title": "Cocktail Rum Swizzle",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: old fashioned ou tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>La recette du cocktail Scorpion a été publiée "
            "pour la première fois en 1947 dans l&#x27;ouvrage de Victor "
            "Bergeron, alias &quot;Trader Vic&quot;, célèbre bartender du "
            "milieu du XXème siècle et notamment créateur du "
            "Maï-Taï.</p><p>À l&#x27;origine, les Scorpions étaient des "
            "cocktails hawaïens découvert par Trader Vic lors d&#x27;une "
            "excursion dans les îles, et qu&#x27;il a beaucoup modifié au "
            "fil des années.</p>",
            "ingredients": [
                "3 cl de rhum blanc",
                "2 cl de Cognac",
                "3 cl de jus d'orange",
                "2 cl de jus de citron pressé et filtré",
                "2 cl de sirop d'orgeat",
            ],
            "summary": "Le cocktail Scorpion : une recette tiki d&#x27;origine hawaïenne "
            "adaptée par le célèbre bartender Trader Vic.",
            "title": "Cocktail Scorpion",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: à long drink</li>\n"
            "<li>Type&nbsp;: long drink (13cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sweet Poison (doux poison) a été "
            "créé par un barman du New York&#x27;s Jekyll and Hyde Club "
            ".</p><p>Avec son dégradé bleu-vert-jaune, le Sweet Poison "
            "est un cocktail qui attire le regard et la curiosité. "
            "C&#x27;est ce qui fait de ce cocktail l&#x27;une des "
            "recettes phare de l&#x27;établissement.</p>",
            "ingredients": [
                "2 cl de Rhum",
                "3 cl de Malibu Coco",
                "3 cl de Curaçao Bleu",
                "7 cl de jus d'ananas",
            ],
            "summary": "Le cocktail Sweet Poison : vous êtes prévenus vous allez "
            "l&#x27;adorer 😉",
            "title": "Cocktail Sweet Poison",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><p>OPTIONNEL : Certains "
            "préfèrent ajouter entre l&#x27;étape 3 et 4 de la glace "
            "pilée et/ou quelques ingrédients divers (vanille ou "
            "cannelle, en bâton ou en poudre).</p><h2>Histoire et "
            "origine</h2><p>Le Ti Punch est l&#x27;abréviation de Petit "
            "Punch , c&#x27;est un cocktail très simple à réaliser qui "
            "remonte au XVIIIème siècle, au temps des sarclages de cannes "
            "à sucre.</p><p>Le Ti Punch porte aussi les noms de CRS "
            "(Citron Rhum Sucre) ou SEC (parce que le rhum est pur). "
            "Selon l&#x27;heure à laquelle les hommes qui sarclaient les "
            "cannes s&#x27;octroyaient un Ti-Punch, ce dernier prenait le "
            "nom de Ti-Feu , Ti-Lagoutte , L&#x27;Heure Du Christ ou "
            "encore Pété-Pied .</p><p>Le Ti Punch est réalisé avec du "
            "rhum agricole. À la différence du rhum traditionnel qui est "
            "fabriqué uniquement à partir de la mélasse de la canne à "
            "sucre, le rhum agricole est fabriqué à partir de la canne "
            "entière.</p>",
            "ingredients": [
                "5 cl de rhum blanc agricole",
                "1 demi citron vert",
                "1 cuillère à café de sucre de canne",
            ],
            "summary": "Le Ti Punch : un cocktail antillais réalisé précisément avec du "
            "rhum agricole.",
            "title": "Cocktail Ti Punch",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>Le Voodoo est un cocktail originaire "
            "d&#x27;Angleterre plutôt récent puisqu&#x27;il date du tout "
            "début des années 2000, il aurait été créé par un certain "
            "Alex Kammerling.</p><p>C&#x27;est une recette riche en "
            "saveurs et parfaitement équilibrée, où les nombreuses "
            "saveurs fruitées se mélangent à merveille avec celles du "
            "vermouth et celles du rhum ambré, le tout adoucit par le "
            "sirop de sucre.</p>",
            "ingredients": [
                "4 cl de rhum ambré",
                "2 cl de vermouth rouge (Martini...)",
                "6 cl de jus de pomme",
                "2 cl de jus de citron pressé et filtré",
                "1 cl de sirop de sucre de canne",
            ],
            "summary": "Le cocktail Voodoo : une recette aux saveurs fruitées enrichie "
            "au vermouth.",
            "title": "Cocktail Voodoo",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail White Lion , traduit "
            "en français par &quot;lion blanc&quot;, apparaît en 1862 "
            "dans &quot;Bartenders Guide : How to mix drinks&quot; de "
            "Jerry Thomas. Le white lion est quelque peu sournois, la "
            "douceur apportée par le sucre fait oublier sa teneur en "
            "alcool.</p><p>Dans cette recette originale de 1862 Jerry "
            "Thomas appelait à utiliser du rhum Santa Cruz.</p>",
            "ingredients": [
                "3 cl de rhum vieilli",
                "2 cl de triple sec (Curaçao)",
                "1 cl de sirop de framboise",
                "1 demi citron vert",
                "1 cuillère à café de sucre en poudre",
            ],
            "summary": "Le White Lion : un cocktail doux mais offensif d&#x27;où son nom "
            "le lion blanc.",
            "title": "Cocktail White Lion",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Yellow Bird fait partie des "
            "cocktails classiques de l&#x27;IBA mais sa recette varie "
            "relativement d&#x27;une source à l&#x27;autre. Les "
            "ingrédients que l&#x27;on retrouve le plus souvent sont ceux "
            "de la présente recette : rhum, citron, liqueur Galliano, "
            "sans oublier le jus d&#x27;orange qui lui confère une "
            "couleur jaune sans laquelle le cocktail porterait bien mal "
            "son nom. Par ailleurs il n&#x27;est pas rare de trouver dans "
            "des yellow birds du jus d&#x27;ananas, liqueur d&#x27;orange "
            "ou crème de banane.</p>",
            "ingredients": [
                "4 cl de rhum",
                "2 cl de liqueur Galliano",
                "1 cl de jus de citron pressé et filtré",
                "2 cl de jus d'orange",
            ],
            "summary": "Le cocktail Yellow Bird : sous sa couleur jaune se cache un "
            "short drink très rafraîchissant.",
            "title": "Cocktail Yellow Bird",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler ou tiki</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Zombie a été créé par Don the "
            "Beachcomber en 1934. La recette a beaucoup évoluée mais "
            "l&#x27;originale telle qu&#x27;elle a été retrouvée dans les "
            "notes personnelles de Don est la suivante.</p><p>Don the "
            "Beachcomber invite d&#x27;ailleurs à servir un zombie "
            "accompagné d&#x27;une fraise.</p><p>Les zombies sont des "
            "cocktails très rafraîchissants, la douceur apportée par le "
            "sirop et le jus d&#x27;ananas font oublier "
            "l&#x27;alcool.</p>",
            "ingredients": [
                "2 cl de rhum blanc",
                "2 cl de rhum ambré",
                "2 cl de Apricot Brandy",
                "2 cl de jus de citron vert pressé et filtré",
                "5 cl de jus d'ananas",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Zombie : une recette &quot;tiki&quot; de Don the "
            "Beachcomber.",
            "title": "Cocktail Zombie",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: shooter</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail B-52 tiendrait son nom du "
            "bombardier américain &quot;B-52 Stratofortress&quot; lancé "
            "vers 1955 et qui servit notamment dans la guerre du "
            "Vietnam.</p><p>L&#x27;origine du cocktail B52 n&#x27;est pas "
            "certaine. Une première version raconte qu&#x27;il aurait été "
            "inventé en 1977 par Keg Steakhouse à Calgary en Alberta "
            "(Canada). Une seconde version raconte qu&#x27;il aurait été "
            "créé au restaurant &quot;Alice&quot; à Malibu (Califorrnie). "
            "Une troisième version dit qu&#x27;il aurait été inventé par "
            "Peter Fich, un barman de l&#x27;Hôtel Banff Springs à Banff "
            "en Alberta (Canada).</p><p>Le B-52 a donné naissance à de "
            "nombreuses variantes : B51, B53, B54, B55, B57...</p>",
            "ingredients": [
                "1/3 de Kahlua",
                "1/3 de Baileys",
                "1/3 de Cointreau",
            ],
            "summary": "Le B52 : un savoureux cocktail flambé à avaler cul-sec, et avec "
            "modération.",
            "title": "Cocktail B52",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: à "
            "étages</li>\n"
            "<li>Verre&nbsp;: à shot</li>\n"
            "<li>Type&nbsp;: shooter (6cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>La "
            "recette du Bazooka Joe peut aussi se réaliser au shaker, la "
            "faire en shooter est malgré tout bien plus présentable mais "
            "il sera plus appréciable dans ce cas de réfrigérer au "
            "préalable les ingrédients. Si vous utilisez de la crème de "
            "banane à la place d&#x27;une liqueur, il vous faudra sans "
            "doute la verser en premier, donc avant le curaçao. La crème "
            "ayant en effet théoriquement un taux de sucre supérieur, "
            "elle ne pourra donc se superposer que si elle est en "
            "première position.</p><p>Bazooka Joe est le personnage phare "
            "d&#x27;une célèbre bande dessinée appelée &quot;Bazooka "
            "Bubble gum&quot;.</p>",
            "ingredients": [
                "2 cl de Curaçao Bleu",
                "2 cl de liqueur de banane",
                "2 cl de Baileys",
            ],
            "summary": "Le cocktail Bazooka Joe : une recette qui porte le nom d&#x27;un "
            "personnage de bande dessinée.",
            "title": "Cocktail Bazooka Joe",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: shooter</li>\n"
            "<li>Type&nbsp;: short drink (≥7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Blow Job est un célèbre shooter souvent proposé "
            "dans les bars de nuit. Il est quelques fois réalisé avec de "
            "l&#x27;Amaretto (liqueur d&#x27;amande) à la place du "
            "Kahlua, un peu plus rarement avec les 3 ingrédients : Kahlua "
            "+ Baileys + Amaretto.</p><p>Le but du jeu avec les Blow Jobs "
            "est de prendre le verre avec la bouche puisque les mains "
            "sont interdites pour boire ce cocktail.</p>",
            "ingredients": [
                "1 part de Kahlua",
                "1 part de Baileys",
                "Chantilly / Crème fouettée",
            ],
            "summary": "Le cocktail Blow Job : un célèbre shooter à boire sans les "
            "mains.",
            "title": "Cocktail Blow Job",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: shooter</li>\n"
            "<li>Type&nbsp;: short drink (6cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le Blue "
            "Kamikaze est la variante du fameux cocktail Kamikaze, le "
            "curacao bleu vient ici remplacer le Cointreau "
            "d&#x27;origine. Les Blue Kamikazes ont plus tendance à être "
            "réalisés en shot qu&#x27;en verre à cocktail.</p>",
            "ingredients": [
                "2 cl de vodka",
                "2 cl de Curaçao Bleu",
                "2 cl de jus de citron vert",
            ],
            "summary": "Le Blue Kamikaze : la variante au curaçao bleu du célèbre "
            "cocktail Kamikaze.",
            "title": "Cocktail Blue Kamikaze",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: shooter</li>\n"
            "<li>Type&nbsp;: short drink (≥7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Bob Marley est un shooter rouge-jaune-vert, "
            "couleurs du drapeau rastafari. La liqueur de banane peut "
            "être remplacée par une autre liqueur jaune telle que le "
            "Galliano.</p><p>Le rhum mélangé à la liqueur de menthe verte "
            "est important, celui-ci diminue le taux de sucre de ce "
            "mélange qui lui permet ainsi de ne pas se mélanger à la "
            "liqueur de banane et d&#x27;être parfaitement superposé au "
            "dessus.</p>",
            "ingredients": [
                "1 part de sirop de grenadine",
                "1 part de liqueur de banane",
                "1/2 part de rhum",
                "1/2 part de liqueur de menthe verte (Get 27...)",
            ],
            "summary": "Le cocktail Bob Marley : un shooter aux couleurs du drapeau "
            "rasta en l&#x27;hommage du chanteur.",
            "title": "Cocktail Bob Marley",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: à shot</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Dallas Stars est réalisé avec de "
            "la crème de menthe verte et du Goldschlager cinnamon "
            "schnapps (schnapps à la cannelle).</p>",
            "ingredients": [
                "5/10 de liqueur ou crème de menthe verte (Get 27...)",
                "5/10 de schnapps à la cannelle (Goldschlager)",
            ],
            "summary": "Le cocktail Dallas Stars : un shooter avec du schnapps à la "
            "cannelle.",
            "title": "Cocktail Dallas stars",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: shooter</li>\n"
            "<li>Type&nbsp;: short drink (5cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Duck Fart semble avoir été "
            "inventé dans un bar appelé Peanut Farm (signifiant la ferme "
            "d&#x27;arachide en français) à Anchorage en Alaska.</p>",
            "ingredients": [
                "2 cl de Kahlua",
                "2 cl de Baileys",
                "1 cl de whisky canadien",
            ],
            "summary": "Le Duck Fart : un cocktail à étages très proche du B-52 qui "
            "signifie &quot;Pet de canard&quot;.",
            "title": "Cocktail Duck Fart",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: à shot</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Flaming Mexican Flag Shooter est un "
            "cocktail aux couleurs du drapeau mexicain. A la différence "
            "du Mexican Flag de base cette recette-ci intègre du rhum, "
            "plus précisément du &quot;151 proof rum&quot; (aussi appelé "
            "&quot;Overproof rum&quot;).</p>",
            "ingredients": [
                "1/4 de sirop de grenadine",
                "1/4 de liqueur ou crème de menthe verte (Get 27...)",
                "1/4 de rhum (151 Proof / Overproof)",
                "1/4 de tequila",
            ],
            "summary": "Le Flaming Mexican Flag Shooter : un cocktail aux couleurs du "
            "Mexique.",
            "title": "Cocktail Flaming Mexican Flag Shooter",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à bière</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Irish Car Bomb porte aussi le nom "
            "de &quot;Irish Carbomb&quot; ou &quot;Belfast Carbomb&quot;, "
            "c&#x27;est un cocktail dérivé du célèbre Boilermaker . Dans "
            "la série &quot;Bombs Cocktails&quot; réalisés de la même "
            "manière, il existe aussi le Jäger Bomb .</p><p>C&#x27;est "
            "une recette qui a un grand succès lors de la Saint Patrick "
            "du fait de son pouvoir un peu enivrant. Le nom du cocktail "
            "qui signifie &quot; explosion irlandaise de voitures &quot; "
            "ferait référence aux attentats qui ont eu lieu lors du "
            "Conflit Nord-Irlandais (1968-1998).</p>",
            "ingredients": [
                '1 bière "stout" (Guinness...)',
                "2 cl de Baileys",
                "2 cl de whisky irlandais (Jameson, etc.)",
            ],
            "summary": "Le cocktail Irish Car Bomb : un effet &quot;bombe&quot; en "
            "plongeant un shooter dans une bière !",
            "title": "Cocktail Irish Car Bomb",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>D&#x27;origine incertaine, le cocktail Jäger "
            "Bomb (ou Jägerbomb) est aussi appelé Perla Negra dans les "
            "pays hispaniques, à l&#x27;origine c&#x27;est de la bière "
            "qui était utilisée à la place de la boisson "
            "énergisante.</p><p>Le Jagermeister est une liqueur à base "
            "d&#x27;herbes et épices.</p>",
            "ingredients": [
                "1 shooter de Jägermeister",
                "1 verre de boisson énergisante (Red Bull...)",
            ],
            "summary": "Le Jäger Bomb : la recette d&#x27;un shooter de Jägermeister à "
            "plonger dans un verre de boisson énergisante.",
            "title": "Cocktail Jäger Bomb",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: à shot</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Mexican Flag signifie &quot;Drapeau "
            "mexicain&quot;, les couleurs du cocktail honore en effet le "
            "drapeau vert, rouge et blanc du Mexique. Il existe une "
            "version flambée de cette recette, le Flaming Mexican Flag "
            "Shooter .</p>",
            "ingredients": [
                "1/3 de sirop de grenadine",
                "1/3 de liqueur ou crème de menthe verte (Get 27...)",
                "1/3 de tequila",
            ],
            "summary": "Le cocktail Mexican Flag : une recette aux couleurs du drapeau "
            "mexicain.",
            "title": "Cocktail Mexican Flag",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: à "
            "étages</li>\n"
            "<li>Verre&nbsp;: à shooter</li>\n"
            "<li>Type&nbsp;: short drink (6cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Ce cocktail Orgasme (&quot;Orgasm&quot; à "
            "l&#x27;étranger) est la version shooter du cocktail Orgasme "
            "de base. L&#x27;esprit du cocktail doit donc absolument "
            "rester le même et inclure les mêmes ingrédients qui font "
            "tout le succès de ce cocktail : liqueur de café, liqueur "
            "d&#x27;amandes et crème de whisky Baileys.</p>",
            "ingredients": [
                "1/3 de Kahlua",
                "1/3 de Amaretto",
                "1/3 de Baileys",
            ],
            "summary": "Le cocktail Orgasme en shooter : son nom plutôt accrocheur lui "
            "vaut un grand succès à l&#x27;étranger.",
            "title": "Cocktail Shooter Orgasme",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: shooter</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Parisian Pousse café est publié "
            "en 1862 dans &quot;Bartenders guide : How to mix "
            "drinks&quot; de Jerry Thomas, il y indique juste qu&#x27;il "
            "s&#x27;agit d&#x27;un célèbre cocktail parisien.</p>",
            "ingredients": [
                "1/3 de chartreuse",
                "1/3 de kirsch",
                "1/3 de Curaçao blanc",
            ],
            "summary": "Le Parisian Pousse café : un cocktail parisien qui a la "
            "particularité de contenir de la chartreuse.",
            "title": "Cocktail Parisian Pousse café",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: cocktail à "
            "étages</li>\n"
            "<li>Verre&nbsp;: shooter</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Santina&#x27;s Pousse café "
            "apparaît en 1862 dans &quot;Bartenders guide : How to mix "
            "drinks&quot; de Jerry Thomas qui y indique que cette recette "
            "a été créée par Santina, le propriétaire du célèbre "
            "établissement espagnol Santina&#x27;s Saloon en Nouvelle "
            "Orléans.</p><p>À l&#x27;origine, les ingrédients du Santinas "
            "pousse café sont mélangés.</p>",
            "ingredients": [
                "1/3 de Cognac",
                "1/3 de marasquin",
                "1/3 de Curaçao blanc",
            ],
            "summary": "Santina&#x27;s Pousse café : un cocktail ancien originaire de la "
            "Nouvelle Orléans.",
            "title": "Cocktail Santina's Pousse café",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: à shot</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail TGV (tequila gin vodka) peut se consommer sec, avec "
            "une simple tranche de citron, ou complété d&#x27;eau "
            "gazeuse, cola ou autre soda. À consommer avec "
            "modération...</p>",
            "ingredients": ["1/3 de tequila", "1/3 de gin", "1/3 de vodka"],
            "summary": "Le TGV : le shooter qui mélange Tequila, Gin et Vodka.",
            "title": "Cocktail TGV",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Très peu d&#x27;informations circulent sur "
            "l&#x27;origine du cocktail Alamo Splash , on entend dire "
            "qu&#x27;il aurait pu être créé dans les années 1980 au "
            "Texas, voire au Mexique puisque Alamo est une ville "
            "mexicaine. En revanche, le terme &quot;splash&quot; "
            "viendrait sans doute du fait que dans la langue de "
            "Shakespear la recette d&#x27;origine indique qu&#x27;il faut "
            "verser &quot;a splash of lemon "
            "soda&quot;.</p><p>Généralement les ingrédients du cocktail "
            "Alamo Splash doivent être mélangés avant d&#x27;être "
            "reversés dans les verres mais il n&#x27;y a pas rééllement "
            "d&#x27;intérêt à ça, nous vous invitons donc ici à le "
            "réaliser directement au verre. Réaliser la recette ainsi "
            "vous permettra en plus de conserver au maximum le gaz de la "
            "limonade.</p>",
            "ingredients": [
                "4 cl de tequila",
                "3 cl de jus d'orange",
                "2 cl de jus d'ananas",
                "3 cl de limonade de citron vert",
            ],
            "summary": "Le cocktail Alamo Splash : doux et rafraîchissant, sa recette "
            "est très simple à réaliser.",
            "title": "Cocktail Alamo Splash",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: flûte à champagne</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Azteca n&#x27;a pas "
            "d&#x27;origine précise, c&#x27;est une recette unique et "
            "originale, l&#x27;un des très rares short drinks réalisés au "
            "blender avec des morceaux de fruits.</p>",
            "ingredients": [
                "3 cl de tequila",
                "1,5 cl de jus de citron vert",
                "1 demi cuillère à café de sucre en poudre",
                "1 cuillère à café d'une mangue découpée en petits morceaux",
            ],
            "summary": "Le cocktail Azteca : une recette en mémoire des aztèques.",
            "title": "Cocktail Azteca",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Batanga a été créé dans les "
            "années 1950, par Don Javier Delgado Corona, le propriétaire "
            "du bar La Capilla au Mexique.</p>",
            "ingredients": [
                "6 cl de tequila",
                "6 cl de cola",
                "1 demi citron vert",
            ],
            "summary": "Le cocktail Batanga : une recette aux airs de Cuba Libre.",
            "title": "Cocktail Batanga",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Bloody Bull est une variante du "
            "Bloody Mary, son originalité est d&#x27;être composé de "
            "bouillon de bœuf.</p><p>Il existe une deuxième recette de "
            "Bloody Bull plus complexe puisque composée de vodka, jus de "
            "tomates, bouillon de bœuf, sauce Worcestershire, jus de "
            "citron vert, tabasco, sel et poivre.</p>",
            "ingredients": [
                "4 cl de tequila",
                "5 cl de jus de tomate",
                "2 cl de jus de citron vert pressé et filtré",
                "1 cube de bouillon de bœuf en marmite",
            ],
            "summary": "Le cocktail Bloody Bull : une recette originale à base de "
            "bouillon de bœuf.",
            "title": "Cocktail Bloody Bull",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à margarita</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Blue Margarita est une variante "
            "de la célèbre Margarita créée au Mexique en 1948 par "
            "Margaret Sames.</p><p>Dans cette recette, le curaçao bleu "
            "remplace simplement le triple sec (Cointreau) "
            "d&#x27;origine.</p>",
            "ingredients": [
                "4 cl de Tequila",
                "2 cl de Curaçao Bleu",
                "2 cl de jus de citron vert pressé et filtré",
            ],
            "summary": "Le cocktail Blue Margarita : la variante bleue de la célèbre "
            "Margarita mexicaine.",
            "title": "Cocktail Blue Margarita",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Brave Bull est apparu en 1972 "
            "dans &quot;Trader Vic&#x27;s Bartender&#x27;s Guide&quot;. "
            "Les Braves Bulls sont toujours composés ni plus ni moins que "
            "de tequila et de liqueur de café.</p>",
            "ingredients": ["6 cl de tequila", "3 cl de Kahlua"],
            "summary": "Le Brave Bull : un cocktail sec fait de tequila et de Kahlua.",
            "title": "Cocktail Brave Bull",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le Cactus "
            "Banger est un cocktail doux que l&#x27;on pourrait traduire "
            "par &quot;pétard de cactus&quot;.</p><p>On pourrait penser "
            "que le nom fait référence à la tequila présente dans ce "
            "cocktail, car effectivement cette eau-de-vie est faite à "
            "partir d&#x27;agave que l&#x27;on confond souvent avec les "
            "cactus.</p>",
            "ingredients": [
                "4 cl de tequila",
                "3 cl de liqueur Galliano",
                "8 cl de jus d'orange",
            ],
            "summary": "Le Cactus Banger : un cocktail doux qui signifie &quot;pétard de "
            "cactus&quot;.",
            "title": "Cocktail Cactus Banger",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail California Dream a la célèbre "
            "particularité d&#x27;allier la tequila avec deux types de "
            "vermouth. Seule la fameuse cerise en décoration vient "
            "accompagner ces ingrédients qui laisse ce cocktail un peu "
            "sec même si les vermouths l&#x27;adoucissent.</p>",
            "ingredients": [
                "2 parts de tequila",
                "1 part de vermouth rouge (Martini...)",
                "1 part de vermouth blanc (Martini...)",
            ],
            "summary": "Le cocktail California Dream : une recette unique qui allie la "
            "tequila avec 2 types de vermouths.",
            "title": "Cocktail California Dream",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Chihuahua est une variante du Greyhound dans lequel "
            "la tequila remplace la vodka.</p>",
            "ingredients": [
                "4 cl de tequila",
                "8 cl de jus de pamplemousse pressé",
            ],
            "summary": "Le cocktail Chihuahua : la recette très simple d&#x27;une "
            "tequila pamplemousse.",
            "title": "Cocktail Chihuahua",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler ou old-fashioned</li>\n"
            "<li>Type&nbsp;: long drink (14cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Chimayo est originaire du "
            "restaurant Rancho de Chimayó situé à Chimayó au "
            "Nouveau-Mexique , il est la boisson phare de "
            "l&#x27;établissement.</p><p>La recette du Chimayo aurait été "
            "créé dès l&#x27;ouverture de cet établissement en 1965 par "
            "son propriétaire Arturo Jaramillo.</p>",
            "ingredients": [
                "4 cl de tequila",
                "2 cl de crème de cassis",
                "2 cl de jus de citron pressé et filtré",
                "4 cl de jus de pomme",
            ],
            "summary": "Le cocktail Chimayo : une recette rafraîchissante provenant du "
            "Nouveau-Mexique.",
            "title": "Cocktail Chimayo",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>Le cocktail El Diablo est apparu pour la "
            "première fois en 1956 dans l&#x27;ouvrage de Trader Vic "
            "intitulé &quot;Trader Vic’s Book of Food and Drink&quot;. "
            "Dans ce dernier ce cocktail s&#x27;appelait alors "
            "&quot;Mexican El Diablo&quot;, raccourci plus tard à "
            "&quot;El Diablo&quot;.</p><p>On suppose que ce nom a été "
            "donné à ce cocktail en raison de sa couleur rouge vive "
            "apportée par la crème de cassis.</p><p>Vous pouvez verser la "
            "crème de cassis au début comme à la fin, cela vous offre des "
            "Diablos visuellement différents, et ne trouble en rien "
            "l&#x27;équilibre de ce délicieux cocktail où les saveurs de "
            "tequila, d&#x27;agrumes, de crème fruitée et de soda au "
            "gingembre s&#x27;allient à merveille.</p>",
            "ingredients": [
                "3 cl de tequila",
                "2 cl de crème de cassis",
                "10 cl de ginger ale (Canada Dry)",
                "2 quartiers de citron vert",
            ],
            "summary": "Le cocktail El Diablo : une recette aux couleurs du diable.",
            "title": "Cocktail El Diablo",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Freddy Fudpucker est un dérivé du "
            "fameux cocktail Harvey Wallbanger où la vodka d&#x27;origine "
            "est ici remplacé par de la tequila. La recette du Freddy "
            "Fudpucker se réalise en théorie avec du jus d&#x27;orange "
            "fraîchement pressé.</p>",
            "ingredients": [
                "7 cl de tequila",
                "12 cl de jus d'orange",
                "1 cl de liqueur Galliano",
            ],
            "summary": "Le cocktail Freddy Fudpucker : une traduction à proposer ?",
            "title": "Cocktail Freddy Fudpucker",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre toddy ou mug</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>La "
            "réalisation du cocktail Hot Piper est à la portée de tous, "
            "c&#x27;est un cocktail chaud qui sera particulièrement "
            "apprécié pendant les périodes hivernales. &quot;Piper&quot; "
            "signifie joueur de pipeau / cornemuseur.</p>",
            "ingredients": [
                "6 cl de tequila",
                "1 cl de jus de citron",
                "1,5 cl de crème de cacao noir",
                "12 cl de café chaud",
            ],
            "summary": "Le cocktail Hot Piper : une recette riche en saveurs idéale "
            "pendant l&#x27;hiver.",
            "title": "Cocktail Hot Piper",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le Jungle "
            "juice est un long drink très fruité et rafraîchissant dont "
            "la recette de base est celle ci-dessus. Ce &quot;jus de la "
            "jungle&quot; peut effectivement être arrangé par "
            "l&#x27;ajout de rhum, de triple sec, lemon/lime soda...</p>",
            "ingredients": [
                "4 cl de tequila",
                "3 cl de jus d'orange",
                "3 cl de jus d'ananas",
                "3 cl de jus de canneberge (cranberry)",
                "2 cl de jus de citron vert",
            ],
            "summary": "Le Jungle Juice : un long drink très fruité et rafraîchissant à "
            "base de tequila.",
            "title": "Cocktail Jungle Juice",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à martini</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail La Bomba est un cocktail aux airs de sunrises avec "
            "son dégradé créé grâce au sirop de grenadine.</p><p>Coloré "
            "et attrayant, c&#x27;est en plus un cocktail doux et fruité "
            "qui plaira forcément à un grand nombre d&#x27;entre "
            "vous.</p>",
            "ingredients": [
                "3 cl de tequila",
                "2 cl de Cointreau",
                "3 cl de jus d'orange",
                "3 cl de jus d'ananas",
                "1 cl de sirop de grenadine",
            ],
            "summary": "La Bomba : un cocktail doux, fruité et coloré que vous allez "
            "adorer !",
            "title": "Cocktail La Bomba",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Beaucoup pensent que le cocktail Long Island "
            "Iced Tea aurait été créé dans les années 1970 par Robert "
            "Butt (alias Rosebug) qui était barman au &quot;Oak Beach "
            "Inn&quot; de Hampton Bays (Long Island, USA) mais il il "
            "semblerait que ce soit une fausse "
            "rumeur.</p><p>Effectivement dans les années 60 la recette "
            "apparaît déjà dans plusieurs ouvrages, mais malheureusement "
            "rien n&#x27;indique qui est réellement à l&#x27;origine de "
            "ce cocktail.</p>",
            "ingredients": [
                "2 cl de tequila",
                "2 cl de rhum brun",
                "2 cl de gin",
                "2 cl de vodka",
                "1 cl de Cointreau",
                "1 cl de jus de citron pressé et filtré",
                "5 cl de cola",
            ],
            "summary": "Le cocktail Long Island Iced Tea : un mélange viril... âmes "
            "sensibles s&#x27;abstenir !",
            "title": "Cocktail Long Island Iced Tea",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à margarita</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Margarita fait aujourd&#x27;hui "
            "partie des cocktails les plus connus au monde, sa "
            "composition courante est de 2 parts de tequila pour 1 part "
            "de triple sec et 1 part de jus de citron vert.</p><p>Ce "
            "serait Margaret Sames, surnommée Margarita, qui aurait créé "
            "la Margarita en 1948 à Acapulco au Mexique, en tout cas sous "
            "ce nom-là... Car effectivement des recettes avec les mêmes "
            "compositions mais sous des noms différents ont été retrouvés "
            "dans des écrits bien avant 1948, et au final "
            "l&#x27;inventeur de la recette à l&#x27;origine n&#x27;a "
            "jamais été officiellement reconnu.</p><p>Margaret Sames qui "
            "pensait donc avoir été la première à créer la recette, avait "
            "fait un mélange de ses boissons préférées : la tequila et le "
            "Cointreau. Après avoir rajouter du citron vert, elle aurait "
            "décidé d&#x27;ajouter du sel sur le rebord du verre sachant "
            "que celui-ci se mariait parfaitement avec la tequila, son "
            "cocktail baptisé Margarita est alors né.</p><p>Margaret "
            "Sames avait l&#x27;habitude de réaliser ce cocktail pour des "
            "invités tous aussi riches et célèbres que son mari, "
            "c&#x27;est ce qui aurait commencé à rendre populaire la "
            "Margarita. Ce n&#x27;est que quelques années plus tard que "
            "le cocktail aurait commencé à voir le jour dans des livres "
            "de recettes sous le nom de Margarita, pour ainsi arriver au "
            "succès qu&#x27;on lui connait aujourd&#x27;hui.</p><p>Les "
            "margaritas ont donné leur nom au verre spécifique "
            "qu&#x27;est le verre à Margarita en photo ci-dessus. Il "
            "existe plusieurs cocktails dérivés de la Margarita, ils sont "
            "aussi servis dans ce verre.</p>",
            "ingredients": [
                "4 cl de tequila",
                "2 cl de Cointreau",
                "2 cl de jus de citron vert pressé et filtré",
            ],
            "summary": "La Margarita : une recette mexicaine composée de tequila, "
            "Cointreau et jus de citron vert.",
            "title": "Cocktail Margarita",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: verre à margarita</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>La "
            "Margarita fraise est une variante de la célèbre Margarita "
            "mexicaine inventée par Margaret Sames, le verre doit donc "
            "être givré de sel et non pas de sucre.</p><p>La recette est "
            "la même que dans la version de base, on y rajoute simplement "
            "des fraises fraîches. Les Margaritas Fraise se réalisent par "
            "conséquent au blender.</p>",
            "ingredients": [
                "4 cl de tequila",
                "2 cl de Cointreau",
                "1 cl de jus de citron vert",
                "5 fraises",
            ],
            "summary": "Le cocktail Margarita Fraise : la célèbre recette mexicaine dans "
            "une version à la fraise.",
            "title": "Cocktail Margarita Fraise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tasse en cuivre</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Mexican Mule est une variante du célèbre Moscow "
            "mule , la tequila vient ici remplacer la vodka "
            "d&#x27;origine.</p><p>Il existe une variante de cette "
            "variante : le Spicy Mexican Mule , dans lequel du piment "
            "&quot;jalapeño&quot; vient s&#x27;inviter. Il suffit alors "
            "de piler 2 ou 3 rondelles de ce piment dans le verre avant "
            "d&#x27;y insérer les ingrédients ci-dessus.</p>",
            "ingredients": [
                "4 cl de tequila",
                "2 cl de jus de citron vert",
                "9 cl de Ginger Beer",
            ],
            "summary": "Le Mexican Mule : la variante à la tequila du célèbre Moscow "
            "Mule.",
            "title": "Cocktail Mexican Mule",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Paloma est un cocktail bien connu au "
            "Mexique puisqu&#x27;il est devenu le cocktail préféré des "
            "mexicains, devant même la Margarita.</p><p>Il s&#x27;agit de "
            "Don Javier Delgado Corona du restaurant La Capilla à Mexico "
            "qui serait à l&#x27;origine de cette recette.</p><p>Les "
            "Palomas sont des cocktails très rafraîchissants dont le nom "
            "signifie &quot;colombe&quot; en espagnol.</p>",
            "ingredients": [
                "4,5 cl de tequila",
                "2 cl de jus de citron vert",
                "1 cl de sirop de sucre",
                "4,5 cl de jus de pamplemousse",
                "3 cl d'eau gazeuse",
            ],
            "summary": "Le Paloma : le cocktail préféré des mexicains, devant même la "
            "Margarita !",
            "title": "Cocktail Paloma",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Vidéo</h2><h2>Histoire et "
            "origine</h2><p>Le cocktail Tequila sunrise fait partie des "
            "cocktails les plus connus et appréciés. Cette fameuse "
            "&quot;Tequila orange grenadine&quot; s&#x27;effectuant "
            "directement au verre et ses ingrédients étant basiques, sa "
            "réalisation est à la portée de tous. Les couleurs chaudes de "
            "ce long drink que nous dégusterions bien sur une terrasse en "
            "plein été nous inspirent un coucher ou un lever de soleil, "
            "et à vrai dire ce n&#x27;est peut-être pas un "
            "hasard.</p><p>L&#x27;histoire raconte que ce cocktail aurait "
            "été créé en 1976 par un barman de San Francisco. Retrouvé "
            "ivre par son patron après être resté toute une nuit dans le "
            "bar où il travaillait, ce barman aurait pretexté être resté "
            "pour créer une recette reproduisant le lever du soleil. Il "
            "se serait alors justifié en exécutant cette fameuse Tequila "
            "Sunrise.</p><p>Une autre version indique que l&#x27;origine "
            "du cocktail Tequila Sunrise remonte à la fin des années 30 "
            "et que ce serait Gene Sulit, barman au Arizona Biltmore "
            "Hôtel à Phoenix, qui l&#x27;aurait créé à la demande "
            "d&#x27;un client qui désirait un cocktail "
            "rafraîchissant.</p><p>La Tequila Sunrise est "
            "aujourd&#x27;hui devenue tellement célèbre qu&#x27;elle a "
            "créé une nouvelle famille de cocktails : les "
            "&quot;sunrises&quot;. Effectivement n&#x27;importe quel "
            "spiritueux devient &quot;sunrise&quot; lorsqu&#x27;on lui "
            "ajoute du jus d&#x27;orange et du sirop de "
            "grenadine.</p><p>Il est à noter qu&#x27;en fonction de la "
            "qualité de votre sirop, il sera peut-être nécessaire de "
            "remuer délicatement avec une cuillère à mélange pour créer "
            "un dégradé plus régulier.</p>",
            "ingredients": [
                "4,5 cl de tequila",
                "9 cl de jus d'orange",
                "1,5 cl de sirop de grenadine",
            ],
            "summary": "Tequila sunrise : c&#x27;est le lever du soleil qui aurait "
            "inspiré l&#x27;inventeur de ce cocktail à étage.",
            "title": "Cocktail Tequila sunrise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Tequini , appelé aussi Tequila "
            "Martini , est une variante du célèbre Dry Martini , la "
            "tequila remplace ici le gin. Tout comme le Dry Martini donc, "
            "la Vodkatini se réalisera au verre à mélange avec une olive "
            "en décoration, symbole du Dry Martini.</p>",
            "ingredients": [
                "6 cl de tequila",
                "2 cl de vermouth blanc (Martini, Noilly Prat...)",
            ],
            "summary": "Tequini : un cocktail aussi connu sous le nom de Tequila "
            "Martini.",
            "title": "Cocktail Tequini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail TNT signifie Tequila N&#x27; Tonic, c&#x27;est une "
            "recette simple qu&#x27;appécieront les amateurs de "
            "tequila.</p><p>Certains mixologistes remplacent les "
            "quartiers de citron vert par du jus de citron, dans quel cas "
            "2 cl suffisent. Et vous comment le préferez-vous ?</p>",
            "ingredients": [
                "5 cl de tequila",
                "10 cl de tonic (Schweppes)",
                "2 quartiers de citron vert",
            ],
            "summary": "Le cocktail TNT : une recette qui signifie Tequila N&#x27; "
            "Tonic.",
            "title": "Cocktail TNT",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (18cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Tomahawk est un cocktail doux et fruité dont la "
            "recette est toujours réalisée avec de la tequila, du triple "
            "sec, du jus d&#x27;ananas et du jus de canneberge "
            "(cranberry).</p>",
            "ingredients": [
                "3 cl de tequila",
                "3 cl de triple sec (Curaçao blanc)",
                "6 cl de jus de canneberge",
                "6 cl de jus d'ananas",
            ],
            "summary": "Le cocktail Tomahawk : une recette douce et fruitée à base de "
            "tequila et Curaçao.",
            "title": "Cocktail Tomahawk",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à margarita</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Tommy&#x27;s Margarita a été créé "
            "par Julio Bermejo dans les années 1980. Julio est le fils de "
            "Tommy Bermejo qui a fondé en 1965 avec son épouse Elmy le "
            "restaurant &quot;Tommy’s Mexican Restaurant&quot; à San "
            "Francisco, un établissement spécialisé dans la tequila qui "
            "propose près de 300 variétés. La recette de la Tommy&#x27;s "
            "Margarita fait désormais partie des cocktails classiques "
            "modernes de l&#x27;IBA.</p><p>Le cocktail est considéré "
            "comme une variante du célèbre cocktail Margarita qui est un "
            "véritable symbole au Mexique, le triple sec original est "
            "remplacé ici par le sirop d&#x27;agave. Le sirop "
            "d&#x27;agave est aussi appelé &quot;nectar "
            "d&#x27;agave&quot; et il a la consistance du miel. Ne le "
            "cherchez donc pas au rayon des sirops mais plutôt au rayon "
            "miel, diététique ou bio, sinon dans un magasin spécialisé "
            "dans ce genre de produit.</p>",
            "ingredients": [
                "5 cl de tequila",
                "2 cl de jus de citron vert pressé et filtré",
                "1 cl de sirop d'agave",
            ],
            "summary": "Le cocktail Tommy&#x27;s Margarita : une version plus douce de "
            "la célèbre Margarita.",
            "title": "Cocktail Tommy's Margarita",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Vampiro est publié en 1972 dans "
            "&quot;Trader Vic&#x27;s Bartender&#x27;s Guide&quot; qui "
            "invite à l&#x27;origine à verser directement dans un verre "
            "givré de sel fin la tequila, le jus de citron vert pressé et "
            "de la sangrita.</p>",
            "ingredients": [
                "6 cl de tequila",
                "3 cl de jus de citron vert pressé et filtré",
                "3 cl de jus d'orange",
                "6 cl de jus de tomate",
                "3 ou 4 gouttes de Tabasco",
                "2 ou 3 traits de sauce Worchestershire",
                "1 demi-pincée de sel",
            ],
            "summary": "Le Vampiro : un cocktail vampirique avec une couleur rouge sang "
            "et une saveur pimentée.",
            "title": "Cocktail Vampiro",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Golden Dream se consomme en "
            "digestif, l&#x27;origine de cette recette n&#x27;est pas "
            "connue mais ses multiples saveurs et sa petite touche de "
            "crème légère rendent ce cocktail assez doux et "
            "onctueux.</p><p>Les Golden Dreams sont d&#x27;ailleurs "
            "encore meilleurs avec du jus d&#x27;orange fraîchement "
            "pressé !</p>",
            "ingredients": [
                "2 cl de Cointreau",
                "2 cl de liqueur Galliano",
                "2 cl de jus d'orange",
                "1 cl de crème légère",
            ],
            "summary": "Le Golden Dream : Un doux cocktail aux saveurs d&#x27;orange à "
            "déguster après le repas.",
            "title": "Cocktail Golden Dream",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Tampico aurait été créé au cours "
            "des années 1960 par Rudolf Slavick, barman de l&#x27;hôtel "
            "Georges V et chevallier de la légion d&#x27;honneur.</p>",
            "ingredients": [
                "2 cl de Cointreau",
                "3 cl de Campari",
                "2 cl de jus de citron pressé",
                "5 cl de tonic (Schweppes)",
            ],
            "summary": "Le Tampico : un cocktail d&#x27;origine française qui mélange "
            "finement l&#x27;amertume avec l&#x27;acidité.",
            "title": "Cocktail Tampico",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail After Sex est une variante du Screwdriver dans "
            "lequel on rajoute de la crème de banane.</p><p>Pour un After "
            "Sex encore plus savoureux, vous pouvez utiliser du jus "
            "d&#x27;orange fraîchement pressé.</p>",
            "ingredients": [
                "4 cl de vodka",
                "2 cl de crème de banane",
                "9 cl de jus d'orange",
            ],
            "summary": "Le cocktail After Sex : la recette d&#x27;une vodka-orange avec "
            "de la crème de banane.",
            "title": "Cocktail After Sex",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à martini</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Apple Martini est aussi appelé "
            "Appletini , c&#x27;est une recette de la famille des "
            "martinis qui aurait été inventé en 1994 au Lola&#x27;s , un "
            "bar de Los Angeles.</p>",
            "ingredients": [
                "4 cl de vodka",
                "2 cl de liqueur de pomme (Manzana, Apple Shnapps...)",
                "2 cl de jus de pomme (optionnel)",
            ],
            "summary": "Le cocktail Apple Martini : une recette aussi connue sous le nom "
            "de Appletini.",
            "title": "Cocktail Apple Martini (Appletini)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old-fashioned ou verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>L&#x27;origine du cocktail Astronaut remonte "
            "au tout début des années 1960, puisqu&#x27;en 1961 le "
            "Washington Post écrit dans un article que deux nouvelles "
            "boissons de l&#x27;ère spatiale ont été servies à Londres, "
            "l&#x27;astronaut et le cosmonaut. Malheureusement peu "
            "d&#x27;informations supplémentaires sur ce cocktail qui "
            "quoiqu&#x27;il en soit reste plutôt sec, d&#x27;ailleurs "
            "s&#x27;il l&#x27;est trop pour vous, n&#x27;hésitez pas à "
            "rajouter du jus de citron.</p>",
            "ingredients": [
                "2,5 cl de vodka",
                "2,5 cl de rhum",
                "1 cl de jus de citron pressé et filtré",
                "1 cl de purée de fruit de la passion",
            ],
            "summary": "Le cocktail Astronaut : une recette pour vous faire décoller...",
            "title": "Cocktail Astronaut",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Balalaïka/Troïka a la même "
            "composition que le cocktail Kamikaze, à la différence près "
            "que l&#x27;on utilise très précisément dans cette recette du "
            "Cointreau quand le Kamikaze vous offre le choix du triple "
            "sec.</p><p>Le Balalaika / Troika aurait été créé selon "
            "certains par Alain Nevers à Nantes, en tout état de cause la "
            "recette serait apparu pour la première fois en 1977 dans "
            "Jones&#x27; Complete Barguide de Stanley Jones.</p>",
            "ingredients": [
                "4 cl de vodka",
                "3 cl de Cointreau",
                "3 cl de jus de citron jaune pressé et filtré",
            ],
            "summary": "Le cocktail Balalaïka Troïka : une version très précise du "
            "cocktail kamikaze.",
            "title": "Cocktail Balalaïka Troïka",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Ballet Russe n&#x27;a pas "
            "d&#x27;origine connue, mais portant internationalement ce "
            "nom francisé, il aurait pu être créé en France en "
            "l&#x27;honneur de la compagnie &quot;Les ballets "
            "russes&quot; créée en 1907 par Serge de Diaghilev et dont la "
            "tournée a commencée à Paris.</p><p>À l&#x27;occasion "
            "d&#x27;une Saint-Valentin, le restaurant new-yorkais "
            "&quot;Russian Tea Room&quot; a décidé de mettre à "
            "l&#x27;honneur une série de cocktails via le mixologiste "
            "Brice Moldovan qui a redeveloppé des classiques comme le "
            "Ballet russe ainsi que le &quot;1917&quot; ou le &quot;Paris "
            "to Moscow&quot;. La version du Ballet Russe repensée par "
            "Brice Moldovan est réalisée avec de la Grey Goose Orange, de "
            "l&#x27;Absolut Citron, du jus de Litchi, du Grand Marnier et "
            "un trait de grenadine... une recette sous le nom de Ballet "
            "Russe mais en fait complétement différente.</p>",
            "ingredients": [
                "4 cl de vodka",
                "2 cl de crème de cassis",
                "1 cl de citron vert pressé et filtré",
            ],
            "summary": "Le cocktail Ballet Russe : quelques notes de douceur et de "
            "fraicheur dans une recette qui reste de caractère.",
            "title": "Cocktail Ballet Russe",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Bay Breeze est une variante du "
            "Sea Breeze où le jus d&#x27;orange remplace le jus de "
            "pamplemousse d&#x27;origine.</p>",
            "ingredients": [
                "5 cl de vodka",
                "6 cl de jus d'orange",
                "4 cl de jus de canneberge (cranberry)",
            ],
            "summary": "Le cocktail Bay Breeze : une recette signifiant brise sur la "
            "baie.",
            "title": "Cocktail Bay Breeze",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à bière</li>\n"
            "<li>Type&nbsp;: long drink (25cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Beer Buster est une recette simple que chacun "
            "pourra réaliser chez soi, la technique de réalisation et les "
            "ingrédients sont en effet à la portée de tous.</p>",
            "ingredients": ["5 cl de vodka", "20 cl de bière", "Tabasco"],
            "summary": "Le cocktail Beer Buster : la recette qui mélange vodka et bière.",
            "title": "Cocktail Beer Buster",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Doux et "
            "fruité, le Bikini martini a la particularité d&#x27;être "
            "l&#x27;une des rares recettes de la famille des Martinis à "
            "posséder un dégradé.</p>",
            "ingredients": [
                "2 cl de vodka",
                "2 cl de Malibu Coco",
                "4 cl de jus d'ananas",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Bikini Martini : l&#x27;une des rares recettes de la "
            "famille des Martinis à avoir un dégradé.",
            "title": "Cocktail Bikini Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Black Russian fait partie des "
            "&quot;after-dinners&quot;, c&#x27;est un digestif raffiné à "
            "condition de respecter le bon dosage : 5 parts de vodka pour "
            "2 parts de liqueur de café (Kalhua...).</p><p>Le cocktail "
            "Black Russian aurait vu le jour en 1949 grâce à Gustave "
            "Tops, un barman belge œuvrant alors à l&#x27;Hôtel Métropôle "
            "à Bruxelles. Il aurait créé le Black Russian en "
            "l&#x27;honneur de Perle Reid Mesta, un socialiste américain "
            "qui fût l&#x27;ambassadeur des États-Unis au Luxembourg de "
            "1949 à 1953. L&#x27;origine du nom &quot;Black Russian&quot; "
            "(russe noir en français) rendrait hommage à la sombre "
            "période de la guerre froide contre l&#x27;Union "
            "soviétique.</p><p>Le dérivé le plus connu du Black Russian "
            "est le cocktail White russian qui contient de la crème "
            "légère en plus. Le Black russian a aussi donné naissance au "
            "cocktail Tall Black russian dans lequel on rajoute "
            "simplement du cola.</p>",
            "ingredients": [
                "5 cl de vodka",
                "2 cl de liqueur de café (Kalhua...)",
            ],
            "summary": "Le cocktail Black Russian : un digestif simple mais efficient "
            "signifiant &quot;russe noir&quot;.",
            "title": "Cocktail Black russian",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Bloody Mary fait aujourd&#x27;hui "
            "partie des grands classiques, l&#x27;originalité et la "
            "complexité de ce cocktail à base de jus de tomates lui vaut "
            "effectivement un grand succès.</p><p>Le cocktail Bloody Mary "
            "aurait été créé en 1921 par Fernand Petiot, barman au "
            "Harry&#x27;s Bar à Paris. A cette époque, sa recette ne "
            "comportait que de la vodka et du jus de tomates et se "
            "nommait &quot;Bucket of blood&quot; (godet de sang). En "
            "1934, Fernand Petiot serait parti au King Cole Bar à New "
            "York en y amenant sa fameuse création. Ce n&#x27;est "
            "qu&#x27;à ce moment qu&#x27;il aurait décidé d&#x27;ajouter "
            "à sa recette de base le tabasco, la sauce worcestershire, le "
            "poivre et le jus de citron. Le doute repose sur l&#x27;ajout "
            "de sel de céleri par Fernand Petiot. Dans ce nouvel "
            "établissement, il aurait été forcé de remplacer la vodka par "
            "du gin, et de changer le nom &quot;Bloody Mary&quot; par "
            "&quot;Red Snapper&quot;.</p><p>Bloody Mary signifie en "
            "français &quot;Marie sanglante&quot; et l&#x27;origine du "
            "nom donné à ce cocktail reste encore à débattre, mais on "
            "pense qu&#x27;il rend hommage à Marie Tudor (ou Marie 1ère "
            "d&#x27;Agleterre), fille d&#x27;Henri VIII, qui régna de "
            "1553 à 1558.</p><p>L&#x27;origine du cocktail Bloody Mary "
            "connaît d&#x27;autres versions parmi lesquelles on dit que "
            "ce cocktail aurait pu être inventé par Bertin, chef barman "
            "du Ritz à Paris, pour la femme d&#x27;Ernest Hemingway "
            "qu&#x27;il surnommait Bloody Mary.</p><p>On dit que le "
            "cocktail Bloody Mary aurait des vertus contre la gueule de "
            "bois, la véracité de cette rumeur est bien loin de faire "
            "l&#x27;unanimité, pour beaucoup il est en effet dûr de "
            "croire que la gueule de bois puisse être guérie avec de "
            "l&#x27;alcool.</p><h2>La légende Bloody Mary</h2><p>Bloody "
            "Mary est aussi le nom d&#x27;une légende selon laquelle "
            "chacun d&#x27;entre vous pourrait faire apparaître une "
            "entité au visage ensanglanté dans un miroir. Plusieurs "
            "façons existeraient pour faire apparaître cette entité, la "
            "plus connue est la suivante.</p><p>Dans une pièce plongée "
            "dans le noir en pleine nuit (certains disent minuit), il "
            "faudrait se placer devant un miroir avec juste 2 cierges "
            "allumées de chaque côté du miroir. Il faudrait alors tourner "
            "13 fois sur vous-même, et à chaque fois que vous passez "
            "devant le miroir il vous faudrait regarder votre reflet et "
            "prononcer &quot;Bloody Mary&quot; et en le criant de plus en "
            "plus fort à chaque tour. L&#x27;entité apparaîtrait alors "
            "dans le miroir, le visage ensanglanté et vous fixant avec "
            "insistance. On raconte que si vous rajoutez &quot;I killed "
            "your baby&quot; (j&#x27;ai tué ton enfant) lors de la "
            "treizième fois, l&#x27;entité vous attaquerait "
            "violemment.</p><p>On dit aussi qu&#x27;en remplaçant "
            "&quot;Bloody Mary&quot; par &quot;Hell Mary&quot;, ce serait "
            "Satan qui apparaîtrait dans le miroir.</p><p>Plusieurs "
            "personnes auraient tenter de faire taire cette légende en "
            "l&#x27;essayant... mais sans y revenir indemne. Une fille se "
            "serait retrouvé la hanche cassée en sortant de sa salle de "
            "bain après avoir exécuté le rituel en disant &quot;Bloody "
            "Mary, je ne crois pas en toi&quot;, et une autre femme "
            "aurait été retrouvé poignardée le lendemain de son "
            "rituel.</p><p>L&#x27;origine de cette légende reste "
            "inconnue. Beaucoup pensent que ce serait la Vierge Marie qui "
            "viendrait vous mettre en garde. D&#x27;autres évoquent le "
            "retour d&#x27;une sorcière qui avait été brûlée vive pour "
            "avoir pratiqué de la magie noire et qui hanterait désormais "
            "les miroirs en punissant les curieux qui "
            "l&#x27;appelleraient. Enfin, certains évoquent une femme qui "
            "aurait péri dans un accident de voiture avec son fils et qui "
            "vivrait dans les miroirs pour venger la mort de son "
            "fils.</p><p>La légende de Bloody Mary est assez connue aux "
            "États-Unis, Janet Langlois en a même écrit un essai en 1978, "
            "et le film d&#x27;horreur &quot;Candyman&quot; a aussi été "
            "réalisé à partir de cette légende.</p><h2>Variantes</h2>",
            "ingredients": [
                "Quelques gouttes de tabasco",
                "1 cl de sauce worcestershire",
                "2 cl de jus de citron pressé et filtré",
                "6 cl de vodka",
                "11 cl de jus de tomate",
            ],
            "summary": "Le cocktail Bloody Mary : une recette originale qui porte le nom "
            "d&#x27;une légende redoutable.",
            "title": "Cocktail Bloody Mary",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: sling ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Aucune information quant à l&#x27;origine de "
            "ce cocktail Blue Bayou , les bayous sont des étendues "
            "d&#x27;eau en Louisiane. Toujours est-il que cette recette "
            "nous offre une agréable couleur bleu/vert et des saveurs "
            "fruitées, idéales par une chaude journée d&#x27;été !</p>",
            "ingredients": [
                "3 cl de vodka",
                "2 cl de Curaçao Bleu",
                "5 cl de jus d'ananas",
                "5 cl de jus de pamplemousse",
            ],
            "summary": "Le cocktail Blue Bayou : une recette fraîche pourvue d&#x27;une "
            "couleur très attrayante.",
            "title": "Cocktail Blue Bayou",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Blue lagoon (lagon bleu en français) est "
            "le cocktail à base de curaçao bleu le plus connu, sa teneur "
            "en alcool s&#x27;élève à 30°. Le cocktail Blue Lagoon a été "
            "créé en 1960 au Harry&#x27;s Bar à Paris par Andy Mac "
            "Elhone. Andy Mac Elhone est le fils de Harry, créateur du "
            "Harry&#x27;s New York Bar à Paris.</p><p>Le Blue lagoon est "
            "un derivé du Balalaïka Troïka dans lequel le cointreau "
            "remplace le curaçao bleu ici présent.</p>",
            "ingredients": [
                "4 cl de Vodka",
                "2 cl de Curaçao Bleu",
                "1 cl de jus de citron jaune pressé et filtré",
            ],
            "summary": "Le Blue Lagoon : la recette d&#x27;un cocktail bleu à base de "
            "vodka et curaçao bleu.",
            "title": "Cocktail Blue lagoon",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Bullfrog (ou Bull Frog) n&#x27;a pas d&#x27;origine "
            "connue, il se veut en tout cas très désaltérant grâce à une "
            "grande présence de citron. Pour plus de simplicité, il vous "
            "est tout à fait possible de réaliser vos bullfrogs avec "
            "simplement de la vodka et de la limonade de citron vert qui "
            "doit en théorie pouvoir se trouver en grande "
            "surface.</p><p>Le Bullfrog n&#x27;a en tout cas pas de "
            "recette &quot;type&quot; mais la recette de base comporte au "
            "moins de la vodka, de la limonade et du citron vert (en jus "
            "pressé, en tranches ou lime cordial), d&#x27;autres recettes "
            "de Bullfrog existent comportant en plus du triple sec, "
            "vermouth ou autre ingrédient.</p>",
            "ingredients": [
                "5 cl de vodka",
                "7 cl de limonade",
                "3 ou 4 demi-tranches de citron vert",
            ],
            "summary": "Le Bullfrog : un cocktail très rafraîchissant grâce à des "
            "saveurs omniprésentes de citron.",
            "title": "Cocktail Bullfrog",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Caipiroska est une variante de la "
            "Caipirinha, le cachaça d&#x27;origine est ici remplacée par "
            "de la vodka.</p>",
            "ingredients": [
                "5 cl de vodka",
                "1/2 citron vert",
                "2 cuillères à café de sucre ou cassonade",
            ],
            "summary": "Le cocktail Caipiroska : une variante de la Caipirinha où la "
            "vodka remplace le cachaça.",
            "title": "Cocktail Caïpiroska",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Cape Codder est aussi appelé Cape "
            "Cod, c&#x27;est une recette simple uniquement composée de "
            "vodka et jus de canneberge (cranberry).</p><p>Le Cape Codder "
            "aurait été créée vers 1945 par la société Ocean Spray "
            "Cranberry pour commercialiser leur jus de canneberge. À "
            "cette époque ce cocktail s&#x27;appelait le Red Devil , ce "
            "n&#x27;est que plus tard dans les années 1960 qu&#x27;il "
            "prend le nom de Cape Codder ou Cape Cod .</p>",
            "ingredients": [
                "4 cl de vodka",
                "8 cl de jus de canneberge (cranberry)",
            ],
            "summary": "Le cocktail Cape Codder : une &quot;vodka cranberry&quot; aussi "
            "appelée Cape Cod .",
            "title": "Cocktail Cape Codder",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Chi Chi est une variante de la "
            "fameuse Pina Colada, la vodka remplace le rhum initial. La "
            "recette du Chi-Chi est apparue en 1972 dans &quot;Trader "
            "Vic&#x27;s Bartender&#x27;s Guide&quot;.</p>",
            "ingredients": [
                "4,5 cl de vodka",
                "3,5 cl de crème de coco",
                "7 cl de jus d'ananas",
            ],
            "summary": "Le cocktail Chi Chi : une variante de la célèbre Pina Colada.",
            "title": "Cocktail Chi Chi",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "blender</li>\n"
            "<li>Verre&nbsp;: sling ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>L&#x27;origine précise du cocktail Chiquita "
            "n&#x27;est pas connue, même si on pourrait trouver un début "
            "de réponse dans une entreprise espagnole produisant des "
            "bananes et portant ce nom. Toujours est-il que les chiquitas "
            "sont des cocktails dont la recette nous offre une panoplie "
            "de saveurs et qui se doit d&#x27;être essayée.</p>",
            "ingredients": [
                "6 cl de vodka",
                "1,5 cl de liqueur de banane",
                "1/2 banane coupée en rondelles",
                "1,5 cl de jus de citron vert pressé et filtré",
                "1 cl de sirop d'orgeat",
            ],
            "summary": "Le cocktail Chiquita : une recette aux saveurs prédominantes de "
            "banane.",
            "title": "Cocktail Chiquita",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Chocolate Martini est aussi "
            "appelé Chocolatini .</p><p>Comme tous les cocktails de la "
            "famille des &quot;martinis&quot;, il est uniquement réalisé "
            "avec une base de vodka.</p>",
            "ingredients": ["4 cl de vodka", "3 cl de crème de cacao"],
            "summary": "Vous aimez le chocolat ?? Le Chocolate Martini est là !!",
            "title": "Cocktail Chocolate Martini (Chocolatini)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: double verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (≥7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Aucune "
            "information sur l&#x27;histoire du cocktail Climax qui "
            "signifie en français orgasme ou point culminant, que "
            "l&#x27;on pourrait idéalement traduire par Everest dans "
            "notre langue. Découvrez en vidéo ci-dessous la recette du "
            "Climax réalisée au Boston Shaker.</p>",
            "ingredients": [
                "1 cl de vodka",
                "1 cl de Amaretto",
                "1 cl de crème de cacao blanc (Marie Brizard...)",
                "1 cl de Cointreau",
                "1 cl de liqueur de banane",
                "2 cl de crème épaisse",
            ],
            "summary": "Le Climax : l&#x27;Everest dans cette recette onctueuse et "
            "savoureuse.",
            "title": "Cocktail Climax",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Comme pour tous les grands classiques, il est "
            "impossible de définir avec certitude l&#x27;origine du "
            "cocktail Cosmopolitan . En 1934, &quot;American Traveling "
            "Mixologist&quot; publient le livre &quot;Pioneers of Mixing "
            "Gin at Elite Bars 1903-1933&quot; dans lequel on trouve la "
            "première recette du cosmopolitan avec du gin à la place de "
            "la vodka.</p><p>Les cosmopolitans pourraient aussi être "
            "attribués à Cherry Cook, barmaid à Miami. En 1985 ou 1986, "
            "elle aurait réalisé un cocktail féminin mais avec du "
            "rose&#x27;s lime juice à la place du jus de "
            "canneberge.</p><p>Avec les ingrédients que nous le "
            "connaissons aujourd&#x27;hui, le cosmopolitan aurait été "
            "servi dès 1987 par John Caine, propriétaire d&#x27;un bar à "
            "San Francisco. On parle aussi de Toby Cecchini, barman à New "
            "York, qui aurait remplacé en 1987 ou 1988 les ingrédients de "
            "Cheryl Cook par ceux que nous connaissons "
            "aujourd&#x27;hui.</p><p>Déjà célèbre en Amérique, le "
            "cosmopolitan a vu sa popularité s&#x27;élargir grâce à la "
            "diffusion du feuilleton &quot;Sex and the city&quot;, dans "
            "lequel on peut voir à de nombreuses reprises les héroïnes "
            "siroter des cosmopolitans.</p>",
            "ingredients": [
                "3 cl de vodka",
                "2 cl de Cointreau",
                "1 cl de jus de citron vert pressé et filtré",
                "1 cl de jus de canneberge (cranberry)",
            ],
            "summary": "Le Cosmopolitan : le cocktail que les héroïnes de &quot;Sex and "
            "the city&quot; aiment déguster.",
            "title": "Cocktail Cosmopolitan",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Cucumber Martini fait partie des "
            "&quot;fresh fruit martinis&quot; dont le but est de mélanger "
            "des fruits frais avec une eau-de-vie, généralement de la "
            "vodka ou du gin.</p>",
            "ingredients": [
                "4 cl de vodka",
                "1 cl de jus de citron vert pressé et filtré",
                "1 cl de sirop de sucre",
                "7 à 8 tranches de concombre",
            ],
            "summary": "Le Cucumber Martini : un cocktail réalisé avec du concombre "
            "fraîchement pressé.",
            "title": "Cocktail Cucumber Martini (concombre)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Dirty Martini est une variante du "
            "fameux Dry Martini devenu mondialement célèbre parce "
            "qu&#x27;il était notamment le cocktail favori de James Bond. "
            "La recette du Dirty Martini inclut simplement en plus du jus "
            "d&#x27;olive (ou saumure), et elle se réalise aussi sous le "
            "même nom lorsque la vodka remplace le gin.</p><p>Le Dirty "
            "Martini signifie &quot;martini sale&quot; en français, il "
            "tient son nom du fait que l&#x27;ajout de saumure "
            "d&#x27;olive donne au cocktail un aspect légèrement verdâtre "
            "et trouble.</p><p>L&#x27;origine de ce cocktail n&#x27;a "
            "jamais été réellement connu, mais diverses théories existent "
            ":</p><p>Les Dirty Martinis ont une origine impossible à "
            "identifier et n&#x27;ont donc pas de recette originale ou de "
            "composition type, c&#x27;est pour cette raison que "
            "c&#x27;est selon le goût de chacun qu&#x27;il faudra "
            "utiliser soit de la vodka soit du gin. La recette a malgré "
            "tout bien voyagée dans le temps sans trop être modifiée, "
            "effectivement mis à part le choix du spiritueux elle se "
            "compose toujours de vermouth et de saumure d&#x27;olive.</p>",
            "ingredients": [
                "5 cl de gin ou vodka",
                "1 cl de vermouth dry (Martini extra dry, Noilly Prat dry)",
                "1 cl de jus ou saumure d'olive",
            ],
            "summary": "Le Dirty Martini : un cocktail caractérisé par la présence de "
            "saumure d&#x27;olive.",
            "title": "Cocktail Dirty Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Espresso Martini , aussi appelé "
            "&quot;Vodka espresso&quot;, est toujours composé de vodka, "
            "liqueur de café, sucre et café expresso frais. Il a été créé "
            "en 1984 par Dick Bradsell, un barman londonien.</p><p>Le "
            "créateur raconte qu&#x27;un jour un célèbre mannequin est "
            "entré au Fred&#x27;s Bar et lui aurait demandé avec les "
            "termes d&#x27;origine &quot;something that&#x27;s gonna wake "
            "me up, then fu*k me up&quot;. Le cocktail fût alors baptisé "
            "le &quot;stimulant&quot; (The Stimulant), plus tard il a été "
            "renommé Espresso Martini.</p>",
            "ingredients": [
                "3 cl de vodka",
                "2 cl de Kahlua",
                "6 cl de café fraîchement préparé",
                "1 cl de sirop de sucre",
            ],
            "summary": "Le cocktail Espresso Martini : une recette créée pour stimuler "
            "l&#x27;organisme.",
            "title": "Cocktail Espresso Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>D&#x27;origine française, le cocktail Formule "
            "3 avec sa petite touche d&#x27;amertume est assez agréable "
            "et original.</p><p>C&#x27;est une recette qui nécessite "
            "d&#x27;être muni de liqueur de fraise, mais qui mérite "
            "d&#x27;être essayée au moins une fois.</p>",
            "ingredients": [
                "4 cl de vodka",
                "2 cl de liqueur de fraise",
                "3 cl de jus de pamplemousse",
                "3 cl de tonic (Schweppes)",
            ],
            "summary": "Le cocktail Formule 3 : l&#x27;une des rares recettes comportant "
            "de la liqueur de fraise.",
            "title": "Cocktail Formule 3",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail French Martini aurait été créé "
            "par la marque de liqueur de framboise Chambord dans le but "
            "de se faire connaître. Dans ce cocktail, seule la liqueur de "
            "framboise est réellement française mais même en faible "
            "quantité, cette liqueur né au XVIIème siècle sur les vallées "
            "de la Loire apporte suffisamment de saveurs et de profondeur "
            "pour rendre ce cocktail parfaitement équilibré.</p>",
            "ingredients": [
                "3,5 cl de vodka",
                "1 cl de liqueur de framboise",
                "2,5 cl de jus d'ananas",
            ],
            "summary": "Le French Martini : une liqueur française à l&#x27;origine de ce "
            "cocktail de la famille des martinis.",
            "title": "Cocktail French Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: flûte</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Godchild est réalisé dans une "
            "flûte, au contraire des cocktails Godfather et Godmother "
            "dont il est issu qui eux sont réalisés dans un verre old "
            "fashioned.</p><p>En théorie la recette du Godchild veut "
            "qu&#x27;il soit composé de 3 parts égales de vodka, "
            "d&#x27;amaretto et de crème. Si vous souhaitez conserver la "
            "contenance règlementaire d&#x27;un short drink qui fait donc "
            "7cl, nous conseillons de rajouter 1cl de vodka pour garder "
            "le plus adéquatement possible l&#x27;équilibre du "
            "cocktail.</p>",
            "ingredients": [
                "3 cl de vodka",
                "3 cl de Amaretto",
                "3 cl de crème légère",
            ],
            "summary": "Le cocktail Godchild : un digestif léger aux douces saveurs "
            "d&#x27;amandes.",
            "title": "Cocktail Godchild",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Godmother , parfois écrit "
            "&quot;God Mother&quot;, est une variante du "
            "Godfather.</p><p>Certains réalisent le Godmother avec ses "
            "ingrédients à parts égales : 5 cl de vodka et 5 cl "
            "d&#x27;Amaretto pour un goût plus prononcé "
            "d&#x27;amandes.</p>",
            "ingredients": ["7 cl de vodka", "3 cl de Amaretto"],
            "summary": "Le Godmother : un cocktail au goût subtil d&#x27;amandes à "
            "siroter en digestif.",
            "title": "Cocktail Godmother",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>La "
            "composition du cocktail Greyhound est similaire au fameux "
            "Salty dog, le seul détail qui les oppose est que dans la "
            "recette du Greyhound le verre n&#x27;est pas givré de "
            "sel.</p>",
            "ingredients": ["5 cl de vodka", "10 cl de jus de pamplemousse"],
            "summary": "Le Greyhound : un cocktail qu&#x27;on pourrait traduire par "
            "lévrier ou levrette, que choisissez-vous ;-)",
            "title": "Cocktail Greyhound",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Hairy Navel est une variante du "
            "cocktail Fuzzy Navel . Le nom de ce cocktail se traduit par "
            "&quot;nombril poilu&quot;, mais c&#x27;est une variété "
            "d&#x27;orange appelée Navel qui est à l&#x27;origine de ce "
            "nom.</p><p>Tout comme son cousin, il est préférable "
            "d&#x27;utiliser du jus d&#x27;orange fraîchement pressé dans "
            "cette recette.</p>",
            "ingredients": [
                "4 cl de vodka",
                "4 cl de Peach Schnapps (liqueur de pêche)",
                "12 cl de jus d'orange",
            ],
            "summary": "Le Hairy Navel : un cocktail aux saveurs fruitées qui signifie "
            "&quot;nombril poilu&quot;.",
            "title": "Cocktail Hairy Navel",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Harvey Wallbanger n&#x27;est rien "
            "de moins qu&#x27;un screwdriver avec du galliano en plus, "
            "mais cette liqueur italienne aux douces saveurs anisées "
            "apporte toute la différence au Harvey "
            "Wallbanger.</p><p>L&#x27;origine de ce cocktail n&#x27;est "
            "pas réellement prouvée, il existe 5 versions. En premier "
            "lieu, il semblerait que le cocktail Harvey wallbanger ait "
            "été inspiré d&#x27;un surfeur californien qui aimait boire "
            "du screwdriver en y rajoutant sa petite touche personnelle, "
            "du galliano. Un jour où il avait perdu un grand concours de "
            "surf, il avait noyé sa déception dans son cocktail préféré. "
            "Après en avoir bu plusieurs, il essaya tant bien que mal de "
            "sortir du bar et rentra en plein dans un mur. Depuis ce "
            "jour, il a été surnommé le wallbanger (&quot;wall&quot; "
            "signifiant mur et &quot;bang&quot; signifiant un coup "
            "violent). On dit qu&#x27;il s&#x27;agirait de Donato "
            "&quot;Duke&quot; Antone, barman du bar favori de Harvey et "
            "aussi créateur du Rusty Nail, qui se serait donc inspiré de "
            "Harvey pour inventer le cocktail en 1952.</p><p>Une deuxième "
            "version raconte que l&#x27;histoire ci-dessus n&#x27;est pas "
            "réellement arrivée et que ce serait sur la base de cette "
            "histoire que le Harvey wallbanger aurait été créé dans les "
            "années 1950 par le barman Robert Pratt.</p><p>Une autre "
            "version raconte que le cocktail Harvey wallbanger aurait été "
            "inventé par un barman du Butch McGuire à Chicago dans les "
            "années 1960.</p><p>Enfin une dernière version raconte que ce "
            "serait le barman Bill Doner qui aurait créé ce cocktail, un "
            "barman à &quot;The Office&quot; à Newport Beach en "
            "Californie.</p><p>Dans les années 1970, c&#x27;est une "
            "grande campagne publicitaire de la liqueur galliano mettant "
            "en scène un personnage nommé &quot;Harvey&quot; qui aurait "
            "rendu célèbre le cocktail Harvey wallbanger. Fort de son "
            "succès, des milliers de votants américains ont voté "
            "&quot;Harvey Wallbanger&quot; pour les présidentielles de "
            "1972, le 5 novembre est d&#x27;ailleurs appelé le jour du "
            "Harvey wallbanger.</p><p>Le cocktail Freddy Fudpucker est "
            "obtenu en remplaçant la vodka par de la tequila.</p>",
            "ingredients": [
                "5 cl de vodka",
                "9 cl de jus d'orange",
                "1 cl de liqueur Galliano",
            ],
            "summary": "Le Harvey Wallbanger : un cocktail qui signifie &quot;Harvey qui "
            "se prend un mur&quot; !",
            "title": "Cocktail Harvey Wallbanger",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: martini</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>L&#x27;origine du cocktail Kamikaze fait "
            "planer le doute. Certains disent qu&#x27;il aurait vu le "
            "jour pendant l&#x27;occupation américaine dans un bar de "
            "Yokosuka, près de Tokyo. Yokosuka possède une base navale et "
            "le cocktail porterait son nom &quot;Kamikaze&quot; en "
            "hommage aux pilotes japonais kamikazes qui combattaient "
            "pendant la seçonde guerre mondiale.</p><p>Une autre version "
            "raconte que le cocktail Kamikaze aurait été créé par un "
            "barman de Boston appelé &quot;Liam&quot; vers le milieu des "
            "années 1970. Il aurait été rendu célèbre quelques années "
            "plus tard grâce à la publicité d&#x27;une célèbre marque de "
            "vodka, et porterait ce nom à cause de sa forte teneur en "
            "alcool.</p><p>Le cocktail Kamikaze se boit de plus en plus "
            "en shooter avec une recette composée d&#x27;ingrédients en "
            "doses égales (2cl de vodka + 2cl de triple sec + 2cl de jus "
            "de citron). L&#x27;origine exacte de ce cocktail restant "
            "inconnue, personne ne peut affirmer la composition originale "
            "du cocktail, ce n&#x27;est donc qu&#x27;une question de goût "
            "propre à chacun...</p><p>La recette du cocktail Balalaïka "
            "Troïka est très semblable au cocktail Kamikaze mais avec du "
            "citron jaune à la place du citron vert.</p>",
            "ingredients": [
                "4 cl de vodka",
                "3 cl de Cointreau",
                "3 cl de jus de citron vert pressé et filtré",
            ],
            "summary": "Le Kamikaze : un cocktail dont le nom signifie &quot;vent "
            "divin&quot; en japonnais.",
            "title": "Cocktail Kamikaze",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le Killer "
            "Punch est un cocktail aux saveurs fruitées qui tient "
            "probablement son nom de la couleur sanglante qu&#x27;il "
            "a.</p>",
            "ingredients": [
                "3 cl de vodka",
                "2 cl de liqueur de melon",
                "2 cl de Amaretto",
                "8 cl de jus de canneberge",
            ],
            "summary": "Le cocktail Killer Punch : une recette (de tueur) aux saveurs "
            "fruitées.",
            "title": "Cocktail Killer Punch",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Dans la famille des martinis, voici donc le "
            "cocktail Lemon Drop Martini . Le cocktail aurait été créé "
            "dans les années 1970 dans un bar de San Francisco appelé "
            "Henry Africa&#x27;s. Le cocktail est aujourd&#x27;hui très "
            "populaire sur la côte ouest de la californie.</p><p>On dit "
            "que le bar avait créé toute une série de &quot;girly "
            "drinks&quot;, des cocktails à la fois puissants et doux qui "
            "conviendraient mieux aux femmes. La recette du Lemon Drop "
            "Martini en fait partie.</p>",
            "ingredients": [
                "3 cl de vodka",
                "1 cl de Cointreau",
                "1,5 cl de jus de citron pressé et filtré",
                "1 cl de sirop de sucre",
                "Sucre fin en poudre",
            ],
            "summary": "Le Lemon Drop Martini : un cocktail puissant et doux à la fois "
            "inventé spécialement pour les femmes.",
            "title": "Cocktail Lemon Drop Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Madras est un cocktail doux et fruité, qui plus est "
            "simple et facile à réaliser. C&#x27;est une recette proche "
            "du Cape Codder avec du jus d&#x27;orange en plus.</p>",
            "ingredients": [
                "4 cl de vodka",
                "6 cl de jus de canneberge",
                "5 cl de jus d'orange",
            ],
            "summary": "Le cocktail Madras : un cocktail doux à base de vodka, jus de "
            "cranberry et d&#x27;orange.",
            "title": "Cocktail Madras",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Martini fraise relève des &quot;fresh fruit "
            "martinis&quot;, ici dans une version à la fraise.</p>",
            "ingredients": [
                "4 cl de vodka",
                "1 cl de sirop de sucre",
                "6 fraises",
            ],
            "summary": "Le cocktail Martini fraise : une recette de martini en version "
            "fraise.",
            "title": "Cocktail Martini Fraise",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Melon Martini fait partie "
            "d&#x27;une famille moderne appelée &quot;fresh fruit "
            "martinis&quot; dont le but consiste à mélanger des fruits "
            "frais avec un spiritueux, généralement de la vodka ou du "
            "gin.</p>",
            "ingredients": [
                "4 cl de vodka",
                "1 cl de liqueur de melon (Midori)",
                "1/4 de melon",
            ],
            "summary": "Le cocktail Melon Martini : sa particularité est d&#x27;être "
            "réalisé avec du melon frais.",
            "title": "Cocktail Melon Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Mitch Martini aurait été créé "
            "vers 1997-1998 par Giovanni Burdi au bar &quot;Match "
            "EC1&quot; à Clerkenwell à Londres. La recette originale "
            "appelle à utiliser de la Zubrowka (vodka à l&#x27;herbe de "
            "bison).</p><p>Concernant l&#x27;origine du nom donné à ce "
            "cocktail, il existe 2 versions. La première raconte que "
            "c&#x27;est en l&#x27;honneur d&#x27;un client qui "
            "s&#x27;appelait Mitch et faisait la voix off pour la "
            "télévision britannique, la deuxième raconte que c&#x27;est "
            "en l&#x27;honneur du gros ouragan appelé &quot;Mitch&quot; "
            "qui a frappé en 1998.</p>",
            "ingredients": [
                "4 cl de vodka à l'herbe de bison (Zubrowka)",
                "0,5 cl de crème de pêche",
                "2 cl de jus de pomme",
                "0,5 cl de sirop de fruits de la passion",
            ],
            "summary": "Le cocktail Mitch Martini : une recette fruitée enrichie par une "
            "vodka à l&#x27;herbe de bison.",
            "title": "Cocktail Mitch Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tasse en cuivre</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Moscow Mule serait né peu avant "
            "1942, date de la première publication de sa recette (dans "
            "&quot;Inside Hollywood&quot; par Eith Gwynn). Dans cette "
            "première publication, l&#x27;auteur appelle à réaliser un "
            "Moscow Mule avec 3 parts égales de vodka, de ginger beer et "
            "de jus de citron vert.</p><p>Des recettes différentes du "
            "Moscow Mule sont alors publiées en 1943, 1944, 1945, 1947, "
            "1948 (2 fois) et 1949 ! Il est donc difficile de se tenir à "
            "une composition type, mais la recette courante est celle "
            "ci-dessus.</p><p>Une théorie raconte que le cocktail aurait "
            "été créé à Manhattan en 1941 par John G. Martin et John A. "
            "Morgan alias Jack, et que ce n&#x27;est qu&#x27;en 1947 "
            "qu&#x27;ils auraient baptisé le cocktail &quot;Moscow "
            "Mule&quot;. Or en 1947, au moins 4 recettes avaient déjà été "
            "publiées sous le même nom en 5 ans.</p><p>Quoiqu&#x27;il en "
            "soit, l&#x27;esprit de départ est toujours là : les Moscow "
            "Mules se réalisent toujours avec de la vodka, de la bière au "
            "gimgembre et du jus de citron vert.</p><p>On dit que le "
            "Moscow Mule est le cocktail qui a lancé l&#x27;engouement "
            "pour les cocktails à la vodka en Amérique. C&#x27;est un "
            "cocktail qui a son propre verre, il est consommé dans une "
            "chope / tasse en cuivre.</p>",
            "ingredients": [
                "4 cl de vodka",
                "2 cl de jus de citron vert pressé et filtré",
                "6 cl de Ginger Beer",
            ],
            "summary": "Le Moscow mule : une recette de 1942 à base de ginger beer, très "
            "à la mode actuellement, et de vodka.",
            "title": "Cocktail Moscow mule",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Pineapple &amp; Ginger Martini "
            "fait partie de la récente famille des &quot;fresh fruit "
            "martinis&quot; dont le but est de mélanger des fruits frais "
            "avec une eau-de-vie, généralement de la vodka ou du gin. Les "
            "Pineapples &amp; Gingers Martinis sont plutôt consommés en "
            "Angleterre et plus précisément à Londres où il aurait été "
            "créé. Plusieurs noms circulent quant au nom du créateur de "
            "cette recette, on cite notamment Tony Conigliaro du "
            "restaurant Isola.</p>",
            "ingredients": [
                "4 cl de vodka",
                "0,5 cl de sirop de sucre",
                "2 tranches d'ananas coupées en morceaux",
                "2 tranches de racine de gingembre",
            ],
            "summary": "Le Pineapple &amp; Ginger Martini : un cocktail réalisé avec "
            "gingembre et ananas frais.",
            "title": "Cocktail Pineapple & Ginger Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (11cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Porn Star Martini a "
            "été créée par Douglas Ankrah du LAB Bar à Londres. À "
            "l&#x27;origine ce cocktail a été mis au point à Cape Town en "
            "Afrique du Sud et était appelé le Maverick "
            "Martini.</p><p>Les Porn Stars Martinis peuvent se réaliser "
            "de plusieurs manières, notamment au niveau de la présence de "
            "vanille. Certains suppriment le sirop de vanille et "
            "remplacent la vodka par de la vodka vanille, d&#x27;autres "
            "font brûler du sucre de vanille sur le demi fruit de la "
            "passion.</p><p>Ce cocktail s&#x27;accompagne généralement "
            "d&#x27;une coupe de Champagne ou d&#x27;un shooter.</p>",
            "ingredients": [
                "2 cl de Passoã",
                "4 cl de vodka",
                "3 cl de purée de fruit de la passion",
                "1 demi fruit de la passion",
                "2 cl de sirop de vanille",
            ],
            "summary": "Le cocktail Porn Star Martini : une recette exotique qui met à "
            "l&#x27;honneur le fruit de la passion.",
            "title": "Cocktail Porn Star Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Purple Hooter signifie &quot;sirène violette&quot; "
            "en français, la présence de jus de citron et de soda citron "
            "rend le cocktail très rafraîchissant et désaltérant.</p>",
            "ingredients": [
                "4 cl de vodka",
                "3 cl de liqueur de framboise",
                "2 cl de jus de citron vert pressé et filtré",
                "6 cl de limonade ou 7up",
            ],
            "summary": "Le cocktail Purple Hooter : une recette rafraîchissante qui "
            "signifie &quot;sirène violette&quot;.",
            "title": "Cocktail Purple Hooter",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball ou tulipe</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Recette en "
            "vidéo</h2><p>Rainbow Cocktail signifie Cocktail Arc-en-ciel "
            ", il s&#x27;agit de la version simplifiée que nous vous "
            "proposons ici car vous pouvez aussi ajouter du jus "
            "d&#x27;ananas au dessus du jus d&#x27;orange.</p>",
            "ingredients": [
                "3 cl de vodka",
                "2 cl de Curaçao Bleu",
                "13 cl de jus d'orange",
                "2 cl de sirop de grenadine",
            ],
            "summary": "Le Rainbow Cocktail : une recette aux couleurs de "
            "l&#x27;arc-en-ciel.",
            "title": "Cocktail Rainbow cocktail",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Raspberry &amp; Mint Martini , "
            "dont l&#x27;origine n&#x27;est pas connue, fait partie de la "
            "famille des &quot;fresh fruit martinis&quot; dont le but est "
            "de mélanger des fruits frais avec une eau-de-vie, "
            "généralement de la vodka voire du gin.</p>",
            "ingredients": [
                "4 cl de vodka",
                "1 cl de sirop de sucre (1 cuillère à café)",
                "8 framboises fraîches",
                "4 feuilles de menthe",
            ],
            "summary": "Le Raspberry &amp; Mint Martini : un cocktail réalisé avec de la "
            "menthe et des framboises fraîches.",
            "title": "Cocktail Raspberry & Mint Martini",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Red Apple n&#x27;a pas d&#x27;origine connue, "
            "c&#x27;est une recette qui a le mérite d&#x27;oser mélanger "
            "le jus de pomme avec des ingrédients qui ne se marient pas "
            "forcément avec.</p><p>Vous pouvez optionnellement ajouter un "
            "trait d&#x27;Orange Bitters et/ou un quartier de pomme en "
            "décoration.</p>",
            "ingredients": [
                "3 cl de vodka",
                "3 cl de jus de pomme",
                "1,5 cl de jus de citron pressé et filtré",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le cocktail Red Apple : une recette audacieuse à base de jus de "
            "pomme.",
            "title": "Cocktail Red Apple",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler ou sling</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Russian Spring Punch a été créé "
            "par le barman londonnien Dick Bradsell, créateur du fameux "
            "cocktail Espresso martini et autres cocktails modernes dans "
            "les années 1980.</p>",
            "ingredients": [
                "2,5 cl de vodka",
                "1,5 cl de jus de citron vert et filtré",
                "1,5 cl de crème de cassis",
                "1 cl de sirop de sucre",
                "5 cl de Champagne",
            ],
            "summary": "Le cocktail Russian Spring Punch : un cocktail classique "
            "nouvelle génération qui surprendra vos invités.",
            "title": "Cocktail Russian Spring Punch",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler ou old fashioned</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Salty dog (chien salé en français) est un "
            "cocktail classique que tous les barmen connaissent, pourtant "
            "sa présence sur les cartes de cocktails n&#x27;est pas "
            "forcément très fréquente. On parle de George Jessel comme "
            "étant le créateur de ce cocktail.</p><p>Il peut arriver de "
            "croiser des recettes de Salty dogs avec du gin à la place de "
            "la vodka, ce n&#x27;est pas la composition originale mais "
            "c&#x27;est en effet l&#x27;alcool qui peut remplacer le "
            "mieux la vodka.</p><p>Le cocktail le plus proche du Salty "
            "dog est le Greyhound, il a la même composition que le Salty "
            "dog à la différence que le verre n&#x27;est pas givré au "
            "sel.</p>",
            "ingredients": ["6 cl de vodka", "9 cl de jus de pamplemousse"],
            "summary": "Le cocktail Salty Dog : la recette d&#x27;une &quot;vodka "
            "pamplemousse&quot;.",
            "title": "Cocktail Salty dog",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail San Francisco pourrait faire partie de la famille "
            "des sunrises puisqu&#x27;il en a clairement des "
            "airs.</p><p>Doux, fruité, et coloré avec son dégradé, "
            "c&#x27;est l&#x27;une des recettes parfaites à siroter en "
            "plein été sur une terrasse de bord de mer.</p>",
            "ingredients": [
                "3,5 cl de vodka",
                "2,5 cl de liqueur de banane",
                "8 cl de jus d'orange",
                "1 cl de sirop de grenadine",
            ],
            "summary": "Le San Francisco : un cocktail doux et fruité aux airs de "
            "&quot;sunrise&quot;.",
            "title": "Cocktail San Francisco",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire</h2><p>Le "
            "cocktail Screwdriver est très répandu et connu de tous, mais "
            "plus sous le nom &quot;vodka orange&quot;. La simplicité de "
            "ce cocktail rend l&#x27;origine de son histoire difficile à "
            "définir, le screwdriver daterait d&#x27;avant les années "
            "1950. Screwdriver signifiant &quot;tournevis&quot; en "
            "français, le cocktail aurait été appelé ainsi car c&#x27;est "
            "à l&#x27;aide de leur tournevis que les travailleurs "
            "d&#x27;une plateforme pétrolière mélangeait les ingrédients "
            "du cocktail.</p><p>Pour déguster au mieux ce cocktail "
            "screwdriver tout comme tous les autres, il faut bien "
            "respecter le dosage indiqué dans la recette ou au pire ne "
            "pas dépasser 8cl de jus d&#x27;orange pour 4cl de vodka "
            "!</p><p>C&#x27;est à partir du cocktail screwdriver que le "
            "cocktail Harvey wallbanger est "
            "né.</p><h2>Variantes</h2><p>Le Sloe Screw (+ Sloe "
            "Gin)</p><p>Le Sloe Comfortable Screw (+ Sloe Gin + Southern "
            "Comfort)</p><p>Le Sloe Comfortable Screw Up Against The Wall "
            "(+ Sloe Gin + Southern Comfort + liqueur Galliano)</p><p>Le "
            "&quot;Sloe Comfortable Fuzzy Screw Against the Wall&quot; "
            "sur la même page que le cocktail précédent (+ Sloe Gin + "
            "Southern Comfort + liqueur Galliano + Peach "
            "Shnapps)</p><p>Le Sloe Comfortable Screw Between the Sheets "
            "(+ Sloe Gin + Southern Comfort + triple sec)</p>",
            "ingredients": ["5 cl de vodka", "7 cl de jus d'orange"],
            "summary": "Le Screwdriver (ou vodka orange) : cocktail signifiant "
            "&quot;tournevis&quot; car c&#x27;est l&#x27;outil grâce auquel "
            "le cocktail aurait été mélangé !",
            "title": "Cocktail Screwdriver",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: highball</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Sea Breeze est un cocktail classique qui "
            "serait né dans les années 1920, la recette originale "
            "comportait du gin et de la grenadine. Plus tard dans les "
            "années 1930, le Sea Breeze se réalise avec du gin, de la "
            "liqueur d&#x27;abricot, du jus de citron et de la grenadine. "
            "Depuis de nombreuses recettes de Sea Breeze ont vu le jour, "
            "c&#x27;est la version la plus courante que nous vous "
            "proposons ici.</p>",
            "ingredients": [
                "5 cl de vodka",
                "3 cl de jus de pamplemousse",
                "7 cl de jus de canneberge",
            ],
            "summary": "Le Sea Breeze : un cocktail doux incontournable en plein été qui "
            "signifie &quot;brise de mer&quot;.",
            "title": "Cocktail Sea Breeze",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sex in the Driveway est une "
            "variante du fameux Sex on the Beach .</p><p>Sa couleur bleue "
            "que lui confère le curaçao fait de lui un joli cocktail, "
            "mais le lien n&#x27;est pas évident à faire entre la couleur "
            "et le nom donné à ce cocktail. Les driveways sont "
            "effectivement les courtes allées situées entre une rue et "
            "une porte de garage...</p><p>Contrairement au Sex On The "
            "Beach, le Sex In The Driveway n&#x27;a pas besoin "
            "d&#x27;être shaké, ce qui le rend plus simple à faire pour "
            "les plus novices.</p>",
            "ingredients": [
                "4 cl de Vodka",
                "2 cl de Liqueur de pêche (Peach schnapps...)",
                "2 cl de Curaçao Bleu",
                "7 cl de Sprite",
            ],
            "summary": "Le cocktail Sex In The Driveway : la variante bleue du célèbre "
            "Sex On The Beach.",
            "title": "Cocktail Sex in the Driveway",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (16cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Vidéo</h2><h2>Histoire et "
            "origine</h2><p>Le cocktail Sex on the beach a une "
            "particularité, il n&#x27;existe pas qu&#x27;une recette "
            "originale mais deux. C&#x27;est un cocktail rempli de "
            "mystère qui serait né dans les années 1980, juste après "
            "l&#x27;arrivée du Peachtree Schnapps et de la liqueur de "
            "melon Midori. De nombreuses variations sont nés de ces deux "
            "recettes de base.</p><p>Plusieurs hypothèses existent quant "
            "à l&#x27;origine du Sex on the beach :</p><p>L&#x27;origine "
            "réelle du Sex on the Beach est donc incertaine mais "
            "quoiqu&#x27;il en soit son nom est très accrocheur, "
            "c&#x27;est l&#x27;une des raisons du succès de ce cocktail "
            "aujourd&#x27;hui. Par temps de chaleur, c&#x27;est un "
            "excellent cocktail aux couleurs chaudement agréables et "
            "assez désaltérant.</p><p>La recette ici présente est la "
            "version courante car il existe de nombreuses variantes, "
            "certaines recettes voient par exemple la vodka être "
            "remplacée par du rhum, quand d&#x27;autres incluent en plus "
            "de l&#x27;amaretto, du malibu, de la liqueur de framboise ou "
            "du jus d&#x27;ananas...</p><p>Notez que de plus en plus le "
            "Sex on the Beach se réalise direct au verre, dans quel cas "
            "vous devrez verser les ingrédients dans un verre rempli de "
            "glace.</p><p>Notez aussi que si vous enlevez le jus de "
            "canneberge, vous obtenez le cocktail Hairy Navel.</p><p>Il "
            "existe une deuxième recette du Sex On The Beach à frapper au "
            "shaker et composée de 4cl de vodka, 2cl de liqueur de melon "
            "Midori, 2cl de Chambord, 2cl de jus d&#x27;ananas et 2cl de "
            "jus de canneberge.</p>",
            "ingredients": [
                "4 cl de vodka",
                "2 cl de liqueur de pêche (Peach schnapps...)",
                "5 cl de jus de canneberge (cranberry)",
                "5 cl de jus d'orange",
            ],
            "summary": "Le Sex on the beach : la vraie recette courante d&#x27;un "
            "cocktail au nom très évocateur.",
            "title": "Cocktail Sex on the Beach",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sloe Comfortable Screw est un "
            "Sloe Screw avec du Southern Comfort en complément. Tout "
            "comme son cousin, le Sloe Comfortable Screw est une variante "
            "du célèbre Screwdriver (vodka orange), retrouvez toutes les "
            "variantes sur la page de ce dernier.</p><p>* Le Sloe Gin est "
            "une liqueur fabriquée à partir du prunellier avec ajout de "
            "gin et de sucre.</p>",
            "ingredients": [
                "4 cl de vodka",
                "3 cl de Sloe Gin *",
                "3 cl de Southern Comfort",
                "10 cl de jus d'orange",
            ],
            "summary": "Le cocktail Sloe Comfortable Screw : un Sloe Screw avec du "
            "Southern Comfort en plus.",
            "title": "Cocktail Sloe Comfortable Screw",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sloe Comfortable Screw Between "
            "the Sheets est un &quot;Sloe Comfortable Screw&quot; avec du "
            "triple sec en plus. Ils sont tous les deux des variantes du "
            "Screwdriver , retrouvez toutes les variantes sur la page de "
            "ce dernier.</p><p>* *Le Sloe Gin est une liqueur fabriquée à "
            "partir du prunellier avec ajout de gin et de sucre.</p>",
            "ingredients": [
                "2 cl de vodka",
                "2 cl de Sloe Gin *",
                "2 cl de Southern Comfort",
                "2 cl de Cointreau",
                "12 cl de jus d'orange",
            ],
            "summary": "Le Sloe Comfortable Screw Between the Sheets : l&#x27;un des "
            "nombreux cocktails dérivés du Screwdriver.",
            "title": "Cocktail Sloe Comfortable Screw Between the Sheets",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sloe Comfortable Screw Up Against "
            "The Wall est un Sloe Comfortable Screw avec un trait de "
            "liqueur Galliano en plus. &quot;Against the wall&quot; fait "
            "allusion à l&#x27;histoire du cocktail Harvey Wallbanger. Ce "
            "sont des variantes du Screwdriver , nom donné à la fameuse "
            "&quot;vodka orange&quot; dont vous pourrez trouver toutes "
            "les variantes sur sa page.</p><p>Notez qu&#x27;en rajoutant "
            "du Peach Schnapps dans ce cocktail, vous obtiendrez un "
            "&quot;Sloe Comfortable Fuzzy Screw Against the "
            "Wall&quot;.</p><p>* Le Sloe Gin est une liqueur fabriquée à "
            "partir du prunellier avec ajout de gin et de sucre.</p>",
            "ingredients": [
                "4 cl de vodka",
                "2 cl de Sloe Gin *",
                "2 cl de Southern Comfort",
                "10 cl de jus d'orange",
                "2 cl de liqueur Galliano",
            ],
            "summary": "Le Sloe Comfortable Screw Up Against The Wall : un cocktail aux "
            "nombreuses saveurs dérivé du screwdriver.",
            "title": "Cocktail Sloe Comfortable Screw Up Against The Wall",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Sloe Screw est une des variantes "
            "du célèbre Screwdriver .</p><p>Le Sloe Gin est une liqueur "
            "fabriquée à partir du prunellier avec ajout de gin et de "
            "sucre.</p>",
            "ingredients": [
                "4 cl de Sloe Gin",
                "4 cl de vodka",
                "12 cl de jus d'orange",
            ],
            "summary": "Le cocktail Sloe Screw : la première d&#x27;une grande lignée de "
            "variantes du fameux screwdriver.",
            "title": "Cocktail Sloe Screw",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (20cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Tall black russian est une "
            "variante du célèbre Black russian créé en 1949 par Gustave "
            "Tops à Bruxelles. En y ajoutant simplement du cola on "
            "obtient ce fameux Tall black russian qui devient un long "
            "drink et que l&#x27;on servira dans un tumbler.</p>",
            "ingredients": [
                "6 cl de vodka",
                "4 cl de liqueur de café",
                "10 cl de cola",
            ],
            "summary": "Le cocktail Tall Black Russian : la recette du Black Russian "
            "avec du cola en plus.",
            "title": "Cocktail Tall Black russian",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Testarossa (écrit parfois Testa Rossa) porte le nom "
            "de la fameuse Ferrari produite entre 1984 et 1996, "
            "c&#x27;est un cocktail plutôt doux avec une petite touche "
            "d&#x27;amerture apportée par le Campari.</p>",
            "ingredients": [
                "3 cl de vodka",
                "4 cl de Campari",
                "8 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Testarossa : la recette du nom de la célèbre "
            "Ferrari.",
            "title": "Cocktail Testarossa",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: à martini ou old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (9cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Vodka Daisy fait partie des "
            "cocktails &quot;daisies&quot; (types de short drinks), il a "
            "donc toujours été fait de 4 ingrédients avec ni plus ni "
            "moins que : vodka, jus de citron, sucre et sirop de "
            "grenadine (ou framboise).</p><p>C&#x27;est un cocktail qui "
            "se veut de caractère, sa recette a été publiée en 1965 dans "
            "&quot;Old Mr Boston&#x27;s De Luxe Official Bartender&#x27;s "
            "Book&quot; de Leo Cotton.</p><p>À l&#x27;origine, la "
            "particularité de la Vodka Daisy était sa verrerie, on la "
            "servait dans des coupes en métal, chopes ou mugs.</p>",
            "ingredients": [
                "5 cl de vodka",
                "2 cl de citron pressé et filtré",
                "1 cl de sirop de grenadine",
                "1 cl de sirop de sucre",
            ],
            "summary": "La Vodka Daisy : un cocktail de caractère qui a toujours gardé "
            "sa recette type.",
            "title": "Cocktail Vodka Daisy",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned ou à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "Origine</h2><p>Le cocktail Vodka Stinger est une recette "
            "très simple de vodka-menthe à consommer en apéritif, "
            "c&#x27;est une variante du fameux Stinger .</p>",
            "ingredients": [
                "5 cl de vodka",
                "2 cl de liqueur/crème de menthe blanche",
            ],
            "summary": "Le cocktail Vodka Stinger : une vodka-menthe à déguster en "
            "apéritif.",
            "title": "Cocktail Vodka Stinger",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La Vodkatini , appelé aussi &quot; Vodka "
            "Martini &quot;, est un dérivé du célèbre Dry Martini, la "
            "vodka remplace ici le gin d&#x27;origine. Tout comme le Dry "
            "martini donc, le Vodkatini se réalise au verre à mélange "
            "avec une olive en décoration, symbole du Dry "
            "martini.</p><p>La Vodkatini est le cocktail préféré de James "
            "Bond, il réclame un Dry Martini avec entre autres de la "
            "vodka à la place du gin.</p>",
            "ingredients": [
                "6 cl de vodka",
                "2 cl de vermouth blanc (Martini, Noilly prat...)",
            ],
            "summary": "La Vodkatini : Appelé aussi Vodka Martini , c&#x27;est le "
            "cocktail préféré de James Bond !",
            "title": "Cocktail Vodkatini (vodka martini)",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail White russian est une variante du "
            "Black russian , il fait aussi partie des after-dinners. "
            "L&#x27;ajout de crème dans le cocktail White russian apporte "
            "une véritable touche de douceur mais nécessite de réaliser "
            "le cocktail au shaker.</p><p>Le White russian aurait vu le "
            "jour en même temps que le cocktail Black russian en 1949 "
            "grâce à Gustave Tops, un barman belge de l&#x27;Hôtel "
            "Métropôle à Bruxelles.</p>",
            "ingredients": [
                "6 cl de vodka",
                "2 cl de Kahlua",
                "2 cl de crème légère",
            ],
            "summary": "Le White Russian : le cocktail préféré du &quot;duc&quot; (The "
            "Dude en v.o.) dans &quot;The Big Lebowski&quot;.",
            "title": "Cocktail White russian",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Woo Woo est une recette que "
            "l&#x27;on peut considérer comme une variante du fameux Sex "
            "on the Beach dans lequel on aurait simplement enlevé le jus "
            "d&#x27;orange.</p>",
            "ingredients": [
                "4 cl de vodka",
                "4 cl de liqueur de pêche (Peach schnapps...)",
                "7 cl de jus de canneberge (cranberry)",
            ],
            "summary": "Le cocktail Woo woo : une recette très proche du Sex on the "
            "Beach.",
            "title": "Cocktail Woo Woo",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail 7&amp;7 (seven and seven) se nomme ainsi car il se "
            "réalise avec du whisky Seagram&#x27;s Seven Crown® et du "
            "7Up®, célèbre soda à base de lime (citron vert).</p>",
            "ingredients": [
                "5 cl de whisky (Seagram's Seven Crown®)",
                "10 cl de soda 7Up®",
            ],
            "summary": "Le 7&amp;7 (seven and seven) : un cocktail mondialement connu à "
            "base de 7Up®.",
            "title": "Cocktail 7&7",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Affinity date du début du 20ème "
            "siècle car on le mentionne dans le Washington Post du 29 "
            "octobre 1907. Il y est mentionné qu&#x27;au premier Affinity "
            "bu l&#x27;horizon prend une teinte rosée, le deuxième fait "
            "apparaître Wall Street avec une quantité d&#x27;agneaux "
            "luisants au centre, et au troisième l&#x27;herbe verte se "
            "déploie autour avec des oiseaux qui chantent dans les "
            "figuiers et c&#x27;est alors que l&#x27;affinité "
            "apparaît.</p><p>Ce même article dévoile la recette "
            "d&#x27;origine des cocktails Affinities qui étaient alors "
            "réalisés avec du whisky écossais, du vermouth italien, de "
            "l&#x27;Orange Bitters et une cuillère de sucre en poudre.</p>",
            "ingredients": [
                "1/3 de whisky (Scotch)",
                "1/3 de vermouth rouge (Martini rosso, Noilly Prat rouge)",
                "1/3 de vermouth dry (Martini extra dry, Noilly Prat dry)",
                "1 trait d'Angostura bitters",
            ],
            "summary": "Le cocktail Affinity : une recette vintage datant du début du "
            "XXème siècle.",
            "title": "Cocktail Affinity",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Algonquin est un cocktail nommé "
            "en l&#x27;honneur de l&#x27;hôtel du même nom créé vers 1902 "
            "et situé dans le quartier new-yorkais de Manhattan. "
            "L&#x27;Algonquin est vite devenu un lieu de rencontre "
            "populaire notamment pour les écrivains et acteurs, y compris "
            "le groupe de la &quot;table ronde "
            "d&#x27;Algonquin&quot;.</p>",
            "ingredients": [
                "4 cl de whisky de seigle (Rye whiskey, etc.)",
                "2 cl de vermouth blanc (Martini...)",
                "2 cl de jus d'ananas",
            ],
            "summary": "Le cocktail Algonquin : une recette en l&#x27;honneur de "
            "l&#x27;hôtel de Manhattan du même nom.",
            "title": "Cocktail Algonquin",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Barbary Coast est apparue dans le "
            "Reno Evening Gazette (Nevada, USA) le 21 novembre 1940, la "
            "recette est restée inchangée depuis, elle est toujours "
            "réalisée sans exception avec du rye whiskey, du vermouth "
            "rouge et du jus d&#x27;orange.</p>",
            "ingredients": [
                "2 parts de whisky de seigle (Rye whiskey, etc.)",
                "1 part de vermouth rouge (Martini rosso, Noilly Prat rouge)",
                "1 part de jus d'orange",
            ],
            "summary": "Le cocktail Barbary Coast : une recette du Nevada datant de "
            "1940.",
            "title": "Cocktail Barbary Coast",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler ou old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (≈7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Bizzy Izzy est apparu pour la "
            "première fois en 1917 dans &quot; The Ideal Bartender &quot; "
            "de Tom Bullock.</p>",
            "ingredients": [
                "3 cl de whisky (Bourbon ou Rye Whiskey)",
                "2,5 cl de sherry (Xérès)",
                "1,5 cl de sirop d'ananas",
                "1 cl de jus de citron pressé et filtré",
            ],
            "summary": "Le cocktail Bizzy Izzy : la recette originale publiée par Tom "
            "Bullock en 1917.",
            "title": "Cocktail Bizzy Izzy",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Blackberry Julep (aussi appelé "
            "Blackberry-Mint Julep) est une énième variante du grand "
            "classique Mint Julep, avec ici de la mûre en plus.</p>",
            "ingredients": [
                "5 cl de Whisky Bourbon",
                "1 cuillère à café de sucre en poudre",
                "5 à 7 feuilles de menthe fraîche",
                "Quelques mûres",
            ],
            "summary": "Le Blackberry Julep : Un dérivé du Mint Julep avec de la mûre en "
            "plus.",
            "title": "Cocktail Blackberry Julep",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul>",
            "ingredients": [
                "3 cl de whisky écossais (Scotch, etc.)",
                "2 cl de Kahlua",
                "1 cl de Cointreau",
                "1 cl de jus de citron filtré et pressé",
            ],
            "summary": "Le cocktail Blackjack : une recette consommée à Las Vegas.",
            "title": "Cocktail Blackjack",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Blood and Sand (Sang "
            "et Sable) est parue pour la première fois dans le fameux "
            "Savoy Cocktail Book de Harry Craddock (1930), puis un peu "
            "plus tard dans le Boothby’s World Drinks and How to Mix Them "
            "de William T. Boothby (1934).</p>",
            "ingredients": [
                "1/4 de whisky écossais (Scotch, etc.)",
                "1/4 de vermouth rouge (Martini...)",
                "1/4 de liqueur de cerise (Cherry brandy)",
                "1/4 de jus d'orange",
            ],
            "summary": "Le cocktail Blood and Sand : une recette vintage née dans le "
            "célèbre Savoy Cocktail Book de 1930.",
            "title": "Cocktail Blood and Sand",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: voir "
            "ci-dessous</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><p>Pour des raisons "
            "évidentes, ne réalisez pas ce cocktail si vous n&#x27;êtes "
            "pas un barman entraîné et qui oeuvre dans des conditions de "
            "sécurité optimales !</p><h2>Histoire et origine</h2><p>Ceci "
            "est la recette originale du cocktail Blue Blazer telle "
            "qu&#x27;elle a été publiée en 1862 par son créateur Jerry "
            "Thomas dans &quot;Bartenders Guide : How to mix drinks&quot; "
            ". Jerry Thomas nous y indique ce cocktail n&#x27;a pas un "
            "nom très classique ou mélodieux, mais il a meilleur goût au "
            "palais qu&#x27;il ne s&#x27;entend à l&#x27;oreille. Il "
            "précise aussi qu&#x27;il est nécessaire de bien "
            "s&#x27;entraîner avec de l&#x27;eau froide pour pouvoir "
            "réussir à transvaser sans dégâts.</p>",
            "ingredients": [
                "5 cl de whisky écossais (Scotch, etc.)",
                "5 cl d'eau plate chaude",
                "1 cuillère à café de sucre en poudre",
            ],
            "summary": "Le Blue Blazer : un cocktail enflammé qui vous offre un grand "
            "spectacle visuel !",
            "title": "Cocktail Blue Blazer",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre à bière large</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Boilermaker peut se consommer "
            "d&#x27;une seconde façon : boire d&#x27;abord le shooter "
            "puis immédiatement la bière.</p><p>On ne sait pas avec "
            "certitude quand ni par qui le Boilermaker a été créé mais il "
            "semblerait que son origine remonte jusqu&#x27;au 19ème "
            "siècle. &quot;Boilermaker&quot; se traduit par chaudronnier "
            "en français et l&#x27;Oxford English Dictionary, largement "
            "considéré comme la première autorité sur l&#x27;origine des "
            "mots, indique que ce terme était utilisé pour désigner les "
            "travailleurs qui construisaient et entretenaient les "
            "locomotives à vapeur en 1834 mais selon certains "
            "étymologistes, il était déjà utilisé pour décrire la "
            "boisson.</p><p>On dit que ce serait peut-être un certain "
            "Richard Trevithick qui serait à l&#x27;origine du nom de ce "
            "cocktail, c&#x27;était un forgeron inventif qui "
            "expérimentait des véhicules à vapeur. En 1801, la nuit de "
            "Noël dans le village de Cambourne au Royaume Uni, il serait "
            "parti pour tester sa dernière invention, un véhicule routier "
            "automoteur à vapeur. Il aurait monté la colline du village "
            "avec quelques amis à bord de son invention. Atteignant le "
            "haut de la colline, le groupe aurait garé le véhicule dans "
            "un hangar et aurait célébré leur succès dans un "
            "établissement hôtellier. Dans l&#x27;euphorie ils auraient "
            "oublié le feu dans la chaufferie du véhicule et auraient "
            "retrouvé ce dernier après la fête réduit en un tas de "
            "ferraille amoncelé avec des éléments en bois réduits en "
            "poussière.</p>",
            "ingredients": ["1 shooter de whisky", "1 bière"],
            "summary": "Le cocktail Boilermaker : une recette unique qui signifie "
            "&quot;chaudronnier&quot; en français.",
            "title": "Cocktail Boilermaker",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Boulevardier est un cocktail classique IBA "
            "(International Bartender Association).</p><p>La recette a "
            "été publiée pour la première fois en 1927 dans le livre "
            "Harry McElhone&#x27;s Barflies and Cocktails , dans un "
            "article en page 80 où Harry McElhone attribue "
            "l&#x27;invention du cocktail à Erskinne Gwynne .</p><p>Dans "
            "cet article, la recette originale était alors de : 1/3 "
            "Campari, 1/3 Italian vermouth, 1/3 bourbon whisky. Mais "
            "cette recette manquant d&#x27;équilibre, les proportions "
            "sont aujourd&#x27;hui de 3/2/2.</p><p>Notez que si vous "
            "rempacez le Bourbon par du gin vous obtenez le cocktail "
            "Negroni.</p>",
            "ingredients": [
                "3 cl de Bourbon",
                "2 cl de Campari",
                "2 cl de vermouth rouge",
            ],
            "summary": "Le Boulevardier : un cocktail classique très sec fait de whisky, "
            "Campari et vermouth rouge.",
            "title": "Cocktail Boulevardier",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12 cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le Canadian Daisy ne dispose d&#x27;aucune "
            "information quant à son origine, il est à cheval entre les "
            "daisies (famille de shorts drinks) et les fizzes, ce qui le "
            "rend à la fois doux, fruité et rafraîchissant.</p>",
            "ingredients": [
                "3 cl de whisky canadien",
                "1,5 cl de Cognac",
                "1,5 cl de jus de citron pressé et filtré",
                "1 cl de sirop de framboise",
                "5 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Canadian Daisy : une recette riche en saveurs, "
            "enrichie avec des fruits frais.",
            "title": "Cocktail Canadian Daisy",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Chancellor n&#x27;a "
            "pas d&#x27;origine connue, chancellor signifie chancelier en "
            "français.</p>",
            "ingredients": [
                "4 cl de whisky écossais (Scotch, etc.)",
                "2 cl de vin de liqueur (Porto)",
                "1 cl de vermouth blanc (Martini...)",
                "2 traits d'Angostura bitters",
            ],
            "summary": "Le Chancellor : un cocktail sec qui se traduit par chancelier en "
            "France.",
            "title": "Cocktail Chancellor",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Churchill a été créé par Joe "
            "Gilmore, chef barman de l&#x27;American bar au Savoy Hotel "
            "de Londres dans lequel il oeuvra de 1940 à 1976. Il y a reçu "
            "les plus grandes célébrités et y a créé des cocktails en "
            "leur hommage, c&#x27;est le cas pour ce cocktail. Joe "
            "Gilmore l&#x27;a concocté en l&#x27;honneur du politicien "
            "Winston Churchill qui lui aurait demandé un soir "
            "d&#x27;inventer un cocktail en son nom.</p><p>Rappelons que "
            "Winston Churchill (1874-1965) est mondialement célèbre pour "
            "avoir été notamment le premier ministre anglais de 1940 à "
            "1945 puis de 1951 à 1955. L&#x27;homme d&#x27;état avait "
            "aussi des talents de peinture mais aussi d&#x27;écriture qui "
            "lui ont valu un prix nobel de littérature à la fin de sa "
            "vie.</p><p>Les Churchills sont des cocktails plutôt secs "
            "avec une petite pointe d&#x27;amertume et d&#x27;acidité, "
            "ils se réalisent aussi parfois avec du vermouth rouge.</p>",
            "ingredients": [
                "3 cl de whisky écossais (Scotch, etc.)",
                "1,5 cl de vermouth blanc (Martini...)",
                "1,5 cl de Cointreau",
                "1 cl de jus de citron vert pressé et filtré",
            ],
            "summary": "Le cocktail Churchill : une recette créée en l&#x27;honneur du "
            "célèbre homme d&#x27;état du même nom.",
            "title": "Cocktail Churchill",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du cocktail Cliquet n&#x27;a pas "
            "d&#x27;origine connue, vous pouvez donc utiliser toute sorte "
            "de whisky selon votre préférence : scotch, rye ou bourbon. "
            "En français un cliquet est un système mécanique de blocage "
            "qui empêche une roue à cran de revenir en arrière, mais le "
            "rapport avec le cocktail ne semble pas évident. Le cocktail "
            "aurait plutôt tendance à avoir des origines américaines et "
            "pourrait dater d&#x27;avant la période de prohibition "
            "(1921-1933).</p>",
            "ingredients": ["4 cl de whisky", "1 cl de rhum brun", "1 orange"],
            "summary": "Le Cliquet : un cocktail au nom francophone qui désigne un "
            "système mécanique.",
            "title": "Cocktail Cliquet",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Derby possède plusieurs recettes "
            "totalement différentes sous ce même nom. En 1947 Trader Vic "
            "publie &quot;Bartender’s Guide&quot; dans lequel on ne "
            "trouve pas moins de 3 recettes de &quot;Derby&quot;. Nous "
            "choisissons cette recette qui met à l&#x27;honneur une "
            "bénedictine au fort potentiel et souvent oubliée, ici mariée "
            "avec du bourbon et de l&#x27;Angostura bitters.</p>",
            "ingredients": [
                "6 cl de Bourbon",
                "1 cl de Bénedictine",
                "1 trait d'Angostura bitters",
            ],
            "summary": "Le cocktail Derby : une parfaite alliance entre Bourbon et "
            "Bénedictine.",
            "title": "Cocktail Derby",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Godfather ou God Father n&#x27;a "
            "pas d&#x27;origine connue, la recette se réalise "
            "généralement avec du scotch mais quelques fois aussi avec du "
            "bourbon. Il a donné naissance à 2 cocktails dérivés : le "
            "godmother et le godchild.</p><p>Quelques barmen réalisent la "
            "recette avec des parts égales de whisky et "
            "d&#x27;Amaretto.</p>",
            "ingredients": [
                "7 cl de whisky écossais (Scotch, etc.)",
                "3 cl de Amaretto",
            ],
            "summary": "Le cocktail Godfather : un digestif aux douces saveurs "
            "d&#x27;amandes.",
            "title": "Cocktail Godfather",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (≥7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Godson se réalise généralement avec du whisky "
            "écossais (Scotch) ou canadien (Canadian). Tout comme les "
            "cocktails Godmother et Godchild , le Godson est une recette "
            "dérivée du célèbre Godfather .</p>",
            "ingredients": [
                "2 parts de whisky",
                "1 part de Amaretto",
                "1 part de crème légère",
            ],
            "summary": "Le cocktail Godson : une recette crémeuse signifiant "
            "&quot;filleul&quot;.",
            "title": "Cocktail Godson",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Horse&#x27;s Neck se fait "
            "connaître vers 1895, à l&#x27;origine la recette comportait "
            "simplement du soda au gimgembre (ginger ale) et un zeste de "
            "citron. Quelques années plus tard, on commence à y rajouter "
            "du bourbon ou parfois du brandy (cognac).</p>",
            "ingredients": [
                "4 cl de Bourbon",
                "5 cl de Ginger Ale (Canada Dry)",
                "Quelques gouttes d'Angostura bitters",
            ],
            "summary": "Le cocktail Horse&#x27;s Neck : sa particularité est son très "
            "long et épais zeste de citron.",
            "title": "Cocktail Horse's Neck",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: toddy</li>\n"
            "<li>Type&nbsp;: long drink (23cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Irish Coffee daterait de la "
            "seconde guerre mondiale bien que de nombreuses histoires se "
            "racontent quant à son origine.</p><p>L&#x27;histoire la plus "
            "courante et probable raconte qu&#x27;à partir du début des "
            "années 1940, l&#x27;Irish Coffee était servi aux passagers "
            "américains qui attérissaient à l&#x27;aéroport de Foynes en "
            "Irlande après avoir voyagé de longues heures. Joseph "
            "Sheridan (1909-1962), chef d&#x27;un restaurant de "
            "l&#x27;aéroport, constatant que les passagers étaient "
            "éreintés et refroidis par le voyage, leur concoctait un "
            "mélange pour les réchauffer et leur remonter le moral. Pour "
            "cela, Sheridan mélangeait notamment du café chaud avec un "
            "peu de bon whisky irlandais. Les passagers appréciaient la "
            "saveur du café, un jour l&#x27;un des passagers aurait "
            "demandé à Joe Sheridan s&#x27;il s&#x27;agissait de café "
            "brésilien, le chef aurait répondu &quot;non, c&#x27;est un "
            "café irlandais (Irish Coffee)&quot;.</p><p>En 1945 cet "
            "aéroport de Foynes consacré aux hydravions ferme, un nouvel "
            "aéroport est inauguré à côté dans la ville de Shannon pour "
            "pouvoir y accueillir des avions &quot;terrestres&quot;. "
            "C&#x27;est dans ce nouvel aéroport que Sheridan est partit "
            "travaillé jusqu&#x27;en 1952 en emmenant avec lui son "
            "invention : l&#x27;Irish Coffee. Une plaque commémorative "
            "rend hommage à Sheridan et sa création dans cet aéroport de "
            "Shannon.</p><p>Le 10 novembre 1952 au café Buena Vista de "
            "San Francisco, le gérant Jack Koppler et le journaliste "
            "Stanton Delaplane du San Francisco Chronicle qui était passé "
            "par l&#x27;aéroport de Shannon tentent de recréer "
            "l&#x27;Irish Coffee. Les essais n&#x27;ont pas vraiment été "
            "au rendez-vous car le goût n&#x27;est pas convenable et la "
            "crème ne tenait pas au dessus du café. Selon la légende, "
            "Stanton Deaplane s&#x27;est presque évanoui après avoir "
            "goûté de nombreux tests d&#x27;Irish Coffee.</p><p>On dit "
            "qu&#x27;en 1952, Sheridan se serait installé aux États-Unis "
            "après avoir accepté une place dans ce Buena Vista de San "
            "Francisco. Il y a une plaque commémorative sur sa tombe à "
            "Oakland en Californie sur laquelle il est inscrit qu&#x27;il "
            "est l&#x27;inventeur de l&#x27;une des boissons les plus "
            "consommées au monde.</p><p>Le musée de l&#x27;aéroport de "
            "Foynes tient chaque année en mai-juin un festival consacré à "
            "l&#x27;Irish Coffee, et inclue un championnat du monde de "
            "réalisation d&#x27;Irish Coffee.</p><p>Une petite parenthèse "
            "pour dire qu&#x27;une autre histoire existe quant à "
            "l&#x27;origine de l&#x27;Irish Coffee et raconte qu&#x27;il "
            "a été inventé par Joe Jackson à l&#x27;Ulster Hôtel situé à "
            "Ballybofey dans le comté irlandais de Donegal, un hôtel "
            "qu&#x27;il a acheté en 1945.</p><p>Conseil Cocktail Mag : La "
            "crème peut parfois difficilement tenir au dessus du café, "
            "c&#x27;est pour cette raison que de nombreux bar la remplace "
            "par de la chantilly même si ce n&#x27;est pas la recette "
            "originale. Petit conseil donc si vous avez du mal a faire "
            "tenir la crème : mélangez et battez de la chantilly avec de "
            "la crème liquide (50/50), et laissez reposer au frais "
            "quelques minutes. Plus léger, le mélange se superposera "
            "beaucoup mieux au dessus du café.</p>",
            "ingredients": [
                "4 cl de whisky irlandais (Jameson, etc.)",
                "12 cl de café chaud",
                "2 cl de sirop de sucre",
                "5 cl de crème liquide",
            ],
            "summary": "Le Irish Coffee : un cocktail chaud au whisky, caf et crème "
            "liquide.",
            "title": "Cocktail Irish Coffee",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre toddy</li>\n"
            "<li>mug</li>\n"
            "<li>Type&nbsp;: long drink (&gt;12cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>À propos</h2><p>La "
            "recette du Irish Cow se réalise aussi parfois avec du "
            "Baileys à la place du whisky pour rendre le cocktail encore "
            "plus doux.</p>",
            "ingredients": [
                "2/10 de whisky irlandais (Jameson, etc.)",
                "8/10 de lait chaud",
                "1 cuillère à café de sucre en poudre",
            ],
            "summary": "Le Irish Cow : un doux cocktail chaud signifiant &quot;vache "
            "irlandaise&quot;.",
            "title": "Cocktail Irish cow",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler</li>\n"
            "<li>Type&nbsp;: long drink (12cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Irish Rickey est une variante du "
            "célèbre cocktail Gin Rickey crée vers 1880. La recette de "
            "l&#x27;Irish Rickey apparaît notamment en 1994 dans Mr. "
            "Boston Official Bartender&#x27;s and Party Guide .</p>",
            "ingredients": [
                "4 cl de whisky irlandais (Jameson, etc.)",
                "3 cl de jus de citron vert",
                "5 cl d'eau gazeuse",
            ],
            "summary": "Le cocktail Irish Rickey : une recette dérivée du fameux Gin "
            "Rickey.",
            "title": "Cocktail Irish Rickey",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: tumbler 20cl</li>\n"
            "<li>Type&nbsp;: long drink (15cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>À propos</h2><p>Le "
            "cocktail Lynchburg Lemonade a la particularité d&#x27;être "
            "précisément réalisé avec du Tenessee Whiskey (Jack "
            "Daniel&#x27;s), un whisky américain assez proche du "
            "Bourbon.</p><p>Créée dans les années 1980, la recette porte "
            "le nom de la ville américaine où est implanté la distillerie "
            "de Jack Daniel&#x27;s, Lynchburg, dans l&#x27;État du "
            "Tenessee.</p>",
            "ingredients": [
                "4 cl de Jack Daniel's no.7",
                "3 cl de triple sec (Curaçao blanc)",
                "2 cl de jus de citron jaune",
                "6 cl de lemon/lime soda (Sprite ou 7up)",
            ],
            "summary": "Le cocktail Lynchburg Lemonade : une recette très désaltérante "
            "au Jack Daniel&#x27;s.",
            "title": "Cocktail Lynchburg Lemonade",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>On dit que le cocktail Manhattan aurait été "
            "créé au &quot;Manhattan Club&quot; de New York par Ian "
            "Marshall dans les années 1870. Il aurait été inventé à "
            "l&#x27;occasion d&#x27;un banquet réalisé par la mère de "
            "Winston Churchill en l&#x27;honneur de Samuel Tilden, "
            "candidat à la présidentielle.</p><p>La recette a été publiée "
            "plus tard en 1922 dans &quot;Cocktails : How to mix "
            "them&quot; de Robert Vermeire qui y indique que ce cocktail "
            "a été appelé ainsi en l&#x27;honneur du district de "
            "New-York.</p>",
            "ingredients": [
                "5 cl de whisky de seigle (Rye whiskey, etc.)",
                "2 cl de vermouth rouge (Martini...)",
                "Quelques gouttes d'Angostura bitters",
            ],
            "summary": "Le cocktail Manhattan : un digestif délicatement amérisé "
            "typiquement américain.",
            "title": "Cocktail Manhattan",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><p>Nous conseillons "
            "d&#x27;ajouter 2 cuillères à café d&#x27;eau avec le sucre "
            "et la menthe pour mieux diffuser les arômes de "
            "menthe.</p><h2>Histoire et origine</h2><p>La recette du "
            "cocktail Mint Julep est apparue pour la première fois en "
            "1803 dans une publication de John Davis qui écrit &quot;A "
            "dram of spirituous liquor that has mint in it, taken by "
            "Virginians in the morning&quot; (un petit verre de "
            "spiritueux qui comporte de la menthe, pris en Virginie dans "
            "la matinée), la consommation de ce cocktail pourrait "
            "remonter au XVIIème ou XVIIIème siècle. John Davis ne "
            "précise pas quel spiriteux était utilisé à l&#x27;origine, "
            "cette question fait encore débat. La recette est ensuite "
            "publiée en 1862 dans &quot;How to mix drinks&quot; de Jerry "
            "Thomas qui appelle à utiliser du brandy (Cognac...), et "
            "décline le Mint Julep en plusieurs variantes : le Brandy "
            "Julep, le Gin Julep, le Whiskey Julep et le Pineapple "
            "Julep.</p><p>Depuis 1938 grâce à Churchill Downs, le Mint "
            "Julep est la boisson phare du &quot;Kentucky Derby&quot;. Il "
            "s&#x27;agit d&#x27;une course hippique qui se déroule à "
            "Louisville dans l&#x27;état du Kentucky aux États-Unis. Sur "
            "2 jours, ce n&#x27;est pas moins de 80 000 mints juleps qui "
            "sont écoulés.</p>",
            "ingredients": [
                "5 cl de Whisky Bourbon",
                "1 cuillère à café de sucre en poudre",
                "5 à 7 feuilles de menthe fraîche",
            ],
            "summary": "Le Mint Julep : L&#x27;un des plus anciens cocktails !",
            "title": "Cocktail Mint Julep",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Old Fashioned est un ancien type "
            "de cocktail comme son nom l&#x27;indique, son nom est "
            "l&#x27;abrégé de &quot;Cocktail Whiskey Old-Fashioned&quot;. "
            "Son origine est incertaine mais on évoque souvent le Club "
            "Pendennis à Louisville du Kentucky aux États-Unis comme "
            "étant à l&#x27;origine de cette recette. Le Old Fashioned "
            "date quoiqu&#x27;il en soit d&#x27;avant 1862 puisque la "
            "recette est déjà publiée sous son ancien nom le "
            "&quot;Whiskey Cocktail&quot; dans &quot;How to mix "
            "drinks&quot; de Jerry Thomas.</p>",
            "ingredients": [
                "6 cl de whisky Bourbon",
                "1 morceau de sucre",
                "2 traits d'Angostura bitters",
            ],
            "summary": "Le cocktail Old Fashioned : Renouez avec un grand classique que "
            "le temps a fait oublier.",
            "title": "Cocktail Old Fashioned",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: martini</li>\n"
            "<li>Type&nbsp;: short drink (8cl)</li>\n"
            "<li>Temps&nbsp;: 5 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Paper Plane qui signifie "
            "&quot;Avion en papier&quot; est classé parmi les nouveaux "
            "cocktails classiques modernes de l&#x27;IBA (International "
            "Bartender Association), composé de Aperol il est à consommer "
            "en apéritif.</p><p>Le Paper Plane a été créé en 2007 par Sam "
            "Ross, barman du Milk&amp;Honey Bar à New-York. Sam Ross a "
            "baptisé son cocktail ainsi en l&#x27;honneur de la chanson "
            "de M.I.A. &quot;Paper planes&quot; qui a tourné en boucle "
            "pendant qu&#x27;il créait cette recette.</p><p>Peu exploité "
            "dans les cocktails, l&#x27;Amaro Nonino est une liqueur "
            "légèrement amère à base d&#x27;herbes et épices.</p>",
            "ingredients": [
                "2 cl de Whisky Bourbon",
                "2 cl d'Amaro (Amaro Nonino...)",
                "2 cl de Apérol",
                "2 cl de jus de citron pressé",
            ],
            "summary": "Le Paper Plane : un nouveau cocktail classique à base de Apérol "
            "qui signifie &quot;Avion en papier&quot;.",
            "title": "Cocktail Paper Plane",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: verre à cocktail</li>\n"
            "<li>Type&nbsp;: short drink (10cl)</li>\n"
            "<li>Temps&nbsp;: 3 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Rob Roy aurait été créé en 1894 à "
            "l&#x27;hôtel Waldorf à New York. Rob Roy était le surnom de "
            "Robert Roy MacGregor (1671-1734), un brigand et héros "
            "populaire écossais qui a inspiré un roman de Sir Walter "
            "Scott ainsi que des adaptations télévisées.</p><p>Le Rob Roy "
            "est la version écossaise du célèbre cocktail classique "
            "Manhattan, où le scotch whisky vient remplacer ici le rye "
            "whiskey du Manhattan.</p>",
            "ingredients": [
                "8 cl de Scotch whisky",
                "2 cl de vermouth rouge",
                "Quelques gouttes d'Angostura bitters",
            ],
            "summary": "Le cocktail Rob Roy : Une version écossaise du Manhattan qui "
            "porte le nom d&#x27;un ancien hors-la-loi.",
            "title": "Cocktail Rob Roy",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 2 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Rusty Nail est le plus célèbre "
            "des cocktails incorporant du Drambuie dans sa recette. Cette "
            "liqueur de whisky, sans lequel un Rusty Nail n&#x27;en "
            "serait pas un, adoucit véritablement le cocktail avec ses "
            "saveurs sucrées de miel, d&#x27;herbes et "
            "d&#x27;épices.</p><p>L&#x27;origine du Rusty Nail n&#x27;est "
            "pas réellement claire, on dit qu&#x27;il a été créé dans les "
            "années 1950 soit par Norman MacKinnon au &quot;New York Club "
            "21&quot;, soit par le barman Donato &quot;Duke&quot; Antone "
            "dont on dit aussi le créateur du cocktail Harvey "
            "Wallbanger.</p>",
            "ingredients": ["4,5 cl de scotch whisky", "2,5 cl de Drambuie"],
            "summary": "Le Rusty Nail : un cocktail de grand caractère signifiant "
            "&quot;clou rouillé&quot;.",
            "title": "Cocktail Rusty Nail",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au verre à "
            "mélange</li>\n"
            "<li>Verre&nbsp;: old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>La recette du Vieux Carré a été publié pour "
            "la première fois en 1938 dans Famous New Orleans Drinks and "
            "how to mix &#x27;em de Stanley Clisby Arthur . Son créateur "
            "est Walter Bergeron, qui était le chef barman du Montelone "
            "cocktail lounge , un établissement situé à la "
            "Nouvelle-Orléans aux États-Unis.</p><p>Walter Bergeron "
            "aurait nommé son cocktail ainsi pour faire honneur au "
            "célèbre quartier historique du même nom situé en "
            "Nouvelle-Orléans (Louisiane, USA).</p><p>Dans la recette "
            "originale publiée en 1938, Stanley Clisby Arthur indique que "
            "les Vieux Carrés peuvent être optionnellement décorés avec "
            "un quartier d&#x27;ananas et une cerise en plus du zeste de "
            "citron.</p>",
            "ingredients": [
                "3 cl de whisky de seigle (Rye whiskey, etc.)",
                "3 cl de Cognac",
                "3 cl de vermouth rouge",
                "1 cl de Bénédictine",
                "2 traits de Peychaud's Bitters",
            ],
            "summary": "Le Vieux Carré : un cocktail assez sec des années 1930.",
            "title": "Cocktail Vieux Carré",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: direct au "
            "verre</li>\n"
            "<li>Verre&nbsp;: verre old-fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Whiskey Julep fait partie de la "
            "famille des &quot;juleps&quot; dont le cocktail le plus "
            "célèbre est le Mint Julep. Ces deux recettes sont quasiment "
            "identiques, la seule différence est que le Mint Julep se "
            "réalise très précisément avec du whisky "
            "bourbon.</p><p>S&#x27;il existe 2 noms distincts pour une "
            "recette quasi identique, c&#x27;est parce qu&#x27;à "
            "l&#x27;origine le Mint Julep n&#x27;était pas forcément fait "
            "avec du whisky. Le Mint Julep était au départ réalisé avec "
            "n&#x27;importe quel spiriteux, puis en 1862 dans &quot;How "
            "to mix drinks&quot;, Jerry Thomas appelle à le réaliser avec "
            "du brandy et rhum (plus d&#x27;informations sur la page du "
            "Mint Julep ). Le Whiskey Julep apparaît aussi en 1862 dans "
            "ce même ouvrage de Jerry Thomas.</p>",
            "ingredients": [
                "5 cl de whiskey (irlandais ou américain)",
                "1 cuillère à café de sucre en poudre",
                "5 à 7 feuilles de menthe fraîche",
            ],
            "summary": "Le Whiskey Julep : un cocktail aujourd&#x27;hui identique au "
            "Mint Julep.",
            "title": "Cocktail Whiskey Julep",
        },
        {
            "description": "<h2>Comment faire</h2><ul><li>Technique&nbsp;: au "
            "shaker</li>\n"
            "<li>Verre&nbsp;: verre old fashioned</li>\n"
            "<li>Type&nbsp;: short drink (7cl)</li>\n"
            "<li>Temps&nbsp;: 4 mn</li></ul><h2>Histoire et "
            "origine</h2><p>Le cocktail Whisky Sour est souvent réalisé "
            "avec un trait de blanc d&#x27;œuf en plus, comme il "
            "n&#x27;est pas rare d&#x27;en trouver dans la famille des "
            "&quot;sours&quot;. Cette famille de cocktails étant très "
            "ancienne, l&#x27;origine du &quot;Whisky Sour&quot; "
            "n&#x27;est pas connue, la recette est publiée pour la "
            "première fois en 1862 dans &quot;How to mix drinks&quot; de "
            "Jerry Thomas.</p><p>De nombreuses variantes existent, la "
            "plus proche est le &quot;Scotch sour&quot; qui est réalisé "
            "avec du whisky écossais à la place du bourbon ou rye.</p>",
            "ingredients": [
                "3,5 cl de whisky (Bourbon ou Rye Whiskey)",
                "2 cl de jus de citron pressé et filtré",
                "1,5 cl de sirop de sucre",
            ],
            "summary": "Le Whisky Sour : le plus célèbre cocktail de la famille des "
            "&quot;sours&quot;.",
            "title": "Cocktail Whisky Sour",
        },
    ]
    quantities_assoc = {}
    for (quantity_type, label, value, min_value, max_value, step) in quantities:
        quantities_assoc[label] = Quantity.objects.create(
            created_by=user,
            updated_by=user,
            quantity_type=quantity_type,
            value=value if value is not None else None,
            min_value=min_value if min_value is not None else None,
            max_value=max_value if max_value is not None else None,
            step=step if step is not None else None,
        )
    units_assoc = {}
    for (name_singular, name_plural) in units:
        unit = Unit.objects.create(
            created_by=user,
            updated_by=user,
            name_singular=name_singular if name_singular is not None else None,
            name_plural=name_plural if name_plural is not None else None,
        )
        units_assoc[name_singular] = unit
        units_assoc[name_plural] = unit

    ingredients_assoc = {}
    for name_singular in ingredients:
        ingredient = Ingredient.objects.create(
            created_by=user,
            updated_by=user,
            name_singular=name_singular if name_singular is not None else None,
            name_plural=None,
        )
        ingredients_assoc[name_singular] = ingredient

    tags_tmp = {}
    for name in tags:
        tags_tmp[name] = Tag.objects.create(
            created_by=user,
            updated_by=user,
            name=name if name is not None else None,
        )

    quantities_txt = [q[1] for q in quantities]
    units_txt = set([u[0] for u in units] + [u[1] for u in units])

    tags_assoc = {}
    tags_tmp = []
    for tab_tags in tags:
        tags_tmp += tab_tags[1:]
    tags_tmp = set(tags_tmp)
    for tag in tags_tmp:
        tags_assoc[tag] = Tag.objects.create(
            created_by=user,
            updated_by=user,
            name=tag,
        )
    tags_by_id = {t[0]: t[1:] for t in tags}

    idx_tag = 0
    try:
        for cocktail in cocktails:
            title = cocktail["title"]
            if title.lower().startswith('cocktail '):
                title = title[9:]
            c = Cocktail.objects.create(
                created_by=user,
                updated_by=user,
                description=cocktail["description"],
                summary=cocktail["summary"],
                title=title,
            )
            for ingredient in cocktail["ingredients"]:
                # print(ingredient)
                i_split = ingredient.split(" ")
                quantity = i_split[0].strip()
                quantity = quantity.lower()
                # by default:
                ingredient_final = ingredient.strip()
                unit = '??'
                if ingredient == "1,5 de vermouth rouge (Martini...)":
                    quantity = "1,5"
                    unit = "l"
                    ingredient_final = " ".join(i_split[2:])
                elif ingredient == "1 demi banane pelée":
                    quantity = "1"
                    unit = "/2"
                    ingredient_final = " ".join(i_split[2:])
                elif ingredient == "1 demi fruit de la passion":
                    quantity = "1"
                    unit = "/2"
                    ingredient_final = " ".join(i_split[2:])
                elif ingredient == "1 demi cuillère à café de sucre en poudre":
                    quantity = "1 demi"
                    unit = "cuillère à café"
                    ingredient_final = " ".join(i_split[6:])
                elif ingredient == "1 demi-pincée de sel":
                    quantity = "1 demi"
                    unit = "pincée"
                    ingredient_final = " ".join(i_split[3:])
                elif (
                    ingredient == "Noix de muscade râpée"
                    or ingredient == "Cannelle en poudre"
                    or ingredient == "Crème fouettée / chantilly"
                    or ingredient == "Poudre de cacao"
                    or ingredient == "Cannelle râpée ou en poudre"
                    or ingredient == "Crème fouettée/chantilly"
                    or ingredient == "Chantilly / Crème fouettée"
                    or ingredient == "Noix de muscade en poudre"
                    or ingredient == "Sel et/ou sel de céleri et/ou poivre"
                    or ingredient == 'Tonic (Schweppes...)'
                    or ingredient == (
                        "Fruits selon votre envie (citrons, oranges, "
                        "bananes, pommes, fraises...)"
                    )
                ):
                    quantity = unit = None
                elif ingredient == "Sucre fin en poudre":
                    quantity = unit = None
                    ingredient_final = "Sucre fin en poudre"
                elif ingredient == "Quelques mûres":
                    quantity = unit = None
                    ingredient_final = "mûres"
                elif ingredient == "Tabasco":
                    quantity = unit = None
                    ingredient_final = "Tabasco"
                elif ingredient == "Le blanc d'un petit oeuf":
                    quantity = "1"
                    unit = None
                    ingredient_final = "blanc d'œuf"
                elif len(i_split) > 1:
                    if len(i_split) > 2 and i_split[2] == "de":
                        ingredient_final = " ".join(i_split[3:])
                    unit = i_split[1].strip()
                    if (
                        quantity == "Fruits"
                        or quantity == "Tonic"
                        or unit == "Sel"
                    ):
                        quantity = None
                        unit = None
                    elif unit == "framboises" or unit == "noix":
                        unit = None
                        ingredient_final = " ".join(i_split[1:])
                    elif (
                        unit == "citron"
                        or unit == "orange"
                        or unit == "mangue"
                        or unit == "cerise"
                        or unit == "fraises"
                        or unit == "banane"
                        or unit == "banane"
                        or unit == "bière"
                    ):
                        quantity = "1"
                        unit = None
                        ingredient_final = " ".join(i_split[1:])
                    elif unit == "demi" and i_split[2] == "citron":
                        quantity = "1 demi"
                        unit = None
                        ingredient_final = " ".join(i_split[2:])
                    elif unit == "ou":
                        # "2 ou 3 traits d'Orange Bitters"
                        quantity = (
                            f"{i_split[0]} " f"{i_split[1]} " f"{i_split[2]}"
                        )
                        unit = i_split[3]
                        if len(i_split) > 5 and i_split[4].startswith("d'"):
                            ingredient_final = "{} {}".format(
                                i_split[4][2:], " ".join(i_split[5:])
                            )
                        elif len(i_split) > 6 and i_split[4] == "de":
                            ingredient_final = " ".join(i_split[5:])
                    elif unit == "oeuf" or unit == "jaune" or unit == "blanc":
                        unit = None
                        ingredient_final = " ".join(i_split[1:])
                        # print(f"{ingredient_final=}")
                    elif quantity.endswith("%"):
                        quantity = quantity[:-1]
                        unit = "%"
                    elif "/" in quantity:
                        quantity, unit = quantity.split("/")
                        unit = "/" + unit
                    elif unit == "de":
                        print(f"? -> {quantity=} -> {ingredient=}")
                    elif unit == "à":  # "5 à 7 feuilles"
                        quantity = f"{quantity} {unit} {i_split[2].strip()}"
                        unit = i_split[3].strip()
                    elif unit not in units_txt:
                        if "cuillère" in unit:
                            unit = (
                                f"{i_split[1]} "
                                f"{i_split[2]} "
                                f"{i_split[3]}"
                            )
                            if len(i_split) > 2 and i_split[4] == "de":
                                ingredient_final = " ".join(i_split[5:])
                            elif len(i_split) > 2 and i_split[4] == "d'une":
                                ingredient_final = " ".join(i_split[5:])
                    if ingredient == ingredient_final:
                        if len(i_split) > 2 and i_split[1] == "de":
                            ingredient_final = " ".join(i_split[2:])
                        elif len(i_split) > 2 and i_split[2].startswith("d'"):
                            ingredient_final = "{} {}".format(
                                i_split[2][2:], " ".join(i_split[3:])
                            )
                        elif len(i_split) > 5 and i_split[4] == "de":
                            ingredient_final = " ".join(i_split[5:])
                ingredient_final = ingredient_final.strip()
                if (
                    ingredient_final == "Angostura bitter"
                    or ingredient_final == "Angostura Bitter"
                    or ingredient_final == "Angostura bitters"
                ):
                    ingredient_final = "Angostura bitters"

                elif ingredient_final == "Peychaud's Bitter":
                    ingredient_final = "Peychaud's Bitters"
                elif (
                    ingredient_final == "vermouth doux (Martini...)"
                    or ingredient_final
                    == "vermouth blanc extra dry (Martini...)"
                    or ingredient_final
                    == "vermouth blanc (Martini, Noilly prat...)"
                    or ingredient_final == "vermouth dry (Martini...)"
                ):
                    ingredient_final = (
                        "vermouth dry (Martini extra dry, Noilly Prat dry)"
                    )
                if ingredient_final not in ingredients:
                    raise Exception(f"{ingredient=} -> {ingredient_final=}")
                if quantity not in quantities_assoc:
                    raise Exception(f"? quantity {quantity=} -> {unit=} -> {ingredient_final=}")
                if unit not in units_assoc:
                    raise Exception(f"? unit {quantity=} -> {unit=} -> {ingredient_final=}")
                if ingredient_final not in ingredients_assoc:
                    raise Exception(f"? ingredient {quantity=} -> {unit=} -> {ingredient_final=}")
                CocktailIngredient.objects.create(
                    created_by=user,
                    updated_by=user,
                    cocktail=c,
                    ingredient=ingredients_assoc[ingredient_final],
                    quantity=quantities_assoc[quantity],
                    unit=units_assoc[unit]
                )
            for tag in tags_by_id[idx_tag]:
                c.tags.add(tags_assoc[tag])
            idx_tag += 1
    except Exception as e:
        print(str(e))
        raise


def empty_tables(apps, schema_editor):
    Quantity = apps.get_model("main", "Quantity")
    Unit = apps.get_model("main", "Unit")
    Ingredient = apps.get_model("main", "Ingredient")
    Tag = apps.get_model("main", "Tag")
    Cocktail = apps.get_model("main", "Cocktail")
    Cocktail.objects.all().delete()
    Quantity.objects.all().delete()
    Unit.objects.all().delete()
    Ingredient.objects.all().delete()
    Tag.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_tables, empty_tables),
    ]
