# postgres specific adapter for connecting to database and querying for desired information
class DbConnection:
    # get tables with SELECT * FROM information_schema.tables WHERE table_schema = 'public' AND table_catalog = %db_name
    # but this won't work for nested schemae
    # SELECT * FROM information_schema.tables WHERE table_catalog = %db_name
    # this will at least probably get every table, and then can be parsed from there, will probably want to build a list
    # of both table and the schema it goes to, for robustness

    # SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'messages'
    # this will get a list of columns from this particular table
    pass
