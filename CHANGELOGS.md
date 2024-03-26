# CHANGELOGS

## Table of Contents
+ [2024-03-25](#2024-03-25)
+ [2024-03-26](#2024-03-26)

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

