TRACK_TYPE_MSG = "What do you want to track? 1.Food 2.Workout::"


class UserDetails:
    name = ""
    gender = ""
    weight_kg = 0.0
    height_cm = 0.0
    age = 0
    track_type_id = 0
    query = ""
    track_query = ""

    def set_user_details(self):
        """
        Take the user inputs and store them in the class variables
        :return:
        """
        self.name = input("Enter your name::").capitalize()
        self.gender = input("Enter your gender:male/female::").lower()
        self.weight_kg = float(input("Enter your weight in kgs::"))
        self.height_cm = float(input("Enter your height in cms::"))
        self.age = int(input("Enter your age rounded off to years::"))

    def get_user_details(self):
        """
        Get the user data that was set by the user
        :return:
        """
        return {"gender": self.gender,
                "weight_kg": self.weight_kg,
                "height_cm": self.height_cm,
                "age": self.age}

    def set_track_type(self):
        """
        Take input of what the user wants to track from either exercise or food
        :return:
        """
        self.track_type_id = int(input(TRACK_TYPE_MSG))

    def get_track_type(self):
        """
        Get what the user chose to track, either exercise or food
        :return:
        """
        return self.track_type_id

    def set_track_query(self):
        """
        User input for the food or workout in natural english language
        :return:
        """
        self.track_query = input("Enter your msg::")

    def get_track_query(self):
        """
        Retrieve the user input
        :return:
        """
        return self.track_query
