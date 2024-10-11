import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "timmyt345345@gmail.com"
MY_PASSWORD = "qbtnsxioriyqxijz"

# 2. Check if today matches a birthday in the birthdays.csv
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

df = pandas.read_csv("birthdays.csv")
matching_birthdays = df[(df['month'] == current_month) & (df['day'] == current_day)]

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv
if not matching_birthdays.empty:
    random_letter = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
    with open(f'letter_templates/{random_letter}', 'r') as letter:
        content = letter.read()
    birthday_name = matching_birthdays['name'].iloc[0]
    updated_letter = content.replace('[NAME]', birthday_name)
    with open('letter_templates/happy_birthday.txt', 'w') as letter:
        letter.write(updated_letter)
    with open(f'letter_templates/happy_birthday.txt', 'r') as letter:
        content = letter.read()

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        birthday_email = matching_birthdays['email'].iloc[0]
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )
