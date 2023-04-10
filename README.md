# ecm2434
[![Contributors][contributors-shield]][contributors-url]


<h3 align="center">Gamification of Sustainabilty on Campus</h3>

  <p align="center">
     Web application that uses gamification to
     promote sustainability on campus for people at the University of Exeter
    <br />
    <a href="https://github.com/guy-watson/ecm2434/blob/main/ideas.md">Add an idea to the project!</a>
  </p>

Welcome to TEEM, a Django web application designed to help users explore the campus, become sustainable students, and earn points on our leaderboard. Our app provides an interactive and gamified experience that encourages users to explore the campus and learn more about sustainable living and how they can make a positive impact on out enviroment.

The Uni of Exeter Campus Explorer allows users to scan QR codes located throughout the campus, unlocking quizzes and articles that provide sustainable learning insights into the area where the code was found. The users earn points from completeting the quizzes and reading the articles, then they are placed on the app's leaderboard.

Our app is designed to be user-friendly and accessible, with a modern and intuitive interface that encourages engagement and exploration. Whether you're a new student or a visitor to the campus, our web app offers a fun and educational way to become a sustainable person.

## Table of Contents
- [Getting Started](#start)
- [Built With](#build)
- [Prerequisites](#preq)
- [Installation](#installation)
- [Testing](#test)
- [Contributing](#contributing)
- [License](#license)


## Getting Started <a name="start"></a>
These instructions will allow you to set up the project for development and testing on your local machine.

## Built With <a name="build"></a>
- Django
- Bootstrap
- SQL
- Python

## Prerequisites <a name="preq"></a>
This section includes the software you will need to run the app and how to install it. You will need to install these in the virtual enviroment you are working in.

[Python](https://www.python.org/) you can download this from the website.

Pyzbar
```bash
pip3 install pyzbar
```
OpenCV
```bash
pip3 install opencv-python-headless
```
## Installation <a name="installation"></a>
Here is a step by step on how to get the developement enviroment working.


1. Clone the repository:
```bash
git clone https://github.com/guy-watson/ecm2434-Group-26/
```

2. Change into the project directory:
```bash
cd ecm2434-Group-26/(directory_name)
```

3. Create a virtual environment:
```bash
python3 -m venv env
```

4. Activate the virtual environment:
```bash
source env/bin/activate # on Linux/MacOS
env\Scripts\activate.bat # on Windows
```

5. Install dependencies:
```bash
pip3 install Django
pip3 install opencv-python-headless
pip3 install pyzbar
```

6. Run migrations:
```bash
python3 manage.py migrate
```

7. Create a superuser. You can login into the site as superuser and then into django admin interface where you can edit the questions and answers for the quizzes.
```bash
python3 manage.py createsuperuser
```

8. Run the development server:
```bash
py manage.py runserver
```
At this point you can copy the provided url into your browser to access the website.

To reset the database:
```bash
python3 manage.py flush
```

## Testing <a name="test"></a>
To run the inbuilt tests input the following command when in the working directory:
```bash
python3 manage.py test
```




 # Initial Contributions <a name="contributing"></a>
 ### Guy Watson -> <a href="https://github.com/guy-watson/ecm2434/blob/main/ecm2434/html">Map Navigation and content display pages</a>
 ### James White -> <a href="https://github.com/guy-watson/ecm2434/blob/main/create:login">Login system</a>
 ### Peisi Zheng -> <a href="https://github.com/guy-watson/ecm2434/">Django implementation</a>
 ### Taariq Fadhill -> <a href="https://github.com/guy-watson/ecm2434/blob/main/ecm2434/leaderboard">Leaderboard</a>
 ### Kaloyan Gaydarov -> <a href="https://github.com/guy-watson/ecm2434/blob/main/ecm2434/leaderboard">Leaderboard</a>
 ### Max Ward -> <a href="https://github.com/guy-watson/ecm2434/blob/main/ideas.md"></a>

 The rest of the details of our contributions are found in the workload unit file and the trello page.

# License<a name="license"></a>
  MIT License

Copyright (c) 2023 taariq-fadhill

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[contributors-shield]: https://img.shields.io/github/contributors/guy-watson/ecm2434.svg?style=for-the-badge
[contributors-url]: https://github.com/guy-watson/ecm2434/graphs/contributors
