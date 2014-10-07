<!DOCTYPE html>
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=GB2312" />
<title><?=$title?></title>
<style type="text/css">
div#container{width:500px;word-wrap:break-word ;height:100%}
div#header {background-color:#99bbbb;word-wrap:break-word ;}
div#menu {background-color:#ffff99;width:150px;float:left;word-wrap:break-word ; height:100%; }
div#content {background-color:#EEEEEE;width:350px;float:left;word-wrap:break-word ; height:100%;}
div#message {background-color:#99bbbb;clear:both;text-align:center;word-wrap:break-word ;}
h1 {margin-bottom:0;}
h2 {margin-bottom:0;font-size:18px;}
ul {margin:0;}
li {list-style:none;}
</style>
</head>
<body>
<div id="container">
<div id="header">
<h1><?=$heading?></h1>
<a href="blog/article"> 写博客</a>
<a href="blog/message"> 留言</a>
</div>

<div id="menu">

<h3>文章列表: </h3>

<ol>
<?php foreach($query_entries as $row_entries): ?>
<li><?=anchor('blog/article_comments/'.$row_entries['id'],$row_entries['title'])?></li>
<?=anchor('blog/article_delete/'.$row_entries['id'],'       删除')?>
<?=anchor('blog/article_update_one/'.$row_entries['id'],'       编辑')?>
<hr/>
<?php endforeach;?>
</ol>

</div>
<div id="content">
<ol>
<?php foreach($query_entries as $row_entries): ?>
<li><?=anchor('blog/article_comments/'.$row_entries['id'],$row_entries['title'])?></li>
<p>Author: <?=$row_entries['author']?></p>
<P><?=$row_entries['halfarticle']?></P>
<p><?=$row_entries['time']?></p>
<?=anchor('blog/article_delete/'.$row_entries['id'],'       删除')?>
<?=anchor('blog/article_update_one/'.$row_entries['id'],'       编辑')?>
<hr/>
<?php endforeach;?>
</ol>

</div>

<div id="message">
<h3>留言</h3>

<ol>
<?php foreach($query_messages as $row_messages): ?>
<li><?=$row_messages['message']?></li>
<p><?=$row_messages['author']?></p>
<p><?=$row_messages['time']?></p>
<?=anchor('blog/message_delete/'.$row_messages['id'],'       删除')?>
<hr/>
<?php endforeach;?>
</ol>
</div>
</div>
</body>
</html>