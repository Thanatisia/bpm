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

            # Process Makefile contents
            contents = self.makefile_parser.format_makefile_Contents(targets, variables)

            # Output accordingly
        else:
            print("Makefile {} does not exist".format(makefile_fullpath))

        return [targets, variables, comments, contents]

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

