# Python Script To Update Database With Previous Data From Excel
from csv import DictReader
# from mysql import connector

def read_csv(path: str):
    with open(path, newline='', encoding='utf-8-sig') as file:
        reader = DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
    return rows

if __name__ == '__main__':
    pass