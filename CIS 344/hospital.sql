CREATE database hospital_portal;

USE hospital_portal;

CREATE TABLE patients (
	patient_id INT NOT NULL,
    patient_name VARCHAR(45) NOT NULL,
    age INT NOT NULL,
    admission_date DATE,
    discharge_date DATE,
    PRIMARY KEY (patient_id)
);

USE hospital_portal;

CREATE TABLE doctors (
    doctor_id INT NOT NULL AUTO_INCREMENT,
    doctor_name VARCHAR(45) NOT NULL,
    specialization VARCHAR(45),
    PRIMARY KEY (doctor_id)

);

USE hospital_portal;

CREATE TABLE Appointments (
	appointment_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time DECIMAL NOT NULL,
    PRIMARY KEY (appointment_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)

);

USE hospital_portal;

INSERT INTO patients (patient_name, age, admission_date, discharge_date)
VALUES 
('John Doe', 30, '2023-12-01', '2023-12-10'),
('Jane Smith', 45, '2023-11-20', '2023-11-30'),
('Robert Johnson', 50, '2023-10-15', '2023-10-25');

DELETE FROM patients WHERE patients_id > 3;

DELIMITER //
CREATE PROCEDURE ScheduleAppointment(IN p_patient_id INT, IN p_doctor_id INT, IN p_appointment_date DATE, IN p_appointment_time DECIMAL)
BEGIN
    INSERT INTO Appointments(patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (p_patient_id, p_doctor_id, p_appointment_date, p_appointment_time);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DischargePatient(IN p_patient_id INT, IN p_discharge_date DATE)
BEGIN
    UPDATE patients
    SET discharge_date = p_discharge_date
    WHERE patient_id = p_patient_id;
END //
DELIMITER ;

INSERT INTO doctors(doctor_name, specialization)
VALUES ('Dr. Roe Botnic', 'Cardiology'),
       ('Dr. Scarlet Smith', 'Neurology'),
       ('Dr. Mary Johnson', 'Orthopedics');
       
CREATE VIEW doctors_appointments_patients AS
SELECT doctors, appointments, patients
FROM appointments
JOIN doctors ON appointments.doctor_id = doctors.id
JOIN patients ON appointments.patient_id = patients.id;


