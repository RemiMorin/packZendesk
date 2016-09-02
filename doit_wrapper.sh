#!/bin/bash
usage="$(basename "$0") [-h] [-i] [-t <TASK>]
Description: create a virtual environment for development

Usage:
    -h      help
    -i      install a virtual environment from conf/virtual_env.conf
    -t      run doit wrapper with a task

More:
    To delete a virtual environment : delete it from the installation directory
        i.e.     rm -rf ~/.virtualenvs/<NAME>"

T1=$(date +%s)
source conf/virtual_env.conf
INSTALL_VIRTUAL_ENV=false
TASK=list
TASK_DEFINED=false

while getopts ':hit:' option; do
    case "$option" in
        h|\?) echo "$usage"
            exit 0
            ;;
        i) INSTALL_VIRTUAL_ENV=true >&2
            ;;
        t) TASK=$OPTARG >&2
           TASK_DEFINED=true
            ;;
        :) printf "missing argument for -%s\n" "$OPTARG" >&2
            echo "$usage" >&2
            exit 1
            ;;
    esac
done

shift $((OPTIND - 1))

#process instalation if -i
if $INSTALL_VIRTUAL_ENV; then

    echo "----------------------------------------"
    echo "  creating a virtual environment"
    echo "----------------------------------------"
    echo "  Virtual environement name       : $VIRTUAL_ENV_NAME"
    echo "  Virtual environement location   : $VIRTUAL_ENV_PATH"
    echo "  Using python interpreter        : $PYTHON_BIN"
    echo "  Using virtualenv executor       : $VIRTUAL_ENV_BIN/virtualenv"
    echo "----------------------------------------"
    if [ ! -d "$VIRTUAL_ENV_PATH/$VIRTUAL_ENV_NAME" ]; then
        $VIRTUAL_ENV_BIN/virtualenv -q -p  $PYTHON_BIN --no-site-packages $VIRTUAL_ENV_PATH/$VIRTUAL_ENV_NAME
        echo -e "  Creation status                 : \033[0;32mCREATED\033[0m"
        else
             echo -e "  Creation status                 : \033[0;31mALREADY EXIST\033[0m"
    fi

    echo " "
    echo "  Installing requirements"
    echo "----------------------------------------"
    echo " "
    source $VIRTUAL_ENV_PATH/$VIRTUAL_ENV_NAME/bin/activate
    pip install pip --upgrade
    grep -v $VIRTUAL_ENV_NAME== requirements.txt | pip install -r /dev/stdin -r tests.req

    echo " "
    echo "----------------------------------------"
    echo -e "  Installing requirements : \033[0;32mOK\033[0m"
    echo "----------------------------------------"
    echo " "

fi

if [ ! -d "$VIRTUAL_ENV_PATH/$VIRTUAL_ENV_NAME" ]; then
    echo -e "  \033[0;31mERROR\033[0m virtual environment doesn't exists

        ./$(basename "$0") -i
    "
    exit 0
fi

source $VIRTUAL_ENV_PATH/$VIRTUAL_ENV_NAME/bin/activate

if $TASK_DEFINED; then
    echo "  Running 'doit' task(s)"
    echo "----------------------------------------"
    else
       echo "  No task defined

         Try with one of the following as -t <TASK>

         Tasks                         Description
------------------------------------------------------------------"
fi

doit $TASK

if $TASK_DEFINED; then
    echo "----------------------------------------"
    echo -e "  Running 'doit' task(s) : \033[0;32mOK\033[0m"
    T2=$(date +%s)
    diffsec="$(expr $T2 - $T1)"
    echo "----------------------------------------"
    echo " "
    echo | awk -v D=$diffsec '{printf "  Execution took : %d second(s) \n",D%60, D}'
fi
