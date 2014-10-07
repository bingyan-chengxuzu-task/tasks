#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx, sys, time, threading, socket, random

#设定系统默认编码
reload(sys)
sys.setdefaultencoding('utf-8')

## 
# Desc: App类
class App(wx.App):
    def OnInit(self):
        basicFrame = chatFrame()
        basicFrame.Show()
        self.SetTopWindow(basicFrame)
        return True

## 
# Desc: 主窗口类
class chatFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, 1, 'Simple Chat Room', pos=(419, 173), size=(610, 455))
        self.s = ''
        #初始化面板
        self.msgPanel = wx.Panel(self, -1, (5, 0), (600, 300))
        self.toolPanel = wx.Panel(self, -1, (5, 300), (600, 20))
        self.inputPanel = wx.Panel(self, -1, (5, 270), (600, 165))
        #初始化菜单栏
        self.menuBar = wx.MenuBar()
        self.menuInit()
        self.SetMenuBar(self.menuBar)
        #初始化基本控件
        self.widgetsInit()

    def menuInit(self):
        #连接菜单
        menuCon = wx.Menu()
        conn_to = menuCon.Append(-1, "新建...")
        quit_now = menuCon.Append(-1, "退出程序")
        self.menuBar.Append(menuCon, "连接")
        #绑定事件
        self.Bind(wx.EVT_MENU, self.newConn, conn_to)
        self.Bind(wx.EVT_MENU, self.quitNow, quit_now)

    def widgetsInit(self):
        #聊天记录部分
        self.msgArea = wx.TextCtrl(self.msgPanel, -1, "", (0, 0), (600, 250), wx.TE_MULTILINE|wx.TE_READONLY)
        self.msgArea.SetInsertionPoint(0)
        #聊天文本输入框
        self.msgInputBox = wx.TextCtrl(self.inputPanel, -1, "", (0, 0), (600, 125), wx.TE_MULTILINE|wx.TE_PROCESS_TAB)
        self.msgInputBox.SetInsertionPoint(0)
        #发送/取消按钮
        canelButton = wx.Button(self.inputPanel, -1, '关闭', (395, 128), (100, 28))
        self.enterButton = wx.Button(self.inputPanel, -1, '发送', (500, 128), (100, 28))
        self.Bind(wx.EVT_BUTTON, self.quitNow, canelButton)

    def newConn(self, e):
        self.connFrame = connFrame(self)
        self.connMgr = self.connFrame.connMgr
        self.connFrame.Show()

    
    #发送消息并刷新本地窗口内容
    def SendMsg(self, conn):
        msg = self.msgInputBox.GetValue().strip()
        msg = {'host':self.c['host'], 'port':self.c['port'],\
                'id':self.c['id'], 'name':self.c['name'],\
                'content':msg, 'count':0,
        }
        if not msg['content']:
            return
        if not self.c['type_s']:
            try:
                conn.sendall(str(msg))
                self.refreshMsg(msg)
            except:
                self.refreshMsg("发送失败", 0)
        else:
            if self.connMgr.condition.acquire():
                self.connMgr.msg_queue.append(msg)
                self.refreshMsg(msg)
                self.connMgr.condition.notifyAll()
                self.connMgr.condition.release()
        self.msgInputBox.SetValue('')
        
    def recvMsg(self, conn):
        while 1:
            data = self.connMgr.recvAllMsg(conn)
            if not data.strip(): continue
            try:
                exec 'recv_msg = ' + data
            except:
                self.refreshMsg('Failed to resolve data from server.', 0)
                continue
            else:
                if recv_msg['content']:
                    self.refreshMsg(recv_msg)
    
    def refreshMsg(self, newMsg, is_dict=1):
        if self.connMgr.lock.acquire():
            msgBox = self.msgArea
            old_msg = msgBox.GetValue().strip()
            old_msg = old_msg + '\n' if old_msg else old_msg
            if is_dict:
                new_msg = "%s: %s" % (newMsg['name'], newMsg['content'].strip())
            else:
                new_msg = newMsg.strip()
            ltime = time.strftime('%H:%M:%S',time.localtime(time.time()))
            st = old_msg + new_msg + 5*' ' + ltime
            msgBox.SetValue(str(st))
            lines = msgBox.GetNumberOfLines()
            xy = msgBox.XYToPosition(lines, 0)
            msgBox.ShowPosition(xy)
        self.connMgr.lock.release()
            

    def quitNow(self, e):
        dlg = wx.MessageDialog(self, '是否退出?','MessageDialog', wx.YES_NO | wx.ICON_QUESTION | wx.NO_DEFAULT)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_YES:
            self.Destroy()
            sys.exit()


## 
# Desc: 新建连接设置类
class connFrame(wx.Frame):
    c = {
    'host' : '127.0.0.1',
    'port' : '1234',
    'id' : 0,
    'name' : 'client',
    #是否作为服务器
    'type_s' : 1,
    #最大连接数，0表示不限制
    's_maxConn' : 50,
    #连接超时与重试
    's_timeout' : 300,
    'c_timeout' : 60,
    'c_retrytimes' : 10,
    'is_active' : 0,
    'maxMsgSize' : 1024*1024*20
    }

    def __init__(self, parent, id=-1):
        wx.Frame.__init__(self, parent=parent, id=id, title='新建连接', pos=(500, 300), size=(285, 170), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        panel = self.panel = wx.Panel(self, -1)
        #传递默认配置到主窗口
        parent.c = self.c.copy()
        #实例化连接管理类
        self.connMgr = connMgr(parent)
        #主机和端口
        wx.StaticText(panel, -1, "主机:", (8,15),(40, 25))
        self.host_inputBox = wx.TextCtrl(panel, -1, self.c['host'], (38, 10), (150, 25), wx.TE_PROCESS_TAB)
  	wx.StaticText(panel, -1, "端口:", (200,15),(40, 25))
        self.port_inputBox = wx.TextCtrl(panel, -1, self.c['port'], (230, 10), (50, 25), wx.TE_PROCESS_TAB)
        #连接类型
  	wx.StaticText(panel, -1, "类型:", (8, 46),(40, 25))
        self.type_server = wx.RadioButton(panel, -1, '服务器', pos=(45, 40), style=wx.RB_GROUP)
        self.type_client= wx.RadioButton(panel, -1, '客户端', pos=(120, 40))
        #最大连接数
     	wx.StaticText(panel, -1, "最大连接数:", (8,77),(70, 25))
        self.maxConn_inputBox = wx.SpinCtrl(panel, -1, str(self.c['s_maxConn']), (75, 72), (60, 25), min=1, max=200, initial=10)
     	wx.StaticText(panel, -1, "超时(s):", (165,77),(70, 25))
        self.timeout_inputBox = wx.TextCtrl(panel, -1, str(self.c['s_timeout']), (210, 72), (60, 25), wx.TE_PROCESS_TAB)
   	wx.StaticText(panel, -1, "用户名:", (8, 108),(50, 25))
        self.uname_inputBox = wx.TextCtrl(panel, -1, "server", (50, 104), (100, 25), wx.TE_PROCESS_TAB)
        #取消和确定按钮
        resetButton = wx.Button(panel, -1, '重置', (50, 141), (60, 28))
        enterButton = wx.Button(panel, -1, '确定', (110, 141), (60, 28))
        canelButton = wx.Button(panel, -1, '取消', (170, 141), (60, 28))
        #绑定事件(将主窗口作为参数传入)
        resetButton.Bind(wx.EVT_BUTTON, self.OnReset)
        enterButton.Bind(wx.EVT_BUTTON, lambda e:self.OnEnter(e, parent))
        canelButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        self.type_client.Bind(wx.EVT_RADIOBUTTON, self.OnClientType)
        self.type_server.Bind(wx.EVT_RADIOBUTTON, self.OnServerType)
        #显示窗口
        self.Show()

    def OnClientType(self, e):
        self.maxConn_inputBox.SetValue(1)
        self.maxConn_inputBox.SetRange(1, 1)
        self.uname_inputBox.SetValue(self.c['name'])

    def OnServerType(self, e):
        self.maxConn_inputBox.SetRange(1, self.c['s_maxConn'])
        self.maxConn_inputBox.SetValue(50)
        self.uname_inputBox.SetValue('server')

    def OnReset(self, e):
        #重置设置
        self.host_inputBox.SetValue(self.c['host'])
        self.port_inputBox.SetValue(self.c['port'])
        self.maxConn_inputBox.SetValue(self.c['s_maxConn'])
        if self.c['type_s']:
            self.type_server.SetValue(True)
        else:
            self.type_client.SetValue(True)

    def OnQuit(self, e):
        self.Destroy()

    def OnEnter(self, e, top):
        #更新设置
        top.c['host'] = self.host_inputBox.GetValue()
        top.c['port'] = self.port_inputBox.GetValue()
        type_s = int(self.type_server.GetValue())
        top.c['type_s'] = 1 if type_s else 0
        top.c['maxConn'] = int(self.maxConn_inputBox.GetValue())
        top.c['name'] = self.uname_inputBox.GetValue()
        top.c['timeout'] = self.timeout_inputBox.GetValue()
        top.SetTitle('simpleChat [服务器]' if type_s else 'simpleChat [客户端]')

        #判断是否有连接正在运行
        top.connMgr.condition = threading.Condition()
        top.connMgr.condition.acquire()
        if top.c['is_active']:
            top.refreshMsg("There has been an active connection.", 0)
        elif type_s == 1:
            t_s = threading.Thread(target=self.connMgr.newSConn,\
                    args=(top.c['host'], top.c['port'], top.c['maxConn'], 1800))
            t_s.start()
        else:
            #新线程创建客户端连接
            t_c = threading.Thread(target=self.connMgr.newCConn, \
                    args=(top.c['host'], top.c['port'], top.c['id'], top.c['name']))
            t_c.start()


        #修改连接状态并进行事件绑定
        top.connMgr.condition.wait()
        if top.connMgr.condition.acquire():
            if top.s:
                top.c['is_active'] = 1
                t_s = threading.Thread(target=self.connMgr.connHandler,args=(top.s, top.c))
                t_s.start()
            else:
                top.c['is_active'] = 0
            top.enterButton.Bind(wx.EVT_BUTTON, lambda e:top.SendMsg(top.s))
            top.connMgr.condition.notifyAll()
            top.connMgr.condition.release()
            top.connMgr.condition.release()
        self.Destroy()


## 
# Desc: 连接管理类
class connMgr():
    activeConn = []
    lock = threading.RLock()
    msg_queue = []
    
    #传入主窗口对象
    def __init__(self, parent):
        self.top = parent
    ## 
    # Desc: newSConn 创建新的服务器连接
    # 
    # @Param host 主机地址，通常为空
    # @Param port 监听端口
    # @Param maxConn 最大连接数
    # @Param timeout 连接等待时间
    # 
    # @Returns   成功创建的连接或0
    def newSConn(self, host, port, maxConn, s_timeout=300):
        self.condition.acquire()
        socket.setdefaulttimeout(s_timeout)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            self.top.refreshMsg('Fail to create socket:%s' % msg[1], 0)
            self.top.c['is_active'] = 0
        try:
            s.bind((host, int(port)))
        except socket.error, msg:
            self.top.refreshMsg("Failed to bind socket:%s" % msg[1], 0)
            self.top.c['is_active'] = 0
        try:
            s.listen(maxConn)
            self.top.refreshMsg("Waiting for connection...", 0)
            self.top.s = s
            self.top.c['is_active'] = 1
        except socket.timeout:
            self.top.refreshMsg("Connection Timeout.Exiting...", 0)
            self.top.c['is_active'] = 0
        except:
            pass
        self.condition.notifyAll()
        self.condition.release()
        

    ## 
    # Desc: newCConn 创建新的客户端连接
    # 
    # @Param host 主机
    # @Param port 端口号
    # @Param id 用户id
    # @Param name 用户名，默认匿名
    # 
    # @Returns   成功创建的连接或0
    def newCConn(self, host, port, id, name='client', c_timeout=300, c_retrytimes=10):
        #设置连接超时时间
        socket.setdefaulttimeout(c_timeout)
        retrytimes = 0
        #创建socket、获取主机ip
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            self.top.refreshMsg('Fail to create socket:%s' % msg[1], 0)
            return 0
        try:
            host_ip = socket.gethostbyname(host)
        except socket.gaierror:
            self.top.refreshMsg("Hostname can't be resolved.", 0)
            return 0
        #失败重连
        while retrytimes < c_retrytimes:
            try:
                self.top.refreshMsg("Connecting to server...", 0)
                s.connect((host_ip,int(port)))
                s.sendall("{'name':'%s','id':-1}" % name)
                self.top.refreshMsg("Waiting for response...", 0)
                while 1:
                    response = s.recv(8192)
                    if not response.strip(): continue
                    try:
                        exec 'r_dict = ' + response
                    except:
                    if r_dict['id']: break
                    self.condition.acquire()
                    self.condition.notifyAll()
                    self.condition.release()
            except socket.timeout:
                self.top.refreshMsg('Connection Timeout.Exiting...', 0)
                self.condition.acquire()
                self.condition.notifyAll()
                self.condition.release()
                return 0
            except socket.error, msg:
                self.top.refreshMsg('Connection Failed:%s' % msg[1], 0)
                self.condition.acquire()
                self.condition.notifyAll()
                self.condition.release()
                return 0
            if r_dict['id']:
                self.top.refreshMsg("Successfully connected to %s:%s" % (host_ip, port), 0)
                self.condition.acquire()
                self.top.c['id'] = r_dict['id']
                self.top.s = s
                self.top.msgArea.SetValue('')
                self.condition.notifyAll()
                self.condition.release()
                return s
            retrytimes += 1
        self.top.refreshMsg("Retried %s times,failed to connect to server." % retrytimes, 0)
        return 0

    #处理连接，创建线程
    def connHandler(self, s, c):
        if c['type_s']:
            while 1:
                conn, addr = s.accept()
                t_conn = threading.Thread(target=self.serverSend, args=(conn, addr[0], addr[1]))
                t_conn.start()
        else:
            t_recv = threading.Thread(target=self.top.recvMsg, args=(self.top.s,))
            t_recv.start()

    #新的线程，确认客户端连接，发送和同步消息
    def serverSend(self, conn, host, port):
        msg = self.recvAllMsg(conn)
        try:
            exec 'msg_dict = ' + msg
        except:
            self.top.refreshMsg('Failed to resolve msg from client.', 0)
        else:       
            name = msg_dict['name']
            id = msg_dict['id']
        #给连接分配一个独有的ID，并将连接放到活跃连接列表中
        if self.lock.acquire():
            if len(self.activeConn):
                activeID = [i['id'] for i in self.activeConn]
            else:
                activeID = []
            while 1:
                id = random.randint(2,5000)
                self.top.refreshMsg("id:%s" % id, 0)
                if not id in activeID:
                    break
            conn_info = {'id':id, 'name':name, 'host':host, 'port':port}
            self.activeConn.append(conn_info)
            conn.sendall(str(conn_info))
            self.top.refreshMsg("Connected:%s  %s:%s" % (name, host, port), 0)
            time.sleep(2)
            self.top.msgArea.SetValue('')
            self.lock.release()
            threading.Thread(target=self.serverRecv, args=(conn,)).start()
        while 1:
            try:
                conn.sendall(' ')
            except:
                sys.exit()
            #同步消息队列
            if self.condition.acquire():
                self.condition.wait()
                if len(self.msg_queue):
                    for i in range(len(self.msg_queue)): #遍历消息列表并发送消息
                        try:
                            if self.msg_queue[i]["id"] != id:
                                conn.sendall(str(self.msg_queue[i]))
                            self.msg_queue[i]['count'] += 1 #消息发送次数+1
                            if self.msg_queue[i]['count'] >= threading.activeCount() - 3:
                                    self.msg_queue.remove(self.msg_queue[i]) #当所有的线程都已发送本条消息，移除
                        except:
                                continue
            self.condition.release()

    def serverRecv(self, conn):
        #从客户端接收消息并添加到待发送队列中
        while 1:
            msg_str= self.recvAllMsg(conn)
            if msg_str:
                try:
                    exec 'msg_dict = ' + msg_str
                except:
                    self.top.refreshMsg('Failed to resolve msg from client.', 0)
                    continue
                else:
                    if self.condition.acquire():
                        self.msg_queue.append(msg_dict)
                        self.top.refreshMsg(msg_dict)
                        self.condition.notifyAll()
                        self.condition.release()
            time.sleep(0.5)

    ## 
    # Desc: recvAllMsg 获取全部响应数据
    # 
    # @Param conn 连接
    # 
    # @Returns   数据字符串
    def recvAllMsg(self, conn):
        data = conn.recv(self.top.c['maxMsgSize'])
        return data.strip()
        





app = App(False)
app.MainLoop()
