def expert_system(weather, temperature):

    if weather == "rainy":
        print("Recommendation: Take an umbrella")

    elif weather == "sunny" and temperature > 30:
        print("Recommendation: Drink water and stay cool")

    elif weather == "sunny":
        print("Recommendation: Good day for outdoor activity")

    else:
        print("Recommendation: Check the weather conditions")


weather = input("Enter weather (sunny/rainy): ")
temperature = int(input("Enter temperature: "))

expert_system(weather, temperature)