# PROJECT ON BIRTHDAY WISHER

import random
import json
import smtplib
from datetime import *

today = datetime.now()

with open("Birthdays.json" , "r") as birthday_file:
    birthday_dict = json.load(birthday_file)


for (name,value) in birthday_dict.items():

    day = birthday_dict[name]["Date of Birth"]["Day"]
    month = birthday_dict[name]["Date of Birth"]["Month"]
    year = birthday_dict[name]["Date of Birth"]["Year"]   

    age = today.year - year

    if age%10 == 1:
        subscript = "st"
    elif age%10 == 2:
        subscript = "nd"
    elif age%10 == 3:
        subscript = "rd"
    else:
        subscript = "th"

    if today.day == day and today.month == month:

        letter_no = random.randint(1, 3)

        with open(f"Letter_Templates/letter_{letter_no}.txt") as data:
            letter = data.read()

        letter = letter.replace("[NAME]" , name)
        letter = letter.replace("[AGE]" , age+subscript)

        port_no = 587 
        smtp_server = "smtp.gmail.com"

        sender_email = "YOUE EMAIL ID"
        receiver_email = birthday_dict[name]["Email"]

        sender_password = "YOUR EMAIL APP PASSWORD"

        message = f"""From: {sender_email}
To: {receiver_email}
Subject: HAPPY BIRTHDAY!!

{letter}
"""

        with smtplib.SMTP(host= smtp_server, port= port_no) as server:

            server.starttls()

            server.login(user= sender_email , password = sender_password)

            server.sendmail(from_addr= sender_email, to_addrs= receiver_email, msg= message)









