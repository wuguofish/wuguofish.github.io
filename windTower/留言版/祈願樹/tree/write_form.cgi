print<<HTML;
<script>
function return_mess() {
	var d = document.f1;
	if (!d.username.value) {alert("請輸入姓名"); d.username.focus(); return false;}
	if (!d.comment.value) {alert("請輸入留言"); d.comment.focus(); return false;}
	opener.document.f1.username.value = d.username.value;
	opener.document.f1.comment.value = d.comment.value;
	opener.document.f1.job.value='write';
	opener.document.f1.target='_self';
	opener.document.f1.submit();
	window.close();
	return false;
}
</script>
<body onload='document.f1.username.focus();' topmargin="0" leftmargin="0" bgcolor="#FFFFFF">
<form name='f1' onsubmit=return(return_mess());>
<table border=0 cellSpacing=0 cellPadding=3 width='100%' height='100%'  align='center'><tr><td align=center class=t4d>
<table border='0' cellSpacing=0 cellPadding=0 width='100%' height='100%' align='center'  class=t4>
<tr><td  align=\"center\">祈福內容限40個中文字內</td></tr>
<tr>
<td align=\"center\">祈福者: <input name='username' maxlength=\"8\" size=12></td></tr>
<tr><td align=\"center\" >
<input type="text" name='comment' size="25" maxlength="40"  value=請寫出您的希望!></td></tr>
<tr><td align=\"center\"><input type='submit' value='美夢成真' class=bot>**<input type='reset' value='尚無願望' class=bot></tr>
</table>

</form>
</body></html>
<noscript><!--#echo banner=""--></noscript>
HTML

exit;