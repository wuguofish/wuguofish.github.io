#!/usr/local/bin/perl
#########################################################
#程式作者	《JL》					#
#版面作者	《bbc》					#
#作者信箱	《jl@830.com.tw》			#
#作者網站	《http://jl.830.com.tw》		#
#完成日期	《2001年10月4日》			#
#程式名稱	《Dream BlackBorder》			#
#程式版本	《V1.0》				#
#使用範圍	《免費用途》				#
#########################################################
$cgi_url	= 'bb.cgi';		 # 程式檔案名稱
$web_admin	= '《&nbsp;祈願風鈴樹，先將左邊的風鈴拖到你要吊放的位置，再進行祈願內容填寫即可完成。';	 # 程式管理人員:風靈兒
$password	= '1378246590';		 # 程式管理密碼
$max_mess	= 50;	 # 留言最大筆數
#########################################################
$| = 1;
@querys = split(/&/, $ENV{'QUERY_STRING'});
for (@querys) {
   ($name, $value) = split/=/;
   $T{$name} = $value;
}

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
for (@pairs) {
   ($name, $value) = split/=/;
   $value =~ tr/+/ /;
   $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
   $T{$name} = $value;
}

$time_miss ='+0'; #時差調整(±小時)
$min_miss ='0'; #分差調整(±分鐘)
($sec,$min,$hour,$day,$mon,$year,$wday,$isdst) = localtime(time+(3600*$time_miss)+(60*$min_miss));
$mon=$mon+1;
$year=$year-11;
if ($mon<10) {$mon="0$mon";}
if ($day<10) {$day="0$day";}
if ($hour<10) {$hour="0$hour";}
if ($min<10) {$min="0$min";}
if ($sec<10) {$sec="0$sec";}
$T{date} = "$year年$mon月$day日";
$T{time} = "$hour點$min分";
$T{seco} = "$sec";
#########################################################

print "Content-type: text/html;CHARSET=big5\n";
print "Pragma:no-cache\n\n";
print "<HTML><HEAD><TITLE>$title</TITLE><meta http-equiv=\"Content-Type\" content=\"text/html; charset=big5\">\n";
print "<meta http-equiv=\"Content-Language\" content=\"zh-tw\"><link rel=\"stylesheet\" type=\"text/css\" href=\"bb.css\"></HEAD>\n";
if ($T{job}) {do "$T{job}.cgi";}
else {
	my @file = &readfile("bb.html");
	my @mess = &readfile('mess.txt');

	for (@file) {
		if ($_ =~ /<!--script_list-->/) {
			for (@mess) {
				$_ =~ s/\n//g;
				($num,$username,$comment,$x_point,$y_point,$date,$ip,$time,$seco) = split/∥/;
				print "\t\t\tif ((z.style.pixelLeft + 10 >= $y_point && z.style.pixelLeft - 10 <= $y_point) && (z.style.pixelTop + 10 >= $x_point && z.style.pixelTop - 10 <= $x_point)) if (confirm('您確定要摘除 [$username] 的\許\願\紙嗎?')) {Point('$num');} else {z.style.pixelLeft = temp1; z.style.pixelTop = temp2;}\n";
				
			}
		}
		elsif ($_ =~ /<!--div_list-->/) {
			for (@mess) {
				$_ =~ s/\n//g;
				($num,$username,$comment,$x_point,$y_point,$date,$ip,$time,$seco) = split/∥/;
				print "<div style='position:absolute; left:$y_point px; top:$x_point px;'>\n";
				print "<table border='0' cellpadding='2' cellspacing='2'><tr><td align=center><table border=0 width=100% cellpadding='2' cellspacing='2' class=t4dd><tr><td align=center class=t4w><span style=cursor:help  onclick='window.open(\"$cgi_url?job=look&num=$num\",\"mess\",\"width=153,height=207,resizable=no,status=no,scrollbars=no,menubar=no\");'><FONT COLOR=#ffffff><!---留言者姓名$username--->$username</FONT></td></tr></table></td></tr><tr><td align=center><IMG SRC=tree/$seco.gif ALT=$username-$date的願望></span></td></tr></table>\n";
				print "</div>\n";
				
			}
		}
		elsif ($_ =~ /<!--div_list1-->/) {
			for (@mess) {
				$_ =~ s/\n//g;
				($num,$username,$comment,$x_point,$y_point,$date,$ip,$time,$seco) = split/∥/;
print "<FONT SIZE=2><FONT COLOR=#009900>【<b>$username</b>】</FONT>的願望<FONT COLOR=#ff0000>《</FONT><FONT COLOR=#aa33aa>$comment</FONT><FONT COLOR=#ff0000>》</FONT>($year/$mon/$day)\n";
				print "<BR>\n";
				
			}
		}
		else {
			$_ =~ s/\$cgi_url/$cgi_url/g;
			$_ =~ s/\$web_admin/$web_admin/g;
			print $_;
		}
	}
}

print "</HTML>\n";
print "<noscript><!--#echo banner=\"\"--></noscript>\n";
#########################################################
sub error {
print<<HTML;
<script>
alert("$_[0]");
history.back();
</script>
HTML
exit;
}
#########################################################
sub readfile {
	open FILE,$_[0];
	my @FILE=<FILE>;
	close FILE;
	return @FILE;
}