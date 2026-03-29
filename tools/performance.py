from db import get_connection

def get_execution_plan(params):
    conn = get_connection(params)
    cursor = conn.cursor()

    cursor.execute(f"EXPLAIN PLAN FOR {params['query']}")
    cursor.execute("SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY)")

    plan = [row[0] for row in cursor.fetchall()]

    return {"status": "success", "data": plan}


def get_table_stats(params):
    conn = get_connection(params)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT num_rows
        FROM all_tables
        WHERE table_name = :t
    """, t=params["table_name"].upper())

    row = cursor.fetchone()

    return {
        "status": "success",
        "data": {"rows": row[0] if row else 0}
    }