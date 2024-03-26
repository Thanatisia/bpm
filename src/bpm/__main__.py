"""
BPM - Build (from Source) Package Manager: Package manager designed to use Makefiles as a primary method of management, building, installation and uninstallation
"""
import os
import sys
import pkg_resources
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
    bpm {options} <arguments> [actions]
    ```

### Parameters
- Positionals
    - actions : Specify the action you wish to take; You can stack multiple actions by appending them in chronological/iterative order
        - Actions
            + import : Import the Makefile contents into the system buffer/memory
            + print : Print all imported Makefile contents; Note: You must use this after 'import' is provided

- Optionals
    - With Arguments
        - `-f | --file-name [makefile-name]`: Explicitly specify the name of the target Makefile
            + Type: String
            + Default: "Makefile"
        - `-p | --file-path [makefile-path]`: Explicitly specify the path to the target Makefile
            + Type: String
            + Default: "."
    - Flags

### Usage
- Import a target Makefile
    ```bash
    bpm -p . -f Makefile import
    ```

- Import and Print a target Makefile
    ```bash
    bpm -p . -f Makefile import print
    ```
    """
    print(help_msg)

def display_version():
    """
    Display System Version
    """
    pkg_name = "bpm"
    pkg_distribution = pkg_resources.get_distribution(pkg_name)
    pkg_version = pkg_distribution.version
    print("Package Name: {}\nPackage Distribution: {}\nPackage Version: {}".format(pkg_name, pkg_distribution, pkg_version))

def init(makefile_name="Makefile", makefile_path="."):
    """
    Perform Pre-Initialization Setup
    """
    # Global Variables
    global bpm

    # Initialize Classes
    bpm = BPM(makefile_name, makefile_path)

def edit_Makefile(makefile_Contents):
    """
    Edit the Makefile contents in a Buffer/REPL
    """
    # Initialize Variables
    line = ""

def start_package_management(makefile_name="Makefile", makefile_path="."):
    """
    Main Package Manager Body
    """
    # Obtain default values
    makefile_parser = bpm.makefile_parser

def obtain_arguments(err_msg=""):
    """
    Obtain CLI arguments and return

    :: Params
    - err_msg : Specify a custom error message to print if an invalid CLI argument is provided
        + Type: String
        - Default: Empty
            - Will print the following if error message is left empty
                ```
                # Invalid Options
                print("Invalid option provided: {}".format(curr_arg))
                ```
    """
    # Initialize Variables
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)
    opts:dict = { "positionals" : [], "optionals" : {"with-arguments" : {"filename" : "Makefile", "filepath" : "."}, "flags" : {"help" : False, "version" : False}} }
    makefile_path = "."
    makefile_name = "Makefile"

    # Check if there are arguments
    if argc >= 1:
        # There are arguments
        i:int = 0
        ## Loop through and obtain all arguments
        while i <= (argc-1):
            ## While the current index is not the last element in the list

            # Get current argument
            curr_arg = argv[i]

            # Match/Switch case the current argument
            match curr_arg:
                ### Positionals ###
                case "start":
                    # One of the actions - Start the package manager (Unused)
                    opts["positionals"].append("start")
                case "import":
                    # Import the files specified into the buffer
                    opts["positionals"].append("import")
                case "print":
                    # Print the file contents imported into the buffer
                    opts["positionals"].append("print")
                ### With Arguments ###
                case "-f" | "--file-name":
                    # Get the next argument
                    target_file_name = argv[i+1]

                    # Set target file name
                    opts["optionals"]["with-arguments"]["filename"] = target_file_name

                    # Shift 1 to the right to push out the next argument
                    i += 1
                case "-p" | "--file-path":
                    # Get the next argument
                    target_file_path = argv[i+1]

                    # Set target file name
                    opts["optionals"]["with-arguments"]["filepath"] = target_file_path

                    # Shift 1 to the right to push out the next argument
                    i += 1
                ### Flags ###
                case "-h" | "--help":
                    # Help Menu
                    opts["optionals"]["flags"]["help"] = True
                case "-v" | "--version":
                    # Help Menu
                    opts["optionals"]["flags"]["version"] = True
                ### Default ###
                case _:
                    ## Append to Positionals
                    ## opts["positionals"].append(curr_arg)

                    # Invalid Options
                    if err_msg == "":
                        print("Invalid option provided: {}".format(curr_arg))
                    else:
                        print(err_msg)

            # Increment index
            i+=1

    """
    Process Positional Arguments - Main Body
    """
    # Obtain both arguments
    makefile_path = opts["optionals"]["with-arguments"]["filepath"]
    makefile_name = opts["optionals"]["with-arguments"]["filename"]

    # Return
    return [makefile_name, makefile_path, opts]

def main():
    print("BPM: Build Package Manager")
    
    # Initialize Variables
    targets = {}
    variables = {}
    comments = {}
    contents = {}
    content_variables = []
    content_targets = []

    # Obtain CLI arguments
    makefile_name, makefile_path, opts = obtain_arguments()

    ## Retrieve nested variables
    positional_actions:list = opts["positionals"]
    number_of_positionals = len(positional_actions)
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
    elif opt_Flags["version"] == True:
        display_version()
        exit(1)

    # Perform system initialization
    init(makefile_name, makefile_path)

    # Loop through all positionals
    for i in range(number_of_positionals):
        # Get current positional argument
        curr_pos_arg = positional_actions[i]

        print("Current Action: {}".format(curr_pos_arg))

        # Process current action
        if curr_pos_arg == "start":
            # Begin Package Manager
            start_package_management(makefile_name, makefile_path)
        elif curr_pos_arg == "import":
            # Import Makefile into system buffer
            targets, variables, comments, contents = bpm.import_makefile(makefile_name, makefile_path)
            content_variables = contents["variables"]
            content_targets = contents["targets"]
        elif curr_pos_arg == "print":
            # Check if variables and targets are imported
            if len(content_variables) == 0 and len(content_targets) == 0:
                print("Makefile is not imported, please specify 'import' before 'print'")
                exit(1)

            if len(content_variables) != 0:
                # Print contents
                print("=========")
                print("Variables")
                print("=========")
                for i in range(len(content_variables)):
                    # Get current line
                    curr_line = content_variables[i]
                    # Print
                    print(curr_line)

                print("")

            if len(content_targets) != 0:
                print("=======")
                print("Targets")
                print("=======")
                for i in range(len(content_targets)):
                    # Get current line
                    curr_line = content_targets[i]
                    # Print
                    print(curr_line)

if __name__ == "__main__":
    main()

