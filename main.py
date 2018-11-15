#!/env/python
#
#  Usage: python main.py <FILE_OR_FOLDER> [OUTPUT_FILENAME [MAIN_TITLE]]
#

from robot.api import TestSuiteBuilder
import sys
import testspec
from testpurpose import TP

# Configuration

DOC_MAIN_TITLE = 'Annex B (informative): Test Cases'
DOC_FILENAME = 'test_spec_from_robot.docx'
FILE=""
        
def keyword_to_line(k):
    '''
    Takes a Robot Framework keyword object and returns
    a string with keyword and arguments on a single line
    '''
    return str(k) + " " + " ".join(k.args)

def keywords_to_text(ks):
    '''
    Takes a list of Robot Framework words and returns a multiline text 
    '''
    return "\n".join(map(keyword_to_line, ks))

def robot2doc(src, doc_fn, doc_main_tit):
    '''
    Converts a Robot test suite to a word document

    src            file or directory containing Robot tests

    doc_fn         the filename for the output

    doc_main_tit   top level title for the section in the doc
    '''

    print "Starting.."
    spec = testspec.TestSpec('ETSI_GS_Skeleton.docx')

    try:
        workspace = TestSuiteBuilder().build(file)
    except:
        print "Please check that first argument is a folder of Robot files or a single file."
        exit(-1)

    print "Loaded "+ str(len(workspace.suites)) + " test suites."
    sec = testspec.DOC_BASE_SEC - 1

    spec.add_main_heading(doc_main_tit)
    for suite in workspace.suites:
        sec = sec + 1
        subsec = 0
        print "  Generating test suite: " + str(suite)
        spec.add_sub_heading(str(suite),sec)
        for i in suite.tests:
            subsec = subsec + 1
            spec.add_heading(str(i), testspec.DOC_TC_LEVEL, sec, subsec)
            TP(i.doc).add_to_spec(spec, keywords_to_text(i.keywords))

    spec.save(doc_fn)
    print "Finished."

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage: robot2doc <robot_file_or_dir> [<out_file> [spec_section_title]]"

    FILE = sys.argv[1]
    DOC_FILENAME = sys.argv[2] if len(sys.argv) > 2 else DOC_FILENAME
    DOC_MAIN_TITLE = sys.argv[3] if len(sys.argv) > 3 else DOC_MAIN_TITLE

    robot2doc(FILE, DOC_FILENAME, DOC_MAIN_TITLE)