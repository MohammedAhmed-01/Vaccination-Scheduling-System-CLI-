




from database import save_data, load_data

class User:
    def __init__(self, user_id, name, email, password, phone_number, national_id):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.national_id = national_id

    def register(self):
        users = load_data("user.json")
        users.append({
            "id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "national_id": self.national_id
        })
        save_data("user.json", users)

    def login(self, email, password):
        users = load_data("user.json")
        return any(user["email"] == email and user["password"] == password for user in users)

    def reserve_vaccination(self):
        vaccination_data = load_data("vaccination.json")
        for idx, vaccination in enumerate(vaccination_data):
            print(f"{idx}. {vaccination['title']}")

    def search_vaccination(self, title):
        vaccinations = load_data("vaccination.json")
        for vaccination in vaccinations:
            if title.lower() in vaccination["title"].lower():
                print(f"{vaccination['id']}. {vaccination['title']}")

    def book_vaccination(self, vaccination_id):
        vaccination_data = load_data("vaccination.json")
        vaccination = next((v for v in vaccination_data if v.get("id") == vaccination_id), None)

        if vaccination:
            vaccination["user_id"] = self.user_id
            vaccination["registered"] = None
            save_data("vaccination.json", vaccination_data)
            print(f"Vaccination booked successfully: {vaccination['title']}")
        else:
            print("Vaccination not found.")

    def see_vaccination_date(self):
        vaccination_data = load_data("vaccination.json")
        user_vaccination = [v for v in vaccination_data if v.get("user_id") == self.user_id]
        if user_vaccination:
            for vaccination in user_vaccination:
                print(f"Your date for vaccination {vaccination['id']}: {vaccination['registered']}")
        else:
            print("No vaccination available.")
