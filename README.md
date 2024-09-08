# Eskool Manager &middot; [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://semver.org)  

A Flask-based web application for managing students, teachers, periods, subjects, and grading in an educational environment.  

## :star2: Main Features  

- User-friendly interface for managing school data  
- Registration forms for students, teachers, periods, subjects, and sections  
- List views for easy access to registered data  
- Flash messages for user feedback on operations  
- Responsive design for accessibility across devices  

## :gear: Installation  

1. Clone this repository:
```
git clone https://github.com/Serverket/school-manager.git && cd school-manager
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Initialize the database (optional):
```
flask db init
flask db migrate
flask db upgrade
```

4. Start the development server:  
```
flask run
```

5. Open your browser and navigate to `http://localhost:5000`.  

## :brain: Acknowledgements
_"Whoever loves discipline loves knowledge, but whoever hates correction is stupid."_

## :scroll: License  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  