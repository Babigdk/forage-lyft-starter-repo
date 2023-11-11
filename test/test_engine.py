import unittest
from datetime import date, timedelta
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestEngine(unittest.TestCase):
    def setUp(self):
        # Set up any common data needed for the tests
        pass

    def test_calliope_needs_service(self):
        # Test the needs_service method of Calliope
        calliope = Calliope(last_service_date=date.today() - timedelta(days=365 * 2))
        self.assertTrue(calliope.needs_service())

    def test_glissade_needs_service(self):
        # Test the needs_service method of Glissade
        glissade = Glissade(last_service_date=date.today() - timedelta(days=365 * 2))
        self.assertTrue(glissade.needs_service())

    def test_palindrome_needs_service(self):
        # Test the needs_service method of Palindrome
        palindrome = Palindrome(last_service_date=date.today() - timedelta(days=365 * 4))
        self.assertTrue(palindrome.needs_service())

    def test_rorschach_needs_service(self):
        # Test the needs_service method of Rorschach
        rorschach = Rorschach(last_service_date=date.today() - timedelta(days=365 * 4))
        self.assertTrue(rorschach.needs_service())

    def test_thovex_needs_service(self):
        # Test the needs_service method of Thovex
        thovex = Thovex(last_service_date=date.today() - timedelta(days=365 * 4))
        self.assertTrue(thovex.needs_service())


if __name__ == '__main__':
    unittest.main()
