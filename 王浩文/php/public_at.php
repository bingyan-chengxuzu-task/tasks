<?php
session_start();
require_once "linkDB.php";
$uID=$_GET["uID"];
$toID=$_GET["toID"];
$text=$_GET["totext"];
if(!$text){
echo "不能为空";
exit();
}
$nickname=$_GET["nickname"];
date_default_timezone_set('PRC');
$now=date('Y-m-d H:i:s',time());
$result=mysql_query("INSERT INTO message_at (main_ID,sub_ID,text_a,Time) values('$uID','$toID','$text','$now')");
$result_a=mysql_query("INSERT INTO message_at (main_ID,sub_ID,text_a,Time) values('$toID','$uID','$text','$now')");
if($result||$result_a)
   {
        echo"1314520";
   }
else 
   {
       echo "发布失败，请重试";
   }
?>