"""Connection and add data to Crate."""
from crate.client import connect


def insert(k, v):
    """Add the couple keys, values to Crate.

    :type k: list
    :type v: list
    """
    connection = connect('127.0.0.1:4200')
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO {} ({}) VALUES ({})""".format(
        'vulnerabilities',
        ', '.join(k),
        ', '.join('?' * len(v))
    ), v)
    cursor.close()
    connection.close()
