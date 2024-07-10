INSERT OVERWRITE TABLE curated.Sightline_application PARTITION (ingest_yr_mn)
SELECT * FROM raw.Sightline_application;


INSERT OVERWRITE TABLE qa.Sightline_application PARTITION (ingest_yr_mn)
SELECT * FROM curated.Sightline_application;


INSERT OVERWRITE TABLE curated.Sightline_application PARTITION (ingest_yr_mn)
SELECT * FROM raw.Sightline_application;


INSERT OVERWRITE TABLE qa.Sightline_application PARTITION (ingest_yr_mn)
SELECT * FROM curated.Sightline_application;


INSERT OVERWRITE TABLE qa.Sightline_application PARTITION (ingest_yr_mn)
SELECT * FROM curated.Sightline_application;

