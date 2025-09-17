import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from learn-ai!")
    print(os.getenv("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
