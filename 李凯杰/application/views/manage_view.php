<html>
<head>
<title>管理</title>
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
	<h1>说说:</h1>
<?=form_open('blog/sayInsert');?>
	<p><?=form_textarea('body', "");?></p>
	<p><input type="submit" value="发布" /></p>
	</form>
	<div id="body">
<?php if ($says->num_rows() > 0):?>
			<?php foreach ($says->result() as $row):?>
				<h4><?=$row->body?></h4>
				<p><?=date("Y-m-d H:i:s", $row->time)?> <?=anchor('blog/saysDel/' . $row->id, "删除");?></p>
				<hr>
<?php endforeach;?>
		<?php endif;?>
</div>
</div>

<div id="container">
	<h1>日志:</h1>
<?=anchor('blog/textEdit/0', "新日志...");?>
	<?php if ($entries->num_rows() > 0):?>
		<?php foreach ($entries->result() as $row):?>
			<div id="container">
				<h1><?=$row->title?></h1>
				<p><?=$row->body?></p>
				<p><?=date("Y-m-d H:i:s", $row->time)?> <?=anchor('blog/textEdit/' . $row->id, "编辑");?> <?=anchor('blog/textDel/' . $row->id, "删除");?></p>
				<hr>
				<div id="body">
<?php foreach ($comments->result() as $comment):?>
						<?php if ($comment->entry_id == $row->id):?>
							<h4><?=$comment->author?> said:</h4>
							<p><?=$comment->body?></p>
							<p><?=date("Y-m-d H:i:s", $comment->time)?> <?=anchor('blog/commentDel/' . $comment->id . "/" . $row->id, "删除");?></p>
<?php endif;?>
					<?php endforeach;?>
</div>
			</div>
<?php endforeach;?>
	<?php endif;?>
</div>
<div id="container">
	<h1>留言板:</h1>
<?php if ($messages->num_rows() > 0):?>
		<?php foreach ($messages->result() as $row):?>
			<div id="body">
				<p><?=$row->message?></p>
				<h4>by: <?=$row->author?></h4>
				<p><?=date("Y-m-d H:i:s", $row->time)?> <?=anchor('blog/messageDel/' . $row->id, "删除");?></p>
				<hr>
			</div>
<?php endforeach;?>
	<?php endif;?>
</div>
<p><?=anchor('blog', "返回");?></p>

</body>
</html>