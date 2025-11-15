def generate_profile(age: int) -> str:
    if age < 0:
        return 0
    elif age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    else:
        return "Adult"
    
user_name = input("Please enter your full name: ")
birth_year_str = input("Enter your year of birth: ")
birth_year = int(birth_year_str)

current_age = 2025 - birth_year
life_stage = generate_profile(current_age)

hobbies = []
while True:
    hobbie = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobbie.lower() == "stop":
        break
    hobbies.append(hobbie)

hobbies_str = f"Favorite Hobbies ({len(hobbies)}):" + "".join(f"\n- {hobbie}" for hobbie in hobbies) if len(hobbies) != 0 else "You didn't mention any hobbies."

user_profile = {"name" : user_name, "age" : current_age, "stage" : life_stage, "hobbies": hobbies}

print(f"Profile Summary:\nName: {user_profile["name"]}\nAge: {user_profile['age']}\nLife Stage: {user_profile["stage"]}\n{hobbies_str}")