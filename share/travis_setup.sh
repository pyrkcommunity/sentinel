#!/bin/bash
set -evx

mkdir ~/.zeroonecore

# safety check
if [ ! -f ~/.zeroonecore/zeroone.conf ]; then
  cp share/zeroone.conf.example ~/.zeroonecore/zeroone.conf
fi
