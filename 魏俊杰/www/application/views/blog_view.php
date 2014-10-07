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
<a href="blog/article"> д����</a>
<a href="blog/message"> ����</a>
</div>

<div id="menu">

<h3>�����б�: </h3>

<ol>
<?php foreach($query_entries as $row_entries): ?>
<li><?=anchor('blog/article_comments/'.$row_entries['id'],$row_entries['title'])?></li>
<?=anchor('blog/article_delete/'.$row_entries['id'],'       ɾ��')?>
<?=anchor('blog/article_update_one/'.$row_entries['id'],'       �༭')?>
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
<?=anchor('blog/article_delete/'.$row_entries['id'],'       ɾ��')?>
<?=anchor('blog/article_update_one/'.$row_entries['id'],'       �༭')?>
<hr/>
<?php endforeach;?>
</ol>

</div>

<div id="message">
<h3>����</h3>

<ol>
<?php foreach($query_messages as $row_messages): ?>
<li><?=$row_messages['message']?></li>
<p><?=$row_messages['author']?></p>
<p><?=$row_messages['time']?></p>
<?=anchor('blog/message_delete/'.$row_messages['id'],'       ɾ��')?>
<hr/>
<?php endforeach;?>
</ol>
</div>
</div>
</body>
</html>