cd $NOTE_HOME/scripts

if [ "$1" ]; then
	touch ../notes/"$1"
	vim ../notes/"$1"
	exit 0
fi;

selected="$($NOTE_HOME/scripts/list_notes.sh | fzf --reverse --height 15 --border --no-info)"

if [ -z $selected ]; then
	exit 0
fi;

filename="$(echo "${selected}" | sed -E "s/[^\t]*\t(.*)/\1/")"

vim "$NOTE_HOME/notes/$filename"
