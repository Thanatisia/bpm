# CHANGELOGS

## Table of Contents
+ [2024-03-25](#2024-03-25)
+ [2024-03-26](#2024-03-26)
+ [2024-03-27](#2024-03-27)
+ [2024-03-28](#2024-03-28)
+ [2024-03-29](#2024-03-29)
+ [2024-03-30](#2024-03-30)

## Entry Logs
### 2024-03-25
#### 2246H
+ Initial Commit
+ Version: v0.1.0

- Version Changes
    - Added python packaging dependencies:
        + [mkparse](https://github.com/Thanatisia/makefile-parser-python) : Makefile-to-Python Parser
    + Added base implementation of the Makefile Parsing operational workflow
    + Added class for the Package Manager

- New
    + Added new file '.gitignore'
    + Added new document 'CHANGELOGS.md'
    + Added new document 'README.md'
    + Added new document 'requirements.txt' : Python packages dependencies
    - Added new directory 'src/' : Contains the project source codes
        - Added new directory 'bpm': Package/application project source directory for the package manager
            + Added new python source file 'main.py' : Simple proof-of-concept implementation and potentially main source file for the package manager
    - Added new directory 'resources/' for holding test resource files
        - Added new directory 'test-cases/' for holding test files during development
            - Added new directory 'Makefiles' for holding Makefile resources
                + Added new test Makefile 'test.Makefile'

#### 2256H
- Updates
    - Updated source file 'main.py' in 'src/bpm'
        + Split function 'select_makefile' => 'set_makefile_name()' and 'set_makefile_path()' respectively

### 2024-03-26
#### 0912H
- New
    + Added new source file '__init__.py' in 'src/bpm' to initialize the folder as a package/module
    + Added new library 'bpm.py' in 'src/bpm' to hold all Build Package Manager contents
    + Added python packaging script 'setup.py' for setuptools

- Updates
    - Updated document 'README.md'
        + Added installation pre-requisites
    - Updated source file 'main.py' in 'src/bpm'
        + Moved class 'BPM' to 'bpm.py' in 'src/bpm'
    + Renamed 'main.py' in 'src/bpm' => '__main__.py'

#### 1000H
+ Version: v0.2.0

- Version Changes
    + Fixed python packaging 'setup.py' to install to be usable as both modules and executables
    + Added entry_points to install the main() module as an executable

- TODO
    + Add CLI argument options

- Updates
    - Updated document 'README.md'
        + Added post-installation steps
        + Added documentations for BPM
    - Updated python packaging script 'setup.py'
        + Fixed python packaging 'setup.py' to install to be usable as both modules and executables
        + Added entry_points to install the main() module as an executable
    - Updated '__main__.py' in 'src/bpm'
        + Added data validation: Null value check

#### 1027H
- Updates
    - Updated source file '__main__.py' in 'src/bpm'
        + Added CLI argument parsing support
        + Added CLI optionals and flags

#### 1159H
- Updates
    - Updated source file '__main__.py' in 'src/bpm'
        + Formatted CLI argument 
        + Added new functions 'import_Makefile()'
        + Added new functions 'obtain_arguments()' meant for obtaining CLI arguments and returning
        + Updated the CLI argument parser
        + Added Positional argument parsing support

#### 1327H
+ Version: v0.3.0

- Version Changes
    + Updated the CLI argument parser
    + Added Positional argument parsing support
    + Fixed python packaging 'setup.py' to install to be usable as both modules and executables
    + Added entry_points to install the main() module as an executable

- TODO

- Updates
    - Updated document 'README.md'
        + Updated CLI utility documentations
        + Added Usages
    - Updated source file '__main__.py' in 'src/bpm'
        + Updated display_help() documentations
        + Moved function 'import_Makefile()' => class BPM of 'bpm.py' in 'src/bpm'
        + Added reference to class variable 'bpm'
    - Updated source file 'bpm.py' in 'src/bpm'
        + Moved function 'import_Makefile()' from '__main__.py' in 'src/bpm'

#### 1348H
+ Version: v0.3.1

- Version Changes
    + Added new option '-v | --version' to display system version

- Updates
    - Updated document 'README.md'
        + Updated package version to '0.3.1'
    - Updated source file '__main__.py' in 'src/bpm'
        + Added dependency 'pkg_resources' to manage python packages
        + Added new option '-v | --version' to display system version
    - Updated python packaging script 'setup.py'
        + Updated package version to '0.3.1'

### 2024-03-27
#### 2215H
+ Version: v0.4.0

- Version Changes
    + Added new option '-t | --trim' to trim special characters like '\n' and '\t' from imported file contents
    - Main CLI utility
        + Added function 'print_formatted_contents(contents:dict)' abstraction for printing the formatted contents string dictionary to standard output
    - bpm.bpm
        + Added function 'remove_target_comments(self, targets:dict)' for removing comments from a 'target' lists

- New
    - Added new directory 'tests/' for holding all unit tests
        + Added new unit test source 'unittest.py'
    - Added new directory 'resources/' for holding test resource files
        - Added new directory 'test-cases/' for holding test files during development
            - Added new directory 'Makefiles' for holding Makefile resources
                + Added new test Makefile 'test.Makefile'

- Updates
    - Updated document 'README.md'
        + Updated package version to '0.4.0'
        + Updated documentations and usages
    - Updated python packaging script 'setup.py'
        + Updated package version to '0.4.0'
    - Updated source file '__main__.py' in 'src/bpm'
        + Added new CLI argument option '-t|--trim' for trimming special characters like '\n' and '\t' from imported file contents
        + Added function 'print_formatted_contents(contents:dict)' abstraction for printing the formatted contents string dictionary to standard output
        + Updated documentations
    - Updated source file 'bpm.py' in 'src/bpm'
        + Added function 'remove_target_comments(self, targets:dict)' for removing comments from a 'target' lists

### 2024-03-28
#### 1513H
- Updates
    - Updated source file '__main__.py' in 'src/bpm'
        + Moved header print into a dedicated function 'display_title()'
        + Added function 'format()' to streamline the formatting of targets and variables dictionary into standard output printable string lists and other formatting factors such as trimming
        + Moved options in 'opts["optionals"]["list"]' => 'opts["optionals"]["list"]["makefiles"]'
        + Added CLI argument options '--list-all', '--list-targets', '--list-variables' to list the various information of the provided Makefile

#### 1520H
+ Version: v0.4.1

- Version Changes
    + Added function 'format()' to streamline the formatting of targets and variables dictionary into standard output printable string lists and other formatting factors such as trimming
    + Moved options in 'opts["optionals"]["list"]' => 'opts["optionals"]["list"]["makefiles"]'
    + Added new CLI argument options '--list-all', '--list-targets', '--list-variables' to list the various information of the provided Makefile

- Updates
    - Updated document 'README.md'
        + Updated package version to '0.4.1'
        + Updated documentations and usages
    - Updated python packaging script 'setup.py'
        + Updated package version to '0.4.1'

#### 1622H
- New
    + Added new source file 'network.py' in 'src/bpm': The Networking module of the Package Manager; performs the networking and web communication side of things

- Updates
    - Updated document 'README.md'
        - Added new python package dependency 
            + requests : For making HTTP API requests and responses
    - Updated document 'requirements.txt'
        - Added new python package dependency 
            + requests : For making HTTP API requests and responses
    - Updated python packaging script 'setup.py'
        - Added new python package dependency 
            + requests : For making HTTP API requests and responses
    - Updated unit test source 'unittest.py' in 'tests/'
        + Added new unit test for testing the GET HTTP request to download files from Github

### 2024-03-29
#### 1818H
- New
    + Added new source file 'files.py' in 'src/bpm': Contains Files-based Management and handling functions

- Updates
    - Updates '.gitignore'
        + Added block files for Makefiles, build directories
    - Updated source file 'network.py' in 'src/bpm'
        + Added mappings for common HTTP status codes
        + Added new function `get_status_message(self, status_code)`: Returns the status message string corresponding to the status code
        + Added new function `save_downloaded_text(self, filename, response_text)`: Saves the response text string received from the GET request into the specified file
    - Updated unit test source file 'unittest.py' in 'tests/'
        - Added new unit test for
            + Send a GET request to githubusercontent and return the response
            + Import the response string from Makefile into Python and return the objects
            + Format the Makefile dictionary contents into human-readable standard output string
            + Print the formatted contents list
            + Save the response string into a file and export it

### 2024-03-30
#### 1059H
- New
    + Added new document 'CONTRIBUTING.md' for adding the contribution steps to be taken note of

- Updates
    - Updated source file 'bpm.py' in 'src/bpm'
        + Renamed import class 'MakefileParser' in library 'mkparse.mkparse' => 'Parser'
        + Renamed class initialization 'MakefileParser' => 'Parser'
        + Added a class attribute/variable 'makefile_template' containing a default makefile template string
        + Added a class function 'import_template_makefile(self)' to import the default template makefile string into the system
        + Added a class function 'generate_Makefile(self, targets=None, variables=None, makefile_name="Makefile", makefile_path=".")' to generate a custom Makefile based on the provided targets and variables containers
    - Updated unit test source file 'unittest.py' in 'tests/'
        + Added a dedicated test function 'test_http_rest_api(target_project_author, target_project_name, target_Makefile)' for testing the HTTP REST-API requests functionality
        + Added a dedicated test function 'test_generate_default_makefile_Template()' for testing the generating of a Makefile file with the contents of the default makefile template string
        + Added a dedicated test function 'test_import_makefile_template_string()' for testing the importing of a Makefile string (specifically the default makefile template string) into the class targets and variables containers
        + Added a operational control flow test function 'test_template_Makefile(target_Makefile)' for testing the generation, printing of template Makefile files and strings (specifically the default makefile template string)

#### 1438H
- New
    + Added new document 'USAGE.md' containing all usage methods as a library/package

- Updates
    - Updated document 'README.md'
        + Added documentation for new option '--generate-default-makefile' to generate a default Makefile template using a defined template string
        + Added usage for new option
    - Updated source file 'src/bpm/__main__.py'
        + Added new option '--generate-default-makefile' to generate a default Makefile template using a defined template string

#### 1500H
- Updates
    - Updated document 'USAGE.md'
        + Added documentation for module/library 'network.py' in 'src/bpm' containing the Networking and GitHub functionalities

#### 1516H
- Updates
    - Updated document 'USAGE.md'
        + Added usage and documentation for 'Files()'
    - Updated source file 'files.py' in 'src/bpm/'
        + Implement hash function 'SHA256' to hash the specified file
    - Updated unit test source file 'unittest.py' in 'tests/'
        + Initialized class variables for 'Files()'
        + Added a dedicated test function for testing the hashing of a specified file using SHA256

#### 1529H
+ Version: v0.5.0

- Version Changes
    - Package
        - Added new python package dependency 
            + requests : For making HTTP API requests and responses
    - bpm CLI utility
        + Added new option '--generate-default-makefile' to generate a default Makefile template using a defined template string
    - bpm.bpm
        + Renamed import class 'MakefileParser' in library 'mkparse.mkparse' => 'Parser'
        + Renamed class initialization 'MakefileParser' => 'Parser'
        + Added a class attribute/variable 'makefile_template' containing a default makefile template string
        + Added a class function 'import_template_makefile(self)' to import the default template makefile string into the system
        + Added a class function 'generate_Makefile(self, targets=None, variables=None, makefile_name="Makefile", makefile_path=".")' to generate a custom Makefile based on the provided targets and variables containers
    - bpm.files
        + Implemented hash function to hash the specified file with the specified hashing algorithm
    - bpm.network
        + Added mappings for common HTTP status codes
        + Added new function `get_status_message(self, status_code)`: Returns the status message string corresponding to the status code
        + Added new function `save_downloaded_text(self, filename, response_text)`: Saves the response text string received from the GET request into the specified file

- New
    + Added new source file 'network.py' in 'src/bpm': The Networking module of the Package Manager; performs the networking and web communication side of things
    + Added new source file 'files.py' in 'src/bpm': Contains Files-based Management and handling functions
    + Added new document 'CONTRIBUTING.md' for adding the contribution steps to be taken note of
    + Added new document 'USAGE.md' containing all usage methods as a library/package

- Updates
    - Updated document 'README.md'
        - Added new python package dependency 
            + requests : For making HTTP API requests and responses
        + Updated package version to '0.5.0'
        + Updated documentations and usages
        + Added documentation for new option '--generate-default-makefile' to generate a default Makefile template using a defined template string
        + Added usage for new option
    - Updated document 'USAGE.md'
        + Added documentation for module/library 'network.py' in 'src/bpm' containing the Networking and GitHub functionalities
        + Added usage and documentation for 'Files()'
    - Updates '.gitignore'
        + Added block files for Makefiles, build directories
    - Updated python packaging script 'setup.py'
        - Added new python package dependency 
            + requests : For making HTTP API requests and responses
        + Updated package version to '0.5.0'
    - Updated document 'requirements.txt'
        - Added new python package dependency 
            + requests : For making HTTP API requests and responses
    - Updated unit test source file 'unittest.py' in 'tests/'
        + Added new unit test for testing the GET HTTP request to download files from Github
        - Added new unit test for
            + Send a GET request to githubusercontent and return the response
            + Import the response string from Makefile into Python and return the objects
            + Format the Makefile dictionary contents into human-readable standard output string
            + Print the formatted contents list
            + Save the response string into a file and export it
        + Added a dedicated test function 'test_http_rest_api(target_project_author, target_project_name, target_Makefile)' for testing the HTTP REST-API requests functionality
        + Added a dedicated test function 'test_generate_default_makefile_Template()' for testing the generating of a Makefile file with the contents of the default makefile template string
        + Added a dedicated test function 'test_import_makefile_template_string()' for testing the importing of a Makefile string (specifically the default makefile template string) into the class targets and variables containers
        + Added a operational control flow test function 'test_template_Makefile(target_Makefile)' for testing the generation, printing of template Makefile files and strings (specifically the default makefile template string)
        + Initialized class variables for 'Files()'
        + Added a dedicated test function for testing the hashing of a specified file using SHA256
    - Updated source file 'network.py' in 'src/bpm'
        + Added mappings for common HTTP status codes
        + Added new function `get_status_message(self, status_code)`: Returns the status message string corresponding to the status code
        + Added new function `save_downloaded_text(self, filename, response_text)`: Saves the response text string received from the GET request into the specified file
    - Updated source file 'bpm.py' in 'src/bpm'
        + Renamed import class 'MakefileParser' in library 'mkparse.mkparse' => 'Parser'
        + Renamed class initialization 'MakefileParser' => 'Parser'
        + Added a class attribute/variable 'makefile_template' containing a default makefile template string
        + Added a class function 'import_template_makefile(self)' to import the default template makefile string into the system
        + Added a class function 'generate_Makefile(self, targets=None, variables=None, makefile_name="Makefile", makefile_path=".")' to generate a custom Makefile based on the provided targets and variables containers
    - Updated source file 'src/bpm/__main__.py'
        + Added new option '--generate-default-makefile' to generate a default Makefile template using a defined template string
    - Updated source file 'files.py' in 'src/bpm/'
        + Implement hash function 'SHA256' to hash the specified file

