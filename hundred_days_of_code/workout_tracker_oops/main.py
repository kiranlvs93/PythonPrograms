from user_details import UserDetails
from calory_details import CalorieCounter
from sheety_actions import Sheety

userDet = UserDetails()
calCounter = CalorieCounter()
sheety = Sheety()


def print_welcome_msg():
    welcome_msg = "Welcome to workout tracker. I need your details to help you track your calories"
    print(welcome_msg)


def set_user_info():
    """
    Get all the user inputs like height, weight, gender, age, workouts done
    :return:
    """
    userDet.set_user_details()
    userDet.set_track_type()
    userDet.set_track_query()


if __name__ == '__main__':
    print_welcome_msg()
    set_user_info()
    params = userDet.get_user_details()
    # params = {'gender': 'male', 'weight_kg': 75.0, 'height_cm': 175.0, 'age': 30, 'query': 'I walked for 3 kms, running for 10 kms and also cycled for 14kms'}
    track_type = userDet.get_track_type()
    # track_type = 2
    params["query"] = userDet.get_track_query()
    print("User Details::", params)
    if track_type == 1:
        print("Tracking food")
        calCounter.get_nutrient_details(params=params)
    elif track_type == 2:
        print("***********Tracking exercise***************")
        calCounter.get_exercise_details(params=params)
        for activity in calCounter.activities:
            print("Adding activity::", activity)
            sheety.update_sheet(activity)
