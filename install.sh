#!/bin/bash

function error()
{
    RC=$1
    shift 1
    echo "ERROR: $1" >/dev/stderr
    exit $RC
}

function warning()
{
    echo "WARNING: $1" >/dev/stderr
}

if [ -z "$(which uname)" ]; then
    error 1 "unable to identify system (uname not found); please use manual installation"
fi

SYSTEM=$(uname -s)

case $SYSTEM in

    Darwin)
        curl -sL https://raw.githubusercontent.com/dchassin/math/master/src/math.py > /usr/local/bin/math
        chmod +x /usr/local/bin/math
        ;;

    *)
        error 1 "not script available for $SYSTEM systems; please use manual installation"
        ;;
esac

if [ -z "$(which math)" ]; then 
    warning "installation folder not in current path; use 'export PATH=/usr/local/bin:\$PATH' to find math"
else
    echo "Math $(math version) installed ok"
    echo "Type 'math license' to read the license agreement"
fi
