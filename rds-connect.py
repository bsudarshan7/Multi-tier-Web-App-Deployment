import pymysql

connection = pymysql.connect(
    host="database-1.cr6c88gmoapu.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="sudarshan",
    database="server_dashboard",  # <-- Put your database name here
    port=3306
)
print("Connected Successfully!")

cursor = connection.cursor()

# Define the query as a Python string
sql_query = """
CREATE TABLE IF NOT EXISTS server_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(100),
    cpu FLOAT,
    memory FLOAT,
    disk FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Execute and save changes
cursor.execute(sql_query)
connection.commit()
print("Table 'server_metrics' created successfully!")

# Clean up connections
cursor.close()
connection.close()
