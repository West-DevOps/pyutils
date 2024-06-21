import sys
import pprint
import pandas
import sqlite3


def main() -> None:
    db_conn = sqlite3.Connection("db.sqlite3")
    pandas_df = pandas.read_json(sys.argv[1])

    pandas_df.to_sql('test', db_conn, index=False, if_exists='replace')
    pprint.pprint(pandas_df)


if __name__ == '__main__':
    main()
