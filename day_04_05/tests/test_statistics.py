from utils.statistics import get_user_statistics

def test_get_user_statistics(users):
    stats = get_user_statistics(users)

    assert stats["total"] == 4
    assert stats["active"] == 3
    assert stats["locked"] == 1
    assert stats["admins"] == 1
    assert stats["customers"] == 3