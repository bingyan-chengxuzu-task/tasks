<?php
session_start();header("Content-Type: text/html;charset=utf-8");
         unset($_SESSION['uID']);
	     unset($_SESSION['username']);
		 unset($_SESSION['sex']);
         unset($_SESSION['nickname']); 
         unset($_SESSION['realname']);
		 unset($_SESSION['age']);
	     unset($_SESSION['mail']);
         unset($_SESSION['picURL']);
    echo "<script language='javascript' type='text/javascript'>";
	echo "alert('注销成功。')"; 
	echo "</script>";
	$url ="../index.html";  
    echo "<script language='javascript' type='text/javascript'>";  
    echo "window.location.href='$url'";  
    echo "</script>";
?>
