#!/usr/bin/python
import psycopg2
from configs import config_db
from datetime import datetime


def connect():
    conn = None
    try:
        params = config_db()

        print('Connecting to the broker database...')
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_registers(topic, disp_id, lat, lng):
    sql = ("INSERT INTO registers(collected, topic, disp_id, lat, lng)\n"
           "             VALUES(%s,%s,%s,%s,%s) RETURNING id;")
    conn = None
    gen_id = None
    try:
        params = config_db()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (datetime.now(), topic, disp_id, lat, lng))
        gen_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return gen_id


def get_registers(topic):
    sql = ("SELECT * from registers\n"
           "             WHERE topic = %s;")
    conn = None
    result = None
    try:
        params = config_db()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (topic,))
        result = cur.fetchall()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return result


if __name__ == '__main__':
    connect()
