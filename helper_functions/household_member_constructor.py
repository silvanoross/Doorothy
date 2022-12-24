# Create a class for a household member to be entered into database

class Member:
    # each member will have a firstname, lastname, voice signature and picture signature
    
    def __init__(self, first_name, last_name, phone_number, ml_model):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.ml_model = ml_model