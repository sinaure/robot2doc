# coding=utf-8

import sys
import logging
import datetime
from robot2doc import generator

LOG = logging.getLogger("Executor")


class Executor():
    def __init__(self, **kwargs):
        
        self.kwargs = kwargs
        self.directory = self.kwargs['directory'] if 'directory' in self.kwargs else None
        self.exclude = self.kwargs['exclude'] if 'exclude' in self.kwargs else None
        self.output_filename_prefix = self.kwargs['output_filename_prefix'] if 'output_filename_prefix' in self.kwargs else None
       
        
        self.output_filename = self.kwargs['output_filename'] if 'output_filename' in self.kwargs else None
        self.file = self.kwargs['file'] if 'file' in self.kwargs else None
        
        LOG.info("******Executor before generator")
        
        if self.directory == None and  self.file != None:
            LOG.info("absolute path file: " + self.file)
            generator.main(
                file=self.file, 
                output=self.output_filename
                )
        if self.directory != None:
            LOG.info("absolute path directory: " + self.directory)
            for filename in os.listdir(self.directory):
                if filename.endswith(".robot"): 
                    prefix = self.output_filename_prefix  if self.output_filename_prefix != None else "" 
                    out_fn = prefix + os.path.splitext(filename)[0] + ".docx"
                    generator.main(
                        os.path.join(directory, filename), 
                        out_fn,
                        )
                continue
            if self.exclude != None:
                LOG.info("exclude file if name contain: " + self.exclude)
            


    def run(self,file,outputFileName,exclude=None):
        
        LOG.info("Executor*****  : inside run method")
        if exclude != None:
            if exclude not in file:
                gen.gen_doc(file, outputFileName)  
        else:
            gen.gen_doc(file, outputFileName)
 

def main(args):
        try:
            LOG.info("****Executor main method")
            executor = Executor(
                file=args.file,
                directory=args.directory,
                exclude=args.exclude,
                output_filename_prefix=args.output_filename_prefix,
                output_filename=args.output_filename,
            )
        except Exception as e:
            LOG.error("%s" % (e.__str__()))
            sys.exit()