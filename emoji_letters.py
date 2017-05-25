import sys

mapping = {
    "a" : "a",
    "b" : "b",
    "c" : "star_and_crescent",
    "d" : "leftwards_arrow_with_hook",
    "e" : "e-mail",
    "f" : "flags",
    "g" : "arrow_right_hook",
    "h" : "pisces",
    "i" : "information_source",
    "j" : "japan",
    "k" : "tanabata_tree",
    "l" : "boot",
    "m" : "m",
    "n" : "capricorn",
    "o" : "o",
    "p" : "parking",
    "q" : "leo",
    "r" : "registered",
    "s" : "heavy_dollar_sign",
    "t" : "latin_cross",
    "u" : "ophiuchus",
    "v" : "aries",
    "x" : "heavy_multiplication_x",
    "y" : "v",
    "z" : "zzz",
    " " : " "
}

if __name__ == "__main__":
    emojis = [":" + mapping.get(x.lower(), x) + ":" for x in sys.argv[1]]
    print " ".join(emojis)    

    

