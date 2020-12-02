<?php
$chosen = explode(' ', $argv[1]);
$list = explode("\n", file_get_contents(__DIR__ . '/list.txt'));
foreach ($list as $item) {
	if (in_array($item, $chosen)){
		echo "\e[7m$item\e[0m\n";
	} else {
		echo "$item\n";
	}
}
