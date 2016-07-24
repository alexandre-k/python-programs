import sqlite3
connection = sqlite3.connect('example.db')

# with connection:
#     connection.execute('CREATE TABLE stocks (symbol text, quantity real, price real)')
#     connection.execute('INSERT INTO stocks (?,?,?)', ("RHAT", 100, 35.14))
#     test = connection.execute('SELECT * FROM stocks')
#     print(test.description)
#     print(test.fetchall())

connection.close()

def sql_value(value):
    if isinstance(value, basestring):
        return "'" + value + "'"
    else:
        return unicode(value)

class Stock(object):
    def __init__(self, symbol='', quantity=0, price=0.0):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

        @classmethod
        def from_row(cls, row):
            return Stock(*row)

class StockDB(object):
    def __init__(self):
        self.connection = sqlite3.connect('example.db',
                                          check_same_thread=False,
                                          isolation_level='DEFERRED')
        # WAL mode is While-Ahead logging, reading and writing at the same time
        # Readers will read what is available in the db, and will read next data
        # when it will have been inserted by writers
        self._connection.execute('PRAGMA journal_mode = WAL')

    def create_table(self):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('CREATE TABLE stocks (symbol text, quantity real, price real)')

    def insert(self, stock):
        places = ','.join(['?'] * len(stock.__dict__))
        keys = ','.join(stock.__dict__.iterkeys())
        values = tuple(stock.__dict__.itervalues())
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('INSERT INTO stocks ({}) VALUES ({})'.format(
                ", ".join(keys), ", ".join(values)
                ))

    def lookup(self, symbol):
        with closing(self._connnection.cursor()) as cursor:
            cursor.execute('SELECT * FROM stocks WHERE symbol= ?', (symbol,))
            row = cursor.fetchone()
            return Stock.from_row(row) if row else None

    # use a lock when writing
    def transaction(self):
        with self._lock:
            try:
                yield
                self._connection.commit()
            except:
                self._connection.rollback()
                raise

    # create one connection per thread. Whenever we have a connection,
    # we lookup in the dictionary from the thread identifier, and a new connection
    # for the thread is made is there is no connection
    @property
    def connection(self):
        db_connection = thread_connections.get(get_ident(), None)
        if db_connection is None:
            db_connection = self._sqlite_connect()
            thread_connections[get_ident()] = db_connection
