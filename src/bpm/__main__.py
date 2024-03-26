"""
BPM - Build (from Source) Package Manager: Package manager designed to use Makefiles as a primary method of management, building, installation and uninstallation
"""
import os
import sys
from .bpm import BPM

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
        # Obtain both arguments
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
    else:
        # Perform data validation - Null value check
        # Less than 2
        print("Insufficient arguments provided, please provide the following arguments in this order: {}, {}".format("Makefile Path", "Makefile Name"))

if __name__ == "__main__":
    main()

