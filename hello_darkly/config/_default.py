import os
from typing import List

AWS_PROFILE = os.environ.get("AWS_PROFILE")
ENVIRONMENT = os.environ.get("APP_ENVIRONMENT")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
REPOS_DIR = os.path.join(REPO_ROOT, "repos")
OUTPUTS_DIR = os.path.join(REPO_ROOT, "outputs")


