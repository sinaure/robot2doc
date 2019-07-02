#!/env/python

import config

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
    def __init__(self, text):
        # t = text.encode('ascii')
        self.lines = text.split("\\n")
        self.tp_fields = map(TpField, self.lines)
        self.tp_id = None

        for field in self.tp_fields:
            if field.key == "Test ID":
                self.tp_id = field.value
        
    def __str__(self):
        return str(self.lines)

    def add_to_spec(self, spec, test):
        spec.add_tp(self.tp_fields, test)
        if config.GIT_COMMIT != "":
            spec.add_commit_url(config.GIT_COMMIT)