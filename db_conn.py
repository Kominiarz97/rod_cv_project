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

def insert_report(conn, filename, gps):
    cur = conn.cursor()
    with open("makao.JPG", "rb") as image:
        file = image.read()
        byte = bytearray(file)
    cur.execute('INSERT INTO public."Zgloszenia"("Zdjecie", "Data_zgloszenia", "Godz_zgloszenia", "Lokalizacja_gps", "Zarejestrowane", "Zgloszenie_sluzbom", id_drona, id_odcinka_trasy, id_trasy, id_uzytkownika, "Rodzaj_zagrozenia") VALUES(psycopg2.Binary(byte), datetime.now().date(), datetime.now().time(), gps, "false", "false", 1, 1, 1, NULL, 2);')
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




