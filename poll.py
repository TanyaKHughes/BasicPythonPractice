# poll.py
# This class has some tests written for it in test_poll.py.  The tests are not complete.

import json

class Poll:
    """This class collects whatever information you want and stores it in a file 
        specified by the user. It asks each user for a name and a list of answers
        to a question."""

    def __init__(self, question, filename, delete_old_results = False, allow_multiple_entries = True):
        """question is the question that is being asked of people in the poll.  
            filename.json is where the results will be stored."""
        self.question = question
        self.filename = filename
        self.allow_multiple_entries = allow_multiple_entries

        # Get old responses, from the file, if there are any.  self.responses is
        # a dictionary of responses. The user's name is the key, and the value is
        # a list of the responses that person gave.
        if delete_old_results:
            self.responses = {}
        else:
            try:
                with open(self.filename,'r') as f:
                    self.responses = json.load(f)
            except FileNotFoundError:
                self.responses = {}

    def get_input(self, text):  # Could be a static method?
        """Because I'm going to want to mock input in unittests"""
        return input(text)

    def collect(self):
        """collect launches the poll, and receives answers from the user."""
        while True:
            # Get data from one user

            name = self.get_input("\nEnter your name to take the poll.  Press * to quit.\n")
            name = name.strip()
            if '*' in name:
                break

            # If we are not allowing multiple entries, we have to check if this 
            # person has already taken the poll. If so, we don't take their responses.
            if not self.allow_multiple_entries:
                if name in self.responses.keys():
                    print("You have already taken the poll.")
                    continue

            # Collect the response of the user
            response = self.get_input(f"{self.question} If you have more than one "
                              "response, separate the responses with commas.\n")

            # Split the response string into a list of responses, and remove
            # whitespace.
            response_list = response.split(',')
            for i in range(len(response_list)):  #comprehension?
                response_list[i] = response_list[i].strip()

            # Add the info to our dictionary.
            self.responses[name] = response_list

    def save(self):
        # Write all the responses to the file. This will write over whatever is there.
        with open(self.filename, 'w') as f:
            json.dump(self.responses, f)
        
    def show_results(self):
        """Prints out the results stored in the file in a nice table."""
        for name, responses in self.responses.items():
            line = f"{name:20}"
            for response in responses:
                line += response + ", "
            print(line[:-2])  # Don't print the last comma/space
        
if __name__ == '__main__':
    age_poll = Poll("How old are you?", "age_poll.json", delete_old_results = True, \
                allow_multiple_entries = True)
    age_poll.collect()
    age_poll.show_results()
