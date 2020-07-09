mix test
mix escript.build

echo "echo \"1 2 3 4\" | ./ex_wordn "
echo "[1]1 [2]2 [3]3 [4]4"
echo "1 2 3 4" | ./ex_wordn
echo
echo "echo \"1#2#3#4\" | ./ex_wordn --separator \"#\""
echo "[1]1 [2]2 [3]3 [4]4"
echo "1#2#3#4" | ./ex_wordn --separator "#"
echo
echo "echo \"1#2#3#4\" | ./ex_wordn 2 3 --separator \"#\""
echo "2 3"
echo "1#2#3#4" | ./ex_wordn 2 3 --separator "#"
echo
echo "echo \"1#2#3#4\" | ./ex_wordn -s \"#\""
echo "[1]1 [2]2 [3]3 [4]4"
echo "1#2#3#4" | ./ex_wordn -s "#"
echo
echo "echo \"1 2 3 4\" | ./ex_wordn 2 4 "
echo "2 4"
echo "1 2 3 4" | ./ex_wordn 2 4
echo
echo "echo \"1 2 3 4\" | ./ex_wordn --delete 2 4 "
echo "1 3"
echo "1 2 3 4" | ./ex_wordn --delete 2 4
echo
echo "echo \"1|2|3|4\" | ./ex_wordn --delete 2 4 --separator \"|\""
echo "1 3"
echo "1|2|3|4" | ./ex_wordn --delete 2 4 --separator "|"
echo
echo "echo \"1|2|3|4\" | ./ex_wordn --separator \"|\" --delete 2 4"
echo "1 3"
echo "1|2|3|4" | ./ex_wordn --separator "|" --delete 2 4
echo
echo "echo \"1 2 3 4\" | ./ex_wordn -d 2 4 "
echo "1 3"
echo "1 2 3 4" | ./ex_wordn -d 2 4
echo
