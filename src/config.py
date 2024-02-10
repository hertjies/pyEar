"""
Module for handling configuration
"""

import src.global_constants as global_constants

class Config():
    """
    Configuration store
    """

    def __init__(self, config_file = "") -> None:
        self.__config_file = config_file
        if self.__config_file == "":
            self.__config_file = global_constants.default_configuration_file
        self.configuration = {}
        self.__build_config()


    def __load_from_file(self, data_file: str) -> list:
        """
        Load data from a local file

        Returns:
            list: items are made up of each line from file
        """
        data = list()
        with open(data_file) as file:
            data = file.readlines()

        formatted_data = []
        for item in data:
            formatted_data.append(item.strip())

        return formatted_data


    def __build_config(self) -> None:
        """Build configuration from user values
        Substitute invalid values with those from global constants

        Set configuration for class
        """

        raw_file_config = self.__load_from_file(self.__config_file)
        raw_file_config_formatted = {}
        for item in raw_file_config:
            setting = item.split(" ")
            if len(setting) == 2:
                raw_file_config_formatted[setting[0].upper()] = setting[1]
            else:
                print(f"WARNING: Configuration file '{self.__config_file}' format error. Issues will be substituted with defaults")

        configuration = {}
        for item_key, item_value in global_constants.default_configuration.items():
            if raw_file_config_formatted.get(item_key) is not None and raw_file_config_formatted.get(item_key) != "":
                configuration[item_key] = raw_file_config_formatted[item_key]
            else:
                configuration[item_key] = global_constants.default_configuration[item_key]

        self.configuration = configuration


    def get_config(self) -> dict:
        return self.configuration


    def set_config(self, configuration, value) -> bool:
        pass


    def write_to_file(self) -> bool:
        pass