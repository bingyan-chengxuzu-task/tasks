<?php
session_start();
require_once "linkDB.php";
$uName=$_GET["uName"];
$PassWord=$_GET["PassWord"];
if(strpbrk($uName,"<>~`!@#$%^&*()_+-=\][{}|';:\",./?【】、；’：“，。、？")){echo "用户名有非法字符";exit;}
if(strpbrk($PassWord,"<>~`!@#$%^&*()_+-=\][{}|';:\",./?【】、；’：“，。、？")){echo "密码含有非法字符";exit;}
$query=mysql_query("SELECT * from user where uName='$uName'");
$result=mysql_fetch_array($query);
if($result)
{
	if($PassWord==$result['uPassword'])
	{
		 $_SESSION['uID'] = $result['uID'];
		 $_SESSION['username'] = $uName;
		 if($result['uSex']==1){
		 $_SESSION['sex'] = "帅哥";}
		 else {
		 $_SESSION['sex'] = "美女";}
         $_SESSION['nickname'] = $result['uNickName'];
         $_SESSION['realname'] = $result['uRealName'];
		 $_SESSION['age'] = $result['uAge'];
	     $_SESSION['mail'] = $result['uMail'];
         $picId= $result['uPicId']; 
$query_1=mysql_query("SELECT * from picture where ID='$picId'");
$result_1=mysql_fetch_array($query_1);
        $_SESSION['picURL'] =$result_1['URL'];
		   echo 9999;
		}
	else  echo "密码错误.";
}

else echo "用户名不存在.";

?>