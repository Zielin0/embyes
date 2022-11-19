if __name__ == "__main__":
    print("This is only include file. Do not run it.")
    exit(1)

import db.Environment as Env
import psycopg2


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
