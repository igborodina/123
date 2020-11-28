#Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой

def my_func (name, surname, year, city, email, telephone):
    print(f"name - {name}; surname - {surname}; year - {year}; city - {city}; email - {email}; telephone - {telephone}" )
my_func(name=Irina, surname=Borodina, year=1990, city=Samara, email=red_fox3@bk.ru, telephone=89153518721)

# не понимаю почему не находит