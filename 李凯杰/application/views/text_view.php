<html>
<head>
<title><?=$title?></title>
	<meta charset="utf-8">

	<style type="text/css">

	::selection{ background-color: #E13300; color: white; }
	::moz-selection{ background-color: #E13300; color: white; }
	::webkit-selection{ background-color: #E13300; color: white; }

	body {
		background-color: #fff;
		margin: 40px;
		font: 13px/20px normal Helvetica, Arial, sans-serif;
		color: #4F5155;
	}

	a {
		color: #003399;
		background-color: transparent;
		font-weight: normal;
	}

	h1 {
		color: #444;
		background-color: transparent;
		border-bottom: 1px solid #D0D0D0;
		font-size: 19px;
		font-weight: normal;
		margin: 0 0 14px 0;
		padding: 14px 15px 10px 15px;
	}

	code {
		font-family: Consolas, Monaco, Courier New, Courier, monospace;
		font-size: 12px;
		background-color: #f9f9f9;
		border: 1px solid #D0D0D0;
		color: #002166;
		display: block;
		margin: 14px 0 14px 0;
		padding: 12px 10px 12px 10px;
	}

	#body{
		margin: 0 15px 0 15px;
	}
	
	p.footer{
		text-align: right;
		font-size: 11px;
		border-top: 1px solid #D0D0D0;
		line-height: 32px;
		padding: 0 10px 0 10px;
		margin: 20px 0 0 0;
	}
	
	#container{
		margin: 10px;
		border: 1px solid #D0D0D0;
		-webkit-box-shadow: 0 0 8px #D0D0D0;
	}
	</style>
</head>
<body>
<div id="container">
	<h1><?=$title?></h3>
	<p><?=$body?></p>
	<hr>
	<p>  @<?=date("Y-m-d H:i:s",$time)?></p>
	<p>  组别:<?=$group?></p>
</div>

<div id="container">
	<h1><?='有 '.$commentNum.' 个评论'?></h1>
	<?php foreach($query->result() as $row): ?>
		<div id="container">
			<h1><?=$row->author?> 说:</h1>
			<p><?=$row->body?></p>
			<p>	at: <?=date("Y-m-d H:i:s",$row->time)?>
		</div>
	<?php endforeach; ?>
	
	<?=form_open('blog/commentInsert');?>
	<?=form_hidden('entry_id',$this->uri->segment(3));?>
	<h2>评论:</h2>
	<p><?=form_textarea('body',"");?></p>
	<p>留名:</p>
	<p><?=form_input('author',"");?></p>
	<p><input type="submit" value="发表评论" /></p>
	</form>
	
</div>
<p><?=anchor('blog', "返回");?></p>

</body>
</html>