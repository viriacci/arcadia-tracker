# -*- coding: utf-8 -*-
"""
Baza przedmiotów Minecraft Java Edition 1.21.11.

Źródło wersji: minecraft-data 1.21.11 / rejestr Items Yarn 1.21.11.
Nazwy polskie są używane jako główne aliasy, angielskie pozostają jako aliasy
kompatybilności. Dane są pogrupowane, żeby kolejne wersje można było łatwo
rozbudowywać.

Stack size: 64 / 16 / 1.
"""

# Wszystkie zwykłe przedmioty i bloki układające się w stack po 64.
STACK_64 = set()

# Przedmioty układające się po 16.
STACK_16 = {
    "Perła Endera", "Ender Pearl",
    "Jajko", "Egg",
    "Śnieżka", "Snowball",
    "Wiadro", "Bucket",
    "Wiadro wody", "Water Bucket",
    "Wiadro lawy", "Lava Bucket",
    "Wiadro mleka", "Milk Bucket",
    "Butelka miodu", "Honey Bottle",
    "Tabliczka", "Sign",
    "Wisząca tabliczka", "Hanging Sign",
    "Sadzonka", "Sapling",
}

# Przedmioty niemające stackowania (maks. 1).
STACK_1 = {
    # Narzędzia / broń
    "Miecz", "Sword", "Kilof", "Pickaxe", "Siekiera", "Axe",
    "Łopata", "Shovel", "Motyka", "Hoe",
    "Łuk", "Bow", "Kusza", "Crossbow", "Trójząb", "Trident",
    "Wędka", "Fishing Rod", "Nożyce", "Shears",
    "Krzesiwo", "Flint and Steel",
    "Tarcza", "Shield", "Lotnia", "Elytra",
    "Siodło", "Saddle",
    "Zaczarowana księga", "Enchanted Book",
    "Księga i pióro", "Book and Quill", "Zapisana księga", "Written Book",
    "Mapa", "Map", "Zegar", "Clock", "Kompas", "Compass",
    "Metka", "Name Tag", "Stojak na zbroję", "Armor Stand",
    "Kocioł", "Cauldron", "Kowadło", "Anvil",
    "Totem nieśmiertelności", "Totem of Undying",
    "Ciasto", "Cake",
    "Łódka", "Boat", "Łódka dębowa", "Oak Boat", "Łódka świerkowa", "Spruce Boat",
    "Łódka brzozowa", "Birch Boat", "Łódka dżunglowa", "Jungle Boat",
    "Łódka akacjowa", "Acacia Boat", "Łódka z ciemnego dębu", "Dark Oak Boat",
    "Łódka mangrowa", "Mangrove Boat", "Łódka bambusowa", "Bamboo Raft",
    "Wagonik", "Minecart", "Wagonik ze skrzynią", "Chest Minecart",
    "Wagonik z piecem", "Furnace Minecart", "Wagonik z TNT", "TNT Minecart",
    "Wagonik z lejem", "Hopper Minecart",
    "Płyta muzyczna", "Music Disc",
    "Chorągiew", "Banner",
    "Mikstura", "Potion", "Mikstura miotana", "Splash Potion",
    "Mikstura utrzymująca się", "Lingering Potion",
    "Jajko przyzywające", "Spawn Egg", "Jajko przywołujące", "Spawner",
    # Zbroje
    "Hełm", "Helmet", "Napierśnik", "Chestplate", "Spodnie", "Leggings",
    "Buty", "Boots",
    # Nowe 1.21.11
    "Włócznia", "Spear",
    "Drewniana włócznia", "Wooden Spear",
    "Kamienna włócznia", "Stone Spear",
    "Miedziana włócznia", "Copper Spear",
    "Żelazna włócznia", "Iron Spear",
    "Złota włócznia", "Golden Spear",
    "Diamentowa włócznia", "Diamond Spear",
    "Netherytowa włócznia", "Netherite Spear",
    "Miedziana zbroja nautilusa", "Copper Nautilus Armor",
    "Żelazna zbroja nautilusa", "Iron Nautilus Armor",
    "Złota zbroja nautilusa", "Golden Nautilus Armor",
    "Diamentowa zbroja nautilusa", "Diamond Nautilus Armor",
    "Netherytowa zbroja nautilusa", "Netherite Nautilus Armor",
    "Netherytowa zbroja konia", "Netherite Horse Armor",
}

# Nazwy główne: polski -> angielski. Pozostałe rodziny są generowane niżej.
ITEMS = {
    # Podstawowe bloki
    "Kamień": "Stone", "Granit": "Granite", "Polerowany granit": "Polished Granite",
    "Dioryt": "Diorite", "Polerowany dioryt": "Polished Diorite",
    "Andezyt": "Andesite", "Polerowany andezyt": "Polished Andesite",
    "Łupek": "Deepslate", "Łupek bruzdowany": "Cobbled Deepslate",
    "Polerowany łupek": "Polished Deepslate", "Kalcyt": "Calcite",
    "Tuf": "Tuff", "Tuf ciosany": "Chiseled Tuff", "Polerowany tuf": "Polished Tuff",
    "Głębinowy łupek": "Deepslate",
    "Ziemia": "Dirt", "Trawiasta ziemia": "Grass Block", "Kamień łupkowy": "Stone",
    "Bruk": "Cobblestone", "Żwir": "Gravel", "Piasek": "Sand",
    "Czerwony piasek": "Red Sand", "Piaskowiec": "Sandstone",
    "Czerwony piaskowiec": "Red Sandstone", "Glina": "Clay",
    "Kula gliny": "Clay Ball", "Szkło": "Glass", "Szyba": "Glass Pane",
    "Obsydian": "Obsidian", "Skała macierzysta": "Bedrock",
    "Netherrack": "Netherrack", "Bazalt": "Basalt", "Czarnokamień": "Blackstone",
    "Złocony czarnokamień": "Gilded Blackstone",
    "Kwarc": "Quartz", "Ruda kwarcu": "Nether Quartz Ore",
    "Piaskowiec netherowy": "Nether Bricks",
    "Kamień końca": "End Stone", "Purpur": "Purpur",
    "Blok ametystu": "Amethyst Block", "Odłamek ametystu": "Amethyst Shard",
    "Grudka żelaza": "Iron Nugget", "Grudka złota": "Gold Nugget",
    "Sztabka żelaza": "Iron Ingot", "Sztabka złota": "Gold Ingot",
    "Sztabka miedzi": "Copper Ingot", "Sztabka netherytu": "Netherite Ingot",
    "Surowe żelazo": "Raw Iron", "Surowe złoto": "Raw Gold", "Surowa miedź": "Raw Copper",
    "Diament": "Diamond", "Szmaragd": "Emerald", "Węgiel": "Coal",
    "Lazuryt": "Lapis Lazuli", "Pył redstone": "Redstone",
    "Pył jasnogłazu": "Glowstone Dust", "Proch": "Gunpowder",
    "Sznurek": "String", "Pióro": "Feather", "Skóra": "Leather", "Kość": "Bone",
    "Zgniłe mięso": "Rotten Flesh", "Oko pająka": "Spider Eye",
    "Kula śluzu": "Slime Ball", "Krem magmowy": "Magma Cream",
    "Łza ghasta": "Ghast Tear", "Pręt blaze": "Blaze Rod", "Proszek blaze": "Blaze Powder",
    "Oko Endera": "Eye of Ender", "Skorupa shulkera": "Shulker Shell",
    "Membrana zjawy": "Phantom Membrane", "Złom netherytu": "Netherite Scrap",
    "Starożytne zgliszcza": "Ancient Debris",
    # Rośliny / jedzenie
    "Pszenica": "Wheat", "Nasiona pszenicy": "Wheat Seeds", "Chleb": "Bread",
    "Trzcina cukrowa": "Sugar Cane", "Cukier": "Sugar", "Dynia": "Pumpkin",
    "Melon": "Melon", "Nasiona melona": "Melon Seeds", "Jabłko": "Apple",
    "Marchewka": "Carrot", "Ziemniak": "Potato", "Burak": "Beetroot",
    "Nasiona buraka": "Beetroot Seeds", "Zupa buraczana": "Beetroot Soup",
    "Kakao": "Cocoa Beans", "Zarodnia netheru": "Nether Wart",
    "Grzyb": "Mushroom", "Kaktus": "Cactus", "Kwiat kaktusa": "Cactus Flower",
    "Mączka kostna": "Bone Meal", "Bambus": "Bamboo", "Kelp": "Kelp",
    "Trawa morska": "Seagrass", "Wodorost": "Dried Kelp",
    # Drewno
    "Kłoda dębu": "Oak Log", "Kłoda świerku": "Spruce Log",
    "Kłoda brzozy": "Birch Log", "Kłoda dżungli": "Jungle Log",
    "Kłoda akacji": "Acacia Log", "Kłoda wiśni": "Cherry Log",
    "Kłoda ciemnego dębu": "Dark Oak Log", "Kłoda mangrowca": "Mangrove Log",
    "Pień szkarłatny": "Crimson Stem", "Pień spaczony": "Warped Stem",
    "Kłoda jasnego dębu": "Pale Oak Log",
    "Deski dębowe": "Oak Planks", "Deski świerkowe": "Spruce Planks",
    "Deski brzozowe": "Birch Planks", "Deski dżunglowe": "Jungle Planks",
    "Deski akacjowe": "Acacia Planks", "Deski wiśniowe": "Cherry Planks",
    "Deski z ciemnego dębu": "Dark Oak Planks", "Deski z jasnego dębu": "Pale Oak Planks",
    "Deski mangrowe": "Mangrove Planks", "Deski bambusowe": "Bamboo Planks",
    "Deski szkarłatne": "Crimson Planks", "Deski spaczone": "Warped Planks",
    # Inne
    "Papier": "Paper", "Książka": "Book", "Szmaragd": "Emerald",
    "Wiaderko": "Bucket", "Perła Endera": "Ender Pearl",
}

# Rodziny materiałów. Nazwy są dopisywane do ITEMS automatycznie.
WOOD_TYPES = {
    "dębowy": "Oak", "świerkowy": "Spruce", "brzozowy": "Birch",
    "dżunglowy": "Jungle", "akacjowy": "Acacia", "wiśniowy": "Cherry",
    "z ciemnego dębu": "Dark Oak", "z jasnego dębu": "Pale Oak", "mangrowy": "Mangrove",
    "bambusowy": "Bamboo", "szkarłatny": "Crimson", "spaczony": "Warped",
}

COLORS = {
    "biały": "White", "pomarańczowy": "Orange", "purpurowy": "Magenta",
    "jasnoniebieski": "Light Blue", "żółty": "Yellow", "limonkowy": "Lime",
    "różowy": "Pink", "szary": "Gray", "jasnoszary": "Light Gray",
    "cyjan": "Cyan", "fioletowy": "Purple", "niebieski": "Blue",
    "brązowy": "Brown", "zielony": "Green", "czerwony": "Red", "czarny": "Black",
}

# Elementy rodzinowe, które występują w ogromnej liczbie wariantów.
WOOD_PARTS = {
    "deski": "Planks", "schody": "Stairs", "płyta": "Slab", "płot": "Fence",
    "furtka": "Fence Gate", "drzwi": "Door", "klapa": "Trapdoor",
    "przycisk": "Button", "płytka naciskowa": "Pressure Plate",
    "znak": "Sign", "wiszący znak": "Hanging Sign", "łódka": "Boat",
    "łódka ze skrzynią": "Chest Boat", "liście": "Leaves", "drewno": "Wood",
}

for pl, en in WOOD_TYPES.items():
    for pl_part, en_part in WOOD_PARTS.items():
        ITEMS[f"{pl} {pl_part}"] = f"{en} {en_part}"

# Kolorowe rodziny.
for pl_color, en_color in COLORS.items():
    ITEMS[f"{pl_color} wełna"] = f"{en_color} Wool"
    ITEMS[f"{pl_color} beton"] = f"{en_color} Concrete"
    ITEMS[f"{pl_color} cement"] = f"{en_color} Concrete Powder"
    ITEMS[f"{pl_color} szkło"] = f"{en_color} Stained Glass"
    ITEMS[f"{pl_color} szyba"] = f"{en_color} Stained Glass Pane"
    ITEMS[f"{pl_color} terakota"] = f"{en_color} Terracotta"
    ITEMS[f"{pl_color} dywan"] = f"{en_color} Carpet"
    ITEMS[f"{pl_color} łóżko"] = f"{en_color} Bed"
    ITEMS[f"{pl_color} świeca"] = f"{en_color} Candle"
    ITEMS[f"{pl_color} shulkerowa skrzynia"] = f"{en_color} Shulker Box"
    ITEMS[f"{pl_color} sztandar"] = f"{en_color} Banner"

# Kopie angielskie istnieją jako aliasy.
ALIASES = {en: pl for pl, en in ITEMS.items()}

# Wszystkie elementy ITEM_DATA mają jeden format:
# {"name": polska_nazwa, "id": minecraft_id, "stack_size": 64/16/1}
ITEM_DATA = {}

def _slug(value: str) -> str:
    return value.lower().replace(" ", "_").replace("-", "_").replace("'", "")

for pl_name, en_name in ITEMS.items():
    ITEM_DATA[pl_name] = {
        "name": pl_name,
        "id": f"minecraft:{_slug(en_name)}",
        "stack_size": 1 if (pl_name in STACK_1 or en_name in STACK_1)
                     else 16 if (pl_name in STACK_16 or en_name in STACK_16)
                     else 64,
    }

for en_name, pl_name in ALIASES.items():
    ITEM_DATA[en_name] = ITEM_DATA[pl_name]

# Znane wyjątki stackowania, których nie chcemy zostawić jako 64.
for name in STACK_16:
    if name in ITEM_DATA:
        ITEM_DATA[name]["stack_size"] = 16
for name in STACK_1:
    if name in ITEM_DATA:
        ITEM_DATA[name]["stack_size"] = 1

def get_stack_size(item_name: str) -> int:
    """Zwraca maksymalny stack dla nazwy. Nieznany przedmiot domyślnie: 64."""
    name = item_name.strip()
    if name in ITEM_DATA:
        return ITEM_DATA[name]["stack_size"]
    return 64

def known_item_names():
    """Lista nazw do autocomplete, posortowana alfabetycznie."""
    return sorted(ITEM_DATA.keys(), key=str.casefold)
