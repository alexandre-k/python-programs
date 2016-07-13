import os
import argparse
from collections import ChainMap

defaults = {'SHELL': '/bin/bash'}

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--shell')
namespace = parser.parse_args([])
command_line_args = {k:v for k,v in vars(namespace).items() if v}


d = ChainMap(command_line_args, os.environ, defaults)
d.update(command_line_args)
