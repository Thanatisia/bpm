"""
Package Manager Networking Infrastructure/functionalities
"""
import os
import sys
import requests # To send HTTP REST API requests
from requests import get, post, put

class Networking():
    """
    Package Manager Networking
    """
    def __init__(self):
        """
        Class constructor/initializer
        """
        self.url = ""
        self.newest_response = {} # Container to store the latest response
        self.http_code = {
            # status-code : message
            200 : "OK",
            404 : "Not Found"
        }

    def set_url(self, url):
        """
        Set the current URL
        """
        self.url = url

    def get_url(self):
        """
        Get the URL
        """
        return self.url

    def get_status_message(self, status_code):
        """
        Get the status message corresponding to the status code
        """

        """
        status_text = self.http_code[status_code]
        match status_code:
            case 200:
                # OK
                status_text = "OK"
            case _:
                status_text = "Unknown"
        """
        return self.http_code[status_code]

    def send_get_Request(self, url):
        """
        Send a GET request to the server
        """
        # Send a GET request and return the response
        response = get(url)

        # Obtain the text
        response_text = response.text

        # Obtain the HTTP headers
        response_header = response.headers

        # Obtain the Content Type
        response_content_Type = response_header["Content-Type"]

        # Obtain the Status Code
        response_status_Code = response.status_code

        # Store the latest responses
        self.newest_response = {
            "text" : response_text,
            "headers" : response_header,
            "content-type" : response_content_Type,
            "status-code" : response_status_Code
        }

        # Return
        return response

    def save_downloaded_text(self, filename, response_text):
        """
        Save the downloaded string obtained from the HTTP GET request
        """
        # File does not exist
        ## Write Makefile content to file
        with open(filename, "w") as download_file:
            # Write GET request contents to file
            download_file.write(response_text)

            # Close file after usage
            download_file.close()

class GitHub(Networking):
    """
    GitHub repository-related class, inheriting functions and attributes from class 'Networking'
    """
    def __init__(self):
        """
        Class Constructor
        """

    def set_github_user_content_url(self, repo_author, repo_name, filepath, branch="main"):
        """
        Set the current URL to the specified 'raw.githubusercontent.com' link of the repository
        """
        self.url = "https://raw.githubusercontent.com/{}/{}/{}/{}".format(repo_author, repo_name, branch, filepath)

    def get_github_user_content_url(self):
        """
        Get the set URL
        """
        return self.url

def main():
    """
    Testbed
    """
    # Initialize Variables
    network = Networking()
    gh = GitHub()
    target_project_author = "git"
    target_project_name = "git"
    target_Makefile = "apt.Makefile"

    # Set the current raw.githubusercontent.com URL to download from
    gh.set_github_user_content_url("Thanatisia", "build-scripts", "packages/github/{}/{}/Makefiles/{}".format(target_project_author, target_project_name, target_Makefile))

    # Perform a GET request to GitHub user content to download the contents of the Makefile
    response = get(gh.url)

    # Obtain the text
    response_text = response.text
    response_header = response.headers
    response_content_Type = response_header["Content-Type"]

    print("Response Text: {}".format(response_text))

if __name__ == "__main__":
    main()

