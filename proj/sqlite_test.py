import sqlite3
import pandas as pd


db_file = 'test.db'
conn = sqlite3.connect(db_file, isolation_level=None,   
                       detect_types=sqlite3.PARSE_COLNAMES)

# table = ['sys_menu', 'sys_role', 'sys_user', 'sys_role_menu', 'sys_user_role']

# for t in table:
#     sql = 'SELECT * FROM ' + t
#     db_df = pd.read_sql_query(sql, conn)
#     file = t + '.csv'
#     db_df.to_csv(file, index=False)

file = 'sys_user_test.csv'
df = pd.read_csv(file)
table = 'sys_user'
df.to_sql(table, conn, if_exists='append', index=False)