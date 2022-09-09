#!/bin/bash
#===============================Colors============================================
COLOR_TEXT_BLACK='\033[30m'
COLOR_TEXT_RED='\033[31m' #'\033[31m'
COLOR_TEXT_GREEN='\033[32m'
COLOR_TEXT_YELLOW='\033[33m'
COLOR_TEXT_BLUE='\033[34m'
COLOR_TEXT_VIOLET='\033[35m'
COLOR_TEXT_SKY_BLUE='\033[36m'
COLOR_TEXT_GRAY='\033[37m'

COLOR_BG_BLACK='\033[40m'
COLOR_BG_RED='\033[41m' #'\033[41m'
COLOR_BG_GREEN='\033[42m'
COLOR_BG_YELLOW='\033[43m'
COLOR_BG_BLUE='\033[44m'
COLOR_BG_VIOLET='\033[45m'
COLOR_BG_SKY_BLUE='\033[46m'
COLOR_BG_GRAY='\033[47m'

COLOR_RESET='\033[0m'
#===============================End colors========================================

#===============================Messagers=========================================
MESSAGE_SUCCESSFULLY_COMPLETED="$COLOR_TEXT_GREEN Operation successfully completed!$COLOR_RESET"
MESSAGE_FAILED="$COLOR_TEXT_RED Operation failed!$COLOR_RESET"
#===============================End messagers=====================================

#============================For docker============================================
RUN="docker exec -it"
INTERPRETATOR="python3"
CONTAINER="rishat_django_test_web_1"

RUN_CONTAINER="$RUN $CONTAINER"
MANAGER_PY="$RUN_CONTAINER $INTERPRETATOR manage.py"

DIR_BACKUP="./backup_db/"
DB_PREFIX="db_"
#=============================End for docker=======================================

USE_GULP_FROM_DOCKER=false #not recommended