# test_poll.py

import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from poll import Poll

class TestPoll(unittest.TestCase):
    """Tests for the class Poll"""
    def setUp(self):
        """setUp will be run before each test method. Actually, a new instance of TestPoll is
            created before each test method is run, and setUp is run for each. Does the tear
            down method need to be called? """
        self.question = "How old are you?"
        self.filename = "test_poll.json"

    @patch.object(Poll,'get_input')
    def test_get_data_with_spaces(self, mocked_get_input):
        """Does Poll.collect() get data and strip whitespace from the results?  Also tests
            that one person can input multiple responses separated by commas and that
            '*' will end the input session."""

        # Set up some fake user input.
        mocked_get_input.side_effect = ['Tanya  ','51', 
                                        '   Blake', '  53 ,  26', 
                                        'Jack', '17, 28, 53',
                                        '*']
        expected_responses = {'Tanya':['51'], 'Blake':['53', '26'], 'Jack':['17', '28', '53']}

        # Run the poll, compare poll.responses to what we expected
        self.age_poll = Poll(self.question, self.filename, delete_old_results = True, 
                                allow_multiple_entries = True)
        self.age_poll.collect()
        self.assertEqual(self.age_poll.responses, expected_responses) 

    @patch.object(Poll,'get_input')
    def test_multiple_entries_not_allowed(self, mocked_get_input):
        """Does Poll.collect() refuse multiple entries if ask tell it to?"""
        # Set up some fake user input.
        mocked_get_input.side_effect = ['Tanya','51', 
                                        'Tanya', 
                                        'Blake', '53',
                                        'Tanya',
                                        'Blake',
                                        'Jack', '17, 29',
                                        '*']
        expected_responses = {'Tanya':['51'], 'Blake':['53'], 'Jack':['17', '29']}

        # Run the poll, saving the screen output. Compare poll.responses to what we expected.
        self.age_poll = Poll(self.question, self.filename, delete_old_results = True, 
                                allow_multiple_entries = False)
        f = StringIO()
        with redirect_stdout(f):
            self.age_poll.collect()
            what_was_printed = f.getvalue()
        self.assertEqual(self.age_poll.responses, expected_responses) 

        # See if it printed the right stuff to the screen
        expected_print = ''
        for i in range(3):
            expected_print += "You have already taken the poll.\n"
        self.assertEqual(what_was_printed, expected_print) 

    @patch.object(Poll,'get_input')
    def test_saving_to_file(self, mocked_get_input):
        """Can we save the data to a file, then come back later and start a new 
            polling instance that includes file info?"""

        # Set up some fake user input.
        mocked_get_input.side_effect = ['Tanya','51', 
                                        'Blake', '53', 
                                        'Jack', '17, 28, 53',
                                        '*']

        # Run the poll, deleting any existing results.
        self.age_poll = Poll(self.question, self.filename, delete_old_results = True, 
                                allow_multiple_entries = True)
        self.age_poll.collect()
        self.age_poll.save()

        # Some more fake input
        mocked_get_input.side_effect = ['Sarah','11', 
                                        'Aaron', '14', 
                                        '*']

        # Run a new instance of the poll, without deleting existing results.
        self.age_poll = Poll(self.question, self.filename, delete_old_results = False, 
                                allow_multiple_entries = True)
        self.age_poll.collect()

        expected_responses = {'Tanya':['51'], 
                                'Blake':['53'], 
                                'Jack':['17', '28', '53'],
                                'Aaron':['14'],
                                'Sarah':['11']}
        self.assertEqual(self.age_poll.responses, expected_responses) 

    @patch.object(Poll,'get_input')
    def test_delete_file(self, mocked_get_input):
        """Does Poll.collect() actually delete entries from the file if we tell it to?"""

        # Set up some fake user input.
        mocked_get_input.side_effect = ['Tanya','51', 
                                        'Blake', '53',
                                        '*']

        # Run the poll. When we get to the * the results should be saved to the file.
        self.age_poll = Poll(self.question, self.filename, delete_old_results = True, 
                                allow_multiple_entries = False)
        self.age_poll.collect()

        # We shouldn't, but we do have to reinit the class to get the info from the file.
        # Set up some fake user input.
        mocked_get_input.side_effect = ['Jack','17', '*']
        expected_responses = {'Jack':['17']}
        self.age_poll = Poll(self.question, self.filename, delete_old_results = True, 
                                allow_multiple_entries = False)
        self.age_poll.collect()
        self.assertEqual(self.age_poll.responses, expected_responses) 

    @patch.object(Poll,'get_input')
    def test_visually_inspect_output(self, mocked_get_input):
        """Simulate normal use of the poll with all output sent to the screen, without
            any test assertions, so you can visually double check the screen output."""

        # Set up some fake user input.
        mocked_get_input.side_effect = ['Tanya  ','51', 
                                        '   Blake', '  53 ,  26', 
                                        'Jack', '17, 28, 53',
                                        '*']
        # Run the poll.  Separate it from the rest of the test output by some blank lines.
        print("\n")
        self.age_poll = Poll(self.question, self.filename, delete_old_results = True, 
                                allow_multiple_entries = True)
        self.age_poll.collect()
        self.age_poll.show_results()
        print("\n")

if __name__ == '__main__':
   unittest.main() 
