import unittest
import utils


class TestUtils(unittest.TestCase):

    def test_get_contacts_source(self):
        path = 'contacts.vcf'
        self.assertEqual(utils.get_contacts_source(path), 'apple')

        path = 'facebook_friends.txt'
        self.assertEqual(utils.get_contacts_source(path), 'facebook')

        path = 'current.txt'
        self.assertEqual(utils.get_contacts_source(path), 'txt')

    def test_is_contact(self):
        previous_line = 'N:Tara;Casteel;;;'
        self.assertTrue(utils.is_contact(previous_line, 'apple'))

        previous_line = 'Friends\n'
        self.assertTrue(utils.is_contact(previous_line, 'facebook'))

    def test_process_contact(self):
        line = 'FN:Tara Casteel'
        expected_processed = 'Tara Casteel'
        self.assertEqual(utils.process_contact(line, 'apple'), expected_processed)

        line = 'Tara Casteel\n'
        expected_processed = 'Tara Casteel'
        self.assertEqual(utils.process_contact(line, 'facebook'), expected_processed)


if __name__ == '__main__':
    unittest.main()
