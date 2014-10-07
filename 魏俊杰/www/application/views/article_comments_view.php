<!DOCTYPE html>
<html>
<head>
<title><?=$title?></title>
<style type="text/css">
div#container{width:500px;word-wrap:break-word ;}
div#header {background-color:#99bbbb;word-wrap:break-word ;}
div#article {background-color:#ffff99;width:500px;float:left;word-wrap:break-word ;}
div#comment {background-color:#EEEEEE;width:500px;float:left;word-wrap:break-word ;}
div#form {background-color:#99bbbb;clear:both;width:500px;word-wrap:break-word ;}
h1 {margin-bottom:0;}
h2 {margin-bottom:0;font-size:18px;}
ul {margin:0;}
li {list-style:none;}
.error {color: #FF0000;}
</style>
</head>
<body>
<div id="container">
<div id="header">
<h1><?=anchor('blog','Coordinate35')?></h1> 
</div>
<div id="article">
<?php foreach($query_entries as $row_entries): ?>     <!--������� -->
   <?php if ($row_entries['id'] === $article_id): ?>
   <h3><?=$row_entries['title']?></h3>
   <p>Author: <?=$row_entries['author']?></p>
   <p>time: <?=$row_entries['time']?></p>
   <p><?=$row_entries['article']?></p>
   <?=anchor('blog/article_delete/'.$row_entries['id'],'       ɾ��')?>
   <?=anchor('blog/article_update_one/'.$row_entries['id'],'       �༭')?>
   <?php endif;?>   
<?php endforeach;?>
</div>

<div id="comment">
<h3>����:</h3>
<?php foreach($query_comments as $row_comments): ?>  <!--������¶�Ӧ���� -->
<p><?=$row_comments['content']?></p>
<p>Author: <?=$row_comments['author']?></p>
<p>Time: <?=$row_comments['time']?></p>
<?=anchor('blog/comment_delete/'.$row_comments['id'].'/'.$row_comments['entry_id'],'       delete')?>
<hr/>
<?php endforeach;?>

</div>

                       <!--�ص���ҳ -->
<div id="form">
<?=form_open('blog/comment_insert');?>
<?=form_hidden('entry_id',$this->uri->segment(3));?>
<p>����: <textarea name='content' rows="10" cols="68" ><?php echo set_value('content'); ?></textarea></p>                <!--�������  -->
<span class="error"> * <?php echo form_error('content'); ?></span>
<p>����: <input type="text" name="author" value="<?php echo set_value('author'); ?>"/></p>
<span class="error"> * <?php echo form_error('author'); ?></span>
<p>����: <input type="text" name="email" value="<?php echo set_value('email'); ?>"/></p>
<span class="error"> * <?php echo form_error('email'); ?><s/pan>
<p><input type="submit" value="�ύ����"></input></p>
</form>
</div>
</div>
</body>
</html>