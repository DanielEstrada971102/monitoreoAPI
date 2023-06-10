import requests

dato = {"lugar":"Girardota", "temperatura": 25, "humedad": 67}

res = requests.post("mongodb+srv://DanielEstrada:danielestrada@iot-example-database.kp5zpry.mongodb.net/?retryWrites=true&w=majority", json=dato)

print(res.text)

