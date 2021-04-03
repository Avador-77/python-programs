def city_country(city, country):

    cityAndcountry = city + "," + country
    return cityAndcountry.title()




while True:
    city_name = input("(Enter 'q' anytime to quit)\nEnter the name of the city: ")
    if city_name == 'q':
        break
    
    country_name = input("(Enter 'q' anytime to quit)\nEnter the name of the country: ")
    if country_name == 'q':
        break

    formatted_name = city_country(city_name, country_name)
    print(formatted_name)
    