from os import system, name
import locale


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def addSpace(value):
    missing = 0
    if len(value) < 35:
        missing = (35 - len(value))
    
    return value.ljust(missing + len(value))


def currencyFormat(value):
    locale.setlocale(locale.LC_ALL, 'en_us')
    return locale.currency(int(value), grouping=True).replace("$", "Rp")