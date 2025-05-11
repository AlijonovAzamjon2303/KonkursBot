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

def get_chanel_by_id(id):
    conn = psycopg2.connect("dbname=azamjon user=azamjon password=1111")
    curr = conn.cursor()
    curr.execute("SELECT * FROM chanels WHERE id=%s", (id, ))
    chanel = curr.fetchone()
    conn.commit()

    curr.close()
    conn.close()

    return chanel

def delete_chanel_by_id(id):
    conn = psycopg2.connect("dbname=azamjon user=azamjon password=1111")
    curr = conn.cursor()
    curr.execute("DELETE FROM chanels WHERE id=%s", (id, ))

    conn.commit()

    curr.close()
    conn.close()
