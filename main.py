# main.py
from fastapi import FastAPI
import psycopg2
from dotenv import load_dotenv
import os

app = FastAPI()

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

@app.get("/health")
def health_check():
# Connect to the database
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )        
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()
        
        # Example query
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        print("Current Time:", result)

        # Close the cursor and connection
        cursor.close()
        connection.close()
        return {"status": "healthy"}

    except Exception as e:
        return {"status": "unhealthy", "details": str(e)}

    



