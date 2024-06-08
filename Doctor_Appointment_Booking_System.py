class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

class Appointment:
    def __init__(self, appointment_id, doctor, patient, date, time):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

class AppointmentSystem:
    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.appointments = {}
        self.next_doctor_id = 1
        self.next_patient_id = 1
        self.next_appointment_id = 1

    def add_doctor(self, name, specialty):
        doctor_id = self.next_doctor_id
        self.doctors[doctor_id] = Doctor(doctor_id, name, specialty)
        self.next_doctor_id += 1
        print(f"Doctor added: {name}, Specialty: {specialty}")

    def add_patient(self, name, age):
        patient_id = self.next_patient_id
        self.patients[patient_id] = Patient(patient_id, name, age)
        self.next_patient_id += 1
        print(f"Patient added: {name}, Age: {age}")

    def book_appointment(self, doctor_id, patient_id, date, time):
        if doctor_id not in self.doctors:
            print("Doctor ID not found.")
            return
        if patient_id not in self.patients:
            print("Patient ID not found.")
            return

        appointment_id = self.next_appointment_id
        doctor = self.doctors[doctor_id]
        patient = self.patients[patient_id]
        self.appointments[appointment_id] = Appointment(appointment_id, doctor, patient, date, time)
        self.next_appointment_id += 1
        print(f"Appointment booked: Doctor {doctor.name}, Patient {patient.name}, Date: {date}, Time: {time}")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments booked.")
            return

        for appointment in self.appointments.values():
            print(f"Appointment ID: {appointment.appointment_id}, Doctor: {appointment.doctor.name}, "
                  f"Patient: {appointment.patient.name}, Date: {appointment.date}, Time: {appointment.time}")

# Example usage
if __name__ == "__main__":
    system = AppointmentSystem()
    
    # Add doctors
    system.add_doctor("Dr. Smith", "Cardiology")
    system.add_doctor("Dr. Johnson", "Neurology")
    
    # Add patients
    system.add_patient("Alice", 30)
    system.add_patient("Bob", 40)
    
    # Book appointments
    system.book_appointment(1, 1, "2024-06-10", "10:00 AM")
    system.book_appointment(2, 2, "2024-06-11", "11:00 AM")
    
    # View appointments
    system.view_appointments()

