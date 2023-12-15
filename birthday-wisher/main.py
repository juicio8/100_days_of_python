##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

email = "juicio0ch@gmail.com"
password=""
birthdays_df = pandas.read_csv('birthdays.csv')
birthdays = [{"name": row["name"], "day": row["day"], "month": row["month"]} for (index, row) in birthdays_df.iterrows()]
print(birthdays)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
print(month, day)
for birthday in birthdays:
    if birthday['day'] == day and birthday['month'] == month:
        letter_no = random.randint(1, 3)
        with open(f'letter_templates/letter_{letter_no}.txt') as file:
            letter = file.read()
            letter = letter.replace('[NAME]', birthday['name'])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=birthday['email'], msg=f'Subject: HappyBirthday\n\n{letter}')

