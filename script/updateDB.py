# Python Script To Update Database With Previous Data From Excel
from csv import DictReader
# from mysql import connector

class MySQLConnection():
    pass

def read_csv(path: str):
    with open(path, newline='', encoding='utf-8-sig') as file:
        reader = DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
    return rows

def update_database_with_record(record, statement):
    pass

def main():
    pass


if __name__ == '__main__':
    pass