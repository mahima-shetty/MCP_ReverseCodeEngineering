import oracledb

def get_connection(params):
    dsn = f"{params['host']}:{params['port']}/{params['service_name']}"
    return oracledb.connect(
        user=params["username"],
        password=params["password"],
        dsn=dsn
    )