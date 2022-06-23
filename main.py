# IMPORTING LIBRARIES
import smtplib
import datetime as dt
import random

# CONSTANTS
# DUMMY CREDENTIALS
TO_MAIL = "random@gmail.com"
FROM_MAIL = "random@yahoo.com"
PASSWORD = "password123"
SMTP_SERVER = "smtp.mail.yahoo.com"
QUOTES_FILE = "quotes.txt"
SUBJECT = "Subject:Motivational Message\n\n"
MONDAY = 0

# QUOTES_SELECTOR
def quotes_selector():
    try:
        with open(QUOTES_FILE, "r") as file:
            quotes_list = file.readlines()
        random_quote = random.choice(quotes_list)
    except:
        random_quote = f"{QUOTES_FILE} could not be opened."
    return random_quote


# MOTIVATIONAL MESSAGE
random_quote = quotes_selector()
motivational_message = SUBJECT + random_quote

# CURRENT DATETIME
current_datetime = dt.datetime.now()
current_weekday = current_datetime.weekday()
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year

if current_weekday == MONDAY:
    try:
        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=FROM_MAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=FROM_MAIL, to_addrs=TO_MAIL, msg=motivational_message
            )
    except:
        print(
            f"Motivational Message could not be sent on {current_year}/{current_month}/{current_day}."
        )
