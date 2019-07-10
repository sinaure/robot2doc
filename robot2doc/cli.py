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
    dir = parser.add_usage_group()
    onlyonefile = parser.add_usage_group()
    
    onlyonefile.add_argument("--file", help="Execute robot2doc on this file")
    dir.add_argument("--directory", help="Execute robot2doc on every file of this directory")
    dir.add_argument("--exclude", help="Exclude files that contains this word")

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

    LOG.info(args) 
    executor.main(args)
    

if __name__ == '__main__':
    main()
