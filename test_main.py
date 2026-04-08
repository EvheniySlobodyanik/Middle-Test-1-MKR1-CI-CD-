import pytest
from main import FileComparator

@pytest.fixture
def comparator():
    return FileComparator()

@pytest.mark.parametrize("team_a, team_b, expected_same, expected_diff", [
    (
        {"Furina", "Neuvillette", "Kazuha", "Baizhu"}, 
        {"Kazuha", "Raiden", "Bennett", "Xiangling"}, 
        {"Kazuha"}, 
        {"Furina", "Neuvillette", "Baizhu", "Raiden", "Bennett", "Xiangling"}
    ),
    (
        {"Zhongli", "Xiao"}, 
        {"Zhongli", "Xiao"}, 
        {"Zhongli", "Xiao"}, 
        set()
    ),
    (
        {"Noelle"}, 
        {"Chasca"}, 
        set(), 
        {"Noelle", "Chasca"}
    )
])

def test_genshin_logic(comparator, team_a, team_b, expected_same, expected_diff):
    assert comparator.find_intersection(team_a, team_b) == expected_same
    assert comparator.find_difference(team_a, team_b) == expected_diff