$T{comment} =~ s/\cM\n/<br>/g;
open FILE,'num.txt';
$num = <FILE>;
close FILE;

open FILE,">num.txt";
print FILE ++$num;
close FILE;

open FILE,">>mess.txt";
print FILE "$num¡ü$T{username}¡ü$T{comment}¡ü$T{x_point}¡ü$T{y_point}¡ü$T{date}¡ü$ENV{REMOTE_ADDR}¡ü$T{time}¡ü$T{seco}\n";
close FILE;

@file = &readfile('mess.txt');
if ($#file > $max_mess - 1) {
	splice(@file,0,$#file - $max_mess + 1);

	open FILE,">mess.txt";
	print FILE @file;
	close FILE;
}

print "<META HTTP-EQUIV=REFRESH CONTENT='0;URL=$cgi_url'>";
exit;