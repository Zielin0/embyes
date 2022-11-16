import os


def get_connection_url() -> str:
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")

    POSTGRES_HOST = "db"

    if None in (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB):
        raise ValueError("Some of the env variables are empty")

    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"


if __name__ == "__main__":
    print("This is only include file. Do not run it.")
    exit(1)
