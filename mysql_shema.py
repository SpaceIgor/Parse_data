from mysql.connector import Error
from config import db_config
import mysql.connector


def create_connection_mysql_db(db_base=None):
    try:
        connection_db = mysql.connector.connect(
            host=db_config['host'],
            port=3306,
            user=db_config['user'],
            password=db_config['password'],
            database=db_base
        )
        print('connection to mysql completed successfully')
    except Error as db_connection_error:
        print('An error has occurred:', db_connection_error)
    return connection_db


def create_database(connection_db, name_db):
    try:
        cursor = connection_db.cursor()
        create_db_sql_query = f'CREATE DATABASE {name_db}'
        cursor.execute(create_db_sql_query)
        cursor.close()
        connection_db.close()
    except Error:
        pass
    finally:
        connection_db.close()


def create_table_data(connection_db):
    my_cursor = connection_db.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS `data` (data_id INT NOT NULL AUTO_INCREMENT, \
                            image VARCHAR(60), \
                            title VARCHAR(50), \
                            date DATE, \
                            location VARCHAR(50), \
                            beds VARCHAR(50), \
                            currency VARCHAR(5), \
                            price  VARCHAR(10), \
                            description TEXT, PRIMARY KEY (data_id));'

    my_cursor.execute(create_table)
    my_cursor.close()
    connection_db.close()


db = 'my_data_parse'
create_database(create_connection_mysql_db(), db)
create_table_data(create_connection_mysql_db(db))
