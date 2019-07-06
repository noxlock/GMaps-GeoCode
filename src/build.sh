#!/bin/sh

pyinstaller geocode.py --clean -F

rm -R ./build/
