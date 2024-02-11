"""pySpaceInvadEars"""
import logging
import src.config as Config

logging.basicConfig(
    filename="debug.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__":
    print("I am main")

    myconf = Config.Config()

