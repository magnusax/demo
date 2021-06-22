import pytest
from pathlib import Path
import sys

root_folder = Path.cwd().resolve().parent
sys.path.insert(0, root_folder)

from ..main import get_data  # noqa: E402


@pytest.fixture(scope="module")
def test_check_datatypes():

    dataset = get_data()
    assert dataset.shape[1] == 100
