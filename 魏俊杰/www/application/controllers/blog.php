<?php

class Blog extends CI_Controller
{
   
   public function __construct()
   {
   parent::__construct();
   $this->load->model('blog_model');
   }
   
   
   function index()
   {
     $data['title']="Coordinate35";
	 $data['heading']="Coordinate35";
	 $data['query_entries']=$this->blog_model->get_entries();
	 $data['query_messages']=$this->blog_model->get_messages();
	
	 $this->load->view('blog_view',$data);
   }

    function article_comments()
	{
	  $data['article_id']=$this->uri->segment(3);
	  $data['title']="Article of Coordinate35";
	  $this->db->where('entry_id',$this->uri->segment(3));
      $data['query_comments']=$this->blog_model->get_comments();
	  $data['query_entries']=$this->blog_model->get_entries();
	 
	  $this->load->view('article_comments_view',$data);
	}
	
	function comment_insert()
	{
	  if ($this->form_validation->run('comment_insert'))
	  
	  {
	     $this->blog_model->set_comments();	  
	     redirect('blog/article_comments/'.$_POST['entry_id']);
	  } else
	   {
	        redirect('blog/article_comments/'.$_POST['entry_id']);
	     }  
	}
	
	function article()//进入编辑博文界面
	{
	   $this->load->view('article_insert_view');
	}
	
	function article_insert()
	{
	  
	  
	  if ($this->form_validation->run('article_insert')== FALSE)
	  {
	     $this->load->view('article_insert_view');
	  }  else
	  {
	  $this->blog_model->set_article();
	  redirect('blog');
	  }
	}
    
	function message()//进入留言编辑页面
	{
	   $this->load->view('message_insert_view');
	}
    
	function message_insert()
	{
	   if ($this->form_validation->run('message_insert') == FALSE)
	   {
	      $this->load->view('message_insert_view');
	   }  else
	   {
	      $this->blog_model->set_message();
	      redirect('blog');
	   }
	}
	
	function article_delete()
	{
	   $id=$this->uri->segment(3);
	   $this->blog_model->del_article_comments($id);
	   //$this->db->where('id',$id);
	   //$this->db->delete('entries');
	   redirect('blog');
	}
	
	function comment_delete()
	{
	   $id=$this->uri->segment(3);
	   $entries_id=$this->uri->segment(4);
	   $this->blog_model->del_comments($id);
	   redirect('blog/article_comments/'.$entries_id);
	}
	
	function message_delete()
	{
	   $id=$this->uri->segment(3);
	   $this->blog_model->del_messages($id);
	   redirect('blog');
	}
	   
    function article_update_one()
    {
	   $this->db->where('id',$this->uri->segment(3));
       $data['query_entries']=$this->blog_model->get_entries();
	   $data['id']=$this->uri->segment(3);
	   $this->load->view('article_update_view',$data);
	   
	}
	
	function article_update_two()
	{
	   if ($this->form_validation->run('article_insert')== FALSE)
	  {
	     $this->load->view('article_update_view');
	  }  else
	  {
	  $this->blog_model->update_article($this->uri->segment(3));
	  redirect('blog');
	  }
	
	}
}
?>