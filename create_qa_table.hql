CREATE EXTERNAL TABLE IF NOT EXISTS qa.Sightline_application (
    application_id STRING,
    application_name STRING,
    application_version STRING,
    release_date TIMESTAMP,
    status STRING,
    created_by STRING,
    created_date TIMESTAMP,
    updated_by STRING,
    updated_date TIMESTAMP,
    ingest_yr_mn STRING
)
PARTITIONED BY (ingest_yr_mn STRING)
STORED AS ORC
LOCATION 'hdfs://<hdfs_env_nm>/qa/healthtech/sightline/hive';
