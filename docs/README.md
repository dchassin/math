[[/README]] - math command syntax

# Synopsis

  math [OPTIONS...]

  Process input lines as python math expressions.  If input is a tty,
  then interactive mode is used. For details on math functions, see
  the python `math` module. General math syntax follows python syntax
  conventions, e.g., `2**3` is "2 raised to the power 3".

# Options

  The following command line options are supported:

    --copyright|copyright   print the copyright

    --credits|credits       print the credits

    -d|--debug              enable debugging traceback output when errors are reported

    -h|--help|help          print this help information

    --license|license       print the license

    -s|--silent             disable initial startup information

    -v|--version|version    print the version number

# Global

  The following globals can be used in math expressions:

    answer    list of answers

    copyright copyright statement

    credits   authoring credits

    debug     boolean indicating whether debug is enabled

    history   list of inputs

    license   license agreement

    prompt    interactive input prompt

    version   math version number