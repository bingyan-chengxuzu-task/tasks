<?php
$config = array(
               'article_insert'=>array(
			                     array(
                                      'field'   => 'title', 
                                      'label'   => '���ı���', 
                                      'rules'   => 'trim|htmlspecialchars|required'
                                      ),
                                 array(
                                       'field'   => 'article', 
                                       'label'   => '����', 
                                       'rules'   => 'trim|htmlspecialchars|required'
                                      ),
                                 array(
                                       'field'   => 'email', 
                                       'label'   => '����', 
                                       'rules'   => 'trim|htmlspecialchars|required|valid_email'
                                      ),   
                                 array(
                                       'field'   => 'author', 
                                       'label'   => '����', 
                                       'rules'   => 'trim|required|min_length[3]|max_length[12]|htmlspecialchars'
                                      )
                                 ),
				'message_insert'=>array(
				                  array(
                                      'field'   => 'message', 
                                      'label'   => '����', 
                                      'rules'   => 'trim|htmlspecialchars|required'
                                      ),
                                  array(
                                      'field'   => 'author', 
                                      'label'   => '����', 
                                      'rules'   => 'trim|required|min_length[3]|max_length[12]|htmlspecialchars'
                                      ),
                                  array(
                                      'field'   => 'email', 
                                      'label'   => '����', 
                                      'rules'   => 'trim|htmlspecialchars|required|valid_email'
                                      )
                                  ),
                'comment_insert'=>array(
				                  array(
                                      'field'   => 'content', 
                                      'label'   => '����', 
                                      'rules'   => 'trim|htmlspecialchars|required'
                                      ),
								  array(
                                      'field'   => 'author', 
                                      'label'   => '����', 
                                      'rules'   => 'trim|required|min_length[3]|max_length[12]|htmlspecialchars'
                                      ),
								  array(
                                      'field'   => 'email', 
                                      'label'   => '����', 
                                      'rules'   => 'trim|htmlspecialchars|required|valid_email'
                                      )
								   )
                  );                    