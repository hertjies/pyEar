"""
Module for handling configuration
"""

from src.global_constants import default_configutaion

class Config():
    """
    Configuration store
    """

    def __init__(self, config_file = "src/config.txt") -> None:
        self.config_file = config_file
        self.__build_config()


    def __load_from_file(self) -> list:
        """
        Load configuration from a local file

        Returns:
            str: Blob of text
        """
        file_config = list()
        with open(self.config_file) as file:
            file_config = file.readlines()

        formatted_config = []
        for config in file_config:
            formatted_config.append(config.strip().upper())

        return formatted_config

    def __build_config(self) -> dict:
        """Build configuration from user values
        Substitute invalid values with those from global constants

        Returns:
            dict: key - value configuration
        """

        raw_file_config = self.__load_from_file()
        configuration = {}
        for setting in raw_file_config:
            setting_list = setting.split(" ")
            configuration[setting_list[0]] = setting_list[1]

        print(configuration)

    def get_config(self) -> dict:
        pass

    def set_config(self) -> bool:
        pass

    def write_to_file(self) -> bool:
        pass