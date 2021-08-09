import mysql.connector
from flask import Flask,request,render_template

#Flask App Conncetion
app = Flask(__name__)

#SQL Connection
global conn,cursor
conn = mysql.connector.connect(
    host='localhost', database='hospital', user='root', password='kailashroot', buffered=True)
cursor = conn.cursor()

global doc_list, doc_details
doc_list = []
doc_details =[]
@app.route('/back')
def maini():
    return render_template('index.html')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result.html', methods = ['POST', 'GET'])
def result():
    select = request.form.get('option')

    if select == 'Book an Appointment':
        sql = 'select dname from doctors_list'
        cursor.execute(sql)
        doctors = cursor.fetchall()
        for doctor in doctors:
            doc_list.append(doctor)
        return render_template('book_appointment.html', result = doc_list)
    else:
        sql = 'select dname, dskill from doctors_list'
        cursor.execute(sql)
        doctors = cursor.fetchall()
        for doctor in doctors:
            doc_details.append([doctor[0], doctor[1]])
        return render_template('search_doctors.html', result = doc_details)

    
@app.route('/booking.html', methods = ['POST', 'GET'])
def booking():
    doc_name = request.form.get('option')
    doc_name = doc_name[1:-2]
    book_date = request.form['book_date']
    sql = "select * from booking_details where dname ={} and booking_date ='{}'".format(doc_name, book_date)
    cursor.execute(sql)
    rows = cursor.rowcount

    if rows < 1:
        cursor.execute("insert into booking_details(dname, booking_date) values({},'{}')".format(doc_name, book_date))
        booking_result = "Successfully Booked"
    else:
        booking_result = "Doctor has other Appointments try another date"
    conn.commit()
    return render_template('booking_result.html', booking = booking_result)

if __name__ == '__main__':
    app.debug = True
    app.run()