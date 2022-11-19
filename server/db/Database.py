if __name__ == "__main__":
    print("This is only include file. Do not run it.")
    exit(1)

from datetime import datetime

import db.Environment as Env
import psycopg2

now = datetime.now()


class Database:
    connection = None
    cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(Env.get_connection_url())
            self.connection.autocommit = True
            print("- Database connection successful")
        except psycopg2.DatabaseError as e:
            raise e
        return self.connection

    def create_cursor(self) -> None:
        if self.connection == None:
            raise ValueError("Connection is not defined")
        self.cursor = self.connection.cursor()

    def create_basic(self, url: str, color: str, title: str, description: str) -> None:
        query = f"INSERT INTO {Env.POSTGRES_DB} (url, color, title, description) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (url, color, title, description))

    def create_full(self, url: str, color: str, title: str, description: str, image: str, small: str) -> None:
        query = f"INSERT INTO {Env.POSTGRES_DB} (url, color, title, description, image, small) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(
            query, (url, color, title, description, image, small))

    def delete_expired(self, url: str) -> bool:
        global now

        try:
            query = f"SELECT * FROM {Env.POSTGRES_DB} WHERE url = %s"
            self.cursor.execute(query, (url, ))

            row = self.cursor.fetchall()
            date = row[0][6]

            if date < now:
                query = f"DELETE FROM {Env.POSTGRES_DB} WHERE url = %s"
                self.cursor.execute(query, (url, ))
                return True
        except IndexError:
            raise IndexError("This URL has expired or had never existed")

    def delete_all_expired(self) -> None:
        global now

        query = f"SELECT * FROM {Env.POSTGRES_DB}"
        self.cursor.execute(query)

        data = self.cursor.fetchall()

        for row in data:
            date = row[6]
            if date < now:
                query = f"DELETE FROM {Env.POSTGRES_DB} WHERE url = %s"
                self.cursor.execute(query, (row[0], ))
