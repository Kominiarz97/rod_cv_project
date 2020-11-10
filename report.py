from gps import get_position
from db_conn import insert_report
def create_report(image, obstacle_type, conn):
    lat, lon = get_position()
    insert_report(conn, "report.jpg")