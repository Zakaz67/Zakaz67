current_users = ["admin", "Lina", "marci", "timbersaw", "nestor"]
new_users = ["Lina", "dima", "jon snow", "ogre mage", "radikaifa"]

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() in current_user.lower():
            print(new_user.lower() + " данное имя занята")
    else:
        print("это имя не занято")