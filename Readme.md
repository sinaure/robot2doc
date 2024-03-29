# robot2doc

A simple Docx generator for Robot Framework Test Suites

## Requirements

    [sudo] pip install --upgrade -r  requirements.txt [--user]

`sudo` or `--user` may be required (but not together!), depending on the local environment (e.g. OS, if using virtualenv, etc.).

## Usage

    python main.py <robot-tests> [OUT_FILENAME [SECTION_TITLE]]

Command line arguments:

* `robot-tests` a folder or a file containing Robot tests
* `OUT_FILENAME` filename for the output (e.g. `my-tests.docx`)
* `SECTION_TITLE` the title for the section in the doc where the tests are included

Other configurable paramenters may be found in `config.py`, such as:

* ` DOC_CLAUSE_LVL_*`, the starting number for the sections numbering, with `LVL_1` being the number of the toplevel clause.
* `DRY_RUN`, if True, no output Docx file is created
* `QUIET`, if True, output on stdout is minimized
* `GIT_COMMIT_PREFIX`, If not empty, a NOTE is added after each test with this URL concatenated to the name of the Robot file(s) in input


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

### Test ID

If one of the fields in the documentation is called `Test ID`, the string next to it is used as the reference number for the subclause of the document.

## Tests

Few tests for the internals are created in the `robot2doc` folder.
To execute the tests you need to install the `pytest` module, then in the folder of the test
run the command:

    $ python -m "pytest"

or to filter only one of the files use `-k`, e.g.:

    $ python -m "pytest" -k testpurpose

## License

Released under the ETSI Software Licese

https://forge.etsi.org/etsi-software-license
