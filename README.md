BPM: Build (from Source) Package Manager
========================================

## Information

*Description*
-------------

Build (from Source) Package Manager for build-scripts, a package manager designed to use Makefiles as a primary method of management, building, installation and uninstallation

- The rules/target steps are based on the project maintainer's steps
    - i.e.
        - if the steps required to build, install is
            make -jN
            sudo make install
        - then the instructions are those

### Project
+ Package Name: bpm
+ Current Version: v0.4.1

## Setup

*Dependencies*
--------------
+ python
+ python-pip
+ python-venv

- Python packages
    + mkparse @ https://github.com/Thanatisia/makefile-python-parser
    + requests : To perform HTTP REST API requests

*Pre-Requisites*
----------------
- Create Python Virtual Environments
    - Generate Virtual Environments
        ```bash
        python3 -m venv [virtual-environment-name]
        ```

    - Chroot into Virtual Environment
        - Linux
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

- Install Python Packages/Dependencies
    ```bash
    pip install -Ur requirements.txt
    ```

- Verify packages
    ```bash
    pip freeze list
    ```

*Installing*
------------
- Install as a module
    - Install locally in development mode
        ```bash
        pip install .
        ```

    - Install locally in editable development mode
        ```bash
        pip install -e .
        ```

    - Install Python package using GitHub repository via setuptools
        ```bash
        pip install git+https://github.com/Thanatisia/bpm
        ```

- Install Python package manually as an executable
    - Install using setuptools
        ```bash
        python setup.py install
        ```

    - (Optional) Append your Virtual Environment's bin directory to system path
        - Notes
            + This is so that you can access the application/module from the system
        ```bash
        export PATH+=[virtual-environment-name]/bin:
        ```

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
        + `-h | --help` : Display help menu
        + `-v | --version` : Show system version
        + `-t | --trim`: Trim and remove all special characters ("\n", "\t" etc) from the imported file contents

### Usage
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

## Wiki

## Resources

## References
+ [StackOverflow - Questions - 4840182 - setup.py and adding file to /bin/](https://stackoverflow.com/questions/4840182/setup-py-and-adding-file-to-bin)

## Remarks

