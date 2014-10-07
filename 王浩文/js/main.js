$(function(){
show();
var val=request("val");
val=parseInt(val);
switch(val)
{
case 1:{$("#atroom").fadeOut();
$("#persenroom").fadeOut();
$("#morefunction").fadeOut();
$("#chatroom").fadeIn();
  break;}
case 2:{$("#chatroom").fadeOut();
$("#persenroom").fadeOut();
$("#morefunction").fadeOut();
$("#atroom").fadeIn();
  break;}
case 3:{$("#atroom").fadeOut();
$("#chatroom").fadeOut();
$("#morefunction").fadeOut();
$("#persenroom").fadeIn();
  break;}
case 4:{$("#atroom").fadeOut();
$("#persenroom").fadeOut();
$("#chatroom").fadeOut();
$("#morefunction").fadeIn();
  break;}

}

$("#friend_list_copy").html($("#friend_list").html());


setInterval(refresh,1000);

function refresh()
{
var xml;
if (window.XMLHttpRequest)
  {
  xml=new XMLHttpRequest();
  } 
xml.open("GET","php/message_all.php",false);
xml.send();
var a=new Array();
a=xml.responseText;
if(a){
 
  $("#messagearea").text($("#messagearea").text()+a);
  var num=parseInt($("#m_n").text())+1;
  $("#m_n").text(num);
    }

   var scrollTop = $("#messagearea")[0].scrollHeight;  
   $("#messagearea").scrollTop(scrollTop);  
}
function refresh_at()
{
var xml;
if (window.XMLHttpRequest)
  {
  xml=new XMLHttpRequest();
  } 
xml.open("GET","php/message_at.php",false);
xml.send();
var a=new Array();
a=xml.responseText;
if(a){
  $("#recordarea").text($("#recordarea").text()+a);
    }

   var scrollTop = $("#recordarea")[0].scrollHeight;  
   $("#recordarea").scrollTop(scrollTop);  
}



$("#choosebar").css('display','none');

$("#set").click(function(){
$("#choosebar").slideToggle();
});

$(".off").mouseover(function(){
    $(this).css('border-style','inset');
    $(this).css('background-color','green');
});

$(".off").mouseout(function(){
    $(this).css('border-style','outset');
    $(this).css('background-color','#82C400');
});


$("#in_chat").click(function(){
var val =1;
location.href="main.php?val="+val;
});

$("#in_at").click(function(){
var val =2;
location.href="main.php?val="+val;
});

$("#in_persen").click(function(){
var val =3;
location.href="main.php?val="+val;
});

$("#in_more").click(function(){
var val =4;
location.href="main.php?val="+val;
});

$(".render").click(function(){
location.href="index.html";
});



$("#regist").click(function () {
      $(".mask").fadeIn();
      $(".reg").fadeIn();
    });

  $(".close_btn").click(function(){
      $(".reg").fadeOut();
      $(".mask").fadeOut();
  });

  $("#login").click(function(){      
var xmlcode;
var username = $("#u")[0].value;
var password = $("#p")[0].value;
if (window.XMLHttpRequest)
  {
  xmlcode=new XMLHttpRequest();
  } 
xmlcode.open("GET","php/login.php?uName="+username+"&PassWord="+password,false);
xmlcode.send();
  if(xmlcode.responseText!=9999) alert(xmlcode.responseText);
  else {
    alert("登录成功!");
 location.href="main.php?val=1";
    } 
  });

  $(".logout").click(function(){
if(confirm("确认注销？"))
{
location.href="php/logout.php";
}
  });

$("#pub").click(function(){      

var xmlp;
var text = $("#textarea").val();
var uID = $("#id").text();
var nickname = $("#nn").text();
if (window.XMLHttpRequest)
  {
  xmlp=new XMLHttpRequest();
  }
xmlp.open("GET","php/public_all.php?text="+text+"&uID="+uID+"&nickname="+nickname,false);
xmlp.send();
  if(xmlp.responseText!=1314520) alert(xmlp.responseText);
  else {
    $("#textarea").val("");
    $("#textarea").focus();
    refresh();
    } 
  });

$("#add_friend").click(function(){      

var xmlp;
var uID = $("#id").text();
var sID= $("#add_text").val();
if(isNaN(sID))return;
if(uID==sID){alert("不能添加自己！");return;}
if(sID<1||isNaN(sID)){alert("ID错误！");return;}
if (window.XMLHttpRequest)
  {
  xmlp=new XMLHttpRequest();
  }
xmlp.open("GET","php/add_friend.php?uID="+uID+"&sID="+sID,false);
xmlp.send();
  if(xmlp.responseText!=1314520) alert(xmlp.responseText);
  else {
alert("添加成功！");
    }
  });

$("#t_UserName").keyup(function(){
var xmluser;
var un=$("#t_UserName").val();
if (window.XMLHttpRequest)
  {
  xmluser=new XMLHttpRequest();
  }

xmluser.onreadystatechange=function()
 {
   $("#t_UserNameTip").text(xmluser.responseText);
    }
  
xmluser.open("GET","php/check_user.php?u="+un,true);
xmluser.send();
});

$("#t_UserPass,#t_RePass").keyup(function(){
var str1=$("#t_UserPass").val();
var str2=$("#t_RePass").val();
if(str1==""||str2=="") var print_out="密码不能为空";
else if(str1!=str2)var print_out="两次输入不一致";
else var print_out="√";

$("#t_UserPassTip").text(print_out);
$("#t_RePassTip").text(print_out);
});


$("#regist_con").click(function(){
var xmlr;
var is_used = $("#t_UserNameTip").text();
var username = $("#t_UserName").val();
var str1=$("#t_UserPass").val();
var password = $("#t_RePass").val();
var nickname = $("#iptNickName").val();
var realname = $("#iptName").val();
var mail = $("#t_Email").val();
var age = $("#age").val();
var sex = $("#form1 input[name='rb_Sex']:checked").val(); 
   if(!username||!password||!nickname||!age||!mail||!realname)
   {
  alert("请补全信息.");
    return;  
   }
 
  if(is_used!="√")
   {

  alert("账号已使用!!");
    return;  
   }
 
  if(age<0||age>99)
   {
  alert("年龄错误!!");
    return;  
   }

 if(str1!=password)
   {
  alert("密码不一致!!");
    return;  
   }


if (window.XMLHttpRequest)
  {
  xmlr=new XMLHttpRequest();
  } 
xmlr.open("GET","php/regist.php?u="+username+"&p="+password+"&nn="+nickname+"&rn="+realname+"&a="+age+"&m="+mail+"&s="+sex,false);
xmlr.send();
if(xmlr.responseText!=15527281213) alert(xmlr.responseText);
  else {
    alert("注册成功!");
    $(".reg").fadeOut("fast");
  $(".mask").css({ display: 'none' });
 $("#u").val(username);
 $("#p").focus();
}

 });


var to_who;
   $(".friend_list_items").hover(function(){
    $(this).css('background-color','green');
  },function(){
    $(this).css('background-color','transparent');
  }).dblclick(function(){
    $(".friend_list_items").css('background-color','transparent');
   $(this).css('opacity','1');
   $(this).css('background-color','yellow');
   $(".friend_list_items").hover(function(){
    $(this).css('background-color','green');
  },function(){
    $(this).css('background-color','transparent');
  });
   $(this).unbind('mouseenter mouseleave');
   to_who=$(this).attr('id');
  });


    $("#send_sub").click(function(){
     if(to_who==null){
        alert("请选择好友！");
        return;
      }
      to_who = to_who.replace(/[^0-9]/ig,"");
      var xmlp;  
      var uID = $("#id").text();
      var toID=to_who;
      var totext=$("#textarea_at").val();
    
if (window.XMLHttpRequest)
  {
  xmlp=new XMLHttpRequest();
  }
xmlp.open("GET","php/public_at.php?uID="+uID+"&toID="+toID+"&totext="+totext,false);
xmlp.send();
  if(xmlp.responseText!=1314520) alert(xmlp.responseText);
  else {
    $("#textarea_at").val("");
    $("#textarea_at").focus();
    refresh();
    } 
  });


});



function show(){
var box = $('.box').text(),
    rs = $('.render')[0],
    f = [
      'arial','verdana','monospace',
      'consolas','impact','helveltica'
    ],
    c = [
      '1ABC9C','3498DB','34495E','E67E22',
      'E74C3C','2ECC71','E74C3C','95A5A6','D35400'
    ];
var out = '';
for (var i = 0; i < box.length; i++) {

  var r = f[Math.floor(Math.random() * f.length)],

      sh = c[Math.floor(Math.random() * c.length)],
      st = 'color:#'+sh+
      ';font-family: '+r+
      ';text-shadow:0px 1px 0px #'+sh+',0px 2px 0px #'+sh+',0px 3px 0px #'+sh+',0px 4px 0px #'+sh+', 0px 5px 0px  #'+sh+',0px 6px 0px #'+sh+', 0px 7px 0px #'+sh+',0px 8px 7px #'+sh;
  out += '<span style="'+st+'">'+box[i]+'</span>';
}  
rs.innerHTML = out; 
setTimeout(show,300);
}

function request(paras)
    { 
        var url = location.href; 
        var paraString = url.substring(url.indexOf("?")+1,url.length).split("&"); 
        var paraObj = {} 
        for (i=0; j=paraString[i]; i++){ 
        paraObj[j.substring(0,j.indexOf("=")).toLowerCase()] = j.substring(j.indexOf("=")+1,j.length); 
        } 
        var returnValue = paraObj[paras.toLowerCase()]; 
        if(typeof(returnValue)=="undefined"){ 
        return ""; 
        }else{ 
        return returnValue; 
        } 
    }