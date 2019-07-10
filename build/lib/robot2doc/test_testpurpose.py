'''
Tests for testpurpose.py
'''

import testpurpose

def test_create_tp():
    '''
    Test creation of a TP object
    '''
    tp_doc = ''' Test ID: X.Y.Z.Y.W\\n\
    Title: my title\\n\
    something: more'''

    tp = testpurpose.TP(tp_doc)

    assert(tp.tp_id.strip() == "X.Y.Z.Y.W")
    assert(len(tp.tp_fields) == 3)


def test_create_tp_with_no_id():
    '''
    Test creation of a TP object with no TP object
    '''
    tp_doc = ''' Test suite: My suite\\n\
    Title: my title\\n\
    something: more'''

    tp = testpurpose.TP(tp_doc)

    assert(tp.tp_id == None)
    assert(len(tp.tp_fields) == 3)

