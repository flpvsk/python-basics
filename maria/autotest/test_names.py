import re
import os
from os import listdir


__all__ = ('test_result_parser',)


def test_result_parser(directory):
    tests = set()
    for test_result_file in listdir(directory):
        path_to_report_file = os.path.join(directory, test_result_file)
        tests.update(extract_tests_from_file(path_to_report_file))
    return tests


def extract_tests_from_file(test_file):
    test_name_regexp = "Test '(?P<test_name>.*)' has been started"
    tests = set()
    with open(test_file, 'r') as text_file:
        for line in text_file:
            match = re.match(test_name_regexp, line, re.I)
            if match:
                tests.add(match.group('test_name'))

    return tests


if __name__ == '__main__':
    test_directory = "C:\\CVS\\test-results"
    for test_names in test_result_parser(test_directory):
        print test_names
