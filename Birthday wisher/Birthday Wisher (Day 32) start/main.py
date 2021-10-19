import datetime as dt
import smtplib
import random

MY_EMAIL = "blueberryapp123@gmail.com"
PASSWARD = "Blueberryapp@123"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)

    print(quote)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWARD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Monday motivation\n\n{quote}"
    )







