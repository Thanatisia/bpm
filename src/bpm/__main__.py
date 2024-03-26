"""
BPM - Build (from Source) Package Manager: Package manager designed to use Makefiles as a primary method of management, building, installation and uninstallation
"""
import os
import sys
from .bpm import BPM

def display_help():
    """
    Display Help Menu
    """
    help_msg = """
## Documentations
### Synopsis/Syntax
- Default
    ```bash
    bpm [makefile-path] [makefile-name]
    ```

### Parameters
- Positionals
    - makefile-path : Specify the path to the target Makefile you wish to manage
        + Type: String
        + Default: "."
    - makefile-name : Specify the name of the target Makefile you wish to manage
        + Type: String
        + Default: "Makefile"

- Optionals
    - With Arguments
    - Flags

### Usage
- Import a target Makefile
    ```bash
    bpm . Makefile
    ```
    """
    print(help_msg)

def main():
    print("BPM: Build Package Manager")

    # Initialize Variables
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)
    opts:dict = { "positionals" : [], "optionals" : {"with-arguments" : {}, "flags" : {"help" : False}} }
    makefile_path = "."
    makefile_name = "Makefile"

    # Check if there are arguments
    if argc >= 1:
        # There are arguments
        ## Loop through and obtain all arguments
        for i in range(argc):
            # Get current argument
            curr_arg = argv[i]

            # Match/Switch case the current argument
            match curr_arg:
                ### With Arguments ###
                ### Flags ###
                case "-h" | "--help":
                    # Help Menu
                    opts["optionals"]["flags"]["help"] = True
                ### Default ###
                case _:
                    ## Append to Positionals
                    opts["positionals"].append(curr_arg)

    # Print optional arguments
    opt_opts:dict = opts["optionals"]
    opt_with_Arguments:dict = opt_opts["with-arguments"]
    opt_Flags:dict = opt_opts["flags"]
    number_of_arg_opts:int = len(opt_with_Arguments)
    number_of_Flags:int = len(opt_Flags)

    """
    Process CLI arguments
    """
    print("With Arguments:")
    for arg_name, arg_value in opt_with_Arguments.items():
        print("{} = {}".format(arg_name, arg_value))

    print("")

    print("Optionals:")
    for flag_name, flag_value in opt_Flags.items():
        print("{} = {}".format(flag_name, flag_value))

    print("")

    # Print Help Message
    if opt_Flags["help"] == True:
        display_help()
        exit(1)

    # Get Positionals Arguments
    pos_opts:list = opts["positionals"]
    number_of_pos = len(pos_opts)

    """
    Process Positional Arguments - Main Body
    """
    if number_of_pos >= 2:
        # Obtain both arguments
        makefile_path = pos_opts[0]
        makefile_name = pos_opts[1]

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

