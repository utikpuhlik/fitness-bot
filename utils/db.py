from dataclasses import dataclass
import pytz
from datetime import timedelta, datetime
import psycopg2
from psycopg2 import errors
from psycopg2.errorcodes import STRING_DATA_RIGHT_TRUNCATION
import re
from data import config

utc = pytz.UTC
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


async def validate_email(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


@dataclass
class Database:
    def __init__(self):
        self.connection = psycopg2.connect(config.DB_URI, sslmode='require')
        self.cursor = self.connection.cursor()
        self.current_date = utc.localize(datetime.now())

    def check_user(self, user_id):
        try:
            with self.connection:
                self.cursor.execute(f"SELECT user_id FROM db_name WHERE user_id = {user_id}")
        except psycopg2.InterfaceError as exc:
            self.connection = psycopg2.connect(config.DB_URI)
            self.cursor = self.connection.cursor()
            with self.connection:
                self.cursor.execute(f"SELECT user_id FROM db_name WHERE user_id = {user_id}")
        finally:
            result = self.cursor.fetchone()

        if result:
            return True
        return False

    def check_user_email(self, user_id, email):
        with self.connection:
            try:
                self.cursor.execute("SELECT email FROM db_name WHERE email = %s and user_id is null", (email,))
                result = self.cursor.fetchone()
            except errors.lookup(STRING_DATA_RIGHT_TRUNCATION):  # handle varchar > 255
                self.cursor.rollback()

            if result:  # Success
                self.cursor.execute("UPDATE db_name SET user_id = %s WHERE email = %s", (user_id, email))
                self.cursor.execute("UPDATE db_name SET date_of_activation = %s WHERE email = %s", ('now()', email))
                self.cursor.execute("UPDATE db_name SET date_of_expiration = %s WHERE email = %s",
                                    (str(datetime.now() + timedelta(days=90)), email))
                return True

            return False  # Mail already has a user_id or wasn't found

    def check_subscription(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT date_of_expiration FROM db_name WHERE user_id = %s", (user_id,))
            end_of_subscription = self.cursor.fetchone()[0]  # Take datetime object from tuple
            if self.current_date < end_of_subscription:
                return True
            return False

    def renew_subscription(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE db_name SET date_of_expiration = %s WHERE user_id = %s",
                                (str(datetime.now() + timedelta(days=90)), user_id))

    def sub_time(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT date_of_expiration FROM db_name WHERE user_id = %s", (user_id,))
            time_diff = self.cursor.fetchone()[0] - self.current_date
            return time_diff.days

    def message_counter(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE db_name SET messages = messages + 1 WHERE user_id = %s", (user_id,))

    def get_all_users(self):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM db_name")
            all_users = self.cursor.fetchall()
        return all_users


