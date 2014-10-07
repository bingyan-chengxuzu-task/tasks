<?php
session_start();
require_once "linkDB.php";
$username=$_GET["u"];
if(strpbrk($username,"<>~`!@#$%^&*()+-=\][{}|';:\",./?【】、；’：“，。、？")){echo "用户名非法";exit;}
$password=$_GET["p"];
if(strpbrk($password,"<>~`!@#$%^&*()+-=\][{}|';:\",./?【】、；’：“，。、？")){echo "密码非法";exit;}
$nickname=$_GET["nn"];
if(strpbrk($nickname,"<>~`!@#$%^&*()+-=\][{}|';:\",./?【】、；’：“，。、？")){echo "昵称非法";exit;}
$realname=$_GET["rn"];
if(strpbrk($realname,"<>~`!@#$%^&*()+-=\][{}|';:\",./?【】、；’：“，。、？")){echo "姓名非法";exit;}
$mail=$_GET["m"];
if(strpbrk($mail,"<>~`#$%^&*()][{}|'\",?【】、；’：“，。、？")){echo "邮箱非法";exit;}
$age=$_GET["a"];
$sex=$_GET["s"];
date_default_timezone_set('PRC');
$now=date('Y-m-d H:i:s',time());

$result=mysql_query("INSERT INTO user (uName,uPassWord,uSex,uNickName,uRealName,uMail,uAge,Time) 
  values('$username','$password','$sex','$nickname','$realname','$mail','$age','$now')");
if($result)
   {
        echo"15527281213";
   }
else 
   {
       echo "注册失败，请重试";
   }
?>