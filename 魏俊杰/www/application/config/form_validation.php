<?php
$config = array(
               'article_insert'=>array(
			                     array(
                                      'field'   => 'title', 
                                      'label'   => '博文标题', 
                                      'rules'   => 'trim|htmlspecialchars|required'
                                      ),
                                 array(
                                       'field'   => 'article', 
                                       'label'   => '博文', 
                                       'rules'   => 'trim|htmlspecialchars|required'
                                      ),
                                 array(
                                       'field'   => 'email', 
                                       'label'   => '邮箱', 
                                       'rules'   => 'trim|htmlspecialchars|required|valid_email'
                                      ),   
                                 array(
                                       'field'   => 'author', 
                                       'label'   => '作者', 
                                       'rules'   => 'trim|required|min_length[3]|max_length[12]|htmlspecialchars'
                                      )
                                 ),
				'message_insert'=>array(
				                  array(
                                      'field'   => 'message', 
                                      'label'   => '留言', 
                                      'rules'   => 'trim|htmlspecialchars|required'
                                      ),
                                  array(
                                      'field'   => 'author', 
                                      'label'   => '作者', 
                                      'rules'   => 'trim|required|min_length[3]|max_length[12]|htmlspecialchars'
                                      ),
                                  array(
                                      'field'   => 'email', 
                                      'label'   => '邮箱', 
                                      'rules'   => 'trim|htmlspecialchars|required|valid_email'
                                      )
                                  ),
                'comment_insert'=>array(
				                  array(
                                      'field'   => 'content', 
                                      'label'   => '评论', 
                                      'rules'   => 'trim|htmlspecialchars|required'
                                      ),
								  array(
                                      'field'   => 'author', 
                                      'label'   => '作者', 
                                      'rules'   => 'trim|required|min_length[3]|max_length[12]|htmlspecialchars'
                                      ),
								  array(
                                      'field'   => 'email', 
                                      'label'   => '邮箱', 
                                      'rules'   => 'trim|htmlspecialchars|required|valid_email'
                                      )
								   )
                  );                    