import requests

API_KEY = "31fc4fee03bc87a6fca0f60658766166"
city = "Thanh Hoa"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

res = requests.get(url)
data = res.json()

if res.status_code == 200:
    print(f"Thời tiết ở {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
else:
    print("Lỗi:", data)
    print()