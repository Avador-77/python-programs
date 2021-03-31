Jimmu = {
    'furiousButLoving':'Rajat sharma'
}

brutos = {
    'tipsyAndFunny':'Rahul'
}

pets = [Jimmu,brutos]

for pet in pets:
    for kindOf, owner_name in pet.items():
        print(kindOf.title(),":",owner_name.title())
