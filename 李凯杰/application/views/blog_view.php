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
<h1><?=$heading?></h1>

<p><?=anchor('blog/textShow/'."","所有日志");?>  <?=anchor('blog/messagetable',"留言板");?></p>

<div id="container">
	<h1> 日志分组:</h1>
	<?php for($i = 1; $i <= $groupNum; $i++): ?>
		<p><?=anchor('blog/textShow/'.$groups[$i],$groups[$i]);?> (<?=$groupBlogNum[$i]?>) </p>
	<?php endfor; ?>
</div>

<div id="container">
	<h1> 动态:</h1>
	<div id="body">
		<?php for($i = 1; $i <= $operateNum; $i++): ?>
			<h3><?=$newsHeading[$i]?></h3>
			<h5><?=$newsTitle[$i]?></h5>
			<?php 
				$linkto = 'blog/text/'.$newsID[$i];
				if($newsOp[$i] == 4)
				{
					$linkto = 'blog/messagetabl/';
				} 
				elseif($newsOp[$i] == 5)
				{
					$linkto = 'blog/';
				}
			?>
			<p><?=$newsBody[$i]?> <?=anchor($linkto, "...");?></p>
			<p><?=date("Y-m-d H:i:s",$newsTime[$i])?></p>
			<hr>

		<?php endfor; ?>
	</div>
</div>

<p><?=anchor('blog/manage',"管理");?></p>

</body>
</html>