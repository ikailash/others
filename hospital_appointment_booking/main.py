import mysql.connector
from flask import Flask,request,render_template

#Flask App Conncetion
app = Flask(__name__)

#SQL Connection
global conn,cursor
conn = mysql.connector.connect(
    host='localhost', database='hospital', user='root', password='kailashroot')
cursor = conn.cursor()

global doc_list
doc_list = []
@app.route('/back')
def maini():
    return render_template('index.html')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result.html', methods = ['POST', 'GET'])
def result():
    select = request.form.get('option')
    #data = request.form['input']

    if select == 'Book an Appointment':
        sql = 'select dname from doctors_list;'
        cursor.execute(sql)
        doctors = cursor.fetchall()
        for doctor in doctors:
            doc_list.append(doctor)
        return render_template('book_appointment.html', result = doc_list)
    
@app.route('/booking.html', methods = ['POST', 'GET'])
def booking():
    select = request.form.get('option')

    if select == 'chandru':
        print("GOT to CHANDRU");
if __name__ == '__main__':
    app.debug = True
    app.run()