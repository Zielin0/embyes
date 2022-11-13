@echo off

echo Restoring latest Database...

cat data/dump_latest.sql | docker exec -i postgres-container psql -U embyes embeds

echo Database Restored