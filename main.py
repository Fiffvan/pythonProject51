import requests

url = "https://www.boredapi.com/api/activity/"

params = {
    "type": "recreational",
    "participants": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if data.get("activity"):
        activity = data["activity"]
        activity_type = data.get("type")
        participants = data.get("participants")
        key = data.get("key")
        availability = data.get("accessibility")

        print("Случайная активность:", activity)
        print("Тип активности:", activity_type)
        print("Участники:", participants)
        print("Ключ:", key)
        print("Доступность:", availability)
    else:
        print("К сожалению, не удалось найти активность по вашем запросу.")
else:
    print("Ошибка при получении данных. Код ответа:", response.status_code)