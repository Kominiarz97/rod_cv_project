import psycopg2
from datetime import datetime
import cv2

def db_connect():
    conn = psycopg2.connect(
        user='postgres',
        password='root',
        host='127.0.0.1',
        port='5432',
        database='rod_web',
        )
    return conn

def insert_report(conn, byte, gps, drone_id, rail_id, obstacle):
    cur = conn.cursor()
    gps=12312312
    cur.execute('INSERT INTO public."Zgloszenia"("Zdjecie", "Data_zgloszenia", "Godz_zgloszenia", "Lokalizacja_gps", id_drona, id_trasy, "Rodzaj_zagrozenia") VALUES (%s, %s, %s, %s, %s, %s, %s);',(psycopg2.Binary(byte), datetime.now().date(), datetime.now().time(), gps, drone_id, rail_id, obstacle))
    conn.commit()
    cur.close()


'''cur.execute('SELECT * FROM public."Obrazek";')
photo=cur.fetchone()[1]

with open("makao2.JPG", "wb") as qqq:
    qqq.write(bytearray(photo))
    qqq.close()'''




'''
cur.execute('INSERT INTO public."Obrazek"("ID", zdjecie) VALUES (%s, %s)', (1, psycopg2.Binary(byte)))
conn.commit()
'''




