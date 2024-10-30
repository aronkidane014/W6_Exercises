import datetime
today= datetime.datetime.now()
formatted_date = today.strftime("Today is %A, %B %d, %Y")
print(formatted_date)

Birthday = datetime.date(1996, 8, 11)
formatted_birthday = Birthday.strftime("My birthday is %m/%d/%Y")
print(formatted_birthday)

ninety_d = today + datetime.timedelta(days=90)
formatted_ninety_d = ninety_d.strftime("90 days from today is %B %d, %Y")
print(formatted_ninety_d)

dinner_time = datetime.time(20, 30)
formatted_dinner_time = dinner_time.strftime("Let's meet for dinner at %I:%M %p")
print(formatted_dinner_time)