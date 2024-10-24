import os

environment = os.environ.get("CONFIG_ENVIRONMENT")
if environment == "default":
    from hello_darkly.config import _default as settings
else:
    raise EnvironmentError(f"Undefined Config Environment. environment={environment}")


