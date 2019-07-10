#!/env/python

from robot2doc import config
from robot2doc import testspec

class TpField():
    '''
    Describe a field in a Test Purpose, via its key and value
    '''
    def __init__(self, text):
        split = text.split(":")
        if len(split) > 1:
            self.key = split[0].strip()
            self.value = split[1].strip()
        else:
            self.key = ""
            self.value = split[0].strip()

class TP():
    '''
    Defines a test purpose. The constructor parses a set of lines
    with key value pairs, each separated by ":".
    '''
    def __init__(self, text : str):
        # t = text.encode('ascii')
        self.lines = text.split("\\n")
        self.tp_fields = [TpField(l) for l in self.lines]
        self.tp_id = None

        for field in self.tp_fields:
            if field.key == "Test ID":
                self.tp_id = field.value
        
    def __str__(self):
        return str(self.lines)

    def add_to_spec(self, spec : testspec.TestSpec, testbehaviour: str, robot_file : str):
        '''
        Given a Test Spec, executes the addition of the this TP in the document.
        '''
        spec.add_tp(self.tp_fields, testbehaviour)
        if config.GIT_COMMIT_PREFIX != "":
            spec.add_commit_url(config.GIT_COMMIT_PREFIX, robot_file)