import datetime as dt
from pathlib import Path
import pandas as pd
import random
import smtplib

MY_EMAIL = "TKPpython@gmail.com"
MY_PASSWORD = "fvbe epbs bwuf bqqp"

today = dt.date.today()
current_month = today.month
current_day = today.day
receiver_email = ""

def send_email(message):
   with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()   #secure connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= receiver_email,
                            msg=f"Subject:Happy Birthday!\n\n{message}"
        )

def construct_email():
    global receiver_email
    receiver_name = entry["name"]
    receiver_email = entry["email"]
    birth_month = entry["month"]
    birth_day = entry["day"]
    if birth_month == current_month and birth_day == current_day:
        letter_template_name = ("./letter_templates/letter_" +
                                str(random.randint(1,3)) + ".txt")
        with open(letter_template_name, "r") as letter_template:
            generic_letter = letter_template.read()
        final_letter = generic_letter.replace("[NAME]", receiver_name)
        send_email(final_letter)

file_path = Path("./birthdays.csv")
data = pd.read_csv(file_path)
birthday_list = data.to_dict(orient="records")

for entry in birthday_list:
   construct_email()