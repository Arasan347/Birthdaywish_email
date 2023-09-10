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







