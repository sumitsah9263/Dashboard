from mysql import connector
import mysql.connector
from mysql.connector import Error
import datetime

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(patient_id, datetime, photo, report, ecg, pcg):
    print("Inserting BLOB into table")
    try:
        mydb = connector.connect(host="database-1.cotkjzj5qzhz.ap-south-1.rds.amazonaws.com",user="admin", passwd="password",use_pure=True, database = 'larkai')
        cursor = mydb.cursor()
        sql_insert_blob_query = """ INSERT INTO visit VALUES (%s,%s,%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(report)
        ecg_data = convertToBinaryData(ecg)
        pcg_data = convertToBinaryData(pcg)
        
        # Convert data into tuple format
        insert_blob_tuple = (patient_id, datetime, empPicture, file, ecg_data, pcg_data)
        
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        mydb.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("{}".format(error))

    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

insertBLOB('PAT123', "NULL", r"C:\Users\sibup\PycharmProjects\Cardio\Sibam2021-01-29\greyscale.bmp",
           r"C:\Users\sibup\PycharmProjects\Cardio\Sibam2021-01-29\Sibam.pdf",
           r"C:\Users\sibup\PycharmProjects\Cardio\692302_ecg.csv",
           r"C:\Users\sibup\PycharmProjects\Cardio\692302_pcg.csv")