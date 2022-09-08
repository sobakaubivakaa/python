import datetime 
def season_events(number): 
    months = ('January','February','March','April','May','June','July','August','September','October','November','December') 
 
    if number > 12: 
        return "You need to enter the real number of the month" 
    elif number == 12 or number <= 2: 
        return "You were born in " + months[number-1] + ", when white snow fell outside the window." 
    elif number > 2 and number <= 5: 
        return "You were born in " + months[number-1] + ", when birds sang beautiful songs." 
    elif number > 5 and number <= 8: 
        return "You were born in " + months[number-1] + ", when the sun shone brighter than ever." 
    else: 
        return "You were born in " + months[number-1] + ", when the harvest was incredible." 
 
month_number = int(input("month number: ")) 
print(season_events(month_number))
