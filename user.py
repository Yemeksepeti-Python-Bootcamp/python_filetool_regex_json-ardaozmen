class UserClass:
    '''
    User Data Class
    '''
    def __init__(
        self,
        email = "None",
        user_name= "None",
        name_surname = "None",
        email_userlk = "0",
        user_namelk = "0",
        birth_year = "9999",
        birth_month = "01",
        birth_day = "01",
        country = "None"):

        self.email = email
        self.user_name = user_name
        self.name_surname = name_surname
        self.email_userlk = email_userlk
        self.user_namelk = user_namelk
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.country = country