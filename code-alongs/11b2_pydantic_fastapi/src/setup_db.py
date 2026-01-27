from utils import query_duckdb

query_duckdb("""
    CREATE TABLE IF NOT EXISTS movies(
             title TEXT,
             year INTEGER,
             genre TEXT,
             rating TINYINT
    );

""")

# to run using old uv standard (with new standard 'uv run set_up.py'):
# 'python setup_db.py' - creates a movies.duckdb db in data folder (acc to script in utils.py)
# to access movies.duckdb in terminal navigate to src folder,then 'duckdb data/movies.duckdb'
# after 'D' type 'desc;' to see df
# type D 'from movies' to see what it contains
# Ctrl D to exit and close connection with duckdb database 