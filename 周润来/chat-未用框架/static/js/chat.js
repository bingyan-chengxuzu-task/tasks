var socket;
function init(){
  var host = "ws://127.0.0.1:57418/";
  try{
    socket = new WebSocket(host);
    socket.onopen    = function(msg){ ; };
    socket.onmessage = function(msg){ log(msg.data); };
    socket.onclose   = function(msg){ log("没有连接上服务器！"); };
  }
  catch(ex){ log(ex); }
  $("msg").focus();
}
function send(){
  var txt,msg;
  txt = $("msg");
  msg = txt.value;
  if(!msg){ alert("发送的消息不能为空！"); return; }
  txt.value="";
  txt.focus();
  try{ socket.send(msg); } catch(ex){ log(ex); }
}
window.onbeforeunload=function(){
    try{
        socket.send('quit');
        socket.close();
        socket=null;
    }
    catch(ex){
        log(ex);
    }
};
function $(id){ return document.getElementById(id); }
function log(msg){ $("log").innerHTML+="<br>"+msg; }
function onkey(event){ if(event.keyCode==13){ send(); } }