<?php
session_start();
require_once "linkDB.php";
$query=mysql_query("SELECT * from message_all");
$result=mysql_num_rows($query);
if($_SESSION['message_all_num']!=$result)
{
$query_1=mysql_query("SELECT * from message_all order by ID DESC limit 1");
$result_1=mysql_fetch_array($query_1);
echo "\r\nID:".$result_1['uID']."【".$result_1['uName']."】:\r\n\t".$result_1['text_content']."(".$result_1['Time'].")\r\n";
$_SESSION['message_all_num']=$result;
}




?>