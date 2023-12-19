import mysql.connector
from mysql.connector import Error

class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="hospital_portal",
                 user='root',
                 password='Blackops@6127'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def addPatient(self, patient_name, age, admission_date, discharge_date):
        ''' Method to insert a new patient into the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO patients (patient_name, age, admission_date, discharge_date) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (patient_name, age, admission_date, discharge_date))
            self.connection.commit()
            return

    def getAllPatients(self):
        ''' Method to get all patients from the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM patients LIMIT 0,3"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def scheduleAppointment(self, appointment_id, p_patient_id, p_doctor_id, p_appointment_date, p_appointment_time):
        ''' Method to schedule an appointment '''
        # Implement the functionality
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CALL scheduleAppointment()"
            self.cursor.execute(query,(appointment_id, p_patient_id, p_doctor_id, p_appointment_date, p_appointment_time))
            self.connection.commit()
        pass

    def viewAppointments(self):
        ''' Method to view all appointments '''
        # Implement the functionality
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CREATE VIEW doctors_appointments_patients AS SELECT doctors, appointments, patients FROM appointments JOIN doctors ON appointments.doctor_id = doctors.id JOIN patients ON appointments.patient_id = patients.id"
            self.cursor.execute(query)
            self.connection.commit()
            records = self.cursor.fetchall()
            return records
        pass

    def dischargePatient(self, p_discharge_date, p_patient_id):
        ''' Method to discharge a patient '''
        # Implement the functionality
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CALL dischargePatient()"
            self.cursor.execute(query, p_discharge_date, p_patient_id)
            self.connection.commit()
        pass


    def addDoctors(self, doctor_name, specialization):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO doctors(doctor_name, specialization) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, doctor_name, specialization)
            self.connection.commit()
        pass
            