import pandas as pd
import numpy as np
import pyodbc
import getpass
import logging
from datetime import datetime

def fetch_hive_table(hive_host, hive_port, hive_username, hive_password, hive_database, hive_table):
    """Fetch data from Hive table into a Pandas DataFrame."""
    conn = hive.Connection(host=hive_host, port=hive_port, username=hive_username, password=hive_password, database=hive_database)
    cursor = conn.cursor()
    query = f"SELECT * FROM {hive_table}"
    cursor.execute(query)
    columns = [col_desc[0] for col_desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    conn.close()
    return df

def compare_tables(df1, df2, env1_info, env2_info):
    """Compare two Pandas DataFrames cell by cell."""
    differences = []
    num_records = len(df1)
    
    # Log environment, database, and table info
    logging.info(f"Comparing tables:")
    logging.info(f"Environment 1: {env1_info['environment']}, Database: {env1_info['database']}, Table: {env1_info['table']}")
    logging.info(f"Environment 2: {env2_info['environment']}, Database: {env2_info['database']}, Table: {env2_info['table']}")
    logging.info(f"Columns: {', '.join(df1.columns)}")
    logging.info(f"Number of records compared: {num_records}")
    
    for col in df1.columns:
        for idx, val1 in df1[col].iteritems():
            val2 = df2.at[idx, col]
            if val1 != val2:
                differences.append((idx, col, val1, val2))
    
    # Log differences if found
    if differences:
        logging.info("Differences found:")
        for diff in differences:
            idx, col, val1, val2 = diff
            logging.info(f"Row {idx}, Column {col}: {val1} (Table1) != {val2} (Table2)")
    else:
        logging.info("No differences found.")

def main():
    """Main function to compare tables between two environments."""
    
    # Example Hive configurations
    hive_config = {
        'hive_server1': {
            'host': 'hive-qa.example.com',         # Change to your Hive server host
            'port': 10000,                         # Change to your Hive server port
            'database': 'qa_database',             # Change to your Hive database name
            'table': 'product_line',               # Change to your Hive table name
            'username': 'qa_user',                 # Change to your Hive username
            'password': 'qa_password',             # Change to your Hive password
            'environment': 'QA'                    # Change to your environment name <qa,curated,raw,prod>
        },
        'hive_server2': {
            'host': 'hive-curated.example.com',    # Change to your Hive server host
            'port': 10000,                         # Change to your  Hive server port
            'database': 'curated_database',        # Change to your  Hive database name
            'table': 'product_line',               # Change to your Hive table name
            'username': 'curated_user',            # Change to your  Hive username
            'password': 'curated_password',        # Change to your   Hive password
            'environment': 'Curated'               # Change to your environment name <qa,curated,raw,prod>
        }
    }
    
    # Establish connections and fetch data
    dfs = {}  # Dictionary to hold DataFrames for each environment
    for server, config in hive_config.items():
        hive_host = config['host']
        hive_port = config['port']
        hive_database = config['database']
        hive_table = config['table']
        hive_username = config['username']
        hive_password = config['password']
        environment = config['environment']

        # Fetch data from Hive table
        dfs[server] = fetch_hive_table(hive_host, hive_port, hive_username, hive_password, hive_database, hive_table)
    
    # Generate log file name
    table_name = hive_config['hive_server1']['table']
    log_file_name = f"log_file_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{table_name}.txt"
    logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Perform comparison if both tables exist
    if 'hive_server1' in dfs and 'hive_server2' in dfs:
        compare_tables(dfs['hive_server1'], dfs['hive_server2'], hive_config['hive_server1'], hive_config['hive_server2'])
    else:
        logging.info("Tables from both environments are required for comparison.")

if __name__ == "__main__":
    main()
