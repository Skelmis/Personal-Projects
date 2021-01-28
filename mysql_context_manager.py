# this normally lives in a class, but this is just to keep it goin
# To use this, create a class or set lines 11-16

@contextmanager
def ensure_db_connection(self):
    """
    A context manager used to manage the database connection
    without the need to duplicate code or multiple methods
    """
    try:
        conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.db
        )

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise Exception("Invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise Exception("Unknown db")
        else:
            raise err

    else:
        cursor = conn.cursor()

    yield cursor

    cursor.close()

    conn.commit()
    conn.close()
