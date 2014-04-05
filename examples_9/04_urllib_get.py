"""Print all issues for python_basics repo.
GitHub API docs: https://developer.github.com/v3/issues/
"""
import urllib2
import json

# GitHub Issues API
API_URL = "https://api.github.com/repos/filipovskii/python-basics/issues"


def main():
    response = urllib2.urlopen(API_URL)
    issues_json = json.loads(response.read())
    for issue in issues_json:
        print(u"{number} - {title}".format(**issue))


if __name__ == '__main__':
    main()

