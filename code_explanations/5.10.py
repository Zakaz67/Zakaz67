current_users = ["admin", "lina", "marci", "timbersaw", "nestor"]
new_users = ["lina", "dima", "jon snow", "ogre mage", "radikaifa"]


for new_user in new_users:
    if new_user in current_users:
        print(new_user.lower() + " данное имя занята")
    else:
        print("это имя не занято")