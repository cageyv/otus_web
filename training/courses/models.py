import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Teacher(User):
    POSTGRADUATE = 1
    ASSOCIATE_PROFESSOR = 2
    HEAD_OF_DEPARTMENT = 3
    POSITIONS = (
        (POSTGRADUATE, 'Postgraduate'),
        (ASSOCIATE_PROFESSOR, 'Associate Professor'),
        (HEAD_OF_DEPARTMENT, 'Head of Departament'),
    )
    position = models.CharField(
        max_length=2, choices=POSITIONS, default=POSTGRADUATE
    )
    courses = models.ManyToManyField(
        'Class', related_name='teachers', blank=True
    )

    def __str__(self):
        return f'{self.position} {self.last_name}'

    class Meta:
        ordering = 'position', 'last_name'


class Student(User):
    FRESHMAN = 1
    SOPHOMORE = 2
    JUNIOR = 3
    SENIOR = 4
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    graduated = models.PositiveIntegerField(
        default=datetime.date.today().year,
        validators=[
            MinValueValidator(1970),
            max_value_current_year
        ]
    )
    year_in_school = models.CharField(
        max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN
    )
    courses = models.ManyToManyField(
        'Class', related_name='students', blank=True
    )

    def __str__(self):
        return f'{self.year_in_school} {self.first_name} {self.last_name}'

    class Meta:
        ordering = '-graduated', 'year_in_school', 'last_name'


class Class(models.Model):
    name = models.CharField(max_length=40)
    started = models.PositiveIntegerField(
        default=datetime.date.today().year,
        validators=[
            MinValueValidator(1970),
            max_value_current_year
        ]
    )

    def __str__(self):
        return f'{self.name} {self.started}'

    class Meta:
        ordering = ('name',)


class Lesson(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    duration = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    learning_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.learning_class} {self.start_time}'

    class Meta:
        ordering = 'learning_class', '-start_time'


class LessonGrade(models.Model):
    A_GRADE = 'A'
    B_GRADE = 'B'
    C_GRADE = 'C'
    D_GRADE = 'D'
    GRADES = (
        (A_GRADE, 'Excellent'),
        (B_GRADE, 'Good'),
        (C_GRADE, 'Fair'),
        (D_GRADE, 'Poor'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=GRADES)

    def __str__(self):
        return f'{self.grade} {self.student} {self.lesson}'

    class Meta:
        ordering = 'student', 'lesson', 'grade'


class ClassGrade(models.Model):
    A_GRADE = 'A'
    B_GRADE = 'B'
    C_GRADE = 'C'
    D_GRADE = 'D'
    GRADES = (
        (A_GRADE, 'Excellent'),
        (B_GRADE, 'Good'),
        (C_GRADE, 'Fair'),
        (D_GRADE, 'Poor'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=GRADES)

    def __str__(self):
        return f'{self.student} {self.course} {self.grade}'

    class Meta:
        ordering = 'student', 'course', 'grade'
