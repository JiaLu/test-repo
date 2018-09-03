#!/bin/bash
#if hbsiotapp and initialized flag file are both NOT exist
#then start to get initial app file from local FTP server
#TODO: check the hbsiot service is up or not.
HBSIOTAPP=/opt/hbs/bin/hbsiotapp
HBSIOTAPP_INSTALLED_FILE=/tmp/hif
FTP_HOST=127.0.0.1
FTP_USER=roka
FTP_PASS=imlujia100
INSTALLER=/installer.tar.gz
CURL_CMD=`which curl`
TAR_CMD=`which tar`

if [ -e ${HBSIOTAPP} ] && [ -e ${HBSIOTAPP_INSTALLED_FILE} ];then
  echo "INSTALLED!!"
  exit
else
  echo "NOT INSTALLED!"
  #Get installer
  cd /tmp/
  ${CURL_CMD} -u ${FTP_USER}:${FTP_PASS} -O ftp://${FTP_HOST}${INSTALLER}
  #Uncompress
  ${TAR_CMD} xvzf ${INSTALLER}
  #Post process

fi
