


#                                                                  ("Vaccination scheduling System")


import json
from admin import Admin  # Assuming you have an Admin class in admin.py
from user import User  # Assuming you have a User class in user.py

def get_user_data():
    user_id = int(input("Enter user ID: "))
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    password = input("Enter user password: ")
    phone_number = input("Enter user phone number: ")
    national_id = int(input("Enter user national ID: "))
    return User(user_id=user_id, name=name, email=email, password=password, phone_number=phone_number, national_id=national_id)

def display_user_menu():
    print("\nUser Menu:")
    print("1. Register as a user")
    print("2. View available vaccinations")
    print("3. Book a vaccination")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    return choice

def get_admin_data():
    admin_id = int(input("Enter admin ID: "))
    name = input("Enter admin name: ")
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")
    return Admin(admin_id=admin_id, name=name, email=email, password=password)

def display_admin_menu():
    print("\nAdmin Menu:")
    print("1. Register as an admin")
    print("2. Add a vaccination")
    print("3. View booked vaccinations")
    print("4. Delete a vaccination")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    return choice

def add_vaccination():
    vaccination_list = []
    while True:
        vaccination_text = input("Enter the vaccination text (or 'exit' to finish): ")
        if vaccination_text.lower() == 'exit':
            break

        choices = [input(f"Enter choice {i + 1}: ") for i in range(4)]

        correct_answer = input("Enter the correct answer (1-4): ")
        while not (correct_answer.isdigit() and 1 <= int(correct_answer) <= 4):
            print("Invalid input. Please enter a number between 1 and 4.")
            correct_answer = input("Enter the correct answer (1-4): ")

        vaccination = {"vaccination": vaccination_text, "choices": choices, "correct_answer": int(correct_answer)}
        vaccination_list.append(vaccination)

    return vaccination_list

def save_vaccination(vaccination_data):
    with open("vaccination.json", "w") as file:
        json.dump(vaccination_data, file)

def load_vaccination():
    try:
        with open("vaccination.json", "r") as file:
            vaccination = json.load(file)
        return vaccination
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Initialize vaccination
vaccination = load_vaccination()

# Determine if the user is an admin or a user
while True:
    user_type = input("Are you an admin or a user? Enter 'admin' or 'user' (or 'exit' to quit): ")

    if user_type.lower() == "exit":
        break

    if user_type.lower() == "admin":
        admin_user = None
        vaccination = load_vaccination()

        while True:
            choice = display_admin_menu()

            if choice == '5':
                # Return to the main menu
                break

            if not choice.isdigit() or int(choice) not in range(1, 6):
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue

            choice = int(choice)

            if choice == 1:
                # Register as an admin
                admin_user = get_admin_data()
            elif choice == 2:
                # Add a vaccination
                if admin_user is not None and len(vaccination) < 5:
                    vaccination_title = input("Enter vaccination title: ")
                    vaccination_id = int(input("Enter a vaccination id (please use a number): "))
                    vaccination_list = add_vaccination()
                    vaccination_data = {"id": vaccination_id, "title": vaccination_title, "vaccination": vaccination_list}
                    vaccination.append(vaccination_data)
                    save_vaccination(vaccination)
                elif len(vaccination) >= 5:
                    print("You can't add more than 5 vaccinations.")
                else:
                    print("Please register as an admin first.")
            elif choice == 3:
                # View booked vaccinations
                if admin_user is not None:
                    vaccination_center_id_to_view = int(input("Enter vaccination id to view available vaccinations: "))
                    admin_user.registered_customers_and_book(vaccination_center_id=vaccination_center_id_to_view)
                else:
                    print("Please register as an admin first.")
            elif choice == 4:
                # Delete a vaccination
                if admin_user is not None:
                    vaccination_id_to_delete = int(input("Enter vaccination id to delete: "))
                    vaccination_to_delete = next((v for v in vaccination if v.get("id") == vaccination_id_to_delete), None)
                    if vaccination_to_delete:
                        print(f"Deleting vaccination: {vaccination_to_delete['title']}")
                        vaccination.remove(vaccination_to_delete)
                        save_vaccination(vaccination)
                        print("Vaccination deleted successfully.")
                    else:
                        print("Vaccination not found.")
                else:
                    print("Please register as an admin first.")

    elif user_type.lower() == "user":
        user_obj = None

        while True:
            user_choice = display_user_menu()

            if user_choice == '4':
                # Return to main menu
                break

            if not user_choice.isdigit() or int(user_choice) not in range(1, 5):
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

            user_choice = int(user_choice)

            if user_choice == 1:
                # Register as a user
                user_obj = get_user_data()
                user_obj.register()
            elif user_choice == 2:
                # View available vaccinations
                if user_obj is not None:
                    print("View available vaccinations not implemented yet.")
                else:
                    print("Please register as a user first.")
            elif user_choice == 3:
                # Book a vaccination
                if user_obj is not None:
                    vaccination_id_to_book = int(input("Enter vaccination id to book: "))
                    # Assuming you have a method like 'book_vaccination' in the User class
                    user_obj.book_vaccination(vaccination_id=vaccination_id_to_book)
                else:
                    print("Please register as a user first.")
            
    else:
        print("Invalid user type. Please run the program again and choose 'admin' or 'user' as the user type.")
