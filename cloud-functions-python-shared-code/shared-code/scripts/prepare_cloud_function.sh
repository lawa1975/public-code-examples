#!/bin/bash
# parameter 1: name of the shared lib package file
# parameter 2: path to cloud function source folder
SCRIPT_DIR=$(dirname "$0")
# copy built whl package from shared lib folder into cloud function source folder
mkdir -p "$2/dist"
cp -f "$SCRIPT_DIR/../dist/$1" "$2/dist"
# overwrite local shared lib dependency in existing requirements.txt with package dependency for deployment
cp -f "$SCRIPT_DIR/../templates/requirements.deploy.txt" "$2/requirements.txt"
# calculate hashes for shared lib package and base requirements file
SHARED_LIB_HASH=$(sha256sum "$2/dist/$1" | cut -d ' ' -f 1)
REQUIREMENTS_BASE_HASH=$(sha256sum "$2/requirements.base.txt" | cut -d ' ' -f 1)
# append hashes as comment line to requirements.txt
echo -e "\n# $SHARED_LIB_HASH $REQUIREMENTS_BASE_HASH" >> "$2/requirements.txt"
