"""
Main Unit Test launcher
"""
import os
import sys
import pkg_resources
from copy import deepcopy
from bpm.bpm import BPM

def init(makefile_name="Makefile", makefile_path="."):
    global bpm, makefile_parser

    # Initialize Variables
    bpm = BPM(makefile_name, makefile_path)
    makefile_parser = bpm.makefile_parser  # Initialize Makefile Parser

def print_makefile_contents(targets:dict, variables:dict):
    """
    Print Makefile Contents
    """
    # Format targets and variables into printable strings
    print("* Formatting removed comments list...")
    contents = makefile_parser.format_makefile_Contents(targets, variables)

    # Print contents
    content_makefile_Targets = contents["targets"]
    content_makefile_Variables = contents["variables"]

    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(content_makefile_Variables)):
        # Get current line
        curr_line = content_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(content_makefile_Targets)):
        # Get current line
        curr_line = content_makefile_Targets[i]
        # Print
        print(curr_line)

def compare_lists(src:list, dst:list):
    """
    Compare a source and destination list and returns the differences

    :: Params
    - src : Specify the source list to use to compare
        + Type: List
    - dst : Specify the destination list to compare to
        + Type: List

    :: Return
    - differences : Dictionary of differences mapping the line to the values
        - Format
            {
                [line-texts] = {
                    "source" : [line-number],
                    "destination" : [line-number]
                }
            }
    """
    # Initialize Variables
    differences:dict = {}

    # Iterate through both dictionaries
    for i in range(len(src)):
        # Get current source
        curr_src = src[i]

        # Initialize Key-Value entry
        if curr_src not in list(differences.keys()):
            differences[curr_src] = {"source" : 0, "destination" : 0} # source|destination : [line-number]

        # Compare key-values and check if the current value of the source is found in the destination 
        if curr_src in dst:
            # Compare
            for j in range(len(dst)):
                # Get current destination
                curr_dst = dst[j]

                # Compare
                if curr_src == curr_dst:
                    # Source Values are found in Destination Values
                    differences[curr_src]["source"] = i
                    differences[curr_src]["destination"] = j
                    break
        else:
            # Source Values are not found in Destination Values
            differences[curr_src]["source"] = i
            differences[curr_src]["destination"] = None

    # Return differences map
    return differences

def test_remove_comments(tmp_targets):
    """
    Test function 'remove_comments()'
    """
    # Initialize Variables

    # Process imported Makefile contents
    tmp_targets = bpm.remove_target_comments(tmp_targets)

    # Use processed data

    # Output processed data
    return tmp_targets

def get_cli_arguments():
    """
    Obtain CLI arguments and options
    """
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

    return [makefile_name, makefile_path]

def main():
    """
    Main Runner
    """
    # Obtain CLI argument parsing
    makefile_name, makefile_path = get_cli_arguments()

    # Initialize System Environment
    init(makefile_name, makefile_path)

    # Import Makefile contents into application runtime
    print("* Importing Makefile contents...")
    targets, variables, comments = makefile_parser.parse_makefile(makefile_name, makefile_path)

    print("* Printing original Makefile contents as a baseline...")
    print_makefile_contents(targets, variables)

    # Test remove comments
    print("* Testing comments removal...")
    targets_comments_removed = test_remove_comments(targets)

    print("* Printing new target list...")
    print_makefile_contents(targets_comments_removed, variables)

    print("[+] Comments removed successfully")

if __name__ == "__main__":
    main()

