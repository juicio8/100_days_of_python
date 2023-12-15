# import smtplib
#
email = "juicio0ch@gmail.com"
password = "smhv ssmr ehcg matw"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=email, password=password)
# connection.sendmail(from_addr=email, to_addrs="wisdomochiche@gmail.com", msg="Subject:Hello Wisdom\n\nBody")
# connection.close()
import datetime as dt
import random
import smtplib

# Getting quote
with open("quotes.txt") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)
    print(quote)

# Checking day
day = dt.datetime.now().weekday()
if day == 0:
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs="wisdomochiche@gmail.com",
                                msg=f"Subject: MOTIVATION QUOTE\n\n{quote}")
    except:
        print("something Happended")
