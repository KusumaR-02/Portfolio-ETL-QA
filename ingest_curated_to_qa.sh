#!/bin/bash

# Variables
HIVE_BIN=/usr/bin/hive
HQL_FILE=/path/to/hql/ingest_curated_to_qa.hql

# Execute Hive script
$HIVE_BIN -f $HQL_FILE
