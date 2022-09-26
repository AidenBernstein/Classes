from array import *

def print_tabs(tab):
    for string in tab:
        for note in string:
            print(note, end="")
        print()
    
def add_note(tab, string, note):
    if note == "s":
        note = "-"
    
    if string == "d":
        tab[3].append(note + "-")
        tab[0].append("--")
        tab[1].append("--")
        tab[2].append("--")
        
    elif string == "a":
        tab[2].append(note + "-")
        tab[0].append("--")
        tab[1].append("--")
        tab[3].append("--")
    
    elif string == "D":
        tab[1].append(note + "-")
        tab[0].append("--")
        tab[2].append("--")
        tab[3].append("--")
    
    elif string == "g":
        tab[0].append(note + "-")
        tab[1].append("--")
        tab[2].append("--")
        tab[3].append("--")
        
    else:
        print("Invalid string")
        return
        
    return tab
        


print("enter tabs")
tabs = input()
tabs = tabs.split(" ")

t = [["G|-"], ["D|-"], ["A|-"], ["D|-"]]

for tab in tabs:
    string = tab[0]
    note = tab[1]
    t = add_note(t, string, note)

print_tabs(t)