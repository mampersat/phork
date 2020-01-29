#!/usr/bin/env python3
""" phish.py
a simple text based adventure
"""

inventory = []

class Location:
    "This is a location class"
    objects = []

outside_nectars = Location()
inside_nectars = Location()
church_and_main = Location()
city_hall = Location()

outside_nectars.title = "Outside Nectars. There are gravy fries for sale"
outside_nectars.inside = inside_nectars
outside_nectars.west = church_and_main
def buy_gravy_fries():
    if 'money' in inventory:
        print("You purchase an order of gravey fries")
        inventory.remove('money')
        inventory.append('gravy fries')
    else:
        print("You don't have any money")
outside_nectars.buy_gravy_fries = buy_gravy_fries

inside_nectars.title = "Inside Nectars. There's a band playing next to the round bar"
inside_nectars.outside = outside_nectars

church_and_main.title = "You are at the intersection of Church St. and Main St."
church_and_main.east = outside_nectars
church_and_main.north = city_hall
church_and_main.objects.append('soap')


city_hall.title = "You are outside city hall. There is a fountain."
city_hall.south = church_and_main
def soap_in_fountain():
    if 'soap' in inventory:
        print("""
The soap turns the fountain into a bubble bath.
People emerge from the alley ways and jump into the fountain
Some money falls our of their pockets as they are drying off""")
        city_hall.objects.append("money")
        inventory.remove("soap")
city_hall.put_soap_in_fountain = soap_in_fountain

def print_inventory():
    print("you have", inventory)

## Start outside nectars
loc = outside_nectars

## Main loop
while True:
    print(loc.title)
    if len(loc.objects):
        # M@ TODO MAKE THIS AS LOOP
        print("There is", loc.objects[0], "on the ground")

    c = input(":")
    print()
    
    ## check for common commands
    if c == "help":
        print("There's no help... yet")
        continue
    
    if c== "inventory":
        print_inventory()
        continue

    ## Check for movement
    if c[:3].lower() == 'go ':
        if hasattr(loc, c[3:]):
            print("Going",c[3:])
            loc = getattr(loc, c[3:])
        else:
            print("I can't go in that direction")

    ## Check for object
    elif c[:4].lower() == 'get ':
        o = c[4:].lower()
        if o in loc.objects:
            loc.objects.remove(o)
            inventory.append(o)
            print("You now have",o)
        else:
            print("There is no",o,"here")

    ## Check for special commant

    elif hasattr(loc, c.lower().replace(' ', '_')):
        f = getattr(loc, c.lower().replace(' ', '_'))
        f()

    else:
        print("I don't understand")

    
