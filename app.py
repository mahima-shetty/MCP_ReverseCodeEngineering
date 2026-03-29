from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.post("/mcp")
def handle_mcp(req: dict):
    tool = req.get("tool")
    params = req.get("params")

    try:
        if tool == "get_table_schema":
            return get_table_schema(params)

        elif tool == "get_plsql_code":
            return get_plsql_code(params)

        elif tool == "get_dependencies":
            return get_dependencies(params)

        elif tool == "get_execution_plan":
            return get_execution_plan(params)

        elif tool == "get_table_stats":
            return get_table_stats(params)

        else:
            return {"status": "error", "message": "Unknown tool"}

    except Exception as e:
        return {"status": "error", "message": str(e)}