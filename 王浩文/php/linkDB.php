<?php
    //php环境编码
    //header("Content-Type:text/html;charset=utf-8");

    //链接数据库
    $link = mysql_connect("localhost","whw","1230904whw");
    if(!$link)  
    {  
       echo "mysql connect failed";
    }	

    //设置数据库编码	
    mysql_query("set names utf8");
    
    //选择数据库
    mysql_select_db("chat",$link);                            
?>