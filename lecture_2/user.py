def generate_profile(age):
    if age >= 0 and age <= 12:
        return 'Child'
    elif age >= 13 and age <= 19:
        return 'Teenager'
    elif age >= 20:
        return 'Adult'
    
user_name = input('Enter your full name: ')
birth_year_str = input('Enter your birth year: ')
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

hobbies = []
while True:
    i = input("Enter a favorite hobby or type 'stop' to finish: ")
    if i == 'stop':
        break
    hobbies.append(i)

life_stage = generate_profile(current_age)

user_profile = {
    'Name': user_name,
    'Age': current_age,
    'Life Stage': life_stage,
    'Favorite Hobbies': hobbies
}

print('---')
print('Profile Summary:')
print(f"Name: {user_profile['Name']}")
print(f"Age: {user_profile['Age']}")
print(f"Life Stage: {user_profile['Life Stage']}")

if len(user_profile['Favorite Hobbies']) <= 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['Favorite Hobbies'])}):")
    for hobby in user_profile['Favorite Hobbies']:
        print(f"- {hobby}")
print('---')


