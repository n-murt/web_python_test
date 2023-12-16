import pytest

from task_1 import check_text


def test_1():
    assert 'молоко' in check_text('малако')


if __name__ == '__main__':
    pytest.main('-vv')
