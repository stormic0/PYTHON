from bs4 import BeautifulSoup
import requests


path = 'https://maktabkhooneh.org/learn/?q=%D8%AF%D9%88%D8%B1%D9%87+%D9%87%D8%A7%DB%8C+%D9%85%DA%A9%D8%AA%D8%A8+%D9%BE%D9%84%D8%A7%D8%B3'
target_courses = []
r = requests.get(path)
soup = BeautifulSoup(r.text, 'html.parser')
all_courses = soup.find_all('div', attrs={'class':'course-card__content'})
for course in all_courses:
    if 'مکتب‌خونه' in str(course):
        target_courses.append(course)
for course in target_courses:
    print(str(course.find('div', attrs={'class':'course-card__title'})).split('>')[1].split('<')[0])