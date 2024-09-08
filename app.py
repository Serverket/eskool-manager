from flask import Flask, render_template, redirect, url_for, flash, request  
from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate  
from models import db, Student, Teacher, Period, Subject, Section, Grade  # Importar modelos  

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SECRET_KEY'] = 'your_secret_key'  
db.init_app(app)  # Inicializar la base de datos  
migrate = Migrate(app, db)  

@app.route('/')  
def index():  
    return render_template('index.html')  

@app.route('/register_student', methods=['GET', 'POST'])  
def register_student():  
    if request.method == 'POST':  
        first_name = request.form['first_name']  
        last_name = request.form['last_name']  
        section = request.form['section']  
        if first_name and last_name and section:  
            new_student = Student(first_name=first_name, last_name=last_name, section=section)  
            db.session.add(new_student)  
            db.session.commit()  
            flash('Estudiante registrado exitosamente.', 'success')  
            return redirect(url_for('list_students'))  
        else:  
            flash('Por favor completa todos los campos obligatorios.', 'danger')  
    return render_template('register_student.html')  

@app.route('/students')  
def list_students():  
    students = Student.query.all()  
    return render_template('list_students.html', students=students)  

@app.route('/register_teacher', methods=['GET', 'POST'])  
def register_teacher():  
    if request.method == 'POST':  
        first_name = request.form['first_name']  
        last_name = request.form['last_name']  
        if first_name and last_name:  
            new_teacher = Teacher(first_name=first_name, last_name=last_name)  
            db.session.add(new_teacher)  
            db.session.commit()  
            flash('Maestro registrado exitosamente.', 'success')  
            return redirect(url_for('list_teachers'))  
        else:  
            flash('Por favor completa todos los campos obligatorios.', 'danger')  
    return render_template('register_teacher.html')  

@app.route('/teachers')  
def list_teachers():  
    teachers = Teacher.query.all()  
    return render_template('list_teachers.html', teachers=teachers)  

@app.route('/register_period', methods=['GET', 'POST'])  
def register_period():  
    if request.method == 'POST':  
        try:  
            name = request.form['name']  
            if name:  
                new_period = Period(name=name)  
                db.session.add(new_period)  
                db.session.commit()  
                flash('Período escolar registrado exitosamente.', 'success')  
                return redirect(url_for('list_periods'))  
            else:  
                flash('Por favor completa todos los campos obligatorios.', 'danger')  
        except KeyError as e:  
            flash(f'Error: Falta el campo {str(e)} en el formulario.', 'danger')  
    return render_template('register_period.html')

@app.route('/periods')  
def list_periods():  
    periods = Period.query.all()  
    return render_template('list_periods.html', periods=periods)  

@app.route('/register_subject', methods=['GET', 'POST'])  
def register_subject():  
    if request.method == 'POST':  
        name = request.form['name']  
        if name:  
            new_subject = Subject(name=name)  
            db.session.add(new_subject)  
            db.session.commit()  
            flash('Materia registrada exitosamente.', 'success')  
            return redirect(url_for('list_subjects'))  
        else:  
            flash('Por favor completa todos los campos obligatorios.', 'danger')  
    return render_template('register_subject.html')  

@app.route('/subjects')  
def list_subjects():  
    subjects = Subject.query.all()  
    return render_template('list_subjects.html', subjects=subjects)  

@app.route('/register_section', methods=['GET', 'POST'])  
def register_section():  
    if request.method == 'POST':  
        name = request.form['name']  
        if name:  
            new_section = Section(name=name)  
            db.session.add(new_section)  
            db.session.commit()  
            flash('Sección registrada exitosamente.', 'success')  
            return redirect(url_for('list_sections'))  
        else:  
            flash('Por favor completa todos los campos obligatorios.', 'danger')  
    return render_template('register_section.html')  

@app.route('/sections')  
def list_sections():  
    sections = Section.query.all()  
    return render_template('list_sections.html', sections=sections)  

@app.route('/assign_teacher', methods=['GET', 'POST'])  
def assign_teacher():  
    teachers = Teacher.query.all()  
    sections = Section.query.all()  
    if request.method == 'POST':  
        teacher_id = request.form['teacher_id']  
        section_ids = request.form.getlist('section_ids')  
        if teacher_id and section_ids:  
            for section_id in section_ids:  
                # Aquí puedes implementar la lógica para almacenar la asignación  
                pass  
            flash('Maestro asignado a secciones exitosamente.', 'success')  
            return redirect(url_for('assign_teacher'))  
        else:  
            flash('Por favor selecciona un maestro y al menos una sección.', 'danger')  
    return render_template('assign_teacher.html', teachers=teachers, sections=sections)  

@app.route('/register_grade', methods=['GET', 'POST'])  
def register_grade():  
    students = Student.query.all()  
    teachers = Teacher.query.all()  
    periods = Period.query.all()  
    subjects = Subject.query.all()  
    if request.method == 'POST':  
        student_id = request.form['student_id']  
        teacher_id = request.form['teacher_id']  
        period_id = request.form['period_id']  
        subject_id = request.form['subject_id']  
        score = request.form['score']  
        if student_id and teacher_id and period_id and subject_id and score:  
            new_grade = Grade(student_id=student_id, teacher_id=teacher_id, period_id=period_id, subject_id=subject_id, score=score)  
            db.session.add(new_grade)  
            db.session.commit()  
            flash('Calificación registrada exitosamente.', 'success')  
            return redirect(url_for('list_grades'))  
        else:  
            flash('Por favor completa todos los campos obligatorios.', 'danger')  
    return render_template('register_grade.html', students=students, teachers=teachers, periods=periods, subjects=subjects)  

@app.route('/grades')  
def list_grades():  
    grades = Grade.query.all()  
    return render_template('list_grades.html', grades=grades)  

@app.route('/reports')  
def reports():  
    students = Student.query.all()  
    teachers = Teacher.query.all()  
    grades = Grade.query.all()  
    periods = Period.query.all()  
    return render_template('reports.html', students=students, teachers=teachers, grades=grades, periods=periods)

@app.errorhandler(404)  
def page_not_found(e):  
    return render_template('404.html'), 404  

@app.errorhandler(500)  
def internal_error(e):  
    return render_template('500.html'), 500  

if __name__ == '__main__':  
    app.run(debug=True)