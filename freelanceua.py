import requests
from bs4 import BeautifulSoup
import json
import time
import csv

# url = "https://freelance.ua/users/"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("index.html", "w", encoding='utf-8') as file:
#     file.write(src)

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_freelancers = soup.find(class_="o-freelancersList").find_all(class_="media")

count = 1
all_freelancers_dict = []

for item in all_freelancers:
    freelancer_link = item.find(class_="f-freelancer-name").find("a").get("href")
    freelancer_name = item.find(class_="f-freelancer-name").find("a").text.strip()
    freelancer_specialization = item.find(class_="f-freelancer-name").find_next("div").find("a").text.strip()
    freelancer_city = item.find(class_="f-freelancer-name").find_next("div").find_next("div").text.strip()
    freelancer_plus = item.find(class_="o-good").text.strip()
    freelancer_rating = item.find(class_="o-feedbacks-inf").find_next("div").find("strong").text.strip()

    all_freelancers_dict.append({
        "name": freelancer_name,
        "link": freelancer_link,
        "specialization": freelancer_specialization,
        "city": freelancer_city,
        "plus": freelancer_plus,
        "rating": freelancer_rating
    })

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(all_freelancers_dict, file, indent=4, ensure_ascii=False)

    count += 1
    print(
        freelancer_link + " : " + freelancer_name + " : " + freelancer_specialization + "\n Город: " + freelancer_city)
    print("Положительных отзывов: " + freelancer_plus + " Рейтинг: " + freelancer_rating)
    print(f"Итерация: {count}")
