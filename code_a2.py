data_a=[
    {"dataType": "xurg"},
    {"dataType": "4by35"},
    {"dataType": "one"},
    {"dataType": "44yt52"},
    {"dataType": "one"},
    {"dataType": "one"},
    {"dataType": "4by35"},
    {"dataType": "one"},
    {"dataType": "one"}
]

a=[element for element in data_a if element['dataType'] == "one"]
print(len(a))
