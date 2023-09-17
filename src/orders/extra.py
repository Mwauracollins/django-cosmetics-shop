from datetime import date, datetime
import random
import string


def generate_tracking_number():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.now().second)
    random_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + random_str
