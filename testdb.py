import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Kamali@123"
)

mycursor = mydb.cursor()
mycursor = mydb.cursor()       
create_table_query_MySql = '''CREATE TABLE IF NOT EXISTS bizcard_details(name varchar(225),
                                                                          designation varchar(225),
                                                                          company_name varchar(225),
                                                                          contact varchar(225),
                                                                          email varchar(225),
                                                                          website text,
                                                                          address text,
                                                                          pincode varchar(225),
                                                                          image text)'''

mycursor.execute(create_table_query_MySql)
mydb.commit()

      # Insert Query

insert_query = '''INSERT INTO bizcard_details(name, designation, company_name,contact, email, website, address,
                                            pincode, image)

                                            values(?,?,?,?,?,?,?,?,?)'''

datas = concat_df.values.tolist()[0]
mycursor.execute(insert_query,datas)
mydb.commit()
       