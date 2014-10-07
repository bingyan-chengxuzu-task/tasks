<!DOCTYPE html>
<html>
<head>

<title><?=$title?></title>
<style type="text/css">
div#container{width:500px;}
div#header {background-color:#99bbbb;}
div#form {background-color:#ffff99;width:500px;float:left;}
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

<h1><?=anchor('blog','Coordinate35')?></h1>                        <!--回到主页 -->
</div>
<div id="form">

<?php foreach($query_entries as $row_entries): ?> <!--没准因为$query_entries是以二维表的形式储存,而$row_entries以一维行储存-->
<span class="error"> * <?=form_open('blog/article_update_two/'.$id);?></span>

<p>标题: <input type="text" name="title" value="<?php echo $row_entries['title']; ?>"/></p>
<span class="error"> * <?php echo form_error('title'); ?></span>

<p>文章: <textarea name='article' rows="20" cols="68" ><?php echo $row_entries['article']; ?></textarea></p>
<span class="error"> * <?php echo form_error('article'); ?></span>


<p>邮箱: <input type="text" name="email" value="<?php echo $row_entries['email']; ?>"/></p>                <!--添加评论  -->
<span class="error"> * <?php echo form_error('email'); ?></span>


<p>作者: <input type="text" name="author" value="<?php echo $row_entries['author']; ?>"/></p>
<span class="error"> * <?php echo form_error('author'); ?></span>

<p><input type="submit" value="提交更新"></input></p>
<? endforeach; ?>

</div>
</div>
</form>
</body>
</html>