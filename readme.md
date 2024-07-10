# Healthtech Sightline Project

## Project Overview

This project is designed to manage and validate ETL processes for the Healthtech Sightline data pipeline. 
It includes scripts for creating tables, ingesting data, and validating data between environments.


## Files and Their Purpose

### HQL Scripts

- `create_raw_table.hql`: Script to create the `Sightline_application` table in the raw environment.
- `create_curated_table.hql`: Script to create the `Sightline_application` table in the curated environment.
- `create_qa_table.hql`: Script to create the `Sightline_application` table in the QA environment.
- `ingest_raw_to_curated.hql`: Script to ingest data from raw to curated environment.
- `ingest_curated_to_qa.hql`: Script to ingest data from curated to QA environment.

### SQL Scripts

- `ingesting.sql`: there are multiple HQL and SQL scripts for data ingestion the data into different environment also mentioned some table names for references.

### Shell Scripts

- `ingest_raw_to_curated.sh`: Shell script to trigger the ingestion process from raw to curated.
- `ingest_curated_to_qa.sh`: Shell script to trigger the ingestion process from curated to QA.

### Python Validation Script

- `data_validation.py`: Python script for data validation between environments, performing cell-by-cell comparison and logging results.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd healthtech_sightline_project
    ```

2. **Set up environment variables**:
    Update the environment variables in the scripts as needed.

3. **Run HQL Scripts**:
    Navigate to the `hql` directory and run the scripts using Hive:
    ```sh
    hive -f create_raw_table.hql
    hive -f create_curated_table.hql
    hive -f create_qa_table.hql
    ```

4. **Run Shell Scripts**:
    Navigate to the `scripts` directory and execute the ingestion scripts:
    ```sh
    ./ingest_raw_to_curated.sh
    ./ingest_curated_to_qa.sh
    ```

5. **Run Python Validation**:
    Ensure you have Python and required libraries installed (`pandas`, `numpy`, `pyodbc`, `getpass`, `logging`). Run the validation script:
    ```sh
    python validation/data_validation.py
    ```

## Usage

1. **Ingest Data**:
    - Run the shell scripts to move data from raw to curated and then from curated to QA.

2. **Validate Data**:
    - Use the `data_validation.py` script to perform data validation between different environments.
    - Update the `server`, `database`, and `table` variables in the script as needed.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.


