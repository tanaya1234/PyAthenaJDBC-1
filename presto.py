from pyathenajdbc import connect

#this returns a Connection object
conn = connect(user='tanayaj', api_token='71c32b76caa544b1bd0106aa4f0a643d70aaf098a92640bd891043c0523731d0')

try:
    with conn.cursor() as cursor: #creates a Cursor object and returns it
        cursor.execute("""
        select * from system.runtime.nodes
        """)
        print(cursor.description)
        for row in cursor:
            print(row)
finally:
    conn.close()
