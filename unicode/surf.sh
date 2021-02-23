HOME_PATH="$(dirname $(which $0))"
cat=$(python3 ${HOME_PATH}/print.py -n | fzf --preview "python3 ${HOME_PATH}/print.py -c {}")
if [ -z "$cat" ]; then
	exit 0
fi
python3 ${HOME_PATH}/print.py -c "$cat"
