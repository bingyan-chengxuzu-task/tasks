<?php
session_start();header("Content-Type:text/html;charset=utf-8");
if(!$_SESSION['uID']){
    echo "<script>alert('请登录');</script>";
 echo "<script>location.href='index.html';</script>";
 exit();
}
?>
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
    <title>chat with me</title>
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/main.js" ></script>

</head>
<body>
    <div class="box">
  <h1>Withme</h1>
</div>
<div id="mainbg">
        <div class="render"></div>
    <div id="set" class="off"></div>
    <div id="choosebar">
            <div class="off" id="in_chat"><p>进入聊天</p></div>
            <div class="off" id="in_at"><p>进入私聊</p></div>
            <div class="off" id="in_persen"><p>个人中心</p></div>
            <div class="off" id="in_more"><p>更多功能</p></div>
    </div>
    <div id="chatroom">
        <div class="information">
            <h3>个人信息：</h3>
            <?php
            echo "<img src='".$_SESSION['picURL']."' id='head'>";
         echo "<h5>账号ID：</h5><p id='id'>".$_SESSION['uID']."</p>";
        echo "<h5>昵称：</h5><p id='nn'>".$_SESSION['nickname']."</p>";
         echo "<h5>性别：</h5><p>".$_SESSION['sex']."</p>";
          echo '<button class="logout">注销</button>';
            ?>
        </div>
        <div id="message">
            <textarea id="messagearea" readonly="readonly" rows="25">
            <?php
            require_once "php/linkDB.php";
            $query=mysql_query("SELECT * from message_all");
            $row=array();
    while($result=mysql_fetch_array($query)){
     $row[]=$result;
      }
            for($i=0;$i<$_SESSION['message_all_num'];$i++)
            {
                echo "\r\nID:".$row[$i][2]."【".$row[$i][3]."】:\r\n\t".$row[$i][1]."(".$row[$i][4].")\r\n";
            }

            ?> 
            </textarea>

        </div>
        <div id="item">
            <h3>房间信息：</h3>
            <?php
            echo "<h5>消息总数：</h5><p align='center' id='m_n'>".$_SESSION['message_all_num']."</p>";
            ?>
        </div>
        <div id="send">
            <textarea id="textarea" rows="6" ></textarea>
            <div class="submit">
                <input type="button" value="发 送" class="login" align="center" id="pub">
                <input type="submit" value="匿 名" class="login" align="center" id="ano">

            </div>
        </div>
    </div>
    <div id="atroom">
        <div class="information">
            <h3>个人信息：</h3>
            <?php

            echo "<img src='".$_SESSION['picURL']."' id='head'>";
         echo "<h5>账号ID：</h5><p>".$_SESSION['uID']."</p>";
        echo "<h5>昵称：</h5><p>".$_SESSION['nickname']."</p>";
        echo "<h5>性别：</h5><p>".$_SESSION['sex']."</p>";
         echo '<button class="logout">注销</button>';


            ?>
        </div>
        <div id="friend">
            <h5>好友列表：</h>
               <div id="friend_list_copy"> </div>
        </div>
        <div id="record">
            <textarea id="recordarea" readonly="readonly" rows="25">
            </textarea>
        </div>
        <div id="send_at">
            <textarea id="textarea_at" rows="6" ></textarea>
            <div class="submit">
                                <input type="button" value="发 送" class="login" align="center" id="send_sub">
            </div>
        </div>


    </div>
    <div id="persenroom">
        <div id="persen_message">
            <button id="change">修改</button>
            <button id="confirm">确认</button>
        </div>
        <div id="friend_item">
             <h5>添加/删除好友：</h5>
             <button onclick="location.reload()">刷新</button>
                  <div id="friend_list">           <?php
                $u_ID=$_SESSION['uID'];
                   $query_fri=mysql_query("SELECT * from friend where main_ID='$u_ID'");
                   $result_fri_num=mysql_num_rows($query_fri);
                   $row_fri=array();
                   while($result_fri=mysql_fetch_array($query_fri))
                   {
                   $row_fri[]=$result_fri;
                   }
                   for($i=0;$i<$result_fri_num;$i++)
                   {
                    $ID_fri=$row_fri[$i][1];
                    echo "<p class='friend_list_items' id='fri_ID_".$ID_fri."'>";
                    echo "<br/><br/>";
                    echo "ID:".$row_fri[$i][1];
                    $query_each=mysql_query("SELECT uNickName from user where uID='$ID_fri'");
                    $result_each=mysql_fetch_array($query_each);
                    echo "【".$result_each[0]."】";
                    echo "</p>";
                   }

                ?></div>
             <input type="text" placeholder="输入好友ID" id="add_text">
             <button id="add_friend">+</button>
        </div>
    </div>
    <div id="morefunction">
        <p style="font-size:170px">尽请期待!</p>
    </div>
</div>
</div>
</body>
</html>