import datetime
import os
import django
import csv

os.environ["DJANGO_SETTINGS_MODULE"] = "employees_manages.settings"
django.setup()

from employees_manages_app.models import *


# new_movie = Movie(movie_name="ccc", release_year=2021, duration_in_min=14)
# new_movie.save()


def get_person_name_by_id(person_id: int) -> str:
    """
    Given person id, return string that represents person full name
    :param person_id:
    :return:
    """
    person = Person.objects.get(id=person_id)
    print(f"{person.first_name} {person.last_name}")
    return f"{person.first_name} {person.last_name}"


def get_people_by_age(age: int) -> list[Person]:
    """
    Given age in years, return list of persons of this age
    :param age:
    :return:
    """
    age_year = datetime.datetime.now().year - age
    person = Person.objects.filter(birth_date__year=age_year)
    return person


def get_people_cnt_by_gender(gender: str) -> list[Person]:
    """
    Given the gender, return list of people of this gender
    :param gender:
    :return:
    """
    person = Person.objects.filter(gender=gender)
    return person


def get_companies_by_country(country: str) -> list[str]:
    """
    Given country name, return list of companies' names in this country
    :param country:
    :return:
    """
    company = Company.objects.filter(country=country)
    return company
    pass


def get_company_employees(company_id: int, current_only: bool) -> list[Person]:
    """
    Given company id, return list of persons whi work(ed) for this company
    :param company_id:
    :param current_only: if True, return only people who are currently work in the company
    :return:
    """
    # comp = Company.objects.get(id=company_id).prefetch_related('persons')
    if current_only:
        return Company.objects.get(id=company_id).persons.filter(employee__is_current_job=True)
    else:
        return Company.objects.get(id=company_id).persons.all()


def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    """
    Given person_id, return list of dictionaries that map from company name to job title
    :param person_id:
    :return:
    """
    # l = []
    # p = Person.objects.get(id=person_id)
    # for per in p.company_set.all().prefetch_related('employee_set'):
    #     l.append({per.company_name: per.employee_set.filter(company_id=per, person_id=p)[0].job_title})
    # print(l)

    l = []
    p = Person.objects.get(id=person_id).company_set.all().values_list('company_name', 'employee__job_title')

    for pp in p:
        l.append({pp[0]: pp[1]})
    return l

    pass


if __name__ == '__main__':
    try:

        get_person_name_by_id(1)
        for val in get_people_by_age(30):
            print(f"{val.first_name} {val.last_name}: {datetime.datetime.now().year - val.birth_date.year} year old")
        for people in get_people_cnt_by_gender('Female'):
            print(f"- {people.first_name} {people.last_name}")
        for comp in get_companies_by_country('China'):
            print(f"{comp.company_name}")

        print(get_company_employees(4, True))
        get_person_jobs(95)

    except Exception as e:
        print(e)


















    # with open('files\\persons.csv', 'r') as cv:
    #     cv_reade = csv.DictReader(cv, delimiter=',')
    #     for item in cv_reade:
    #         # date = datetime.datetime.strptime(item['birth_date'], "%d/%m/%Y")
    #
    #         Person(first_name=item['first_name'],
    #                last_name=item['last_name'],
    #                personal_email=item['personal_email'],
    #                gender=item['gender'],
    #                birth_date=datetime.datetime.strptime(item['birth_date'], "%m/%d/%Y").date(),
    #                id=int(item['id'])).save()

    # id,company_name,country,city,address,phone_num
    # with open('files\\companies.csv', 'r', encoding='utf-8') as cv:
    #     cv_reade = csv.DictReader(cv, delimiter=',')
    #     for item in cv_reade:
    #         Company(id=item['id'],
    #                 company_name=item['company_name'],
    #                 country=item['country'],
    #                 city=item['city'],
    #                 address=item['address'],
    #                 phone_num=item['phone_num']).save()

    # id,person_id,company_id,job_title,is_current_job,company_email
    # with open('files\\employees.csv', 'r') as cv:
    #     cv_reade = csv.DictReader(cv, delimiter=',')
    #     for item in cv_reade:
    #         p = Person.objects.get(id=item['person_id'])
    #         c = Company.objects.get(id=item['company_id'])
    #         Employee(id=item['id'],
    #                  person=p,
    #                  company=c,
    #                  job_title=item['job_title'],
    #                  is_current_job=item['is_current_job'].title(),
    #                  company_email=item['company_email']).save()
