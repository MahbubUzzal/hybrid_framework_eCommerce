import configparser
config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get("common info", "base_url")
        return url

    @staticmethod
    def get_user_email():
        username = config.get("common info", "user_email")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password


