import sqlite3

#create database or connect to existing one
con=sqlite3.connect('./data.db')

#create a cursor to fetch or send data to database
c=con.cursor()

#creating tables
# c.execute("""CREATE TABLE details(
#     website text,
#     password text,
#     other_details text
# )""")

#inserting entries
# c.execute("INSERT INTO details VALUES (:website,:password,:other_details)",
#     {
#         'website':"ktz.in",
#         'password':"23242",
#         'other_details':"this is a trial"
#     })


#querying entries
c.execute("SELECT *,oid FROM details")
# c.fetchone()

print(c.fetchall())

#deleting entries
s="this is a trial"
c.execute("DELETE from details WHERE other_details="+s)

#updating entries
c.execute("""UPDATE details SET
    website=:var,
    password=:var,
    
    WHERE oid=:oid""",
    {
        'var':value
    } )
    
#commit changes to database
con.commit()

#closing connection to database
con.close()