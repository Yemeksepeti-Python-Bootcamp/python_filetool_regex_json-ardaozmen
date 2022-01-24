import json
from regex import RegexOperations as REGEX
from user import UserClass
class FileOperations():
    
    def __init__(self, json_path):
        self.json_path = json_path
    
    def extractFromJson(self):
        
        recordList = []
        with open(self.json_path) as json_file:
            allJson = json.load(json_file)
            for data in allJson:
                user = UserClass()
                user.email = data["email"]
                user.user_name = data["username"]
                user.name_surname = data["profile"]["name"]
                user.birth_day = REGEX.getBirthDay(data["profile"]["dob"])
                user.birth_month = REGEX.getBirthMonth(data["profile"]["dob"])
                user.birth_year = REGEX.getBirthYear(data["profile"]["dob"])
                user.country = data["profile"]["address"].split(',')[2]
                user.email_userlk = REGEX.verifyEmailUser(user.user_name,user.email)
                user.user_namelk = REGEX.verifyUserName(user.user_name,user.name_surname)
                a = (user.email, user.user_name, user.name_surname, user.birth_day, user.birth_month, user.birth_year, user.country, user.email_userlk, user.user_namelk)
                recordList.append(a)
        
        return recordList