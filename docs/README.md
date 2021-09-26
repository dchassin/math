[[/README]] - math command syntax

SYNOPSIS

  math [OPTIONS...]

DESCRIPTION

  Process input lines as python math expressions.  If input is a tty,
  then interactive mode is used.

OPTIONS

  The following command line options are supported:

    -d|--debug       enable debugging traceback output when errors are reported

    -h|--help|help   print this help information

    -s|--silent      disable initial startup information

GLOBALS

  The following globals can be used in math expressions:

    answer    list of answers

    debug     boolean indicating whether debug is enabled

    history   list of inputs

    prompt    interactive input prompt

    version   math version number
    