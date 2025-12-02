from app.schemas.env_schema import settings 


def get_connection_string():
        USER = settings.POSTGRES_USER
        PASSWORD = settings.POSTGRES_PASSWORD
        DB = settings.POSTGRES_DB
        HOST = settings.POSTGRES_HOST
        PORT = settings.POSTGRES_PORT

        return f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

CONN_STRING = get_connection_string()
 

