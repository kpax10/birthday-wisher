# import smtplib
#
# my_email = "timmyt345345@gmail.com"
# password = "qbtnsxioriyqxijz"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="anniet345345@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)

