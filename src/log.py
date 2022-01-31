#!/usr/bin/env python3

import argparse
import datetime
import pathlib
import subprocess
import sys
import typing

class CmdLineParser:
    def __init__(self):

        self.parser = argparse.ArgumentParser(description="Log versions of installed software.")

        self.parser.add_argument(
            "-o", "--output", type=pathlib.Path, help="Outputfile.", required=False, default="installed_software.txt"
        )

    def parse(self) -> typing.Tuple[argparse.Namespace, typing.List]:

        return self.parser.parse_known_args(args=sys.argv[1:])

def exist_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None

def exist_env_variable(name):
    from os import getenv
    return getenv(name) is not None

def run_command(args, output_file):
    output_file.write('====== Output of command \'')
    output_file.write(" ".join(args))
    output_file.write("\':\n")
    output_file.flush()
    subprocess.run(args, stdout=output_file, stderr=subprocess.DEVNULL)
    output_file.flush()


if __name__ == "__main__":
    # Parse command line
    args, extra_args = CmdLineParser().parse()
    version = "0.0.1"

    output_file = open(args.output, "w")

    # Header
    output_file.write('=== File creation with log-installed-software ver %s started at %s.\n' %  (version, datetime.datetime.now()))
    output_file.flush()

    # Dump apt packages if apt exists
    if (exist_tool("apt")):
        run_command(['apt', 'list', '--installed'], output_file)

    # Dump conda packages if we are in a conda environment
    if (exist_env_variable("CONDA_PREFIX")):
        run_command(['conda', 'info'], output_file)
        run_command(['conda', 'list'], output_file)

    # Dump pip packages if pip exists
    if (exist_tool("pip")):
        run_command(['pip', 'list', '--verbose'], output_file)

    # Dump brew packages if brew exists
    if (exist_tool("brew")):
        run_command(['brew', 'list'], output_file)
        run_command(['brew', 'list', '--cask'], output_file)

    # Footer
    output_file.write('=== File creation with log-installed-software ver %s ended at %s.\n' %  (version, datetime.datetime.now()))
    output_file.flush()
