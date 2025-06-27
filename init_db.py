from tinydb import TinyDB

db = TinyDB("db.json")
db.truncate()

# Добавим формы
db.insert({
    "name": "User Form",
    "login": "email",
    "tel": "phone"
})

db.insert({
    "name": "Order Form",
    "customer": "text",
    "order_id": "text",
    "order_date": "date",
    "contact": "phone"
})
