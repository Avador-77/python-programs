favourite_languages = {
    'rajat':['c','c++','python'],
    'pankaj':['html','css','android','java'],
    'shilpa':['c++'],
    }

for name, languages in favourite_languages.items():
    if len(languages) == 1:
        print("\n",name.title(),"'s", "favourite language is")
        for language in languages:
            print(language.title())
            
    else:
        print("\n",name.title(),"'s favourite languages are ")
        for language in languages:
            print(language.title())


        

            

