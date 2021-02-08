from . import http, errors
import re, random

no_response = "Couldn't contact the API right now..."


def textcat():
    try:
        return http.get("/cat")["cat"]
    except Exception as e:
        raise errors.NothingFound(no_response)


def why():
    try:
        return http.get("/why")["why"]
    except Exception as e:
        raise errors.NothingFound(no_response)


def fact():
    try:
        return http.get("/fact")["fact"]
    except Exception as e:
        raise errors.NothingFound(no_response)


def owoify(owomsg):
    faces = ["OwO", "uwu", ">w<", "^w^", "x3"]
    owomsg = re.sub("(?:r|l)", "w", owomsg)
    owomsg = re.sub("(?:R|L)", "W", owomsg)
    owomsg = re.sub("n([aeiou])", "ny\\1", owomsg)
    owomsg = re.sub("N([aeiou])", "Ny\\1", owomsg)
    owomsg = re.sub("N([AEIOU])", "NY\\1", owomsg)
    while "!" in owomsg:
        owomsg = re.sub("\!+", "r" + random.choice(faces), owomsg, 1)  # adding r and l to read the ! and ? later on

    while "?" in owomsg:
        owomsg = re.sub("\?+", "r" + random.choice(faces), owomsg, 1)
        owomsg = owomsg.replace("r", "!")
        owomsg = owomsg.replace("l", "?")
    return owomsg


def nekogirl():
    try:
        r = http.get("/img/" + "neko")
    except Exception as e:
        raise errors.NothingFound(no_response)
    return r["url"]
