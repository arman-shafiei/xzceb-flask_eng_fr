import unittest
import translator as tr

class TestTranslator(unittest.TestCase):
    def test_en2fr_1(self):
        response = tr.english_to_french("")
        self.assertNotEqual(response["translations"][0]["translation"],"Bonjour")

    def test_en2fr_2(self):
        response = tr.english_to_french("Hello")
        self.assertEqual(response["translations"][0]["translation"],"Bonjour")

    def test_fr2en_1(self):
        response = tr.french_to_english("")
        self.assertNotEqual(response["translations"][0]["translation"],"Hello")

    def test_fr2en_2(self):
        response = tr.french_to_english("Bonjour")
        self.assertEqual(response["translations"][0]["translation"],"Hello")

if __name__ == "__main__":
    unittest.main()