Usage and Customization
=======================

```
Information regarding the various ways to use the Package Manager
```

## Documentations

*CLI Application*
-----------------
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
        + `--generate-default-makefile` : Generate a template Makefile file using the defined makefile template string (Default Path = '.', Filename = 'Makefile)
        + `-h | --help` : Display help menu
        + `-v | --version` : Show system version
        + `-t | --trim`: Trim and remove all special characters ("\n", "\t" etc) from the imported file contents

*Library*
---------

### Package
- bpm

### Modules
- bpm : The main BPM - Build (from Source) Package Manager library
- network : The Package Manager's Network Management and server-related handler library (i.e. HTTP REST API etc etc)

### Classes
- bpm
    - `.BPM(makefile_name="Makefile", makefile_path=".")` : Primary Build from Source Package Manager class
        - Class Constructor Parameters
            - makefile_name : Specify the file name of the target Makefile
                + Type: String
                + Default: "Makefile"
            - makefile_path : Specify the file path of the target Makefile
                + Type: String
                + Default: "." (Current Working Directory)
- network
    - `.Networking()` : The Package Manager Network Management and handler library (i.e. HTTP REST API etc etc)
    - `.GitHub()` : GitHub repository-related class, inheriting functions and attributes from class 'Networking'

### Functions
- bpm.BPM
    - `.import_makefile(makefile_name="Makefile", makefile_path=".")` : Import the specified Makefile file into the class 'targets' and 'variables' container
        - Parameter/Argument Signatures
            - makefile_name : Specify the file name of the target Makefile file to import
                + Type: String
                + Default: "Makefile"
            - makefile_path : Specify the file path to the target Makefile file to import
                + Type: String
                + Default: "."
        - Return
            + Type: List
            - Values
                + targets   : Makefile rules/targets + dependencies
                + variables : Makefile variables/build arguments
                + comments  : Makefile comments from the global scope (not tied to any targets); Currently unused
    - `.import_template_makefile()` : Import the default Makefile build template into Python
        - Return
            + Type: List
            - Values
                + targets   : Makefile rules/targets + dependencies
                + variables : Makefile variables/build arguments
                + comments  : Makefile comments from the global scope (not tied to any targets); Currently unused
    - `.remove_target_comments(targets:dict)`: Remove comments from imported Makefile targets
        - Parameter/Argument Signatures
            - targets : Specify the dictionary object containing the Makefile targets (aka Rules) you wish to delete comments from
                + Type: Dictionary
        - Return
            - targets   : Makefile rules/targets + dependencies with the comments removed
                + Type: Dictionary
    - `.set_makefile_name(makefile_name="Makefile")` : Set a new Makefile filename into the class
        - Parameter/Argument Signatures
            - makefile_name : Specify the new Makefile filename to overwrite
                + Type: String
                + Default: "Makefile"
    - `.set_makefile_path(makefile_path=".")` : Set a new Makefile filepath into the class
        - Parameter/Argument Signatures
            - makefile_path : Specify the new Makefile filepath to overwrite
                + Type: String
                + Default: "."
    - `.get_makefile_name()` : Getter method to return the makefile_name attribute
        - Return
            - makefile_name : The currently-set Makefile file name
                +  Type: String
    - `.get_makefile_path()` : Getter method to return the makefile_path attribute
        - Return
            - makefile_path : The currently-set Makefile file path
                +  Type: String
    - `.get_makefile_targets()` : Getter method to return the makefile_targets attribute
        - Return
            - makefile_targets : The currently imported Makefile target dictionary
                +  Type: Dictionary (Key-Value Mapping/Associative Array)
    - `.get_makefile_variables()` : Getter method to return the makefile_variables attribute
        - Return
            - makefile_variables : The currently imported Makefile variables dictionary
                +  Type: Dictionary (Key-Value Mapping/Associative Array)
    - `.get_makefile_comments()` : Getter method to return the makefile_comments attribute
        - Return
            - makefile_comments : The currently imported Makefile comments dictionary
                +  Type: Dictionary (Key-Value Mapping/Associative Array)
    - `.generate_Makefile(targets=None, variables=None, makefile_name="Makefile", makefile_path=".")`: Generate a custom makefile based on the targets and variables of your choice
        - Parameter/Argument Signatures
            - targets : Specify the dictionary object containing the Makefile targets (aka Rules) you wish to add into the output Makefile
                + Type: Dictionary
            - variables : Specify the dictionary object containing the Makefile variables you wish to add into the output Makefile
                + Type: Dictionary
            - makefile_name : Specify the file name of the target Makefile file to export to
                + Type: String
                + Default: "Makefile"
            - makefile_path : Specify the file path to the target Makefile file to export to
                + Type: String
                + Default: "."
        - Return
            - targets   : Makefile rules/targets + dependencies with the comments removed
                + Type: Dictionary

- network.Networking
    - `.set_url(url)`: Set the current URL
        - Parameter/Argument Signatures
            - url: Contains the currently set URL
                + Type: String

    - `.get_url():`: Getter method to obtain the currently set URL
        - Return
            - url: Contains the currently set URL
                + Type: String

    - `.get_status_message(status_code): Get the status message corresponding to the status code
        - Return
            - `status_message`: The message/string corresponding to the HTTP response status code
                + Type: String

    - `.send_get_Request(url)`: Send a GET request to the specified server/URL and return the response
        - Parameter/Argument Signatures
            - url: Contains the URL to the target server to send a GET request to
                + Type: String
        - Return
            - `response`: The response object returned by the HTTP GET request
                + Type: requests.response

    - `.save_downloaded_text(filename, response_text)`: Save the downloaded string obtained from the HTTP GET request
        - Parameter/Argument Signatures
            - filename : Specify the name of the output file
                + Type: String
            - response_text : Specify the response text/string returned from the HTTP request sent (obtained from response.text)
                + Type: String

- network.GitHub
    - `.set_github_user_content_url(repo_author, repo_name, filepath, branch="main")`: Set the current URL to the specified 'raw.githubusercontent.com' link of the repository
        - Parameter/Argument Signatures
            - repo_author: Specify the author of the repository
                + Type: String
            - repo_name: Specify the name of the repository
                + Type: String
            - filepath: Specify the path to the Makefile in the github repository
                + Type: String
            - branch: Specify the target branch to pull the Makefile build script from
                + Type: String
                + Default: main
    - `.get_github_user_content_url()`: Getter method to obtain the currently set GitHub URL
        - Return
            - url: Contains the currently set GitHub user content URL
                + Type: String

### Data Classes/Types

### Attributes/Variables Objects
- bpm.BPM
    - `.makefile_parser` : Parser object from the 'mkparse' library
        + Type: Parser
    - `.makefile_targets` : Currently-imported Makefile targets
        + Type: Dictionary
        + Default: {}
    - `.makefile_variables` : # Currently-imported Makefile variables
        + Type: Dictionary
        + Default: {}
    - `.makefile_comments` : Currently-imported Makefile comments
        + Default: {}
    - `.makefile_template` : Default Makefile template string
        - Default:
            ```make
            # Makefile
            # for Building from Source

            ### Build Info
            CC = your-cross-compiler (i.e. make|ninja etc)
            CFLAGS = your-cross-compilation-flags
            DEPENDENCIES = your-dependencies-here

            ### Package Information
            PKG_AUTHOR = author-name
            PKG_NAME = package-name
            BIN_NAME = binaries and executables
            SRC_URL = https://github.com/$(PKG_AUTHOR)/$(PKG_NAME)
            INSTALL_PATH = installation-path (Default: /usr/local)
            CONFIGURE_OPTS = "--prefix=$(INSTALL_PATH)"

            ### System Information
            EDITOR=vim
            SHELL := /bin/bash
            .PHONY := help install-dependencies setup build install uninstall clean enter
            .DEFAULT_RULES := help

            ## Recipe/Targets
            help:
                ## Display help message
                @echo -e "[+] help  : Display Help message"
                @echo -e "[+] install-dependencies : Install system packages"
                @echo -e "[+] clone : Clone repository if doesnt exist and initialize submodules"
                @echo -e "[+] configure : Configure the repository source files before building"
                @echo -e "[+] setup : Setup pre-requisites"
                @echo -e "[+] build : Compile/Build everything"
                @echo -e "[+] build-all : Build the project from Source"
                @echo -e "[+] build-doc : Build the project documentations from Source"
                @echo -e "[+] install: Install everything to the host system"
                @echo -e "[+] install-bin : Install and move the compiled binary to the host system"
                @echo -e "[+] install-html : Install HTML to the host system"
                @echo -e "[+] install-doc : Install documentations to the host system"
                @echo -e "[+] uninstall : Uninstall and remove the installed files from the host system"
                @echo -e "[+] clean : Clean/Remove all temporarily-generated files from repository"
                @echo -e "[+] enter : Enter the package repository"

            install-dependencies:
                ## Install dependencies
                @apt update && apt upgrade && apt install ${DEPENDENCIES}

            clone:
                ### Clone repository if doesnt exist and initialize submodules
                @test -d ${PKG_NAME} || git clone "${SRC_URL}" && cd ${PKG_NAME}; \\
                    # Initialize git submodule contents
                    ## 2>&1 : Redirect stderr to stdout
                    echo -e "Initializing git submodules..."; git submodule init 2>&1; \\
                    # Update and clone all git submodules recursively
                    echo -e "Cloning all git submodules..."; git submodule update --recursive 2>&1

            configure: clone
                ## Configure the repository source files before building
                @cd ${PKG_NAME}; ${CC} configure && ./configure ${CONFIGURE_OPTS}

            setup: clone configure
                ## Setup and perform pre-requisites

            build: build-all build-doc
                ## Compile/Build everything

            build-all: setup
                ## Compile and Build/make the source code into an executable
                @cd ${PKG_NAME}; ${CC} ${CFLAGS} all && \\
                    echo -e "[+] Compilation Successful." || \\
                    echo -e "[-] Compilation Error."

            build-doc: setup
                ## Compile and Build documentations
                @cd ${PKG_NAME}; ${CC} ${CFLAGS} doc && \\
                    echo -e "[+] Compilation Successful." || \\
                    echo -e "[-] Compilation Error."

            install: install-bin install-html install-doc
                ## Install everything to the host system

            install-bin: clone
                ## Install and move the compiled binary to the host system
                @cd ${PKG_NAME}; ${CC} ${CFLAGS} install && \\
                    echo -e "[+] Executable Installation Successful." || \\
                    echo -e "[-] Executable Installation Error."

            install-html: clone
                ## Install HTML to the host system
                @cd ${PKG_NAME}; ${CC} ${CFLAGS} install-html && \\
                    echo -e "[+] HTML Documentations Installation Successful." || \\
                    echo -e "[-] HTML Documentations Installation Error."

            install-doc: clone
                ## Install documentations to the host system
                @cd ${PKG_NAME}; ${CC} ${CFLAGS} install-doc && \\
                    echo -e "[+] Documentations Installation Successful." || \\
                    echo -e "[+] Documentations Installation Error."

            uninstall: clone
                ## Uninstall and remove installed files from the host system
                ### Uninstall a binary
                @rm /usr/local/bin/{binaries,here,...}
                ### Uninstall a directory
                @test -d /usr/local/[directory] && rm -r /usr/local/[directory]
                ### Uninstall manuals (man1)
                @rm /usr/local/share/man/man1/[manual].1
                ### Uninstall manuals (man3)
                @rm /usr/local/share/man/man3/[manual].3pm
                ### Uninstall manuals (man5)
                @rm /usr/local/share/man/man5/[manual]*
                ### Uninstall manuals (man7)
                @rm /usr/local/share/man/man7/[manual]*

            clean: clone
                ## Cleanup and remove temporary files generated during compilation
                @cd ${PKG_NAME}; ${CC} clean && \\
                    echo -e "[+] Cleanup Successful." || \\
                    echo -e "[-] Cleanup Error."

            enter: clone
                ## Enter the package repository
                @cd ${PKG_NAME};
            ```

- network.Networking
    - `.url` : Contains the currently set URL
        + Type: String
    - `.newest_response` : Container to store the latest response
        + Type: Dictionary
    - `.http_code` : Dictionary (Key-Value) mapping the HTTP status codes to the relevant message
        - Defaults
            ```python
            {
                # status-code : message
                200 : "OK",
                404 : "Not Found"
            }
            ```

- network.GitHub
    - `.url` : Contains the currently set GitHub URL
        + Type: String

## Usages

### CLI utility
- Import a target Makefile
    ```bash
    bpm -p . -f Makefile import
    ```

- Import and Print a target Makefile
    ```bash
    bpm -p . -f Makefile import print
    ```

- Import and trim the imported Makefile contents
    ```bash
    bpm -t -p . -f Makefile import print
    ```

- Generate a template Makefile of the name 'Makefile'
    ```bash
    bpm -p [file-path] -f [filename] --generate-default-makefile
    ```

### As a library

- Import python package
    ```python
    from bpm.bpm import BPM
    from bpm.network import Networking, GitHub
    ```

- Initialize Variables
    ```python
    # Initialize Variables
    makefile_path = "."
    makefile_name = "Makefile"
    ```

- (Optional) Obtain makefile arguments as a CLI argument
    ```python
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
    ```

- Initialize Module Classes
    - BPM : The core Package Manager logic
        ```python
        # Initialize Package Manager class
        bpm = BPM(makefile_name, makefile_path)
        ```
    - Networking : The Package Manager Network Management and handler library (i.e. HTTP REST API etc etc)
        ```python
        network = Networking()
        ```
    - GitHub : Github-related git remote repository server Networking utilities
        ```python
        gh = GitHub()
        ```

- Obtaining sub-dependencies
    - Initialize Makefile Parser from mkparse
        ```python
        # Initialize Makefile Parser
        makefile_parser = bpm.makefile_parser
        ```

- Import Makefile file contents into python dictionary (key-value mappings; i.e. HashMap/Associative Array)
    - Import from a Makefile file
        - Notes
            - If you do not require any of the return objects
                - You can just replace the output object with '_'
                    - i.e.
                        ```python
                        targets, variables, _ = makefile_parser.parse_makefile(makefile_name, makefile_path)
                        ```
        ```python
        # Import Makefile contents into application runtime
        targets, variables, comments = makefile_parser.parse_makefile(makefile_name, makefile_path)
        ```
    - Import using a Makefile string
        ```python
        # Import Makefile string into application runtime
        makefile_string = """# Makefile
        variable = value

        target: dependencies
            # statement
        """
        targets, variables, comments = makefile_parser.parse_makefile_string(makefile_string)
        ```

- Process imported Makefile contents
    - Trim imported Makefile contents
        - Trim both targets and variables
            ```python
            # Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
            targets, variables = makefile_parser.trim_contents(targets, variables)
            ```
        - Trim 'targets' dictionary only
            ```python
            # Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
            targets = makefile_parser.trim_contents(targets=targets)
            ```
        - Trim 'variables' dictionary only
            ```python
            # Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
            variables = makefile_parser.trim_contents(variables=variables)
            ```
    - Format Makefile contents into string
        - Format both 'targets' and 'variables' dictionary
            ```python
            # Format Makefile output into formatted string
            formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets, variables)

            # Process imported Makefile contents
            formatted_makefile_Targets = formatted_makefile_Contents["targets"]
            formatted_makefile_Variables = formatted_makefile_Contents["variables"]
            ```
        - Format 'targets' dictionary only
            ```python
            # Format Makefile output into formatted string
            formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets=targets)

            # Process imported Makefile contents
            formatted_makefile_Targets = formatted_makefile_Contents["targets"]
            ```
        - Format 'variables' dictionary only
            ```python
            # Format Makefile output into formatted string
            formatted_makefile_Contents = makefile_parser.format_makefile_Contents(variables=variables)

            # Process imported Makefile contents
            formatted_makefile_Targets = formatted_makefile_Contents["variables"]
            ```

- Use processed data
    ```python
    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(formatted_makefile_Variables)):
        # Get current line
        curr_line = formatted_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(formatted_makefile_Targets)):
        # Get current line
        curr_line = formatted_makefile_Targets[i]
        # Print
        print(curr_line)

    print("")
    ```

- Output processed data 
    - Export dictionaries to Makefile
        ```python
        # Export Makefile dictionaries to Makefile
        makefile_parser.export_Makefile(targets, variables, makefile_name, makefile_path)       
        ```

## Resources

## References

## Remarks

