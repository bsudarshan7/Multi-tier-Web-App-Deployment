import pymysql


connection = pymysql.connect(
    host="database-1.cr6c88gmoapu.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="sudarshan",
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