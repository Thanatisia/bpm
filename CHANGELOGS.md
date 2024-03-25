# CHANGELOGS

## Table of Contents
+ [2024-03-25](#2024-03-25)

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

