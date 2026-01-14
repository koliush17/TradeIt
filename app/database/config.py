from app.schemas.env_schema import settings 

def get_connection_string():
        USER = settings.POSTGRES_USER
        PASSWORD = settings.POSTGRES_PASSWORD
        DB = settings.POSTGRES_DB
        HOST = settings.POSTGRES_HOST

        return f"postgresql://{USER}:{PASSWORD}@/{DB}?host=/cloudsql/{HOST}"

CONN_STRING = get_connection_string()
 
def get_connection_string_local():
        USER = settings.POSTGRES_USER
        PASSWORD = settings.POSTGRES_PASSWORD
        DB = settings.POSTGRES_DB
        HOST = "localhost"
        PORT = 9999

        return f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

CONN_STRING_LOCAL = get_connection_string_local()


