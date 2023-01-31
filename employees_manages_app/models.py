from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.

# Person, Company, Employee
# id,first_name,last_name,personal_email,gender,birth_date
# id,company_name,country,city,address,phone_num
# id,person_id,company_id,job_title,is_current_job,company_email


class Person(models.Model):

    first_name = models.CharField(db_column='first_name', max_length=256, null=False, blank=False)
    last_name = models.CharField(db_column='last_name', max_length=256, null=False, blank=False)
    personal_email = models.EmailField(db_column='personal_email', null=False, blank=False)
    FEMALE = 'female'
    MALE = 'male'
    OTHER = 'other'
    POLYGENDER= 'Polygender'
    GENDERFLUID = 'Genderfluid'
    BIGENDER = 'Bigender'
    AGENDER = 'Agender'
    GENDER_CHOICES = [
        (FEMALE, 'female'),
        (MALE, 'male'),
        (OTHER, 'other'),
        (POLYGENDER, 'Polygender'),
        (GENDERFLUID, 'Genderfluid'),
        (BIGENDER, 'Bigender'),
        (AGENDER, 'Agender')
    ]
    gender = models.CharField(db_column='gender', max_length=16, choices=GENDER_CHOICES)
    birth_date = models.DateField(db_column='birth_date',
                                  validators=[MinValueValidator(datetime.datetime(year=1900, month=1, day=1)),
                                              MaxValueValidator(datetime.datetime.now)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'person'


class Company(models.Model):

    company_name = models.CharField(db_column='company_name', max_length=256, null=False, blank=False)
    country = models.CharField(db_column='country', max_length=256, null=True)
    city = models.CharField(db_column='city', max_length=256, null=True)
    address = models.CharField(db_column='address', max_length=256, null=True)
    phone_num = models.CharField(db_column='phone_num', max_length=16)

    persons = models.ManyToManyField(Person, through='Employee')

    class Meta:
        db_table = 'company'


class Employee(models.Model):

    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    job_title = models.CharField(db_column='job_title', max_length=256, null=False, blank=False)
    is_current_job = models.BooleanField(db_column='is_current_job', null=False, blank=False)
    company_email = models.EmailField(db_column='company_email')

    class Meta:
        db_table = 'employee'












