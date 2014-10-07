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
<h1><?=anchor('blog','Coordinate35')?></h1>
</div>                        <!--回到主页 -->
<div id="form">

    
<?=form_open('blog/message_insert');?>
<p>留言: <textarea name='message' rows="20" cols="68" ><?php echo set_value('message'); ?></textarea></p>                <!--添加留言 -->
<span class="error"> * <?php echo form_error('message'); ?></span>
<p>作者: <input type="text" name="author" value="<?php echo set_value('author'); ?>" /></p>
<span class="error"> * <?php echo form_error('author'); ?></span>
<p>邮箱: <input type="text" name="email" value="<?php echo set_value('email'); ?>"/></p>
<span class="error"> * <?php echo form_error('email'); ?></span>
<p><input type="submit" value="提交留言"></input></p>
</form>

</div>
</div>
</body>
</html>