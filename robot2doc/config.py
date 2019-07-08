#!/env/python

VERSION = "0.0.3"

DOC_CLAUSE_LVL_1 = "9"
DOC_CLAUSE_LVL_2 = 8
DOC_CLAUSE_LVL_3 = 7
DOC_CLAUSE_LVL_4 = 6

ANNEX_TITLE_LEVEL = 1
DOC_SUITE_LEVEL = 4
DOC_TC_LEVEL = 5

DOC_TC_FONT_SIZE = 8
DOC_TC_FONT_NAME = "Courier New"

DOC_MAIN_TITLE = '9 Test Cases'
DOC_FILENAME = 'test_spec_from_robot.docx'
FILE = ""
BASE_SPEC = 'basespec.docx'

# If DRY_RUN is True, no output file is created
DRY_RUN = False

# If QUIET is True, output on stdout is minimized
QUIET = False

# Prefix for the commit URL that may be added after each table. If the GIT_COMMIT
# is the empty string, nothing is added. The prefix is concatenated with the filename of
# the Robot file. NOTE: if the final slash is not present it will not be included.
# Example: 
# GIT_COMMIT = "http://acme.com/my/example/abcde/"
GIT_COMMIT_PREFIX = "https://forge.etsi.org/gitlab/nfv/api-tests/raw/XX-commit-XX/SOL00Y/AAA-API/"