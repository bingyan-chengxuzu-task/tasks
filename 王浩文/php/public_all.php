<?php
session_start();
require_once "linkDB.php";
$text=$_GET["text"];
if(!$text){
echo "不能为空";
exit();
}
$uID=$_GET["uID"];
$nickname=$_GET["nickname"];
date_default_timezone_set('PRC');
$now=date('Y-m-d H:i:s',time());
$result=mysql_query("INSERT INTO message_all (text_content,uID,uName,Time) values('$text','$uID','$nickname','$now')");
if($result)
   {
        echo"1314520";
   }
else 
   {
       echo "发布失败，请重试";
   }
?>