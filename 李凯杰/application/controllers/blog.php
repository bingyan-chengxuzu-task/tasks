<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

function substrs($content,$length='20') //辅助函数，截取字符串
{ 
	if($length && strlen($content) > $length) 
	{ 
		$num=0; 
		for($i=0;$i<$length-3;$i++) 
		{ 
			if(ord($content[$i])>127) 
			{ 
				$num++; 
			} 
		} 
		$num%2==1 ? $content=substr($content,0,$length-4):$content=substr($content,0,$length-3); 
	} 
	return $content; 
}

class Blog extends CI_Controller {	
	function __construct()
	{
		parent::__construct();
		date_default_timezone_set('Etc/GMT-8');     
		$this->load->database();
		$this->load->helper('url');
		$this->load->helper('form');
	}
	
	function index()
	{
		$data['title'] = "Blog";
		$data['heading'] = "Welcome!";
		
		$groups[0] = '';		//整理组别
		$groupBlogNum[0] = 0;
		$groupNum = 1;
		foreach($this->db->query('select distinct `group` from `entries`')->result() as $row)
		{
			$groups[$groupNum] = $row->group;
			$groupBlogNum[$groupNum] = $this->db->query("select * from `entries` where `group` = '".$row->group."'")->num_rows();
			$groupNum++;
		}

		$operations = $this->db->query('select * from operations order by id desc');  //整理最近操作数据	
		$operateNum = 1;						
		$newsOp[0] = 0;
		$newsBody[0] = "";
		$newsHeading[0] = "";
		$newsTitle[0] = "";
		$newsID[0] = 0;
		$newsTime[0] = "";
		foreach($operations->result() as $row)		
		{
			if($row->operate == 1)
			{
				$queryData = $this->db->query('select * from entries where id = '.$row->t_id);
				$newsHeading[$operateNum]  =  '新日志:';
				$newsTitle[$operateNum] = $queryData->row()->title;
				$newsBody[$operateNum] = substrs($queryData->row()->body,150);
				$newsID[$operateNum] = $row->t_id;
				$newsTime[$operateNum] = $row->time;
				$newsOp[$operateNum] = $row->operate;
			}
			elseif($row->operate == 2)
			{
				$queryData = $this->db->query('select * from entries where id = '.$row->t_id);
				$newsHeading[$operateNum] = '更改了一篇日志:';
				$newsTitle[$operateNum] = $queryData->row()->title;
				$newsBody[$operateNum] = substrs($queryData->row()->body,150);
				$newsID[$operateNum] = $row->t_id;
				$newsTime[$operateNum] = $row->time;
				$newsOp[$operateNum] = $row->operate;
			}
			elseif($row->operate == 3)
			{
				$queryData = $this->db->query('select * from comments where id = '.$row->t_id);
				$newsHeading[$operateNum]  =  '新评论!';
				$newsTitle[$operateNum] = $queryData->row()->author.' said:';
				$newsBody[$operateNum] = substrs($queryData->row()->body,150);
				$newsID[$operateNum] = $row->t_entry_id;
				$newsTime[$operateNum] = $row->time;
				$newsOp[$operateNum] = $row->operate;
			}
			elseif($row->operate == 4)
			{
				$queryData = $this->db->query('select * from messages where id = '.$row->t_id);
				$newsHeading[$operateNum]  =  '新留言！';
				$newsTitle[$operateNum] = $queryData->row()->author.' said to you:';
				$newsBody[$operateNum] = substrs($queryData->row()->message,150);
				$newsID[$operateNum] = $row->t_id;
				$newsTime[$operateNum] = $row->time;
				$newsOp[$operateNum] = $row->operate;
			}
			elseif($row->operate == 5)
			{
				$queryData=$this->db->query('select * from says where id = '.$row->t_id);
				$newsHeading[$operateNum]  =  '忍不住的吐槽···';
				$newsTitle[$operateNum] = '说道：';
				$newsBody[$operateNum] = substrs($queryData->row()->body,150);
				$newsID[$operateNum] = $row->t_id;
				$newsTime[$operateNum] = $row->time;
				$newsOp[$operateNum] = $row->operate;
			}
			$operateNum++;
		}
		
		$data['groups'] = $groups;
		$data['groupBlogNum'] = $groupBlogNum;
		$data['groupNum'] = $groupNum - 1;
		$data['newsBody'] = $newsBody;
		$data['newsHeading'] = $newsHeading;
		$data['newsTitle'] = $newsTitle;
		$data['newsID'] = $newsID;
		$data['newsTime'] = $newsTime;
		$data['newsOp'] = $newsOp;
		$data['operateNum'] = $operateNum - 1;
		
		$this->load->view('blog_view',$data);
	}
	
	function textShow($group = '')
	{
		if($group == '')
		{
			$entries = $this->db->get('entries');
			$data['heading'] = "所有日志";
		}
		else
		{
			$entries = $this->db->query("select * from `entries` where `group` = '".$group."'");
			$data['heading'] = $group;
		}
		
		$textBody[0] = "";
		$textTitle[0] = "";
		$textID[0] = 0;
		$textTime[0] = "";
		$commentsNum[0] = 0;
		$i = 1;
		foreach($entries->result() as $row)
		{
			$textBody[$i] = substrs($row->body);
			$textTitle[$i] = $row->title;
			$textID[$i] = $row->id;
			$textTime[$i] = $row->time;
			$commentsNum[$i] = $this->db->query("select * from comments where entry_id=".$row->id)->num_rows();
			$i++;
		}
		$data['commentsNum'] = $commentsNum;
		$data['textTime'] = $textTime;
		$data['textID'] = $textID;
		$data['textTitle'] = $textTitle;
		$data['textBody'] = $textBody;
		$data['textNum'] = $i - 1;
		
		
		$this->load->view('textShow_view',$data);
	}
	
	function text($id)
	{
		$textInfo = $this->db->query('select * from entries where id = '.$id);
		$data['id'] = $id;
		$data['title'] = $textInfo->row()->title;
		$data['body'] = $textInfo->row()->body;
		$data['time'] = $textInfo->row()->time;
		$data['group'] = $textInfo->row()->group;
		$data['query'] = $this->db->query("select * from comments where entry_id = ".$id);
		$data['commentNum'] = $data['query']->num_rows();
		$this->load->view('text_view',$data);
	}
	
	function textEdit($id)
	{
		if($id == 0)	//判断新建或是修改
		{
			$data['title'] = "";
			$data['body'] = "";
			$data['group'] = "Group1";
		}
		else
		{
			$textInfo = $this->db->query('select * from entries where id = '.$id);
			$data['title'] = $textInfo->row()->title;
			$data['body'] = $textInfo->row()->body;
			$data['group'] = $textInfo->row()->group;
		}
		$data['id'] = $id;
		
		$this->load->view('textEdit_view',$data);
		
	}
	
	function textEdit_updata($id)
	{
		if($_POST['group'] == '')
		{
			$_POST['group'] = 'Group1';
		}
		if($id == 0)
		{
			$_POST['time'] = time();
			$this->db->insert('entries',$_POST);
			$id = $this->db->insert_id();
			$this->db->insert('operations',array('operate' => 1,
												't_id' => $id,
												't_entry_id' => 0,
												'time' => time()));
		}
		else
		{
			//$this->db->query('update entries set body = "'.$_POST['body'].'", title = "'.$_POST['title'].'", time = '.time().' where id = '.$id);
			$this->db->query('update entries set `body` = ?, `title` = ?, `time` = ?, `group` = ? where `id` = ?', array($_POST['body'], $_POST['title'], time(), $_POST['group'], $id));
			$this->db->insert('operations',array('operate' => 2,
												't_id' => $id,
												't_entry_id' => 0,
												'time' => time()));
		}
		
		redirect('blog/text/'.$id);
	}
	
	function comments()
	{
		$data['title'] = "评论:";
		$data['heading'] = "评论:";
		//$data['id'] = $data['query'] = $this->db->get('comments')->num_rows()+1;
		$this->db->where('entry_id', $this->uri->segment(3));
		$data['query'] = $this->db->get('comments');
		
		$this->load->view('comments_view',$data);
	}
	
	function commentInsert()
	{
		$_POST['time'] = time();
		if(strlen($_POST['body']) > 150)	//控制长度不超过最大值
		{
			$_POST['body'] = substrs($_POST['body'],150);
		}
		if(strlen($_POST['author']) > 100)
		{
			$_POST['author'] = substrs($_POST['author'],100);
		}
		$this->db->insert('comments',$_POST);
		$this->db->insert('operations',array('operate' => 3,
												't_id' => $this->db->insert_id(),
												't_entry_id' => $_POST['entry_id'],
												'time' => time()));
		
		redirect('blog/text/'.$_POST['entry_id']);
	}
	
	function manage()
	{
		$data['entries'] = $this->db->get('entries');
		$data['comments'] = $this->db->get('comments');
		$data['messages'] = $this->db->get('messages');
		$data['says'] = $this->db->get('says');
		
		$this->load->view('manage_view',$data);
	}
	
	function textDel($id)
	{
		$this->db->query('delete from entries where id = '.$id);
		$this->db->query('delete from operations where t_id = '.$id.' and t_entry_id = 0');
		redirect("blog/manage");
	}
	
	function commentDel($id,$entry_id)
	{
		$this->db->query('delete from comments where id = '.$id);
		$this->db->query('delete from operations where t_id = '.$id.' and t_entry_id = '.$entry_id);
		redirect("blog/manage");
	}
	
	function messageDel($id)
	{
		$this->db->query('delete from messages where id = '.$id);
		$this->db->query('delete from operations where t_id = '.$id.' and t_entry_id = -1');
		redirect("blog/manage");
	}
	
	function saysDel($id)
	{
		$this->db->query('delete from says where id = '.$id);
		$this->db->query('delete from operations where t_id = '.$id.' and t_entry_id = -2');
		redirect("blog/manage");
	}
	
	function messagetable()
	{
		$data['title'] = "留言板";
		$data['messages'] = $this->db->get('messages');
		
		$this->load->view('messagetable_view',$data);
	}
	
	function messageInsert()
	{
		$_POST['time'] = time();
		if(strlen($_POST['message']) > 250)	//控制长度不超过最大值
		{
			$_POST['message'] = substrs($_POST['message'],250);
		}
		if(strlen($_POST['author']) > 100)
		{
			$_POST['author'] = substrs($_POST['author'],100);
		}
		$this->db->insert('messages',$_POST);
		$this->db->insert('operations',array('operate' => 4,
												't_id' => $this->db->insert_id(),
												't_entry_id' => -1,
												'time' => time()));
		redirect("blog/messagetable");
	}
	
	function sayInsert()
	{
		$_POST['time'] = time();
		if(strlen($_POST['body']) > 150)	//控制长度不超过最大值
		{
			$_POST['body'] = substrs($_POST['body'],150);
		}
		$this->db->insert('says',$_POST);
		$this->db->insert('operations',array('operate' => 5,
												't_id' => $this->db->insert_id(),
												't_entry_id' => -2,
												'time' => time()));
		redirect("blog/manage");
	}
}
?>