from datetime import datetime

hour = datetime.now().hour
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")
