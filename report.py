from gps import get_position
from db_conn import insert_report

def report_obstacle(conn, drone_id, rep_nr, obstacle_type):
    lat, lon = get_position() #pozycja gps
    with open(f"report_photos/{drone_id}_{rep_nr}.JPG", "rb") as image:
        file = image.read() #odczyt pliku obrazu
        byte = bytearray(file) #konwersja do formaru macierzy bitów
    gps = str(lat) + ", " + str(lon)
    #dodanie zgłosznia
    insert_report(conn, byte, str(gps), drone_id, 1, obstacle_type)

