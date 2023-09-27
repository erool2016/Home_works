import datetime
from application.salary import print_salary
from application.db.people import people_map
from bs4_.req import response



if __name__ == '__main__':
    print('Сегодняшняя дата - ',datetime.datetime.now())
    print_salary()
    people_map()
    print(response.text)


