from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import mongo_db, mysql_cursor, mysql_db


app = Flask(__name__)
app.secret_key = 'secret_key' 

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Page    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Kanishq" and password == "Kanishq=07":
            return redirect('/dashboard')
        else:
            flash("Invalid username or password", "danger")
    return render_template('login.html')

# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Add Patient
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        # Get data from the form
        patient_data = {
            "Patient_ID": request.form['Patient_ID'],
            "Name": request.form['Name'],
            "Age": int(request.form['Age']),
            "Gender": request.form['Gender'],
            "Address": request.form['Address'],
            "Phone": request.form['Phone'],
            "Medical_History": request.form['Medical_History']
        }
        
        # Insert data into MongoDB
        mongo_db.Patients.insert_one(patient_data)

        # Insert data into MySQL
        query = """INSERT INTO Patients (Patient_ID, Name, Age, Gender, Address, Phone, Medical_History)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (
            patient_data["Patient_ID"],
            patient_data["Name"],
            patient_data["Age"],
            patient_data["Gender"],
            patient_data["Address"],
            patient_data["Phone"],
            patient_data["Medical_History"]
        )
        mysql_cursor.execute(query, values)
        mysql_db.commit()  # Commit the transaction to MySQL

        flash("Patient added successfully!", "success")
        return redirect('/dashboard')
    return render_template('add_patient.html')



# View Patients
@app.route('/view_patients')
def view_patients():
    patients = list(mongo_db.Patients.find())
    return render_template('view_patients.html', patients=patients)

# Add Doctor
@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        # Get data from the form
        doctor_data = {
            "Doctor_ID": request.form['Doctor_ID'],
            "Name": request.form['Name'],
            "Specialization": request.form['Specialization'],
            "Phone": request.form['Phone'],
            "Experience": request.form['Experience']
        }
        
        # Insert data into MongoDB
        mongo_db.Doctors.insert_one(doctor_data)

        # Insert data into MySQL
        query = """INSERT INTO Doctors (Doctor_ID, Name, Specialization, Phone, Experience)
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (
            doctor_data["Doctor_ID"],
            doctor_data["Name"],
            doctor_data["Specialization"],
            doctor_data["Phone"],
            doctor_data["Experience"]
        )
        mysql_cursor.execute(query, values)
        mysql_db.commit()  # Commit the transaction to MySQL

        flash("Doctor added successfully!", "success")
        return redirect('/dashboard')
    return render_template('add_doctor.html')


# View Doctors
@app.route('/view_doctors')
def view_doctors():
    doctors = list(mongo_db.Doctors.find())
    return render_template('view_doctors.html', doctors=doctors)

# Schedule Appointment
@app.route('/schedule_appointment', methods=['GET', 'POST'])
def schedule_appointment():
    if request.method == 'POST':
        # Get data from the form
        appointment_data = {
            "Appointment_ID": request.form['Appointment_ID'],
            "Patient_ID": request.form['Patient_ID'],
            "Doctor_ID": request.form['Doctor_ID'],
            "Date": request.form['Date'],
            "Time": request.form['Time'],
            "Status": "Scheduled"
        }

        # Insert data into MongoDB
        mongo_db.Appointments.insert_one(appointment_data)

        # Insert data into MySQL
        query = """INSERT INTO Appointments (Appointment_ID, Patient_ID, Doctor_ID, Date, Time, Status)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (
            appointment_data["Appointment_ID"],
            appointment_data["Patient_ID"],
            appointment_data["Doctor_ID"],
            appointment_data["Date"],
            appointment_data["Time"],
            appointment_data["Status"]
        )
        mysql_cursor.execute(query, values)
        mysql_db.commit()  # Commit the transaction to MySQL

        flash("Appointment scheduled successfully!", "success")
        return redirect('/dashboard')
    return render_template('schedule_appointment.html')


# View Appointments
@app.route('/view_appointments')
def view_appointments():
    appointments = list(mongo_db.Appointments.find())
    return render_template('view_appointments.html', appointments=appointments)

# Generate Bill
@app.route('/generate_bill', methods=['GET', 'POST'])
def generate_bill():
    if request.method == 'POST':
        appointment_id = request.form['Appointment_ID']
        
        # Check if appointment exists in MongoDB
        appointment = mongo_db.Appointments.find_one({"Appointment_ID": appointment_id})
        if not appointment:
            flash("Invalid Appointment ID!", "danger")
            return redirect('/generate_bill')

        # Proceed with bill generation
        bill_data = {
            "Bill_ID": request.form['Bill_ID'],
            "Appointment_ID": appointment_id,
            "Total_Amount": float(request.form['Total_Amount']),
            "Payment_Status": "Pending"
        }

        # Insert data into MongoDB
        mongo_db.Billing.insert_one(bill_data)

        # Insert data into MySQL
        query = """INSERT INTO Billing (Bill_ID, Appointment_ID, Total_Amount, Payment_Status)
                   VALUES (%s, %s, %s, %s)"""
        values = (
            bill_data["Bill_ID"],
            bill_data["Appointment_ID"],
            bill_data["Total_Amount"],
            bill_data["Payment_Status"]
        )
        mysql_cursor.execute(query, values)
        mysql_db.commit()  # Commit the transaction to MySQL

        flash("Bill generated successfully!", "success")
        return redirect('/dashboard')
    return render_template('generate_bills.html')



# View Bills
@app.route('/view_bills')
def view_bills():
    bills = list(mongo_db.Billing.find())
    return render_template('view_bills.html', bills=bills)

@app.route('/update_payment_status/<int:payment_id>', methods=['POST'])
def update_payment_status(payment_id):
    # Extract the payment status from the request form
    payment_status = request.form.get('Payment_Status')

    # Example logic to update the payment status in your database
    if payment_status:
        # Add database update logic here
        return f"Payment status for ID {payment_id} updated to {payment_status}", 200
    else:
        return "Payment status not provided", 400



if __name__ == '__main__':
    app.run(debug=True)
