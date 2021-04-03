def show_magicians(magicians_list):
    make_great(magicians_list[:]) #sending only the copy of original list and that's the syntax [:]
    print("\nInside show magician's function:")
    for name in magicians_list:
        print(name.title())
    print('\nFunction ends.')

def make_great(again_magicians_list):
    print("\nInside make great function:")
    for name in again_magicians_list:
        print("The Great "+ name.title())
    print('\nFunction ends.')




listOfMagicians = ['rajat','sunaina','jyoti','kamal']

show_magicians(listOfMagicians)