'''
Main tests for robot2doc
'''
import os

from zipfile import is_zipfile

import docx

from testspec import TestSpec
from main import BASE_SPEC

def test_doc_present():
    assert os.path.isfile(BASE_SPEC)

def test_open_doc_main_nofile():
    TestSpec()

def test_open_doc_docx():
    docx.Document(BASE_SPEC)

def test_is_zipfile():
    assert is_zipfile(BASE_SPEC)

def dont_test_open_doc_main():
    TestSpec(BASE_SPEC)
