import keisan


class TestKeisan(object):
    def test_add_number_plus_double(self):
        cal = keisan.Keisan()
        assert cal.add_number_plus_double(20, 10) == 60
    def test_add_number_plus_double2(self):
        cal = keisan.Keisan()
        assert cal.add_number_plus_double(40, 10) == 90
