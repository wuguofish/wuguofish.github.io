
風鈴樹祈願版

###########################
#程式作者	《JL》					#
#版面作者	《bbc》					#
#作者信箱	《jl@830.com.tw》			#
#作者網站	《http://jl.830.com.tw》		#
#完成日期	《2001年10月4日》			#
#程式名稱	《Dream BlackBorder》		#
#程式版本	《V1.0》				        #
#使用範圍	《免費用途》				#
###########################

######################################

版面編修美化 《 R's Studio~麗塔小窩   http://www.fan.idv.tw  》

######################################

上傳檔案

    cgi-bin/
	 |
	 |-- tree 755 or 777
	   |
	   |-- bb.cgi  (755)
	   |-- bb.css  (644)
	   |-- bb.html  (644)
	   |-- del_mess.cgi  (755)
	   |-- index.htm  (644)
	   |-- look.cgi  (755)
	   |-- mess.txt   (666)  訪客祈願儲存檔
	   |-- num.txt   (666)  計算訪客祈願的總數量
	   |-- write.cgi  (755)
	   |-- write_form.cgi  (755)

	   |-- tree (圖檔資料夾)


修改設定

bb.cgi

第一行
#!/usr/local/bin/perl
請修改為你主機設定的perl,如果不清楚可以詢問主機的管理者

第12行 (這個不需要做更改)
$cgi_url	= 'bb.cgi';		 # 程式檔案名稱


第13行 (設定在祈願版上方的管理者公告)
$web_admin	= '《&nbsp;祈願風鈴樹，先將左邊的風鈴拖到你要吊放的位置，再進行祈願內容填寫即可完成。';	 # 程式管理人員


第14行 設定管理者密碼,此密碼可以刪除訪客祈願條的
$password	= '0123';		 # 程式管理密碼


第15行  設定最大的留言數量,當數量超過時,舊的祈願條會被新的蓋過
$max_mess	= 50;	 # 留言最大筆數


PS....風鈴祈願樹因為版面容易有狀況
所以利用iframe的語法將他框住

請連結  wish_tree.htm 的頁面來執行程式