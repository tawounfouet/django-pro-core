import os

# Set on the earliest possible moment
os.environ['PYTEST_RUNNING'] = 'true'

from src.accounts.tests.fixtures import *  # noqa: F401, F403, E402
from src.general.tests.fixtures import *  # noqa: F401, F403, E402
