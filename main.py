from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "timmyt345345@gmail.com"
MY_PASSWORD = "qbtnsxioriyqxijz"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
if today_tuple in birthdays_dict:
    for key in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as letter:
            content = letter.read()
            content = content.replace('[NAME]', birthday_person['name'])
        with open('letter_templates/happy_birthday.txt', 'w') as letter:
            letter.write(content)
        with open(f'letter_templates/happy_birthday.txt', 'r') as letter:
            content = letter.read()

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            birthday_email = birthday_person['email']
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"Subject:Happy Birthday!\n\n{content}"
            )

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv



