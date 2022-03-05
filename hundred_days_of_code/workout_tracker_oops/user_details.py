track_type_msg = "What do you want to track? 1.Food 2.Workout::"


class UserDetails:
    name = ""
    gender = ""
    weight_kg = 0.0
    height_cm = 0.0
    age = 30
    track_type_id = 0
    query = ""
    track_query = ""

    def set_user_details(self):
        self.name = input("Enter your name::").capitalize()
        self.gender = input("Enter your gender:male/female::").lower()
        self.weight_kg = float(input("Enter your weight in kgs::"))
        self.height_cm = float(input("Enter your height in cms::"))
        self.age = int(input("Enter your age rounded off to years::"))

    def get_user_details(self):
        return {"gender": self.gender,
                "weight_kg": self.weight_kg,
                "height_cm": self.height_cm,
                "age": self.age}

    def set_track_type(self):
        self.track_type_id = int(input(track_type_msg))

    def get_track_type(self):
        return self.track_type_id

    def set_track_query(self):
        self.track_query = input("Enter your msg::")

    def get_track_query(self):
        return self.track_query
