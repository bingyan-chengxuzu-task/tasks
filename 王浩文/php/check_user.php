<?php
header("Content-Type: text/html;charset=utf-8");
require_once "linkDB.php";
$uName=$_GET["u"];
$query=mysql_query("SELECT * from user where uName='$uName'");
if(strpbrk($uName,"<>~`!@#$%^&*()_+-=\][{}|';:\",./?【】、；’：“，。、？")){echo "非法字符";exit;}
$row=mysql_num_rows($query);
if($uName==null)
            echo "不能为空";
else if($row!=0)
            echo "用户名已存在";
else 
            echo "√";
?>
