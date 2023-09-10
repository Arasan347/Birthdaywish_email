##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import smtplib
import datetime as dt
import random

#smtp connection to send mail

my_email = "arasanengineer@gmail.com"
password = "expqifscwcbvbzqk"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

df = pd.read_csv('birthdays.csv')
birth_data = df.to_dict()
month = birth_data["month"][0]
day = birth_data["day"][0]
name = birth_data["name"][0]

now = dt.datetime.now()
day_of_week = now.weekday()
month_of_year = now.month

#opening letter file
with open(f"letter_templates/letter_1.txt") as letter_name:
    letters = letter_name.read()

birthday_txt = letters.replace("[NAME]", name)

if (day_of_week, month_of_year) == (day_of_week, month_of_year):
    connection.sendmail(from_addr=my_email, to_addrs="arasansmart770@gmail.com",
                        msg=f"Subject:BIRTHDAY WISH\n\n{birthday_txt}")

connection.close()







