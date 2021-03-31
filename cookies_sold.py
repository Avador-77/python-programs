def cookies_sold(flightsTookOff, flightsLanded, capacityTookOff, capacityLanded):

    cookiesSoldTookOff = (flightsTookOff * capacityTookOff) * 2

    cookiesSoldLanded = ((flightsLanded * capacityLanded) / 2) * 2

    totalCookiesSold = cookiesSoldTookOff + cookiesSoldLanded

    return totalCookiesSold

flightsTookOff = int(input("How many flights took off?"))
flightsLanded = int(input("How many flights landed?"))
capacityTookOff = int(input("What is the seating capacity of flights that took off?"))
capacityLanded = int(input("What is the seating capacity of flights that landed?"))

totalCookies = cookies_sold(100, 110, 150, 185)

print("Total cookies that are sold on the airport are ", totalCookies)
