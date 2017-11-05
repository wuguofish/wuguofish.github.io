my @file = &readfile("mess.txt");

for (@file) {
	($num,$username,$comment,$x_point,$y_point,$date,$ip,$time) = split/¡ü/;
	last if ($T{num} == $num);
}
print<<HTML;
<BODY bgcolor="#FFFFFF" topmargin="0" leftmargin="0">
<table border='0' cellpadding='5' cellspacing='0' width='153' height='207' align='center' class=t4d>
<tr>
<td height="25" class=sha><img src="tree/heart03.gif" border=0>&nbsp;¬èÄ@ªÌ: <b>$username</b></td></tr>
<tr><td align='center'>
<table width="130" cellpadding='0' height='100%' cellspacing='5'  class=t4 style="table-layout:fixed"><tr> 
<td width="130" class=sha valign=top style="word-wrap:break-word">$comment</td></tr></table>
</td></tr>
<tr><td align="right" height='18' class=sha>$date<BR>$time</td></tr>
</table></HTML>
HTML
exit;