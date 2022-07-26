#!/bin/bash
uname -a
echo "======================"
code --version
echo "======================"
python --version
echo "======================"
code --list-extensions --show-versions | grep ms-python
echo "======================"
pyright --version
pyright --verbose test.py