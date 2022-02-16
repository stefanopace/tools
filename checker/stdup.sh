SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
eeks -c $SCRIPTPATH/../checker/izi.json -e $SCRIPTPATH/../checker/check.sh
