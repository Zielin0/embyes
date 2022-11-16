import db.Environment as Env
import psycopg2

connection = None


def connect():
    global connection
    try:
        connection = psycopg2.connect(Env.get_connection_url())
        connection.autocommit = True
        print("- Database connection successful")
    except psycopg2.DatabaseError as e:
        raise e
    return connection


if __name__ == "__main__":
    print("This is only include file. Do not run it.")
    exit(1)
