import random
import smtplib
import datetime as dt
import pandas as pd
import personal

def send_email(message):

    my_email = personal.my_email
    password = personal.password
    connection = smtplib.SMTP('smtp.gmail.com',587)

    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=personal.receiver_email, 
        # msg=f"Subject: Motivation\n\n {message['quote']} - {message['author']}")
        msg=f"Subject: Happy Birthday!\n\n {message}")
    
    connection.quit()


def get_message():
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        split_quote = quote.split('-')
        message = {'quote': split_quote[0], 'author': split_quote[1].strip()}
        return message

birthday_data = pd.read_csv('birthdays.csv')
birthday_dict = birthday_data.to_dict(orient='records')
# print(birthday_dict)
for birthday in birthday_dict:
    today = dt.datetime.now()
    if birthday['month'] == today.month and birthday['day'] == today.day:
        # print(f"Today is {birthday['name']}'s birthday!")
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt', 'r') as letter_file:
            letter_content = letter_file.read()
            letter_content = letter_content.replace('[NAME]', birthday['name'])
            send_email(letter_content)


