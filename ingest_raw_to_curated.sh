#!/bin/bash

# Variables
HIVE_BIN=/usr/bin/hive
HQL_FILE=/path/to/hql/ingest_raw_to_curated.hql

# Execute Hive script
$HIVE_BIN -f $HQL_FILE
