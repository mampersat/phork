#!/usr/bin/env python3
""" phish.py
a simple text based adventure
"""

inventory = ["soap"]

# print current location and inventory
def display(s):
    print(s)

    print("Inventory:")
    for o in inventory:
        print(o, end='')
    print('')

# only accept a specific input
def only_accept( s ):
    t = ""
    while t != s:
        t = input(':')
    print('')

# main sequence
display("""You find yourself on Church St. in Burlington, VT.
There is a water fountain""")

only_accept('goto nectars')

display('Nectars is closed but theres a window selling gravy Fries')

only_accept('buy gravy fries')

display('You dont have any money')

only_accept('put soap in fountain')

inventory.remove('soap')

display("""The fountain erupts into a bubble bath
Pople emerge from the alleys and bathe in the fountain
It looks like many of them have left money in the fountain.""")

only_accept('get money from fountain')

inventory.append('money')

display('You now have money')

only_accept('buy gravy fries')
inventory.remove('money')
inventory.append('gravy fries')

display("""You now have gravy fries""")

print("You have completed phork 0.1")


