import psycopg2
from datetime import datetime
import cv2

def db_connect():
    conn = psycopg2.connect(
        user='cxsmexgltcamdl',
        password='26451c9c964f41c1289ad0560b6c19822790f9eac333858ff4ed29be2db71b04',
        host='ec2-54-247-122-209.eu-west-1.compute.amazonaws.com',
        port='5432',
        database='d83erikgcdpmpu',
        )
    return conn

def insert_report(conn, byte, gps, drone_id, rail_id, obstacle):
    cur = conn.cursor()
    cur.execute('INSERT INTO public."Zgloszenia"("Zdjecie", "Data_zgloszenia", "Godz_zgloszenia", "Lokalizacja_gps", "Dron", "Trasa", "Rodzaj_zagrozenia") VALUES (%s, %s, %s, %s, %s, %s, %s);',(psycopg2.Binary(byte), datetime.now().date(), datetime.now().time(), gps, drone_id, rail_id, obstacle))
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




