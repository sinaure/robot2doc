# robot2doc

A simple Docx generator for Robot Framework Test Suites

## Requirements

    pip install

## Usage

    python main.py <robot-tests> [OUT_FILENAME [SECTION_TITLE]]

Command line arguments:

* `robot-tests` a folder or a file containing Robot tests
* `OUT_FILENAME` filename for the output (e.g. `my-tests.docx`)
* `SECTION_TITLE` the title for the section in the doc where the tests are included

## How to write the tests

For each test in each test suite, the tool will extract the documentation and parse
each line as a key-value pair, separated by `:`.

If the separator is not present, the entire line is used as the value and the key
is omitted.

Example:

    [Documentation]    Test Name: This is the test name. 
        ...    Another key: Another value. 
        ...    This line does not present a key, therefore the key is omitted. 
        ...    Post-conditions: After the test you will be happy.
        Log    Test starts...
        Etc. etc.

## License

Released under the ETSI Software Licese

https://forge.etsi.org/etsi-software-license
