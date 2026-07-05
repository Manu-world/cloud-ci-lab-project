import unittest

class TestCloudApp(unittest.TestCase):
    def test_app_runs(self):
        # A simple test to ensure our CI environment is working
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()