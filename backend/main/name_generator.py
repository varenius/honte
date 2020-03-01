import random
import logging


COLOURS = ["Bronze", "IndianRed", "LightCoral", "Salmon", "DarkSalmon", "LightSalmon", "Crimson", "Red", "FireBrick",
           "DarkRed", "Pink", "LightPink", "HotPink", "DeepPink", "MediumVioletRed", "PaleVioletRed",
           "Coral", "Tomato", "OrangeRed", "DarkOrange", "Orange", "Gold", "Yellow", "LightYellow", "LemonChiffon",
           "LightGoldenrodYellow", "PapayaWhip", "Moccasin", "PeachPuff", "PaleGoldenrod", "Khaki", "DarkKhaki",
           "Lavender", "Thistle", "Plum", "Violet", "Orchid", "Fuchsia", "Magenta", "MediumOrchid", "MediumPurple",
           "Amethyst", "BlueViolet", "DarkViolet", "DarkOrchid", "DarkMagenta", "Purple", "Indigo", "SlateBlue",
           "DarkSlateBlue", "MediumSlateBlue", "GreenYellow", "Chartreuse", "LawnGreen", "Lime", "LimeGreen",
           "PaleGreen", "LightGreen", "MediumSpringGreen", "SpringGreen", "MediumSeaGreen", "SeaGreen", "ForestGreen",
           "Green", "DarkGreen", "YellowGreen", "OliveDrab", "Olive", "DarkOliveGreen", "MediumAquamarine",
           "DarkSeaGreen", "LightSeaGreen", "DarkCyan", "Teal", "Aqua", "Cyan", "LightCyan", "PaleTurquoise",
           "Aquamarine", "Turquoise", "MediumTurquoise", "DarkTurquoise", "CadetBlue", "SteelBlue", "LightSteelBlue",
           "PowderBlue", "LightBlue", "SkyBlue", "LightSkyBlue", "DeepSkyBlue", "DodgerBlue", "CornflowerBlue",
           "RoyalBlue", "Blue", "MediumBlue", "DarkBlue", "Navy", "MidnightBlue", "Cornsilk",
           "BlanchedAlmond", "Bisque", "NavajoWhite", "Wheat", "BurlyWood", "Tan", "RosyBrown", "SandyBrown",
           "Goldenrod", "DarkGoldenrod", "Peru", "Chocolate", "SaddleBrown", "Sienna", "Brown", "Maroon", "White",
           "Snow", "Honeydew", "MintCream", "Azure", "AliceBlue", "GhostWhite", "WhiteSmoke", "Seashell", "Beige",
           "OldLace", "FloralWhite", "Ivory", "AntiqueWhite", "Linen", "LavenderBlush", "MistyRose", "Gainsboro",
           "LightGrey", "Silver", "DarkGray", "Gray", "DimGray", "LightSlateGray", "SlateGray", "DarkSlateGray",
           "Black"]
ANIMALS = ["Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater", "Antelope", "Ape", "Armadillo", "Ass",
           "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Bird", "Bison", "Boar", "Buffalo",
           "Butterfly", "Camel", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cattle", "Chamois", "Cheetah",
           "Chicken", "Chimpanzee", "Chinchilla", "Chough", "Coati", "Cobra", "Cockroach", "Cod", "Cormorant", "Coyote",
           "Crab", "Crane", "Crocodile", "Crow", "Curlew", "Deer", "Dinosaur", "Dog", "Dogfish", "Dolphin", "Donkey",
           "Dotterel", "Dove", "Dragonfly", "Duck", "Dugong", "Dunlin", "Eagle", "Echidna", "Eel", "Eland", "Elephant",
           "ElephantSeal", "Elk", "Emu", "Falcon", "Ferret", "Finch", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Gaur",
           "Gazelle", "Gerbil", "Giant panda", "Giraffe", "Gnat", "Gnu", "Goat", "Goldfinch", "Goosander", "Goose",
           "Gorilla", "Goshawk", "Grasshopper", "Grouse", "Guanaco", "GuineaFowl", "GuineaPig", "Gull", "Hamster",
           "Hare", "Hawk", "Hedgehog", "Heron", "Herring", "Hippo", "Hornet", "Horse", "Hummingbird", "Hyena", "Ibex",
           "Ibis", "Jackal", "Jaguar", "Jay", "Jellyfish", "Kangaroo", "Kinkajou", "Koala", "KomodoDragon", "Kouprey",
           "Kudu", "Lapwing", "Lark", "Lemur", "Leopard", "Lion", "Llama", "Lobster", "Locust", "Loris", "Louse",
           "Lyrebird", "Magpie", "Mallard", "Mammoth", "Manatee", "Mandrill", "Mink", "Mole", "Mongoose", "Monkey",
           "Moose", "Mouse", "Mosquito", "Narwhal", "Newt", "Nightingale", "Octopus", "Okapi", "Opossum", "Ostrich",
           "Otter", "Owl", "Oyster", "Panther", "Parrot", "Panda", "Partridge", "Peafowl", "Pelican", "Penguin",
           "Pheasant", "Pig", "Pigeon", "Polar bear", "Pony", "Porcupine", "Porpoise", "PrairieDog", "Quail", "Quelea",
           "Quetzal", "Rabbit", "Raccoon", "Ram", "Rat", "Raven", "Reindeer", "Rhinoceros", "Rook", "Salamander",
           "Salmon", "SandDollar", "Sandpiper", "Sardine", "SeaLion", "Seahorse", "Seal", "Shark", "Sheep", "Shrew",
           "Skunk", "Sloth", "Snail", "Snake", "Spider", "Squirrel", "Starling", "Stegosaurus", "Swan", "Tapir",
           "Tarsier", "Termite", "Tiger", "Toad", "Turkey", "Turtle", "Vicuna", "Wallaby", "Walrus", "Wasp",
           "WaterBuffalo", "Weasel", "Whale", "Wolf", "Wolverine", "Wombat", "Wren", "Yak", "Zebra"]


class _NameGenerator:
    def __init__(self):
        self.names = iter([])

    def get_name(self, add_number):
        try:
            return next(self.names)
        except StopIteration:
            if add_number:
                number = random.randint(0, 1000)
                log = logging.getLogger('fakedata.name_generator')
                log.info('number: {}'.format(number))
                all_names = [(colour, f'{animal}{str(number)}')
                             for animal in ANIMALS
                             for colour in COLOURS]
            else:
                all_names = [(colour, animal)
                             for animal in ANIMALS
                             for colour in COLOURS]
            random.shuffle(all_names)
            self.names = iter(all_names)
            return self.get_name(add_number)


_nameGenerator = _NameGenerator()


def get_name(add_number: bool = True):
    return _nameGenerator.get_name(add_number)
