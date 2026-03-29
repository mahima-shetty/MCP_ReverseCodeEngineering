from db import get_connection

def get_dependencies(params):
    conn = get_connection(params)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT referenced_name, referenced_type
        FROM all_dependencies
        WHERE name = :name
    """, name=params["object_name"].upper())

    deps = cursor.fetchall()

    return {
        "status": "success",
        "data": [{"name": d[0], "type": d[1]} for d in deps]
    }