# Embyes

Work in progress...

## Issues

High Severity issue!!!

When calling `/new` route SQL Injection is possible

Need unique url that does not exist in db and change description to `'); query; --`

For example:

```sql
'); DELETE FROM embeds; --
```

`http://localhost:6969/new?url=uniqueurl&color=00ff00&title=title&description='); DELETE FROM embeds; --`

And all table data will be deleted.