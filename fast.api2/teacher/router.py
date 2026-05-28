from fastapi import APIRouter, Depends, UploadFile, File, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from databases import get_db
from .schemas import TeacherProfile
from .models import TeacherModel

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/teacher",
    tags=["teacher"],
    responses={404: {"description": "Not found"}},
)


# DASHBOARD
@router.get("/dashboard", response_class=HTMLResponse)
async def read_teacher_dashboard():

    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Teacher Dashboard</title>

        <style>

            body{
                font-family:Arial;
                background:#f4f6f9;
                padding:40px;
                text-align:center;
            }

            h1{
                margin-bottom:30px;
            }

            a{
                text-decoration:none;
                background:#007bff;
                color:white;
                padding:12px 20px;
                border-radius:6px;
                margin:10px;
                display:inline-block;
            }

            a:hover{
                background:#0056b3;
            }

        </style>

    </head>

    <body>

        <h1>Teacher Dashboard</h1>

        <a href="/teacher/form">
            Add Teacher
        </a>

        <a href="/teacher/view-teachers">
            View Teachers
        </a>

    </body>

    </html>
    """


# CREATE TEACHER
@router.post("/create-teacher")
async def create_teacher(
    id: int = Form(...),
    username: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
    full_name: str = Form(...),
    address: str = Form(...),
    subject: str = Form(...),
    qualification: str = Form(...),
    experience_years: int = Form(...),
    salary: float = Form(...),
    bio: str = Form(None),
    db: Session = Depends(get_db)
):

    new_teacher = TeacherModel(
        id=id,
        username=username,
        email=email,
        age=age,
        full_name=full_name,
        address=address,
        subject=subject,
        qualification=qualification,
        experience_years=experience_years,
        salary=salary,
        bio=bio
    )

    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return f"""
    <html>

    <head>
        <title>Success</title>

        <style>

            body{{
                font-family:Arial;
                background:#f4f6f9;
                text-align:center;
                padding-top:100px;
            }}

            a{{
                text-decoration:none;
                background:#007bff;
                color:white;
                padding:12px 20px;
                border-radius:6px;
                display:inline-block;
                margin-top:20px;
            }}

        </style>

    </head>

    <body>

        <h1>Teacher Created Successfully</h1>

        <h2>{new_teacher.username}</h2>

        <a href="/teacher/view-teachers">
            View Teachers
        </a>

    </body>

    </html>
    """


# API GET ALL TEACHERS
@router.get("/teachers")
async def teachers(db: Session = Depends(get_db)):

    teachers = db.query(TeacherModel).all()

    return {
        "all_teachers": teachers,
        "access": "full"
    }


# UPLOAD FILE
@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):

    content = await file.read()

    text = content.decode("utf-8")

    return {
        "filename": file.filename,
        "text": text
    }


# COUNT WORDS
@router.post("/count-words")
async def count_words(file: UploadFile = File(...)):

    content = await file.read()

    try:
        text = content.decode("utf-8")
    except:
        return {"error": "Only text files are supported"}

    word_count = len(text.split())

    return {
        "filename": file.filename,
        "word_count": word_count
    }


# SUMMARIZE FILE
@router.post("/summarize")
async def summarize_file(file: UploadFile = File(...)):

    content = await file.read()

    try:
        text = content.decode("utf-8")
    except:
        return {"error": "Only text files are supported"}

    summary = text[:200]

    return {
        "filename": file.filename,
        "summary": summary
    }


# FORM PAGE
@router.get("/form", response_class=HTMLResponse)
async def teacher_form():

    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Teacher Form</title>

        <style>

            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial;
            }

            body{
                background:#f4f4f4;
                display:flex;
                justify-content:center;
                align-items:center;
                min-height:100vh;
                padding:20px;
            }

            .container{
                width:100%;
                max-width:700px;
                background:white;
                padding:30px;
                border-radius:10px;
                box-shadow:0 0 10px rgba(0,0,0,0.1);
            }

            h1{
                text-align:center;
                margin-bottom:20px;
            }

            .nav-links{
                text-align:center;
                margin-bottom:25px;
            }

            .nav-links a{
                text-decoration:none;
                background:#007bff;
                color:white;
                padding:10px 18px;
                border-radius:6px;
                margin:5px;
                display:inline-block;
            }

            .form-group{
                margin-bottom:15px;
            }

            label{
                display:block;
                margin-bottom:5px;
                font-weight:bold;
            }

            input, textarea{
                width:100%;
                padding:10px;
                border:1px solid #ccc;
                border-radius:5px;
            }

            button{
                width:100%;
                padding:12px;
                border:none;
                background:#007bff;
                color:white;
                font-size:16px;
                border-radius:5px;
                cursor:pointer;
            }

            button:hover{
                background:#0056b3;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>Add Teacher</h1>

            <div class="nav-links">

                <a href="/teacher/dashboard">
                    Dashboard
                </a>

                <a href="/teacher/view-teachers">
                    View Teachers
                </a>

            </div>

            <form action="/teacher/create-teacher" method="post">

                <div class="form-group">
                    <label>ID</label>
                    <input type="number" name="id" required>
                </div>

                <div class="form-group">
                    <label>Username</label>
                    <input type="text" name="username" required>
                </div>

                <div class="form-group">
                    <label>Email</label>
                    <input type="email" name="email" required>
                </div>

                <div class="form-group">
                    <label>Age</label>
                    <input type="number" name="age" required>
                </div>

                <div class="form-group">
                    <label>Full Name</label>
                    <input type="text" name="full_name" required>
                </div>

                <div class="form-group">
                    <label>Address</label>
                    <textarea name="address"></textarea>
                </div>

                <div class="form-group">
                    <label>Subject</label>
                    <input type="text" name="subject" required>
                </div>

                <div class="form-group">
                    <label>Qualification</label>
                    <input type="text" name="qualification" required>
                </div>

                <div class="form-group">
                    <label>Experience Years</label>
                    <input type="number" name="experience_years" required>
                </div>

                <div class="form-group">
                    <label>Salary</label>
                    <input type="number" step="0.01" name="salary" required>
                </div>

                <div class="form-group">
                    <label>Bio</label>
                    <textarea name="bio"></textarea>
                </div>

                <button type="submit">
                    Create Teacher
                </button>

            </form>

        </div>

    </body>

    </html>
    """


# VIEW TEACHERS PAGE
@router.get("/view-teachers", response_class=HTMLResponse)
async def view_teachers(db: Session = Depends(get_db)):

    teachers = db.query(TeacherModel).all()

    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Teachers List</title>

        <style>

            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial;
            }

            body{
                background:#f4f6f9;
                padding:40px;
            }

            h1{
                text-align:center;
                margin-bottom:30px;
                color:#333;
            }

            .nav-links{
                text-align:center;
                margin-bottom:25px;
            }

            .nav-links a{
                text-decoration:none;
                background:#007bff;
                color:white;
                padding:10px 18px;
                border-radius:6px;
                margin:5px;
                display:inline-block;
            }

            table{
                width:100%;
                border-collapse:collapse;
                background:white;
                box-shadow:0 0 10px rgba(0,0,0,0.1);
                border-radius:10px;
                overflow:hidden;
            }

            th{
                background:#007bff;
                color:white;
                padding:15px;
                text-align:left;
            }

            td{
                padding:12px;
                border-bottom:1px solid #ddd;
            }

            tr:hover{
                background:#f1f1f1;
            }

            .active{
                color:green;
                font-weight:bold;
            }

            .inactive{
                color:red;
                font-weight:bold;
            }

        </style>

    </head>

    <body>

        <h1>Teachers List</h1>

        <div class="nav-links">

            <a href="/teacher/dashboard">
                Dashboard
            </a>

            <a href="/teacher/form">
                Add Teacher
            </a>

            <a href="/teacher/view-teachers">
                Refresh
            </a>

        </div>

        <table>

            <thead>

                <tr>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Email</th>
                    <th>Full Name</th>
                    <th>Subject</th>
                    <th>Qualification</th>
                    <th>Experience</th>
                    <th>Salary</th>
                    <th>Status</th>
                </tr>

            </thead>

            <tbody>
    """

    for teacher in teachers:

        status = (
            "<span class='active'>Active</span>"
            if teacher.is_active
            else "<span class='inactive'>Inactive</span>"
        )

        html += f"""

            <tr>
                <td>{teacher.id}</td>
                <td>{teacher.username}</td>
                <td>{teacher.email}</td>
                <td>{teacher.full_name}</td>
                <td>{teacher.subject}</td>
                <td>{teacher.qualification}</td>
                <td>{teacher.experience_years} Years</td>
                <td>${teacher.salary}</td>
                <td>{status}</td>
            </tr>

        """

    html += """

            </tbody>

        </table>

    </body>

    </html>
    """

    return html