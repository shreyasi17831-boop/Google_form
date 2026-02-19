print("hello")
from flask import Flask , render_template,request
import sqlite3

app = Flask(__name__)

#create database

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS students
                   (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email TEXT,
                   password TEXT,
                   dob DATE,
                   gender TEXT,
                   course TEXT,
                   skills TEXT,
                   msg TEXT,
                   rating INTEGER
                   )
                   """)
    conn.commit()
    conn.close()
init_db()


@app.route("/")
def home():
        return render_template("googleform.html")
    

@app.route("/submit",methods=["POST"])

def submit():
        name= request.form.get("name")
        email = request.form.get("email")
        password =request.form.get("password")
        dob=request.form.get("dob")
        gender =request.form.get("gender")
        course=request.form.get("course")
        msg = request.form.get("msg")
        rating = request.form.get("rating")

        skills = request.form.getlist("skills")
        skills = ",".join(skills)

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students
        (name , email , password , dob, gender,course, skills, msg, rating)
                       VALUES(?,?,?,?,?,?,?,?,?)
                       """, (name,email,password,dob,gender,course,skills,msg,rating))
        
        conn.commit()
        conn.close()

        return "Form Submitted successfully!"
    
if __name__ == "__main__":
        app.run(debug=True, port=8000)
