from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()  

class Student(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    first_name = db.Column(db.String(100), nullable=False)  
    last_name = db.Column(db.String(100), nullable=False)  
    section = db.Column(db.String(100), nullable=False)  

class Teacher(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    first_name = db.Column(db.String(100), nullable=False)  
    last_name = db.Column(db.String(100), nullable=False)  

class Period(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), nullable=False)  

class Subject(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), nullable=False)  

class Section(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), nullable=False)  

class Grade(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)  
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)  
    period_id = db.Column(db.Integer, db.ForeignKey('period.id'), nullable=False)  
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)  
    score = db.Column(db.Float, nullable=False)