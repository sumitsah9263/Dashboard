from mysql.connector import Error
from mysql import connector

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def readDetail(visit_id):
    print("Reading BLOB data from python_employee table")

    try:
        mydb = connector.connect(host="database-1.cotkjzj5qzhz.ap-south-1.rds.amazonaws.com",user="admin", passwd="password",use_pure=True, database = 'larkai')

        cursor = mydb.cursor()
        sql_fetch_blob_query = """SELECT * from visit where visit_id = %s"""

        cursor.execute(sql_fetch_blob_query, (visit_id,))
        rows = cursor.fetchall()
        
        for row in rows:
            id = row[0]
            datetime = row[1]
            image = row[2]
            file = row[3]
            ecg_data = row[4]
            pcg_data = row[5]
            Visit_ID=row[6]

        print("Storing employee image and bio-data on disk \n")
        write_file(image, "static/receive_data/new.png")
        write_file(file, "static/receive_data/new.pdf",)
        write_file(ecg_data, "static/receive_data/ecg.csv")
        write_file(pcg_data, "static/receive_data/pcg.csv")
        
        cursor.execute('select * from patient where patient_id="{}"'.format(id))
        row=cursor.fetchall()
        print(row)
        for i in row:
            data=list(i)

        data.append(datetime)
        data.append(Visit_ID)
    except Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        mydb.close()
        print("MySQL connection is closed")
        return data

# readBLOB("visit1")