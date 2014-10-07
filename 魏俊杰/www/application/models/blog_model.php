<?php
class Blog_model extends CI_Model
{
   public function get_entries()
   {
      
	  $query_entries= $this->db->get('entries');
      return $query_entries->result_array();
   }
   
   public function get_comments()
   {
      
	  $query_comments= $this->db->get('comments');
      return $query_comments->result_array();
   }
   
   public function get_messages()
   {
      
	  $query_messages= $this->db->get('messages');
	  return $query_messages->result_array();
   }
   
   
   public function set_comments()
   {
      $data=array(
      'content'=>$this->input->post('content'),
      'author'=>$this->input->post('author'),
      'entry_id'=>$this->input->post('entry_id'),
      'time'=>unix_to_human(now()+360*60,TRUE,'us'),
	  'email'=>$this->input->post('email')
	  );
   
      return $this->db->insert('comments',$data);
   }
   
   public function set_article()
   {
      $data=array(
      'title'=>$this->input->post('title'),
	  'article'=>$this->input->post('article'),
      'author'=>$this->input->post('author'),
	  'email'=>$this->input->post('email'),
	  'time'=>unix_to_human(now()+360*60,TRUE,'us')
	  );
	  if (strlen($this->input->post('article'))>100)
	  {
	      $data['halfarticle']=mb_substr($this->input->post('article'),0,100,"utf-8").'......';
	  }   else
	  {
	      $data['halfarticle']=$this->input->post('article');
	  }
	 
	  return $this->db->insert('entries',$data);
   }   
   
   public function set_message()
   {
      $data=array(
	  'author'=>$this->input->post('author'),
	  'message'=>$this->input->post('message'),
	  'email'=>$this->input->post('email'),
	  'time'=>unix_to_human(now()+360*60,TRUE,'us')
	  );
	  return $this->db->insert('messages',$data);
   }
   
   public function del_article_comments($id)
   {
	  $this->db->where('id',$id);
	  $this->db->delete('entries');
	  $this->db->where('entry_id',$id);
	  $this->db->delete('comments');
   }
   
   public function del_comments($id)
   {
      $this->db->where('id',$id);
	  $this->db->delete('comments');
   }
   
   public function del_messages($id)
   {
      $this->db->where('id',$id);
	  $this->db->delete('messages');
	}
   public function update_article($id)
   {
    $data=array(
      'title'=>$this->input->post('title'),
	  'article'=>$this->input->post('article'),
      'author'=>$this->input->post('author'),
	  'email'=>$this->input->post('email'),
	  'time'=>unix_to_human(now()+360*60,TRUE,'us')
	  );
	  if (strlen($this->input->post('article'))>100)
	  {
	      $data['halfarticle']=mb_substr($this->input->post('article'),0,100,"utf-8").'......';
	  }   else
	  {
	      $data['halfarticle']=$this->input->post('article');
	  }
	  $this->db->where('id',$id);
	  return $this->db->update('entries',$data);
        
   }
}
