import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="trading_system",
    user="trading",
    password="tradingpass"
)
