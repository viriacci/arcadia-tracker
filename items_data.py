# -*- coding: utf-8 -*-
"""
Baza wielkości stacków dla przedmiotów Minecraft.
Domyślnie: 64. Poniżej wyjątki (16 i 1).
To są tylko liczby z mechaniki gry — nie zawiera żadnych grafik ani
tekstur (te są własnością Mojang/Microsoft i nie są tu rozpowszechniane).
"""

STACK_16 = {
    "Ender Pearl", "Perła Endera",
    "Egg", "Jajko",
    "Snowball", "Śnieżka",
    "Bucket", "Wiadro",
    "Water Bucket", "Wiadro wody",
    "Lava Bucket", "Wiadro lawy",
    "Milk Bucket", "Wiadro mleka",
    "Sign", "Tabliczka",
    "Honey Bottle", "Butelka miodu",
    "Boat", "Łódka",
    "Minecart", "Wagonik",
    "Chest Minecart", "Wagonik ze skrzynią",
}

STACK_1 = {
    "Sword", "Miecz",
    "Pickaxe", "Kilof",
    "Axe", "Siekiera",
    "Shovel", "Łopata",
    "Hoe", "Motyka",
    "Helmet", "Hełm",
    "Chestplate", "Napierśnik",
    "Leggings", "Spodnie",
    "Boots", "Buty",
    "Shield", "Tarcza",
    "Bow", "Łuk",
    "Crossbow", "Kusza",
    "Trident", "Trójząb",
    "Fishing Rod", "Wędka",
    "Elytra", "Lotniki",
    "Saddle", "Siodło",
    "Potion", "Mikstura",
    "Splash Potion", "Rzucana mikstura",
    "Lingering Potion", "Zalegająca mikstura",
    "Enchanted Book", "Zaczarowana księga",
    "Cake", "Ciasto",
    "Totem of Undying", "Totem Nieśmiertelności",
    "Shears", "Nożyce",
    "Flint and Steel", "Krzesiwo",
    "Clock", "Zegar",
    "Compass", "Kompas",
    "Map", "Mapa",
    "Book and Quill", "Księga i pióro",
    "Written Book", "Zapisana księga",
    "Armor Stand", "Stojak na zbroję",
    "Cauldron", "Kocioł",
    "Anvil", "Kowadło",
    "Music Disc", "Płyta muzyczna",
    "Banner", "Chorągiew",
    "Bed", "Łóżko",
    "Spawner", "Jajko przywoływacza (Spawner)",
    "Name Tag", "Metka",
    "Lead", "Smycz",
}

# Popularne itemy do podpowiadania w polu wyszukiwania (nazwa: stack size)
COMMON_ITEMS = {}
for name in [
    "Stone", "Kamień", "Cobblestone", "Bruk", "Dirt", "Ziemia", "Grass Block", "Blok trawy",
    "Oak Log", "Kłoda dębu", "Oak Planks", "Deski dębowe", "Sand", "Piasek", "Gravel", "Żwir",
    "Iron Ore", "Ruda żelaza", "Iron Ingot", "Sztabka żelaza", "Gold Ore", "Ruda złota",
    "Gold Ingot", "Sztabka złota", "Diamond", "Diament", "Diamond Ore", "Ruda diamentu",
    "Emerald", "Szmaragd", "Coal", "Węgiel", "Redstone", "Redstone Dust", "Redstone (proch)",
    "Lapis Lazuli", "Lazuryt", "Netherite Ingot", "Sztabka netherytu", "Netherite Scrap", "Złom netherytu",
    "Quartz", "Kwarc", "Obsidian", "Obsydian", "Glowstone Dust", "Pył jasnogłazu",
    "String", "Sznurek", "Feather", "Pióro", "Leather", "Skóra", "Bone", "Kość",
    "Gunpowder", "Proch strzelniczy", "Spider Eye", "Oko pająka", "Rotten Flesh", "Zgniłe mięso",
    "Wheat", "Pszenica", "Wheat Seeds", "Nasiona pszenicy", "Bread", "Chleb",
    "Sugar Cane", "Trzcina cukrowa", "Sugar", "Cukier", "Pumpkin", "Dynia", "Melon", "Melon",
    "Cocoa Beans", "Ziarna kakaowca", "Apple", "Jabłko", "Carrot", "Marchewka", "Potato", "Ziemniak",
    "Nether Wart", "Zarodnia netheru", "Blaze Rod", "Różdżka blaze", "Blaze Powder", "Proszek blaze",
    "Ghast Tear", "Łza ghasta", "Slime Ball", "Kula śluzu", "Magma Cream", "Krem magmowy",
    "Ender Eye", "Oko Endera", "Shulker Shell", "Skorupa shulkera", "Phantom Membrane", "Membrana zjawy",
    "Amethyst Shard", "Odłamek ametystu", "Copper Ingot", "Sztabka miedzi", "Raw Copper", "Surowa miedź",
    "Raw Iron", "Surowe żelazo", "Raw Gold", "Surowe złoto", "Clay Ball", "Kula gliny",
    "Brick", "Cegła", "Nether Brick", "Cegła netheru", "Glass", "Szkło", "Sandstone", "Piaskowiec",
    "Wool", "Wełna", "TNT", "Ender Pearl", "Perła Endera", "Egg", "Jajko",
]:
    STACK_1_HIT = name in STACK_1
    STACK_16_HIT = name in STACK_16
    COMMON_ITEMS[name] = 1 if STACK_1_HIT else (16 if STACK_16_HIT else 64)


def get_stack_size(item_name: str) -> int:
    """Zwraca wielkość stacku dla danej nazwy przedmiotu (domyślnie 64)."""
    name = item_name.strip()
    if name in STACK_1:
        return 1
    if name in STACK_16:
        return 16
    if name in COMMON_ITEMS:
        return COMMON_ITEMS[name]
    return 64


def known_item_names():
    names = set(COMMON_ITEMS.keys()) | STACK_1 | STACK_16
    return sorted(names)
