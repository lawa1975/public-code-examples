#!/bin/bash
# fixed value for SOURCE_DATE_EPOCH prevents different timestamp on every build, so builds on unchanged sources will have same hash
export SOURCE_DATE_EPOCH=0
SHARED_LIB_DIR="$(dirname $0)/.."
cd "$SHARED_LIB_DIR" || exit
pip install -r src/requirements.txt
python -m build
