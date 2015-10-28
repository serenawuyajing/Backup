
def deleteAllTables(hd):
    hd.execute("select tablename from pg_tables where schemaname = 'public'")
    tables = hd.fetchall()
    for table in tables:
        print table[0]
        hd.execute("drop table "+table[0]+" cascade")
        hd.commit()
    hd.close()
    return 0
