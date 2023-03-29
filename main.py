import datetime as dt
import pandas
import random
import smtplib

#Provide Email Credentials
MY_EMAIL = "xxxxxxx@yahoo.com"
MY_PASSWORD = "yyyyyyyyy"


#Define date/time parameters and create tuple
today = dt.datetime.now()
today_tuple = (today.month, today.day)


#Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#Create If statement to check the current day and see if it matches a birthday in the csv file
#If it does then pick a random letter and populate it with their name
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

#Send email using your email credentials, the birthday person's email address and a random letter contents

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
