import psycopg2

async def add_chanel_to_db(name):
    conn = psycopg2.connect("dbname=azamjon user=azamjon password=1111")
    curr = conn.cursor()
    curr.execute("INSERT INTO chanels(name) VALUES(%s);", (name, ))
    conn.commit()

    curr.close()
    conn.close()


def get_all_chanels():
    conn = psycopg2.connect("dbname=azamjon user=azamjon password=1111")
    curr = conn.cursor()
    curr.execute("SELECT * FROM chanels")
    chanels = curr.fetchall()
    conn.commit()

    curr.close()
    conn.close()

    return chanels

