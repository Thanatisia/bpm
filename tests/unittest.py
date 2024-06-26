"""
Main Unit Test launcher
"""
import os
import sys
import pkg_resources
from copy import deepcopy
from bpm.bpm import BPM
from bpm.network import Networking, GitHub
from bpm.files import Files

def init(makefile_name="Makefile", makefile_path="."):
    global bpm, makefile_parser, network, gh, files

    # Initialize Variables
    bpm = BPM(makefile_name, makefile_path)
    makefile_parser = bpm.makefile_parser  # Initialize Makefile Parser
    network = Networking()
    gh = GitHub()
    files = Files()

def print_makefile_contents(targets:dict, variables:dict):
    """
    Print Makefile Contents
    """
    # Format targets and variables into printable strings
    print("* Formatting removed comments list...")
    contents = makefile_parser.format_makefile_Contents(targets, variables)

    # Print contents
    content_makefile_Targets = contents["targets"]
    content_makefile_Variables = contents["variables"]

    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(content_makefile_Variables)):
        # Get current line
        curr_line = content_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(content_makefile_Targets)):
        # Get current line
        curr_line = content_makefile_Targets[i]
        # Print
        print(curr_line)

def compare_lists(src:list, dst:list):
    """
    Compare a source and destination list and returns the differences

    :: Params
    - src : Specify the source list to use to compare
        + Type: List
    - dst : Specify the destination list to compare to
        + Type: List

    :: Return
    - differences : Dictionary of differences mapping the line to the values
        - Format
            {
                [line-texts] = {
                    "source" : [line-number],
                    "destination" : [line-number]
                }
            }
    """
    # Initialize Variables
    differences:dict = {}

    # Iterate through both dictionaries
    for i in range(len(src)):
        # Get current source
        curr_src = src[i]

        # Initialize Key-Value entry
        if curr_src not in list(differences.keys()):
            differences[curr_src] = {"source" : 0, "destination" : 0} # source|destination : [line-number]

        # Compare key-values and check if the current value of the source is found in the destination 
        if curr_src in dst:
            # Compare
            for j in range(len(dst)):
                # Get current destination
                curr_dst = dst[j]

                # Compare
                if curr_src == curr_dst:
                    # Source Values are found in Destination Values
                    differences[curr_src]["source"] = i
                    differences[curr_src]["destination"] = j
                    break
        else:
            # Source Values are not found in Destination Values
            differences[curr_src]["source"] = i
            differences[curr_src]["destination"] = None

    # Return differences map
    return differences

def test_remove_comments(tmp_targets):
    """
    Test function 'remove_comments()'
    """
    # Initialize Variables

    # Process imported Makefile contents
    tmp_targets = bpm.remove_target_comments(tmp_targets)

    # Use processed data

    # Output processed data
    return tmp_targets

def test_get_request(target_project_author, target_project_name, target_Makefile):
    """
    Test downloading files from raw.githubusercontent.com using HTTP GET request
    """
    # Initialize Variables

    # Set the current raw.githubusercontent.com URL to download from
    gh.set_github_user_content_url("Thanatisia", "build-scripts", "packages/github/{}/{}/Makefiles/{}".format(target_project_author, target_project_name, target_Makefile))

    # Perform a GET request and return
    response = network.send_get_Request(gh.url)
    status_code = response.status_code
    status_text = network.get_status_message(status_code)
    response_text = response.text

    # Close connection after completion
    response.close()

    return [status_code, status_text, response_text]

def test_http_rest_api(target_project_author, target_project_name, target_Makefile):
    """
    Test HTTP REST API GET request
    """
    ## Initialize Variables


    print("* Testing HTTP REST API GET request...")
    try:
        # Check if Makefile exists in current working directory
        if not (os.path.isfile(target_Makefile)):
            # Send a GET request to GitHub user content
            status_code, status_text, response_text = test_get_request(target_project_author, target_project_name, target_Makefile)
            print("Status [{} : {}]".format(status_code, status_text))

            # File does not exist
            ## Write Makefile content to file
            network.save_downloaded_text(target_Makefile, response_text)
            print("[+] File {} downloaded successfully.".format(target_Makefile))
        else:
            print("[-] File {} exists".format(target_Makefile))

        # Import Makefile to dictionary
        targets, variables, comments = makefile_parser.parse_makefile(target_Makefile)
        print_makefile_contents(targets, variables)

        # Export Makefile for comparison
        makefile_parser.export_Makefile(targets, variables, "apt-exported.Makefile")
    except Exception as ex:
        print("[-] Exception detected when performing test for GET request: {}".format(ex))

def test_generate_default_makefile_Template():
    # Generate default template Makefile
    bpm.generate_Makefile(makefile_name="test.Makefile")

def test_import_makefile_template_string():
    # Initialize Variables

    # Import string into dictionary object
    targets, variables, comments = bpm.import_template_makefile()

    return [targets, variables, comments]

def test_template_Makefile(target_Makefile):
    """
    Test the generation, printing of template Makefile files and strings
    """
    # Initialize Variables
    target_makefile_split = target_Makefile.split(".")
    target_makefile_filepath = target_makefile_split[0]
    target_makefile_ext = target_makefile_split[1]
    target_makefile_paths = target_makefile_filepath.split("/")
    target_makefile_filename = target_makefile_paths[::-1][0]

    # Add 'exported' to target makefile name
    target_makefile_exported = "{}-exported.{}".format(target_makefile_filename, target_makefile_ext)

    """
    Template Makefile files
    """
    # Generate default template Makefile
    test_generate_default_makefile_Template()

    # Import generated default template Makefile to dictionary
    targets, variables, comments = makefile_parser.parse_makefile(target_Makefile)

    # Export Makefile for comparison
    makefile_parser.export_Makefile(targets, variables, target_makefile_exported)

    """
    Template Makefile Strings
    """
    # Import Makefile template string
    targets, variables, comments = test_import_makefile_template_string()
    print_makefile_contents(targets, variables)
    # Export generated template Makefile
    makefile_parser.export_Makefile(targets, variables, "template.Makefile")

def test_hash(filename="Makefile"):
    """
    Test the hash function and return the hash hex digest
    """
    # Hash the file
    hash_hexdigest = files.hash_file(filename)

    # Return
    return hash_hexdigest

def get_cli_arguments():
    """
    Obtain CLI arguments and options
    """
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

    return [makefile_name, makefile_path]

def main():
    """
    Main Runner
    """
    # Obtain CLI argument parsing
    makefile_name, makefile_path = get_cli_arguments()

    # Initialize System Environment
    init(makefile_name, makefile_path)

    # Import Makefile contents into application runtime
    print("* Importing Makefile contents...")
    targets, variables, comments = makefile_parser.parse_makefile(makefile_name, makefile_path)

    print("* Printing original Makefile contents as a baseline...")
    print_makefile_contents(targets, variables)

    # Test remove comments
    print("* Testing comments removal...")
    targets_comments_removed = test_remove_comments(targets)

    print("* Printing new target list...")
    print_makefile_contents(targets_comments_removed, variables)

    print("[+] Comments removed successfully")

    print("")

    # Test HTTP REST API GET request
    target_project_author = "git"
    target_project_name = "git"
    target_Makefile = "apt.Makefile"
    test_http_rest_api(target_project_author, target_project_name, target_Makefile)

    # Test the generation, printing of template Makefile files and strings
    target_Makefile = "test.Makefile"
    test_template_Makefile(target_Makefile)

    print("")

    # Test the file and return the hex digest
    target_Makefile = "template.Makefile"
    hexdigest = test_hash(target_Makefile)
    print("Hex Digest: {}".format(hexdigest))

if __name__ == "__main__":
    main()

