#!/env/python
#
#  Usage: python main.py <FILE_OR_FOLDER> [OUTPUT_FILENAME [MAIN_TITLE]]
#

import sys
import os

from robot.api import TestSuiteBuilder

from testspec import TestSpec, DOC_TC_LEVEL
from testpurpose import TP
import config as cfg
# Configuration

DOC_CLAUSE_LVL_1 = cfg.DOC_CLAUSE_LVL_1
DOC_CLAUSE_LVL_2 = cfg.DOC_CLAUSE_LVL_2
DOC_CLAUSE_LVL_3 = cfg.DOC_CLAUSE_LVL_3
DOC_CLAUSE_LVL_4 = cfg.DOC_CLAUSE_LVL_4

DOC_MAIN_TITLE = cfg.DOC_MAIN_TITLE
DOC_FILENAME = cfg.DOC_FILENAME
FILE = cfg.DOC_FILENAME
BASE_SPEC = cfg.BASE_SPEC

DRY_RUN = cfg.DRY_RUN
QUIET = cfg.QUIET

def keyword_to_line(k):
    '''
    Takes a Robot Framework keyword object and returns
    a string with keyword and arguments on a single line
    '''
    return str(k) + " " + " ".join(k.args)

def keywords_to_text(kws):
    '''
    Takes a list of Robot Framework words and returns a multiline text
    '''
    return "\n".join(map(keyword_to_line, kws))

def gen_test(suite, this_test, spec, sec, subsec, workspace):
    '''
    Generate the Docx part for an individual test
    '''
    global DRY_RUN

    tp = TP(this_test.doc)

    log_line = ["TD", str(workspace), str(suite), str(this_test), tp.tp_id or "No ID" ]
    not QUIET and print(",".join(log_line))

    if DRY_RUN:
        return
    if tp.tp_id != None:
        spec.add_heading(str(this_test), DOC_TC_LEVEL, tp.tp_id)
    else:
        subsec = subsec + 1
        spec.add_heading(str(this_test), DOC_TC_LEVEL, DOC_CLAUSE_LVL_1, sec, DOC_CLAUSE_LVL_3, subsec)
    tp.add_to_spec(spec, keywords_to_text(this_test.keywords), str(suite)+".robot")

def gen_doc(src, doc_fn, doc_main_tit):
    '''
    Converts a Robot test suite to a word document

    src            file or directory containing Robot tests

    doc_fn         the filename for the output

    doc_main_tit   top level title for the section in the doc
    '''

    not QUIET and print("### robot2doc version " + cfg.VERSION)
    not QUIET and print("Starting..")
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cwd = os.getcwd()
    
    # Using the absolute path has caused issues. The quick fix is to
    # move temporarily to the source directory
    os.chdir(script_dir)
    try:
        spec = TestSpec(BASE_SPEC)
    finally:
        os.chdir(cwd)

    print("Loading tests from: " + src)
    try:
        workspace = TestSuiteBuilder().build(src)
    except:
        print("Please check that first argument is a folder of Robot files or a single file.")
        exit(-1)

    not QUIET and print("Loaded "+ str(len(workspace.suites)) + " test suites.")
    not QUIET and print("Loaded "+ str(len(workspace.tests)) + " tests.")
    sec = DOC_CLAUSE_LVL_2 - 1

    spec.add_main_heading(doc_main_tit)
    
    for suite in workspace.suites:
        sec = sec + 1
        subsec = DOC_CLAUSE_LVL_4
        print("  Generating test suite: " + str(suite))
        spec.add_sub_heading(str(suite), DOC_CLAUSE_LVL_1, sec, DOC_CLAUSE_LVL_3, subsec)
        for i in suite.tests:
            gen_test(suite, i, spec, sec, subsec, workspace)
    
    if len(workspace.suites) == 0:
        sec = sec + 1
        subsec = DOC_CLAUSE_LVL_4
        suite = str(workspace)
        spec.add_sub_heading(suite, DOC_CLAUSE_LVL_1, sec, DOC_CLAUSE_LVL_3, subsec)
        for i in workspace.tests:
            gen_test(suite, i, spec, sec, subsec, workspace)
            
    not QUIET and print("Saving to: " + doc_fn)
    not DRY_RUN and spec.save(doc_fn)
    not QUIET and print("Finished.")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: robot2doc <robot_file_or_dir> [<out_file> [spec_section_title]]")
        exit(-1)

    FILE = sys.argv[1]
    DOC_FILENAME = sys.argv[2] if len(sys.argv) > 2 else DOC_FILENAME
    DOC_MAIN_TITLE = sys.argv[3] if len(sys.argv) > 3 else DOC_MAIN_TITLE

    gen_doc(FILE, DOC_FILENAME, DOC_MAIN_TITLE)
