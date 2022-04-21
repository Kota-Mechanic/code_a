logs=[
    {"logType": "xurg"},
    {"logType": "4by35"},
    {"logType": "one"},
    {"logType": "44yt52"},
    {"logType": "one"},
    {"logType": "one"},
    {"logType": "4by35"},
    {"logType": "one"},
    {"logType": "one"}
]

a=[element for element in logs if element['logType'] == "one"]
print(len(a))
