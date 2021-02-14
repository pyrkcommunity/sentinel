#!/bin/bash
set -evx

mkdir ~/.pyrkcore

# safety check
if [ ! -f ~/.pyrkcore/.pyrk.conf ]; then
  cp share/pyrk.conf.example ~/.pyrkcore/pyrk.conf
fi
