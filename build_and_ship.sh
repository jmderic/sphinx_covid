#!/bin/bash -xe

SCRIPT_DIR=$(dirname $(readlink -e $0))
BUILD_DIR=$(readlink -e $SCRIPT_DIR/../covid_build)
BASE_NAME=$(sed -ne "s|^    'html_path_prefix' : '/\(.*\)',|\1|p" website/conf.py)
SSH_HOST=webserv@192.168.13.11
TARBALL_DEST=/var/www/vhosts/www.dericnet.com

cd $SCRIPT_DIR/website
which pipenv
VENV_DIR=$(pipenv --venv)

pipenv run make clean
pipenv run make html

cd $BUILD_DIR

mv html $BASE_NAME
tar czf $BASE_NAME.tar.gz $BASE_NAME

scp $BASE_NAME.tar.gz $SSH_HOST:$TARBALL_DEST
ssh $SSH_HOST "cd $TARBALL_DEST; rm -rf $BASE_NAME; tar xzf $BASE_NAME.tar.gz; rm $BASE_NAME.tar.gz"
