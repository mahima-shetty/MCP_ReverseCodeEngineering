from db import get_connection

def get_table_schema(params):
    conn = get_connection(params)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT column_name, data_type
        FROM all_tab_columns
        WHERE table_name = :t
    """, t=params["table_name"].upper())

    result = cursor.fetchall()

    return {
        "status": "success",
        "data": [{"column": r[0], "type": r[1]} for r in result]
    }