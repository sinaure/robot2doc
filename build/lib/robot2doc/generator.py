#!/env/python
#
#  Usage: python main.py <FILE_OR_FOLDER> [OUTPUT_FILENAME [MAIN_TITLE]]
#

import sys
import os

from robot.api import TestSuiteBuilder

from robot2doc  import testspec as TS
from robot2doc import testpurpose as TP
from robot2doc import config as cfg
import sys
import logging
import datetime
# Configuration

# coding=utf-8



LOG = logging.getLogger("Generator")


class Generator():
    def __init__(self, out_filename=None, out_filename_prefix=None ):
        super(Generator, self).__init__()
        
        LOG.info("********Generator constructor")
        self.output_filename_prefix = out_filename
        self.output_filename = out_filename_prefix

        
        try:
            LOG.info("setting default cfg")
            self.DOC_CLAUSE_LVL_1 = cfg.DOC_CLAUSE_LVL_1
            self.DOC_CLAUSE_LVL_2 = cfg.DOC_CLAUSE_LVL_2
            self.DOC_CLAUSE_LVL_3 = cfg.DOC_CLAUSE_LVL_3
            self.DOC_CLAUSE_LVL_4 = cfg.DOC_CLAUSE_LVL_4
            
            self.DOC_MAIN_TITLE = cfg.DOC_MAIN_TITLE
            self.DOC_FILENAME = self.output_filename if self.output_filename!=None else cfg.DOC_FILENAME
            self.FILE = cfg.DOC_FILENAME
            self.BASE_SPEC = cfg.BASE_SPEC
            
            self.DRY_RUN = cfg.DRY_RUN
            self.QUIET = cfg.QUIET
            
        except Exception as e:
            LOG.error("%s" % (e.__str__()))
            sys.exit()
        

    
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
        tp = TP(this_test.doc)
    
        log_line = ["TD", str(workspace), str(suite), str(this_test), tp.tp_id or "No ID" ]
        not QUIET and print(",".join(log_line))
    
        if self.DRY_RUN:
            return
        if tp.tp_id != None:
            spec.add_heading(str(this_test), self.DOC_TC_LEVEL, tp.tp_id)
        else:
            subsec = subsec + 1
            spec.add_heading(str(this_test), self.DOC_TC_LEVEL, self.DOC_CLAUSE_LVL_1, sec, self.DOC_CLAUSE_LVL_3, subsec)
        tp.add_to_spec(spec, keywords_to_text(this_test.keywords), str(suite)+".robot")
    
    def gen_doc(self, src, doc_fn, doc_main_tit=None, prefix=None):
        '''
        Converts a Robot test suite to a word document
    
        src            file or directory containing Robot tests
    
        doc_fn         the filename for the output
    
        doc_main_tit   top level title for the section in the doc
        '''
    
        not self.QUIET and print("### robot2doc version " + cfg.VERSION)
        not self.QUIET and print("Starting..")
        script_dir = os.path.dirname(os.path.realpath(__file__))
        cwd = os.getcwd()
        
        # Using the absolute path has caused issues. The quick fix is to
        # move temporarily to the source directory
        os.chdir(script_dir)
        try:
            spec = TS(self.BASE_SPEC)
        finally:
            os.chdir(cwd)
    
        print("Loading tests from: " + src)
        try:
            workspace = TestSuiteBuilder().build(src)
        except:
            print("Please check that first argument is a folder of Robot files or a single file.")
            exit(-1)
    
        not self.QUIET and print("Loaded "+ str(len(workspace.suites)) + " test suites.")
        not self.QUIET and print("Loaded "+ str(len(workspace.tests)) + " tests.")
        sec = self.DOC_CLAUSE_LVL_2 - 1
    
        spec.add_main_heading(doc_main_tit if doc_main_tit!=None else self.DOC_MAIN_TITLE)
        
        for suite in workspace.suites:
            sec = sec + 1
            subsec = self.DOC_CLAUSE_LVL_4
            print("  Generating test suite: " + str(suite))
            spec.add_sub_heading(str(suite), self.DOC_CLAUSE_LVL_1, sec, self.DOC_CLAUSE_LVL_3, subsec)
            for i in suite.tests:
                gen_test(suite, i, spec, sec, subsec, workspace)
        
        if len(workspace.suites) == 0:
            sec = sec + 1
            subsec = self.DOC_CLAUSE_LVL_4
            suite = str(workspace)
            spec.add_sub_heading(suite, self.DOC_CLAUSE_LVL_1, sec, self.DOC_CLAUSE_LVL_3, subsec)
            for i in workspace.tests:
                gen_test(suite, i, spec, sec, subsec, workspace)
                
        not self.QUIET and print("Saving to: " + doc_fn)
        not self.DRY_RUN and spec.save(doc_fn)
        not self.QUIET and print("Finished.")
    
