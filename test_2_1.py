import pytest

from task_2_1 import create_post


def test_2_1():
    assert 'title test' in create_post()['title']


if __name__ == '__main__':
    pytest.main('-vv')
