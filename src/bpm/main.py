"""
BPM - Build (from Source) Package Manager: Package manager designed to use Makefiles as a primary method of management, building, installation and uninstallation
"""
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

    def import_makefile(self, makefile_name="Makefile", makefile_path="."):
        """
        Import Makefile into system buffer
        """
        # Initialize Variables

        # Import Makefile
        targets, variables, comments = self.makefile_parser.parse_makefile(makefile_name, makefile_path)

        # Set currently imported contents
        self.makefile_targets = targets
        self.makefile_variables = variables
        self.makefile_comments = comments

        # Return 
        return [targets, variables, comments]

    def set_makefile_name(self, makefile_name="Makefile"):
        """
        Explicitly specify the name of the new Makefile
        """
        # Initialize Variables

        # Overwrite current file name
        self.makefile_parser.makefile_name = makefile_name

    def set_makefile_path(self, makefile_path="."):
        """
        Explicitly specify the name of the new Makefile
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

def main():
    print("BPM: Build Package Manager")

    # Initialize Variables
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)
    makefile_path = "."
    makefile_name = "Makefile"

    # Get Arguments
    if argc >= 2:
        makefile_path = argv[0]
        makefile_name = argv[1]

    # Initialize Classes
    bpm = BPM(makefile_name, makefile_path)

    # Obtain default values
    makefile_parser = bpm.makefile_parser

    # Check if file exists
    makefile_fullpath = os.path.join(makefile_path, makefile_name)

    if os.path.isfile(makefile_fullpath):
        # File exists
        # Import Makefile
        targets, variables, comments = bpm.import_makefile(makefile_name, makefile_path)

        # Process Makefile contents
        contents = makefile_parser.format_makefile_Contents(targets, variables)
        content_variables = contents["variables"]
        content_targets = contents["targets"]

        # Output accordingly
        print("=========")
        print("Variables")
        print("=========")
        for i in range(len(content_variables)):
            # Get current line
            curr_line = content_variables[i]
            # Print
            print(curr_line)

        print("")

        print("=======")
        print("Targets")
        print("=======")
        for i in range(len(content_targets)):
            # Get current line
            curr_line = content_targets[i]
            # Print
            print(curr_line)
    else:
        print("Makefile {} does not exist".format(makefile_fullpath))

if __name__ == "__main__":
    main()

