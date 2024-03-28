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

        # Store the latest responses
        self.newest_response = {
            "text" : response_text,
            "headers" : response_header,
            "content-type" : response_content_Type
        }

        # Return
        return response

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

