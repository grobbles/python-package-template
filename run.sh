#!/bin/bash

############################################################################################################
## Constant Block
PACKAGE_NAME="python-package-template"

############################################################################################################
## Description Function Block
function usage {
cat << EOF

Usage: $0 <arguments>

Arguments:
    -h | --help         : print the help description

    -b | --build        : build the python package

    -i | --install      : install the package to your system

    -u | --uninstall    : uninstall the package from your system

    -c | --cleanProject : clean the project

EOF
}

############################################################################################################
## Start Function Block
function build(){
    cd src
    python3 setup.py sdist bdist_wheel
    cd ..
}

function install(){
    pip3 install dist/$PACKAGE_NAME-*.tar.gz
}

function uninstall(){
    pip3 uninstall -y $PACKAGE_NAME
}

function cleanProject(){
    # remove python cache
    find . -name ".pytest_cache" -type d -exec rm -rf "{}" \;
    find . -name "__pycache__" -type d -exec rm -rf "{}" \;

    # remove python package stuff
    find . -name "build" -type d -exec rm -rf "{}" \;
    find . -name "dist" -type d -exec rm -rf "{}" \;
    find . -name "*.egg-info" -type d -exec rm -rf "{}" \;

    # remove test output and log files
    find ./tests/ -name "testOutput" -type d -exec rm -rf "{}" \;
    find ./tests/ -name "resources" -type d -exec rm -rf "{}" \;
}

############################################################################################################
## Start Main Block
case "$1" in
    -b | --build)
            echo "build the python package"
            build
            exit $?
        ;;

    -c | --cleanProject)
            echo "clean the project"
            cleanProject
            exit $?
        ;;

    -i | --install)
            echo "install the package"
            install
            exit $?
        ;;

    -u | --uninstall)
            echo "uninstall the project"
            uninstall
            exit $?
        ;;

    -h | --help | *)
            usage
            exit $?
        ;;
        
esac
## End Main Block
############################################################################################################