from typing import TypedDict
import emotes


class Rarity(TypedDict):
    name: str
    multiplier: float
    probability: float


class Catch(TypedDict):
    name: str
    value: int


RARITIES: list[Rarity] = [
    { "name": "common",   "multiplier": 0.8,  "probability": 0.5   },
    { "name": "uncommon", "multiplier": 1.0,  "probability": 0.3   },
    { "name": "rare",     "multiplier": 2.5,  "probability": 0.15  },
    { "name": "mythical", "multiplier": 10.0, "probability": 0.045 },
    { "name": "godly",    "multiplier": 50.0, "probability": 0.005 },
]

CATCHES: list[Catch] = [
    { "name": "Cardboard Box",            "value": 5   },
    { "name": "Eliv Plush",               "value": 100 },
    { "name": "Nwero Plush",              "value": 100 },
    { "name": emotes.JOEL,                "value": 50  },
    { "name": "Tutel",                    "value": 80  },
    { "name": "Cookie",                   "value": 70  },
    { "name": "RAM",                      "value": 500 },
    { "name": "Gymbag",                   "value": 150 },
    { "name": "Harpoon",                  "value": 200 },
    { "name": "Programmer's Socks",       "value": 70  },
    { "name": "Metal Pipes",              "value": 150 },
    { "name": emotes.NEURO_BWAA,          "value": 300 },
    { "name": emotes.EVIL_BWAA,           "value": 300 },
    { "name": "The Duck on Neuro's Head", "value": 250 }
]

