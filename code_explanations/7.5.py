while True:
    vozrast = int(input("ваш возрасть:"))
    if vozrast < 3:
        print("бесплатно")
    elif vozrast < 12:
        print("10 баксов")
    else:
        print("15 баксов ")
