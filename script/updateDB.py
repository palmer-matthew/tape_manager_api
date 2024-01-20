#!/bin/bash
# Creation Date: Dec 13, 2023
# Version: 0.1.0
# Author: Matthew Palmer
# Decsription: Python Script To Update Database With Previous Data From Excel

from argparse import ArgumentParser
from csv import DictReader
from dotenv import dotenv_values
from mysql.connector import connection as packageConnection, errorcode
import json, csv, os
from datetime import datetime

class DatabaseConnection:
    def __init__(self, config:dict):
        self.config = config

    def openConnection(self):
        self.connection = packageConnection.MySQLConnection(self.config)
    
    def closeConnection(self):
        if self.connectionExists():
            self.connection.close()
            self.connection = None

    def createDBCursor(self):
        if self.connectionExists():
            self.cursor = self.connection.cursor(buffered=True)
    
    def closeDBCursor(self):
        if self.cursorExists():
            self.cursor.close()
            self.cursor = None

    def connectionExists(self):
        return self.connection is not None
    
    def cursorExists(self):
        return self.cursor is not None
    
    def commitChangesToDb(self):
        if self.cursorExists():
            self.cursor.commit()
    
    def executeSQLStatement(self, statement:str , data:tuple):
        if self.cursorExists:
            self.cursor.execute(statement, data)

def read_csv(path: str):
    with open(path, newline='', encoding='utf-8-sig') as file:
        reader = DictReader(file)
        rows = []
        for row in reader:
            del row['']
            rows.append(row)
    return rows

def update_database_with_record(record, statement):
    pass

def create_db_queries_file(data):
    TABLES = ['media']
    TABLES_PROPS = [
        ['mediaID varchar(8)', 'creationDate date', 'modifiedDate date', 'site varchar(255)', 'location varchar(255)', 'compartment varchar(255)', 'primary key(mediaID)']
    ]
    CREATE_STMT = 'CREATE TABLE %s(%s);\r'
    INSERT_SMT = 'INSERT INTO media(mediaID, creationDate, modifiedDate, site, location, compartment) VALUES("%s", "%s", "%s", "%s", "%s", "%s");\r'
    try:
        with open('./query.sql', 'w') as ptr:
            newline = '\r'

            ptr.write("DROP DATABASE IF EXISTS tapeManager;\r")
            ptr.write("CREATE DATABASE tapeManager;\r")
            ptr.write("USE tapeManager;\r")

            ptr.write(newline)

            ptr.write(CREATE_STMT % (TABLES[0], ','.join(TABLES_PROPS[0])))

            ptr.write(newline)

            ptr.write("/*======================================INSERTING DATA INTO TABLE======================================*/\r")
            
            for item in data:
                currentDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ptr.write(INSERT_SMT % (item['Tape ID'], currentDate, currentDate, item['Facility'], item['Cabinet No.'], item['Draw No.']))
    except:
        pass


def main():
     # Initialize Object to conduct argument handling
    commandLineParser = ArgumentParser()

    commandLineParser.add_argument('-c', '--configuration', help="Absolute or Relative File Path to .env or configuration file.")
    commandLineParser.add_argument('-f', '--file', help="Absolute or Relative File Path to the csv containing data to be uploaded.")
    # commandLineParser.add_argument()

    arguments = commandLineParser.parse_args()

    if arguments.configuration:
        # # Intialize the program instance with environment variables needed for functionality
        configuration = dotenv_values(str(arguments.configuration))
    else:
        commandLineParser.exit(1, message="Please provide the file path to the environment file.\n")

    if not arguments.file:
        commandLineParser.exit(1, message="Please provide the file path to the csv file.\n")

    data = read_csv(arguments.file)

    create_db_queries_file(data)


if __name__ == "__main__":
    main()