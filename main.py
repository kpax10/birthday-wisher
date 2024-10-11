import datetime as dt
import random
import smtplib

MY_EMAIL = "timmyt345345@gmail.com"
MY_PASSWORD = "qbtnsxioriyqxijz"

today = dt.datetime.now().weekday()
if today == 4:
    with open("quotes.txt") as file:
        lines = file.readlines()
        random_quote = random.choice(lines)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="anniet345345@yahoo.com",
            msg=f"Subject:Today's Quote\n\n{random_quote}"
        )
