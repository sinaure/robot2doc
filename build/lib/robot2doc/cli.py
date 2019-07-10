# coding=utf-8

import sys
import argparse
import logging
import textwrap

from robot2doc import executor
from robot2doc.common import logs

LOG = logging.getLogger("CLI")

__header__ = textwrap.dedent("""
  _  _  _   _  _____  ___   _
 | \| || | | ||_   _|/ __| (_)    _ __      __ _     __
 | .` || |_| |  | | | (__  | | _ | '  \  _ / _` | _ / _|
 |_|\_| \___/   |_|  \___| |_|(_)|_|_|_|(_)\__,_|(_)\__|

""")


def get_parser():
    parser = argparse.ArgumentParser(
        prog='robot2doc',
        formatter_class=argparse.RawTextHelpFormatter,
        description='Robot2Doc for python\n\n%s' % __header__,
    )
    
    parser.add_argument("--file", help="Execute robot2doc on this file")
    parser.add_argument("--output_filename", help="Specify output file name file only usage")
    
    parser.add_argument("--directory", help="Execute robot2doc on every file of this directory")
    parser.add_argument("--exclude", help="Exclude files that contains this word")
    parser.add_argument("--output_filename_prefix", help="just add a prefix to the existing file name and strip .robot extension")


    return parser


def main():

    sh = logging.StreamHandler()
    sh.setFormatter(logs.color_format())
    sh.setLevel(logging.WARNING)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(sh)
    sh.setLevel(logging.DEBUG)

    parser = get_parser()
    args = parser.parse_args()

    print(args)
    if args.directory is not None:
       if args.file is not None:
          parser.error('Cannot use file with directory')

    LOG.info(args) 
    executor.main(args)
    

if __name__ == '__main__':
    main()
