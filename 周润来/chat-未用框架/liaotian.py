import socket
import struct
import hashlib
import threading,random

def sendMessage(message):
    global connectionlist
    for connection in connectionlist.values():
        connection.send("\x00%s\xFF" % message)

def deleteconnection(item):
    global connectionlist
    del connectionlist['connection'+item]

class WebSocket(threading.Thread):
    def __init__(self,conn,index,name,remote, path="/"):
        threading.Thread.__init__(self)
        self.conn = conn
        self.index = index
        self.name = name
        self.remote = remote
        self.path = path
        self.buffer = ""

    def run(self):
        print 'Socket%s Start!' % self.index
        headers = {}
        self.handshaken = False

        while True:
            if self.handshaken == False:
                print 'Socket%s Start Handshaken with %s!' % (self.index,self.remote)
                self.buffer += self.conn.recv(1024)
                if self.buffer.find('\r\n\r\n') != -1:
                    header, data = self.buffer.split('\r\n\r\n', 1)
                    for line in header.split("\r\n")[1:]:
                        key, value = line.split(": ", 1)
                        headers[key] = value

                    headers["Location"] = "ws://%s%s" %(headers["Host"], self.path)
                    key1 = headers["Sec-WebSocket-Key1"]
                    key2 = headers["Sec-WebSocket-Key2"]
                    if len(data) < 8:
                        data += self.conn.recv(8-len(data))
                    key3 = data[:8]
                    self.buffer = data[8:]
                    token = self.generate_token(key1, key2, key3)

                    handshake = '\
							HTTP/1.1 101 Web Socket Protocol Handshake\r\n\
							Upgrade: WebSocket\r\n\
							Connection: Upgrade\r\n\
							Sec-WebSocket-Origin: %s\r\n\
							Sec-WebSocket-Location: %s\r\n\r\n\
							' %(headers['Origin'], headers['Location'])

                    self.conn.send(handshake+token)
                    self.handshaken = True
                    print 'Socket%s Handshaken with %s success!' % (self.index,self.remote)
                    sendMessage('Welcome, '+self.name+' !')
            else:
                self.buffer += self.conn.recv(64)
                if self.buffer.find("\xFF")!=-1:
                    s = self.buffer.split("\xFF")[0][1:]
                    if s=='quit':
                        print 'Socket%s Logout!' % (self.index)
                        sendMessage(self.name+' Logout')
                        deleteconnection(str(self.index))
                        self.conn.close()
                        break
                    else:
                        print 'Socket%s Got msg:%s from %s!' % (self.index,s,self.remote)
                        sendMessage(self.name+':'+s)
                    self.buffer = ""

    def generate_token(self, key1, key2, key3):
        num1 = int("".join([digit for digit in list(key1) if digit.isdigit()]))
        spaces1 = len([char for char in list(key1) if char == " "])
        num2 = int("".join([digit for digit in list(key2) if digit.isdigit()]))
        spaces2 = len([char for char in list(key2) if char == " "])

        combined = struct.pack(">II", num1/spaces1, num2/spaces2) + key3
        return hashlib.md5(combined).digest()

class WebSocketServer(object):
    def __init__(self):
        self.socket = None
    def begin(self):
        print 'WebSocketServer Start!'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("127.0.0.1",80))
        self.socket.listen(80)

        global connectionlist

        i=0
        while True:
            connection, address = self.socket.accept()

            username=address[0]

            newSocket = WebSocket(connection,i,username,address)
            newSocket.start()
            connectionlist['connection'+str(i)]=connection
            i = i + 1

if __name__ == "__main__":
    server = WebSocketServer()
    server.begin()