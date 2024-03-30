import os
import sys
from mkparse.mkparse import Parser

class BPM:
    """
    BPM - Build (from Source) Package Manager
    """
    def __init__(self, makefile_name="Makefile", makefile_path="."):
        """
        Class constructor/initializer
        """
        # Initialize Makefile Parser class
        self.makefile_parser = Parser(makefile_name, makefile_path)
        self.makefile_targets = {}   # Currently-imported Makefile targets
        self.makefile_variables = {} # Currently-imported Makefile variables
        self.makefile_comments = {}  # Currently-imported Makefile comments
        self.makefile_template = """# Makefile
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
        """

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

    def import_template_makefile(self):
        """
        Import the default Makefile build template into system buffer
        """
        # Initialize Variables
        targets:dict = {}
        variables:dict = {}
        comments:dict = {}
        contents = {}

        # Import Makefile
        targets, variables, comments = self.makefile_parser.parse_makefile_string(self.makefile_template)

        # Set currently imported contents
        self.makefile_targets = targets
        self.makefile_variables = variables
        self.makefile_comments = comments

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

    def generate_Makefile(self, targets=None, variables=None, makefile_name="Makefile", makefile_path="."):
        """
        Generate a custom makefile based on the targets and variables of your choice
        """
        # Initialize Variables
        error_msg = ""
        makefile_fullpath = os.path.join(makefile_path, makefile_name)

        # Check if both are not available (generate template)
        if (targets == None) and (variables == None):
            print("Generate Template")
            # Check if file exists
            if not (os.path.isfile(makefile_fullpath)):
                # Open file
                with open(makefile_fullpath, "a+") as export_template_Makefile:
                    # Write the Makefile build template 
                    export_template_Makefile.write(self.makefile_template + "\n")

                    # Close file after usage
                    export_template_Makefile.close()
            else:
                error_msg = "Makefile {} already exists".format(makefile_fullpath)
        else:
            # Check if variables is available
            if variables == None:
                variables = {}

            # Check if targets is available
            if targets == None:
                targets = {}

            try:
                # Export Makefile
                self.makefile_parser.export_Makefile(targets, variables)
            except Exception as ex:
                error_msg = "Exception: {}".format(ex)

        return error_msg

