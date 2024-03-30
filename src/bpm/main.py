"""
BPM - Build (from Source) Package Manager: Package manager designed to use Makefiles as a primary method of management, building, installation and uninstallation
"""
import os
import sys
import pkg_resources
from .bpm import BPM

def display_title():
    """
    Display bootup header title
    """
    print("BPM: Build Package Manager")

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
            + start : Start the Package Management main body (WIP; unused currently)

- Optionals
    - With Arguments
        - `-f | --file-name [makefile-name]`: Explicitly specify the name of the target Makefile
            + Type: String
            + Default: "Makefile"
        - `-p | --file-path [makefile-path]`: Explicitly specify the path to the target Makefile
            + Type: String
            + Default: "."
    - Flags
        + `--generate-default-makefile` : Generate a default Makefile template file
        + `-h | --help` : Display help menu
        + `-v | --version` : Show system version
        + `-t | --trim` : Trim and remove all special characters ("\n", "\t" etc) from the imported file contents

### Usage
- Import a target Makefile
    ```bash
    bpm -p . -f Makefile import
    ```

- Import and Print a target Makefile
    ```bash
    bpm -p . -f Makefile import print
    ```

- Generate a template Makefile of the name 'Makefile'
    bpm -p . --generate-default-makefile
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
    global bpm, makefile_parser

    # Initialize Classes
    bpm = BPM(makefile_name, makefile_path)
    makefile_parser = bpm.makefile_parser

def edit_Makefile(makefile_Contents):
    """
    Edit the Makefile contents in a Buffer/REPL
    """
    # Initialize Variables
    line = ""

def format(targets=None, variables=None, trim=False):
    """
    Format Makefile target and/or variables dictionary and other actions like trimming

    :: Params
    - targets : Optional; The imported Makefile targets dictionary that you wish to format into a printable string you can display on standard output
        + Type: Dictionary
        + Default Value: None
    - variables : Optional; The imported Makefile variables dictionary that you wish to format into a printable string you can display on standard output
        + Type: Dictionary
        + Default Value: None
    - trim : Enable/Disable trimming of the formatted printable content strings
        + Type: Boolean
        + Default: False
    """
    # Initialize Variables

    # Check if the 'trim' argument is True
    if trim == True:
         ## Trim all special characters from left and right side ("\n", "\t" etc etc) if the '-t|--trim' flag is enabled
        print("[O] Trimming Makefile and removing special characters from both ends...")
        # Check for Null-values
        if (targets != None) and (variables != None):
            targets, variables = makefile_parser.trim_contents(targets, variables)
        elif (targets != None):
            targets, variables = makefile_parser.trim_contents(targets=targets)
        elif (variables != None):
            variables = makefile_parser.trim_contents(variables=variables)

    # Process Makefile contents
    contents = makefile_parser.format_makefile_Contents(targets, variables)

    return contents

def print_formatted_contents(contents:dict):
    """
    Print formatted content strings
    """
    # Output accordingly
    content_variables = contents["variables"]
    content_targets = contents["targets"]

    # Check if variables and targets are imported
    if len(content_variables) == 0 and len(content_targets) == 0:
        print("Makefile is not imported, please specify 'import' before 'print'")
    else:
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

def start_package_management(targets:dict, variables:dict, makefile_name="Makefile", makefile_path="."):
    """
    Main Package Manager Body
    """
    # Obtain default values

    # Initialize Variables
    target_dependencies:dict = {}
    target_statements:dict = {}
    target_variable_values:dict = {}
    line = ""

    # Loop until the input is quit
    while True:
        # Print output
        print("""
Choices:
> dir : List all contents in the current directory
> ls : Same as dir
> get [name|path] : Get the currently-set file name/path
> set {name=[name] path=[path]} : Set a new file name/path
> in | import : Import a target Makefile file
> p | print : Print all currently imported targets and variables
> export {name=[new-filename] path=[new-filepath]} : Export the currently imported file contents to a new output Makefile
> tr | trim: Trim contents
> q | quit | exit : Exit program
              """)
        # Get user input
        line = input("Your Input > ")

        # Split the provided input into a list
        input_list = line.split(" ")

        # Check if list contains anything
        if len(input_list) > 0:
            # Input detected

            # Get action
            keyword = input_list[0]

            # Try catch
            try:
                # Match, switch-case condition check
                match keyword:
                    case "dir" | "ls":
                        """
                        List all contents in the current directory
                        """
                        dir_contents = os.listdir(makefile_path)
                        print("Directory Contents: {}".format(', '.join(dir_contents)))
                    case "export":
                        """
                        Export the currently imported file contents to a new output Makefile

                        Syntax: export {name=[new-filename] path=[new-filepath]}
                        """
                        # Initialize Variables
                        output_filename = ""
                        output_filepath = ""

                        # Get Input Values
                        input_values = input_list[1:]

                        # Loop through the input values and split by '=' delimiter to get the targets and its value
                        for i in range(len(input_values)):
                            # Get current element
                            curr_element = input_values[i]

                            # Split current element by the '=' delimiter
                            curr_element_spl = curr_element.split('=')

                            # Obtain the LHS and RHS values
                            curr_element_key = curr_element_spl[0]
                            curr_element_value = curr_element_spl[1]

                            # Check if target is file name or file path
                            match curr_element_key:
                                case "name":
                                    # Set the output filename
                                    output_filename = curr_element_value
                                case "path":
                                    # Set the output filename
                                    output_filepath = curr_element_value
                                case _:
                                    # Default value
                                    print("Invalid parameter: {}={}".format(curr_element_key, curr_element_value))

                        # Check if output filename and file path are provided
                        if (output_filename != "") and (output_filepath != ""):
                            # Format output file paths
                            output_fullpath = os.path.join(output_filepath, output_filename)

                            # Validate targets and variables
                            print("Targets: {}".format(targets))
                            print("Variables: {}".format(variables))

                            # File name and path are provided
                            print("Writing contents to output file: [{}]...".format(output_fullpath))
                            err = bpm.generate_Makefile(targets, variables, output_filename, output_filepath)

                            # Print errors if any
                            if err != "":
                                print("Error Message: {}".format(err))
                        else:
                            if (output_filename == ""):
                                print("File name is not provided")
                            if (output_filepath == ""):
                                print("File path is not provided")

                    case "get":
                        """
                        Get the currently-set file name/path
                        """
                        # Get Target (file name/path)
                        file_target = input_list[1]

                        # Check if target is file name or file path
                        match file_target:
                            case "name":
                                # Print the current file name
                                print("Current File Name: {}".format(makefile_name))
                            case "path":
                                # Print the current file path
                                print("Current File Path: {}".format(makefile_path))
                            case _:
                                # Default value
                                print("Invalid target: {}".format(file_target))
                    case "in" | "import":
                        """
                        Import a target Makefile file
                        """
                        # Import a specified file
                        targets, variables, comments = bpm.import_makefile(makefile_name, makefile_path)
                    case "p" | "print":
                        """
                        Print all currently imported targets and variables
                        """
                        # Process Makefile contents
                        contents = format(targets, variables)

                        # List all variables
                        print_formatted_contents(contents)
                    case "set":
                        """
                        Set a new file name/path

                        Syntax: set {name=[name] path=[path]}
                        """
                        # Get Input Values
                        input_values = input_list[1:]

                        # Loop through the input values and split by '=' delimiter to get the targets and its value
                        for i in range(len(input_values)):
                            # Get current element
                            curr_element = input_values[i]

                            # Split current element by the '=' delimiter
                            curr_element_spl = curr_element.split('=')

                            # Obtain the LHS and RHS values
                            curr_element_key = curr_element_spl[0]
                            curr_element_value = curr_element_spl[1]

                            # Check if target is file name or file path
                            match curr_element_key:
                                case "name":
                                    # Set a new file name
                                    makefile_name = curr_element_value
                                case "path":
                                    # Set a new file path
                                    makefile_path = curr_element_value
                                case _:
                                    # Default value
                                    print("Invalid parameter: {}={}".format(curr_element_key, curr_element_value))

                        """
                        # Get Target (file name/path)
                        file_target = input_list[1]

                        # Get Input Value
                        input_value = input_list[2]

                        # Check if target is file name or file path
                        match file_target:
                            case "name":
                                # Set a new file name
                                makefile_name = input_value
                                print("New Makefile name [{}] has been set".format(input_value))
                            case "path":
                                # Set a new file path
                                makefile_path = input_value
                                print("New Makefile path [{}] has been set".format(input_value))
                            case _:
                                # Default value
                                print("Invalid target: {}".format(file_target))
                        """
                    case "tr" | "trim":
                        # Trim the provided targets and variables
                        if len(targets) != 0:
                            print("Original Variables: {}".format(variables))
                            print("Original Targets: {}".format(targets))

                            # Trim and remove all special characters ("\n", "\t" etc)
                            targets, variables = makefile_parser.trim_contents(targets, variables)

                            print("Stripped Variables: {}".format(variables))
                            print("Stripped Targets: {}".format(targets))
                        else:
                            print("No targets imported")
                    case "q" | "quit":
                        break
                    case _:
                        print("Invalid option: {}".format(line))
            except Exception as ex:
                print("Exception detected: {}".format(ex))
        else:
            print("No input provided.")

def print_cli_arguments(opt_with_Arguments, opt_Flags):
    print("With Arguments:")
    for arg_name, arg_value in opt_with_Arguments.items():
        print("{} = {}".format(arg_name, arg_value))

    print("")

    print("Optionals:")
    for flag_name, flag_value in opt_Flags.items():
        print("{} = {}".format(flag_name, flag_value))

    print("")

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
    opts:dict = { 
        "positionals" : [], 
        "optionals" : {
            "with-arguments" : {"filename" : "Makefile", "filepath" : "."}, 
            "flags" : {
                "generate-default-template" : False,
                "help" : False, 
                "list" : { 
                    "makefiles" : {"all" : False, "variables" : False, "targets" : False}, 
                }, 
                "version" : False, 
                "trim" : False
            }
        } 
    }
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
                case "--generate-default-makefile":
                    # Generate a default Makefile template
                    opts["optionals"]["flags"]["generate-default-template"] = True
                case "--list-all":
                    # List all targets and variables
                    opts["optionals"]["flags"]["list"]["makefiles"]["all"] = True
                case "--list-targets":
                    # List all targets
                    opts["optionals"]["flags"]["list"]["makefiles"]["targets"] = True
                case "--list-variables":
                    # List all variables
                    opts["optionals"]["flags"]["list"]["makefiles"]["variables"] = True
                case "-h" | "--help":
                    # Help Menu
                    opts["optionals"]["flags"]["help"] = True
                case "-v" | "--version":
                    # Help Menu
                    opts["optionals"]["flags"]["version"] = True
                case "-t" | "--trim":
                    # Trim the imported file contents during import
                    opts["optionals"]["flags"]["trim"] = True
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
    makefile_fullpath = os.path.join(makefile_path, makefile_name)

    # Perform system initialization
    init(makefile_name, makefile_path)

    """
    Process CLI arguments
    """
    # print_cli_arguments(opt_with_Arguments, opt_Flags)

    # Print Help Message
    if opt_Flags["help"] == True:
        # Display Help Menu
        display_help()
        exit(1)
    elif opt_Flags["version"] == True:
        # Display System Version
        display_version()
        exit(1)
    elif opt_Flags["generate-default-template"] == True:
        # Get specified path
        makefile_path = opts["optionals"]["with-arguments"]["filepath"]
        makefile_name = opts["optionals"]["with-arguments"]["filename"]

        # Generate a default Makefile template
        bpm.generate_Makefile(makefile_name=makefile_name, makefile_path=makefile_path)
    elif True in list(opt_Flags["list"]["makefiles"].values()):
        # If there are anything enabled in '--list-*'
        makefile_flags_List = opt_Flags["list"]["makefiles"]

        ## Check for '--list-*' flags
        if makefile_flags_List["all"] == True:
            # Import Makefile into system buffer
            targets, variables, comments = bpm.import_makefile(makefile_name, makefile_path)

            # Process Makefile contents
            contents = format(targets, variables, opt_Flags["trim"])

            # List all targets and variables
            print_formatted_contents(contents)
        elif makefile_flags_List["targets"] == True:
            # Import Makefile into system buffer
            targets, _, comments = bpm.import_makefile(makefile_name, makefile_path)

            # Process Makefile contents
            contents = format(targets, variables, opt_Flags["trim"])

            # List all targets
            print_formatted_contents(contents)
        elif makefile_flags_List["variables"] == True:
            # Import Makefile into system buffer
            _, variables, comments = bpm.import_makefile(makefile_name, makefile_path)

            # Process Makefile contents
            contents = format(targets, variables, opt_Flags["trim"])

            # List all variables
            print_formatted_contents(contents)

    # Start main application body
    display_title()

    # Loop through all positionals
    for i in range(number_of_positionals):
        # Get current positional argument
        curr_pos_arg = positional_actions[i]

        print("Current Action: {}".format(curr_pos_arg))

        # Process current action
        if curr_pos_arg == "start":
            # Begin Package Manager
            print("Starting Package Manager {}...".format(makefile_fullpath))

            start_package_management(targets, variables, makefile_name, makefile_path)
        elif curr_pos_arg == "import":
            print("Importing Makefile {}...".format(makefile_fullpath))

            # Import Makefile into system buffer
            targets, variables, comments = bpm.import_makefile(makefile_name, makefile_path)

            # Trim all special characters from left and right side ("\n", "\t" etc etc) if the '-t|--trim' flag is enabled
            if opt_Flags["trim"] == True:
                print("[O] Trimming Makefile and removing special characters from both ends...")
                targets, variables = makefile_parser.trim_contents(targets, variables)

            print("[+] Makefile {} imported.".format(makefile_fullpath))

            # Print newline
            print("")
        elif curr_pos_arg == "print":
            # Process Makefile contents
            contents = makefile_parser.format_makefile_Contents(targets, variables)

            # Print formatted contents
            print_formatted_contents(contents)

            # Print newline
            print("")

if __name__ == "__main__":
    main()

