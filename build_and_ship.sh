#!/bin/bash -xe

SCRIPT_DIR=$(dirname $(readlink -e $0))
BUILD_DIR=$(readlink -e $SCRIPT_DIR/../covid_build)
BASE_NAME=$(cat $SCRIPT_DIR/html_path_prefix.txt)
BASE_NAME=${BASE_NAME#/}
SSH_HOST=webserv@192.168.13.11
TARBALL_DEST=/var/www/vhosts/www.dericnet.com

cd $SCRIPT_DIR/website
which pipenv
VENV_DIR=$(pipenv --venv)

pipenv run make clean
#export SPHINXOPTS="-v -v"
pipenv run make html

cd $BUILD_DIR

mv html $BASE_NAME

# if there are any arguments, just build, don't ship
if [ $# -gt 0 ]; then
    exit 0
fi

tar czf $BASE_NAME.tar.gz $BASE_NAME
scp $BASE_NAME.tar.gz $SSH_HOST:$TARBALL_DEST
ssh $SSH_HOST "cd $TARBALL_DEST; rm -rf $BASE_NAME; tar xzf $BASE_NAME.tar.gz; rm $BASE_NAME.tar.gz"
