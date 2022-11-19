@echo off

echo Dumping latest Database...

if not exist "data" (
  mkdir data
)

docker exec -t postgres-container pg_dump -U embyes --table="embeds" --data-only --column-inserts embeds > data/dump_latest.sql

echo Database Dumped