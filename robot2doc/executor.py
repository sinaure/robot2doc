# coding=utf-8

import sys
import logging
import datetime

LOG = logging.getLogger("Executor")


class Executor():
    def __init__(self, **kwargs):
        super(Executor, self).__init__()

        self.kwargs = kwargs
        self.directory = self.kwargs['directory'] if 'directory' in self.kwargs else None
        self.exclude = self.kwargs['exclude'] if 'exclude' in self.kwargs else None
        self.file = self.kwargs['file'] if 'file' in self.kwargs else None
        
        if self.directory == None &  self.file != None:
            LOG.info("absolute path file: " % self.file)
        if self.directory != None:
            LOG.info("absolute path directory: " % self.directory)
            if self.exclude != None:
                LOG.info("exclude file if name contain: " % self.exclude)
            


def main(args):
    try:
        LOG.info("Executing robotToDoc on: ".format(args.file, args.filename, args.directory, args.exclude))
        executor = Executor(
            file=args.file,
            directory=args.directory,
            exclude=args.exclude,
        )
    except Exception as e:
        LOG.error("%s" % (e.__str__()))
        sys.exit()
