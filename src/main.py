from src.loader import Loader

print(f"Called filename: {__name__}")

global_loader = Loader()
print(global_loader.config.configuration)