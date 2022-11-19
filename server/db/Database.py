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

    def create_basic(url: str, color: str, title: str, description: str) -> None:
        pass

    def create_full(url: str, color: str, title: str, description: str, image: str = "", small: str = "") -> None:
        pass
