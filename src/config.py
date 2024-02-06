"""
Module for handling configuration
"""

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
        Substitute invalid values with those from global contants

        Returns:
            dict: key - value configuration
        """

        file_config = self.__load_from_file()
        print(file_config)