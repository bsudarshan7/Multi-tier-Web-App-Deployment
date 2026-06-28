import pymysql


connection = pymysql.connect(
   host="YOUR_RDS_ENDPOINT"
user="YOUR_USERNAME"
password="YOUR_PASSWORD"
database="server_dashboard",
    port=3306,
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)


def save_metrics(hostname, cpu, memory, disk):

    try:

        with connection.cursor() as cursor:

            sql = """
            INSERT INTO server_metrics
            (hostname,cpu,memory,disk)
            VALUES(%s,%s,%s,%s)
            """

            cursor.execute(
                sql,
                (
                    hostname,
                    cpu,
                    memory,
                    disk
                )
            )

    except Exception as e:

        print(e)


def get_metrics():

    try:

        with connection.cursor() as cursor:

            cursor.execute("""

            SELECT *

            FROM server_metrics

            ORDER BY created_at DESC

            """)

            return cursor.fetchall()

    except Exception as e:

        print(e)

        return []
