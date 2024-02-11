"""
Module for handling configuration
"""

import logging
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


    def load_from_file(self, data_file: str) -> list:
        """
        Load data from a local file

        Protected scope

        Returns:
            list: items are made up of each line from file
        """
        data = list()

        try:
            with open(data_file, "r") as file:
                data = file.readlines()

            formatted_data = []
            for item in data:
                formatted_data.append(item.strip())

            return formatted_data
        except Exception as e:
            logging.error(f"Cannot read file '{data_file}': {e}")
            return []


    def write_to_file(self, config_file = "", configuration = {}) -> bool:
        """Write configuration to file

        Args:
            config_file (str, optional): Location and name of file to write to. Defaults to "".
            configuration (dict, optional): Dictionary of data to write

        Returns:
            bool: True is successful, else False
        """
        if config_file == "":
            config_file = self.__config_file

        if configuration == "":
            configuration = self.configuration

        try:
            with open(config_file, 'w') as file:
                for key, value in configuration.items():
                    file.write(f"{key} {value}\n")
            return True
        except Exception as e:
            logging.warning(f"Unable to write configuration to file: {e}")
            return False


    def __build_config(self) -> None:
        """Build configuration from user values
        Substitute invalid values with those from global constants

        Protected scope

        Set configuration for class
        """

        raw_file_config = self.load_from_file(self.__config_file)
        raw_file_config_formatted = {}
        for item in raw_file_config:
            setting = item.split(" ")
            if len(setting) == 2:
                raw_file_config_formatted[setting[0].upper()] = setting[1]
            else:
                logging.warning(f"Configuration file '{self.__config_file}' format error. Issues will be substituted with defaults")

        configuration = {}
        for item_key, item_value in global_constants.default_configuration.items():
            if raw_file_config_formatted.get(item_key) is not None and raw_file_config_formatted.get(item_key) != "":
                configuration[item_key] = raw_file_config_formatted[item_key]
            else:
                configuration[item_key] = global_constants.default_configuration[item_key]

        self.configuration = configuration


    def get_config(self) -> dict:
        """Return the class configuration

        Returns:
            dict: configuration
        """
        return self.configuration


    def set_config(self, configuration: str, value: str) -> bool:
        """Set configuration if valid

        Args:
            configuration (str): configuration key to set
            value (str): value to set for the configuration

        Returns:
            bool: True is valid, False if invalid
        """
        if configuration.upper() in global_constants.default_configuration:
            if value != "":
                self.configuration[configuration] = value
                return True
            else:
                logging.error(f"{configuration} value cannot be empty")
                return False
        else:
            logging.error(f"{configuration} not in set of valid configurations to be set")
            return False


