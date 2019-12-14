from flask import Flask , render_template , request , flash, redirect , url_for
from formwt import Represent , Vote
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

#CSRF TOKEN 

app.config['SECRET_KEY'] = 'ChaosIsALadder' #PROTECTING CSRF

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aryan'
app.config['MYSQL_DB'] = 'polling'

#DIRECTING TO HOME PAGE
@app.route('/')
def homepage():
    return render_template('homepage.html')

#DIRECTING TO REPRESENTAIVE PAGE
@app.route('/represent' , methods = ['GET','POST'])
def representpage():
    error = ''
    form = Represent()
    if form.validate_on_submit():
        details = request.form
        name = details['name']
        username = details['username']
        age = details['age']
        cur = mysql.connection.cursor()
        check_user = cur.execute(f'SELECT username FROM register WHERE username = "{username}"')
        if check_user > 0:
            error = 'Username already exists . Please choose a different one'
        else:
            cur.execute(f'INSERT INTO register(name,username,age) VALUES ("{name}","{username}",{age})')
            mysql.connection.commit()
            cur.close() 
            flash('Successfully registered as a representative')
            return redirect(url_for('homepage'))
        mysql.connection.commit()
        cur.close()   
    return render_template('represent.html' , reg = form , message1 = error)

#DIRECTING TO VOTER PAGE: 
@app.route('/vote' , methods = ['GET','POST'])
def aboutpage():
    message2 = ''
    form = Vote()
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM register")
    usernames = cur.fetchall()
    cur.execute("SELECT age FROM register")
    ages = cur.fetchall()
    cur.execute("SELECT id FROM register")
    ids = cur.fetchall()
    final = sorted(list(zip(usernames,ages,ids)) , key = lambda item : item[2][0])
    if final == []:
        message2 = 'No registered representatives'
        mysql.connection.commit()
        cur.close()
    else:
        if form.validate_on_submit():
            detail = request.form
            value = detail['ieee']
            cur = mysql.connection.cursor()
            cur.execute(f'SELECT votes FROM register WHERE username = "{value}"')
            current_votes = cur.fetchall()[0][0]
            cur.execute(f'UPDATE register SET votes = {current_votes+1} WHERE username = "{value}"')
            mysql.connection.commit()
            cur.close()
            flash('Your precious vote has been recorded !')
            return redirect(url_for('homepage'))
    return render_template('voter.html' , form =form , new = final , message2=message2)

#DIRECTING TO ABOUT PAGE: 
@app.route('/about')
def voterpage():
    return render_template('about.html')

#REDIRECTING TO RESULT PAGE
@app.route('/result')
def resultpage():
    message1 = ''
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM register ORDER BY id")
    usernames = cur.fetchall()
    cur.execute("SELECT votes FROM register")
    votes = cur.fetchall()
    final = sorted(list(zip(usernames,votes)) , key = lambda item: item[1][0], reverse=True)
    if final == []:
        message1 = 'No results to display'
    mysql.connection.commit()
    cur.close()
    return render_template('result.html', message1 = message1 , new = final)

#CLEARING DATABASE

@app.route('/clear')
def cleardatabase():
    cur = mysql.connection.cursor()
    cur.execute('TRUNCATE TABLE register')
    flash('Successfully deleted all records')
    return redirect(url_for('homepage'))


if "__main__" == __name__:
    app.run(debug=True) 
