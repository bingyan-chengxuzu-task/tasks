<?php
session_start();
require_once "linkDB.php";
$uID=$_GET["uID"];
$sID=$_GET["sID"];
$query_a=mysql_query("SELECT * from user where uID='$sID'");
$row_a=mysql_num_rows($query_a);
if($row_a==0){echo "该用户不存在";exit();}
$query=mysql_query("SELECT * from friend where main_ID='$uID' AND sub_ID='$sID'");
$row=mysql_num_rows($query);
if($row!=0){echo "已成为好友，不能重复添加";exit();}
date_default_timezone_set('PRC');
$now=date('Y-m-d H:i:s',time());
$result=mysql_query("INSERT INTO friend (main_ID,sub_ID,Time) values('$uID','$sID','$now')");
$result_1=mysql_query("INSERT INTO friend (main_ID,sub_ID,Time) values('$sID','$uID','$now')");
if($result||$result_1)
   {
        echo"1314520";
   }
else 
   {
       echo "添加失败，请重试";
   }
?>