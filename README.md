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

## Setup

*Dependencies*
--------------
+ python
+ python-pip
+ python-venv

- Python packages
    + mkparse @ https://github.com/Thanatisia/makefile-python-parser

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

## Wiki

## Resources

## References
+ [StackOverflow - Questions - 4840182 - setup.py and adding file to /bin/](https://stackoverflow.com/questions/4840182/setup-py-and-adding-file-to-bin)

## Remarks

