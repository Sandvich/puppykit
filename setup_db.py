#!/usr/bin/env python3
import sqlite3
import os
import json

def fill_db(connection):
    with open('rpg_data.json', 'r') as f:
        data = json.loads(f.read())
    
    cursor = connection.cursor()
    for i, row in enumerate(data):
        if len(row) == 5:
            data[i].append(0)
    cursor.executemany('INSERT INTO rpgs VALUES (?, ?, ?, ?, ?, ?)', data)
    connection.commit()

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE rpgs
                (name text, format text, publisher_id text, notes text, system text, to_gm integer);''')
    connection.commit()

def delete_db():
    # Simply checks if the db already exists and deletes it if so.
    # Intended primarily for dev.
    if os.path.exists('rpgs.db'):
        os.remove('rpgs.db')

if __name__ == '__main__':
    delete_db()
    with sqlite3.connect('rpgs.db') as connection:
        create_table(connection)
        fill_db(connection)
