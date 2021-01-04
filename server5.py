import numpy as np

import socket

import pickle

HOST = '127.0.0.1'

PORT = 50000

i = 0

class Server():

    def __init__(self):

        self.weight = np.array([[0,0,0,0,0,2,2,0,0,0,1,0,0,0,0,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0]
                                ,[0,0,0,0,0,1,1,0,0,0,2,0,0,0,0,0,0,3,1,0,0,1,0,0,0,0,0,0,1,0]
                                ,[1,1,0,0,2,0,0,0,0,0,1,0,0,0,0,0,1,0,0,2,0,0,0,0,0,1,0,0,0,1]
                                ,[0,0,2,2,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0]
                                ,[0,0,0,1,0,0,0,0,0,0,0,1,0,1,5,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0]
                                ,[0,0,1,1,0,0,0,0,0,0,0,1,0,1,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                ,[0,0,2,2,0,0,0,0,0,0,0,0,1,0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
                                ,[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,4,0,0,4,0,0,0,0,0,0,0,0,0,1]
                                ,[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,1,0,1]
                                ,[0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,2,1,0,2,0,0,0,1,0,0,0,1,0,0]
                                ,[1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0]
                                ,[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0]
                                ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,4,0,0,0,1,0,0,0,1,0,0]
                                ,[0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,2,0,0,2,0,0,0,1,0,0,0,2,0,0]
                                ,[0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,2,0,1,1,0,0,0,0,0,0,0,0,1,1]
                                ,[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,2,0,0,0,1,0,0,0,1,1,1]
                                ,[1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0]
                                ,[0,0,0,0,0,2,2,2,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
                                ,[1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0]
                                ,[1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0]
                                ,[1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,0,0,0,0]
                                ,[3,2,0,0,0,2,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
                                ,[3,2,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0]
                                ,[3,2,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]
                                ,[1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0]
                                ,[1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0]
                                ,[1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0]
                                ,[1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0]
                                ,[1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0]
                                ,[1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0]])



    def setList(self,list):

        self.studentList = list

        print(self.studentList)



    def judge(self):
      global i
      i += 1
      self.studentList = list(map(lambda x: x/i,self.studentList))
      self.resultList = np.dot(self.weight,self.studentList)



def main():



    server = Server()

    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    s.bind((HOST, PORT))



    while True:

        s.listen()



        client, _ = s.accept()

        recv_data = client.recv(8192)

        recv_data = pickle.loads(recv_data)



        print("以下のデータをユーザから受信しました\n")

        print("---------------------------------------------")

        server.setList(recv_data)

        print("---------------------------------------------\n")



        server.judge()



        print("以下のデータをユーザへ送信します\n")

        print("---------------------------------------------")

        print(server.resultList)

        print("---------------------------------------------\n")  



        send_data = pickle.dumps(server.resultList)

        client.send(send_data)



    client.close()



if __name__ == '__main__':

    main()