from mysql.connector import Error
from mysql import connector


def patient(doctor_username):
    try:
        mydb = connector.connect(host="database-1.cotkjzj5qzhz.ap-south-1.rds.amazonaws.com",
                                 user="admin", passwd="password", use_pure=True, database='larkai')

        cursor = mydb.cursor()
        cursor.execute(
            'select * from patient where doctor_username = "'+doctor_username+'"')
        data = cursor.fetchall()

    except Error as error:
        print("Failed to retrieve Patient data from MySQL table {}".format(error))

    finally:
        mydb.close()
        return data


def visit_detail(patient_id):
    try:
        mydb = connector.connect(host="database-1.cotkjzj5qzhz.ap-south-1.rds.amazonaws.com",
                                 user="admin", passwd="password", use_pure=True, database='larkai')

        cursor = mydb.cursor()
        cursor.execute(
            'select patient_id,visit_id,datetime from visit where patient_id = "'+patient_id+'"')
        data = cursor.fetchall()

        cursor.execute(
            'select * from patient where patient_id = "'+data[0][0]+'"')
        pdata = cursor.fetchall()

    except Error as error:
        print("Failed to retrieve Patient data from MySQL table {}".format(error))

    finally:
        mydb.close()
        return data, pdata

# print(visit('PAT123'))
