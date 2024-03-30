"""
File-related Management utilities
"""
import os
import sys
import hashlib

class Files():
    """
    File Management class
    """
    def __init__(self):
        """
        Constructor
        """

    def hash_file(self, filename, hash_alg="sha256", BUF_SIZE=65536):
        """
        Hash the specified file and return the hash digest

        :: Params
        - filename: Specify the name of the target file to hash
            + Type: String
        - hash_alg: Specify the hashing algorithm to hash the file with
            + Type: String
            + Default: sha256
            - Supported Algorithms
                + sha256 : SHA256
        - BUF_SIZE: Buffer memory size; 65536 = 65536 bytes = 64 kilobytes
            + Type: Integer
            + Default: 65536

        :: Return
        - hash_digest: The generated hash hexdigest
            + Type: Hexadecimal Integer
        """
        # Initialize Variables
        hash_digest = ""

        # Check hashing algorithm
        match hash_alg:
            case "sha256":
                """
                using SHA256
                """
                sha256 = hashlib.sha256() # Initialize the SHA256 hash method

                # Open file to be hashed
                with open(filename, "rb") as read_file_bin:
                    """
                    # Read current line
                    line = read_file_bin.readline()

                    # Loop through the entire file and hash the new line
                    while line != None:
                        # While there are still lines

                        # Attempt to hash the file to obtain

                        # Update hash digest

                        # Read next line
                        line = read_file_bin.readline()
                    """
                    while True:
                        # reading data = BUF_SIZE from
                        # the file and saving it in a
                        # variable
                        data = read_file_bin.read(BUF_SIZE)

                        # True if eof = 1
                        if not data:
                            break

                        # Passing that data to that sh256 hash
                        # function (updating the function with
                        # that data)
                        sha256.update(data)

                    # Close file after usage
                    read_file_bin.close()

                # Obtain hash hex digest
                hash_digest = sha256.hexdigest()
            case _:
                hash_digest = ""

        # Output
        return hash_digest

