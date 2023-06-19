"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

'''Подключение к БД'''
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="Dfcmrf74"
)

csv_files = {
    "north_data/customers_data.csv": "customers",
    "north_data/employees_data.csv": "employees",
    "north_data/orders_data.csv": "orders"
}
for csv_file, table_name in csv_files.items():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок в файле CSV
        cursor = conn.cursor()
        for row in reader:
            insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['%s']*len(row))})"
            cursor.execute(insert_query, row)
        conn.commit()

cursor.close()
conn.close()
