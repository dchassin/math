#!/usr/bin/python3
"""math [OPTIONS...]

  Process input lines as python math expressions.  If input is a tty,
  then interactive mode is used. For details on math functions, see
  the python `math` module. General math syntax follows python syntax
  conventions, e.g., `2**3` is "2 raised to the power 3".

OPTIONS

  The following command line options are supported:

    -d|--debug            enable debugging traceback output when errors are reported

    -h|--help|help        print this help information

    -s|--silent           disable initial startup information

    -v|--version|version  print the version number

GLOBALS

  The following globals can be used in math expressions:

    answer    list of answers

    copyright copyright statement

    credits   authoring credits

    debug     boolean indicating whether debug is enabled

    history   list of inputs

    license   license agreement

    prompt    interactive input prompt

    version   math version number
"""

import sys

copyright = "Copyright (C) 2021, David P. Chassin"
credits = "Written by David P. Chassin"
version = "0.1.0"
prompt = "math> "
debug = False
answer = []
history = []
license = """
BSD 3-Clause License

Copyright (c) 2021, David P. Chassin
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

if "-h" in sys.argv or "--help" in sys.argv or "help" in sys.argv:
    if sys.stdin.isatty():
        help(__name__)
    else:
        print("Syntax:",__doc__)
    quit(0)

if "-v" in sys.argv or "--version" in sys.argv or "version" in sys.argv:
    print(version)
    quit(0)

if sys.stdin.isatty() and not "-s" in sys.argv and not "--silent" in sys.argv:
    print(f"Math {version}",file=sys.stderr)
    print(f"Python {sys.version}",file=sys.stderr)
    if "-d" in sys.argv or "--debug" in sys.argv:
        debug =True
        print(f"debugging in enabled",file=sys.stderr)

def show_prompt(prompt=prompt,prefix="",end=""):
    if sys.stdin.isatty():
        print(f"{prefix}{prompt}",file=sys.stderr,end=end,flush=True)    

show_prompt(prefix="\n")
from math import *
for line in sys.stdin:
    try:
        code = line.strip()
        result = eval(compile(code,'<string>','eval'),globals())
        if type(result) in [int,float,complex]:
            history.append(code)
            answer.append(result)
        print(result,file=sys.stdout,flush=True,end="\n")
    except:
        e_type, e_value, e_trace = sys.exc_info()
        print(f"ERROR: {e_value}",file=sys.stderr,flush=True)
        if debug:
            from traceback import *
            print(f"TRACEBACK: {e_type}",file=sys.stderr,flush=True)
            print_tb(e_trace,file=sys.stderr)
            print(f"GLOBALS:",file=sys.stderr,flush=True)
            for key, value in globals().items():
                if key != "__builtins__":
                    print(f"{key}={value}",file=sys.stderr,flush=True)
    show_prompt()
