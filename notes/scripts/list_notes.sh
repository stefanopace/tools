find $NOTE_HOME/notes/ -maxdepth 1 -type f -printf '%AY-%Ab-%Ad %Aa %AH:%AM\t%f\n' | sort --reverse
