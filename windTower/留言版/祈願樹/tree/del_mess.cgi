&error("±K½X¿ù»~") if ($T{username} ne $password);
my @file = &readfile('mess.txt');

open FILE,'>mess.txt';
for (@file) {
	print FILE $_ unless ($_ =~ /^$T{x_point}¡ü(.*)/);
}
close FILE;
print "<META HTTP-EQUIV=REFRESH CONTENT='0;URL=$cgi_url'>";
exit;