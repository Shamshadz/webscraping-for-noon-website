import mysql.connector

#establishing the connection
conn = mysql.connector.connect( user='choudhary', password='choudhary', host='127.0.0.1',port='3306', database='job_data',auth_plugin='mysql_native_password')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
cursor.execute("INSERT INTO job_companydetail (name,description,job_sub_categorey_id,state_id) VALUES (%s,%s,%s,%s)",
            ("company_name","description","Web Developer","punjab",))

# Commit your changes in the database
conn.commit()

cursor.execute("INSERT INTO job_jobdetail (job_position,company_id,location,job_sub_categorey_id) VALUES (%s,%s,%s,%s)",
                                       ("lst[0]","company_name","lst[2]","Web Developer",))

conn.commit()
