import os


from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
    