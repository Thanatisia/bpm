import os
import sys
from mkparse.mkparse import MakefileParser

class BPM:
    """
    BPM - Build (from Source) Package Manager
    """
    def __init__(self, makefile_name="Makefile", makefile_path="."):
        """
        Class constructor/initializer
        """
        # Initialize Makefile Parser class
        self.makefile_parser = MakefileParser(makefile_name, makefile_path)
        self.makefile_targets = {}   # Currently-imported Makefile targets
        self.makefile_variables = {} # Currently-imported Makefile variables
        self.makefile_comments = {}  # Currently-imported Makefile comments

    def import_makefile(self, makefile_name="Makefile", makefile_path="."):
        """
        Import Makefile into system buffer
        """
        # Initialize Variables
        targets:dict = {}
        variables:dict = {}
        comments:dict = {}
        contents = {}

        # Check if file exists
        makefile_fullpath = os.path.join(makefile_path, makefile_name)
        if os.path.isfile(makefile_fullpath):
            # File exists
            # Import Makefile
            targets, variables, comments = self.makefile_parser.parse_makefile(makefile_name, makefile_path)

            # Set currently imported contents
            self.makefile_targets = targets
            self.makefile_variables = variables
            self.makefile_comments = comments
        else:
            print("Makefile {} does not exist".format(makefile_fullpath))

        return [targets, variables, comments]

    def remove_target_comments(self, targets:dict):
        """
        Remove comments from imported Makefile targets
        """
        # Loop through Makefile targets
        for target_name, target_mappings in targets.items():
            # Get target statements
            curr_target_statements:list = target_mappings["statements"]

            # Initialize Counter
            i = 0;

            # Loop through all statements using a while loop
            while i <= len(curr_target_statements)-1:
                # Get current statement
                curr_statement = curr_target_statements[i]

                # Check if '#' in current statement
                if '#' in curr_statement:
                    # Check if the current statements starts with the comment delimiter '#'
                    ## Strip all special characters and Obtain first element
                    first_character = curr_statement.strip()[0]
                    if first_character == '#':
                        ## Remove that line from the list
                        curr_target_statements.pop(i)
                        i+=1

                # Increment counter by 1
                i+=1

            # Replace with new statements list
            targets[target_name]["statements"] = curr_target_statements
        return targets

    def set_makefile_name(self, makefile_name="Makefile"):
        """
        Explicitly specify the name of the new Makefile
        """
        # Initialize Variables

        # Overwrite current file name
        self.makefile_parser.makefile_name = makefile_name

    def set_makefile_path(self, makefile_path="."):
        """
        Explicitly specify the path of the new Makefile
        """
        # Initialize Variables

        # Overwrite current file path
        self.makefile_parser.makefile_path = makefile_path

    def get_makefile_name(self):
        """
        Getter method to receive the currently selected makefile name
        """
        return self.makefile_parser.makefile_name

    def get_makefile_path(self):
        """
        Getter method to receive the currently selected makefile path
        """
        return self.makefile_parser.makefile_path

    def get_makefile_targets(self):
        """
        Getter method to receive the currently selected makefile's imported targets
        """
        return self.makefile_targets

    def get_makefile_variables(self):
        """
        Getter method to receive the currently selected makefile's imported variables
        """
        return self.makefile_variables

    def get_makefile_comments(self):
        """
        Getter method to receive the currently selected makefile's imported comments
        """
        return self.makefile_comments


