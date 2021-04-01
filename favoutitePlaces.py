favourite_places = {
    'Rajat':['Udhampur','goa','switzerland'],
    'bablu':['jammu','pancheri','landar'],
    'chuha chacha':['kareda','tandvaal'],
}

for name, favPlaces in favourite_places.items():
    if len(favPlaces) > 1:
        print("\n",name.title(),"'s favourite places are ")
        for places in favPlaces:
            print(places.title())
    elif len(favPlaces) == 1:
        print(name.title(),"'s favourite place is")
        for places in favPlaces:
            print("    ",places.title())
    else:
        print("No, that's not an appropriate input.")
