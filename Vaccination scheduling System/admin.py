



from database import save_data, load_data

class Admin:
    def __init__(self, admin_id, name, email, password):
        self.admin_id = admin_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, email, password):
        return self.email == email and self.password == password

    def vaccination_center(self, title, vaccination_center_ids):
        vaccination_centers = load_data("vaccination_center.json")
        vaccination_center_ids = int(input("Enter Vaccination Center IDs: "))
        vaccination_center = {"id": vaccination_center_ids, "title": title, "vaccination_center_ids": vaccination_center_ids}
        vaccination_centers.append(vaccination_center)
        save_data("vaccination_center.json", vaccination_centers)

    def registered_customers_and_book(self, vaccination_center_id):
        vaccination_centers_list = load_data("vaccination_centers_list.json")
        admin = load_data("admin.json")
        vaccination_centers_list = [v for v in vaccination_centers_list if v["vaccination_center_id"] == vaccination_center_id]

        for a in admin:
            sent_reserve_vaccination = next((v for v in vaccination_centers_list if v["vaccination_center_id"] == a["id"]), None)
            if sent_reserve_vaccination:
                print(f"{a['name']} ({a['id']}): Reserved")
            else:
                print(f"{a['name']} ({a['id']}): Not Reserved")

    def give_vaccination(self, user_id, vaccination_id, list_registered_users):
        list_registered_users = load_data("list_registered_users.json")
        user_vaccination = next((v for v in list_registered_users if v["user_id"] == user_id and v["vaccination_id"] == vaccination_id), None)
        
        if user_vaccination:
            user_vaccination["given"] = True
            save_data("list_registered_users.json", list_registered_users)
            print(f"Vaccination given to {user_vaccination['user_id']} for Vaccination {user_vaccination['vaccination_id']}")
        else:
            print("Vaccination not found.")
