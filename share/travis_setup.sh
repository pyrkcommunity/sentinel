#!/bin/bash
set -evx

mkdir ~/.pyrk

# safety check
if [ ! -f ~/.pyrk/pyrk.conf ]; then
  cp share/pyrk.conf.example ~/.pyrk/pyrk.conf
fi
