import pytest

from task_2 import get_id


def test_2():
    assert 92674 in get_id()


if __name__ == '__main__':
    pytest.main('-vv')
