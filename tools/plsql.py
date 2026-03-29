from db import get_connection

def get_plsql_code(params):
    conn = get_connection(params)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT text FROM all_source
        WHERE name = :name
        ORDER BY line
    """, name=params["object_name"].upper())

    code = "".join([r[0] for r in cursor.fetchall()])

    return {"status": "success", "data": code}