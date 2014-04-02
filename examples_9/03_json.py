import json
import os
from maria.autotest import assert_equal
from maria.autotest.decorators import with_tear_down
from maria.autotest.test_runner import TestRunner


JSON_FILE = 'test.json'


def remove_json_file():
    os.remove(JSON_FILE)


def test_dumps_empty_dict():
    obj = {}
    result = json.dumps(obj)
    expected = '{}'
    assert_equal(expected, result)


def test_dumps_dict_with_key():
    obj = {'key': 'value'}
    result = json.dumps(obj)
    expected = '{"key": "value"}'
    assert_equal(expected, result)


def test_dumps_dict_with_list():
    obj = {'key': ['value1', 'value2']}
    result = json.dumps(obj)
    expected = '{"key": ["value1", "value2"]}'
    assert_equal(expected, result)


@with_tear_down(remove_json_file)
def test_dump_to_file():
    obj = {'key': 'value'}
    with open(JSON_FILE, 'w+') as test_json:
        json.dump(obj, test_json)

        test_json.seek(0)
        result = test_json.read()
        expected = '{"key": "value"}'
        assert_equal(expected, result)


def test_loads_json_with_one_key():
    json_str = '{"key": "value"}'
    result = json.loads(json_str)
    expected = {'key': 'value'}
    assert_equal(expected, result)


@with_tear_down(remove_json_file)
def test_load_json_from_file():
    with open(JSON_FILE, 'w+') as test_json:
        test_json.write('{"key": "value"}')

        test_json.seek(0)
        result = json.load(test_json)
        expected = {"key": "value"}
        assert_equal(expected, result)


def main():
    runner = TestRunner.with_verbose_reporter()
    for name in globals():
        if name.startswith("test_"):
            runner.add_test(globals()[name])

    runner.run()


if __name__ == '__main__':
    main()


