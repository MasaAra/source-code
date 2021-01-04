from phe import paillier as pl

import numpy as np

import socket

import pickle

import tkinter as tk

import tkinter.ttk as ttk

import pandas as pd


HOST = '127.0.0.1'

PORT = 50000

N = 30

BG = 'pink'

FONT = ("メイリオ", "9", "bold")





class Application(tk.Frame):

    def __init__(self,master):

        super().__init__(master)

        self.pack()

        master.withdraw()



        self.window = []

        self.user = []



        for i in ["ユーザ"]:

            self.window.append(tk.Toplevel())

            self.user.append(User(self.window[len(self.window)-1],i))



class User(tk.Frame):

    def __init__(self,master,name):

        super().__init__(master)

        self.pack()



        self.name = name



        self.pk, self.sk = pl.generate_paillier_keypair(n_length=256)

        self.score = [0] * N

        self.encScore = [0] * N

        self.decScore = [0] * N

        self.resultScore = [0] * N

        self.subList = ["セブン＆アイ・ホールディンクス","リクルートホールディンクス","信越化学工業","花王","アステラス製薬","第一三共","武田薬品工業"
                        ,"ダイキン工業","日立製作所","日本電産"
                        ,"ソニー","キーエンス","ファナック","村田製作所","トヨタ自動車","HONDA","HOYA","任天堂","伊藤忠商事","三井物産"
                        ,"三菱商事","三菱UFJフィナンシャルグループ","三井住友フィナンシャルグループ"
                        ,"みずほフィナンシャルグループ","東京海上ホールディンクス","東海旅客鉄道","日本電信電話","KDDI","NTTドコモ","ソフトバンクグループ"]





        master.geometry("900x500")

        master.title("進路評価システム")

        master.config(bg=BG)



        self.lblUser = tk.Label(master, text = "【"+self.name + "】", bg= BG, font = FONT)

        self.lblUser.place(x=20,y=10)



        self.lbl1 = tk.Label(master, width=20, text = "経済学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl1.place(x=75,y=50)



        self.com1 = ttk.Combobox(master, state='readonly', width=5)

        self.com1["values"] = (0,1,2,3,4)

        self.com1.current(0)

        self.com1.place(x=240,y=50)



        self.lbl2 = tk.Label(master, width=20, text = "英語：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl2.place(x=75,y=80)



        self.com2 = ttk.Combobox(master, state='readonly', width=5)

        self.com2["values"] = (0,1,2,3,4)

        self.com2.current(0)

        self.com2.place(x=240,y=80)



        self.lbl3 = tk.Label(master, width=22, text = "化学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl3.place(x=59,y=110)

    

        self.com3 = ttk.Combobox(master, state='readonly', width=5)

        self.com3["values"] = (0,1,2,3,4)

        self.com3.current(0)

        self.com3.place(x=240,y=110)
        
        
        
        self.lbl4 = tk.Label(master, width=22, text = "生物学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl4.place(x=59,y=140)



        self.com4 = ttk.Combobox(master, state='readonly', width=5)

        self.com4["values"] = (0,1,2,3,4)

        self.com4.current(0)

        self.com4.place(x=240,y=140)
        
        
        
        self.lbl5 = tk.Label(master, width=20, text = "物理学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl5.place(x=75,y=170)



        self.com5 = ttk.Combobox(master, state='readonly', width=5)

        self.com5["values"] = (0,1,2,3,4)

        self.com5.current(0)

        self.com5.place(x=240,y=170)



        self.lbl6 = tk.Label(master, width=22, text = "コンピュータプログラミング：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl6.place(x=59,y=200)



        self.com6 = ttk.Combobox(master, state='readonly', width=5)

        self.com6["values"] = (0,1,2,3,4)

        self.com6.current(0)

        self.com6.place(x=240,y=200)
        
        
        
        self.lbl7 = tk.Label(master, width=20, text = "ソフトウェア工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl7.place(x=75,y=230)



        self.com7 = ttk.Combobox(master, state='readonly', width=5)

        self.com7["values"] = (0,1,2,3,4)

        self.com7.current(0)

        self.com7.place(x=240,y=230)
        
        
        
        self.lbl8 = tk.Label(master, width=20, text = "CGプログラミング：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl8.place(x=75,y=260)



        self.com8 = ttk.Combobox(master, state='readonly', width=5)

        self.com8["values"] = (0,1,2,3,4)

        self.com8.current(0)

        self.com8.place(x=240,y=260)
        
        
        self.lbl9 = tk.Label(master, width=20, text = "人工知能論：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl9.place(x=75,y=290)



        self.com9 = ttk.Combobox(master, state='readonly', width=5)

        self.com9["values"] = (0,1,2,3,4)

        self.com9.current(0)

        self.com9.place(x=240,y=290)
        
            
        
        self.lbl10 = tk.Label(master, width=20, text = "医用画像工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl10.place(x=75,y=320)



        self.com10 = ttk.Combobox(master, state='readonly', width=5)

        self.com10["values"] = (0,1,2,3,4)

        self.com10.current(0)

        self.com10.place(x=240,y=320)
        
        
        self.lbl11 = tk.Label(master, width=20, text = "数理統計学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl11.place(x=320,y=50)



        self.com11 = ttk.Combobox(master, state='readonly', width=5)

        self.com11["values"] = (0,1,2,3,4)

        self.com11.current(0)

        self.com11.place(x=485,y=50)
        
        
        
        self.lbl12 = tk.Label(master, width=20, text = "栽培：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl12.place(x=320,y=80)



        self.com12 = ttk.Combobox(master, state='readonly', width=5)

        self.com12["values"] = (0,1,2,3,4)

        self.com12.current(0)

        self.com12.place(x=485,y=80)
        
        
        
        self.lbl13 = tk.Label(master, width=20, text = "資格英語(TOEIC)：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl13.place(x=320,y=110)



        self.com13 = ttk.Combobox(master, state='readonly', width=5)

        self.com13["values"] = (0,1,2,3,4)

        self.com13.current(0)

        self.com13.place(x=485,y=110)
        
        
        
        self.lbl14 = tk.Label(master, width=20, text = "微生物工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl14.place(x=320,y=140)



        self.com14 = ttk.Combobox(master, state='readonly', width=5)

        self.com14["values"] = (0,1,2,3,4)

        self.com14.current(0)

        self.com14.place(x=485,y=140)
        
        
        
        self.lbl15 = tk.Label(master, width=20, text = "生化学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl15.place(x=320,y=170)



        self.com15 = ttk.Combobox(master, state='readonly', width=5)

        self.com15["values"] = (0,1,2,3,4)

        self.com15.current(0)

        self.com15.place(x=485,y=170)
        
        
        
        self.lbl16 = tk.Label(master, width=20, text = "法学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl16.place(x=320,y=200)



        self.com16 = ttk.Combobox(master, state='readonly', width=5)

        self.com16["values"] = (0,1,2,3,4)

        self.com16.current(0)

        self.com16.place(x=485,y=200)
        
        
        
        self.lbl17 = tk.Label(master, width=20, text = "電子工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl17.place(x=320,y=230)



        self.com17 = ttk.Combobox(master, state='readonly', width=5)

        self.com17["values"] = (0,1,2,3,4)

        self.com17.current(0)

        self.com17.place(x=485,y=230)
        
        
        
        self.lbl18 = tk.Label(master, width=20, text = "Webプログラミング：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl18.place(x=320,y=260)



        self.com18 = ttk.Combobox(master, state='readonly', width=5)

        self.com18["values"] = (0,1,2,3,4)

        self.com18.current(0)

        self.com18.place(x=485,y=260)
        
        
        
        self.lbl19 = tk.Label(master, width=20, text = "3D-CAD演習：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl19.place(x=320,y=290)



        self.com19 = ttk.Combobox(master, state='readonly', width=5)

        self.com19["values"] = (0,1,2,3,4)

        self.com19.current(0)

        self.com19.place(x=485,y=290)
        

        
        self.lbl20 = tk.Label(master, width=20, text = "メカトロニクス：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl20.place(x=320,y=320)



        self.com20 = ttk.Combobox(master, state='readonly', width=5)

        self.com20["values"] = (0,1,2,3,4)

        self.com20.current(0)

        self.com20.place(x=485,y=320)
        
                
        self.lbl21 = tk.Label(master, width=20, text = "心理学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl21.place(x=555,y=50)



        self.com21 = ttk.Combobox(master, state='readonly', width=5)

        self.com21["values"] = (0,1,2,3,4)

        self.com21.current(0)

        self.com21.place(x=720,y=50)
        
        
        
        self.lbl22 = tk.Label(master, width=20, text = "ネットワーク演習：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl22.place(x=555,y=80)



        self.com22 = ttk.Combobox(master, state='readonly', width=5)

        self.com22["values"] = (0,1,2,3,4)

        self.com22.current(0)

        self.com22.place(x=720,y=80)
        
        
        
        self.lbl23 = tk.Label(master, width=20, text = "ビジネスイングリッシュ：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl23.place(x=555,y=110)



        self.com23 = ttk.Combobox(master, state='readonly', width=5)

        self.com23["values"] = (0,1,2,3,4)

        self.com23.current(0)

        self.com23.place(x=720,y=110)
        
        
        
        self.lbl24 = tk.Label(master, width=20, text = "通信工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl24.place(x=555,y=140)



        self.com24 = ttk.Combobox(master, state='readonly', width=5)

        self.com24["values"] = (0,1,2,3,4)

        self.com24.current(0)

        self.com24.place(x=720,y=140)
        
        
        
        self.lbl25 = tk.Label(master, width=20, text = "分析化学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl25.place(x=555,y=170)



        self.com25 = ttk.Combobox(master, state='readonly', width=5)

        self.com25["values"] = (0,1,2,3,4)

        self.com25.current(0)

        self.com25.place(x=720,y=170)
        
        
        
        self.lbl26 = tk.Label(master, width=20, text = "経営学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl26.place(x=555,y=200)



        self.com26 = ttk.Combobox(master, state='readonly', width=5)

        self.com26["values"] = (0,1,2,3,4)

        self.com26.current(0)

        self.com26.place(x=720,y=200)
        
        
        
        self.lbl27 = tk.Label(master, width=20, text = "医用工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl27.place(x=555,y=230)



        self.com27 = ttk.Combobox(master, state='readonly', width=5)

        self.com27["values"] = (0,1,2,3,4)

        self.com27.current(0)

        self.com27.place(x=720,y=230)
        
        
        
        self.lbl28 = tk.Label(master, width=20, text = "システム工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl28.place(x=555,y=260)



        self.com28 = ttk.Combobox(master, state='readonly', width=5)

        self.com28["values"] = (0,1,2,3,4)

        self.com28.current(0)

        self.com28.place(x=720,y=260)
        
        
        
        self.lbl29 = tk.Label(master, width=20, text = "3DCG演習：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl29.place(x=555,y=290)



        self.com29 = ttk.Combobox(master, state='readonly', width=5)

        self.com29["values"] = (0,1,2,3,4)

        self.com29.current(0)

        self.com29.place(x=720,y=290)
        

        
        self.lbl30 = tk.Label(master, width=20, text = "制御工学：", anchor='e', justify='right', bg=BG, font = FONT)

        self.lbl30.place(x=555,y=320)



        self.com30 = ttk.Combobox(master, state='readonly', width=5)

        self.com30["values"] = (0,1,2,3,4)

        self.com30.current(0)

        self.com30.place(x=720,y=320)



        self.button = tk.Button(master,text="送信",command=self.buttonClick,width=10, font = FONT)

        self.button.place(x=405, y=370)

        self.button.config(fg="black", bg="skyblue")



        self.lblDec = tk.Label(master,text = "復号結果：", bg=BG, font = FONT)

        self.lblDec.place(x=20,y=400)



        self.entDec = tk.Entry(master, width=125)

        self.entDec.place(x=20,y=420)



        self.lblJob = tk.Label(master,text = self.name+"さんのおすすめは：", bg=BG, font = FONT)

        self.lblJob.place(x=20,y=440)



        self.entJob = tk.Entry(master, width=30)

        self.entJob.place(x=20,y=460)



    def buttonClick(self):

        self.entDec.delete(0, tk.END)

        self.entJob.delete(0, tk.END)

        self.setScore(int(self.com1.get()),int(self.com2.get()),int(self.com3.get()),int(self.com4.get()),int(self.com5.get()),int(self.com6.get()),
                      int(self.com7.get()),int(self.com8.get()),int(self.com9.get()),int(self.com10.get()),int(self.com11.get()),int(self.com12.get()),
                      int(self.com13.get()),int(self.com14.get()),int(self.com15.get()),int(self.com16.get()),int(self.com17.get()),int(self.com18.get()),
                      int(self.com19.get()),int(self.com20.get()),int(self.com21.get()),int(self.com22.get()),int(self.com23.get()),int(self.com24.get()),
                      int(self.com25.get()),int(self.com26.get()),int(self.com27.get()),int(self.com28.get()),int(self.com29.get()),int(self.com30.get()))



        self.encList()



        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.connect((HOST, PORT))



        print(self.name + "の暗号化された成績データをサーバへ送信します\n")



        self.send_data = pickle.dumps(self.encScore)

        self.s.send(self.send_data)



        self.recv_data = self.s.recv(8192)

        self.recv_data = pickle.loads(self.recv_data)



        print(self.name +"が暗号化された判定データをサーバから受信しました\n")



        self.decList(self.recv_data)



        self.recSub()





    def setScore(self,seiseki1,seiseki2,seiseki3,seiseki4,seiseki5,seiseki6,seiseki7,seiseki8,seiseki9,seiseki10
                 ,seiseki11,seiseki12,seiseki13,seiseki14,seiseki15,seiseki16,seiseki17,seiseki18,seiseki19,seiseki20
                 ,seiseki21,seiseki22,seiseki23,seiseki24,seiseki25,seiseki26,seiseki27,seiseki28,seiseki29,seiseki30):

        self.score[0] = self.score[0]+seiseki1

        self.score[1] = self.score[1]+seiseki2

        self.score[2] = self.score[2]+seiseki3
        
        self.score[3] = self.score[3]+seiseki4

        self.score[4] = self.score[4]+seiseki5

        self.score[5] = self.score[5]+seiseki6
        
        self.score[6] = self.score[6]+seiseki7

        self.score[7] = self.score[7]+seiseki8

        self.score[8] = self.score[8]+seiseki9
        
        self.score[9] = self.score[9]+seiseki10

        self.score[10] = self.score[10]+seiseki11

        self.score[11] = self.score[11]+seiseki12
        
        self.score[12] = self.score[12]+seiseki13

        self.score[13] = self.score[13]+seiseki14

        self.score[14] = self.score[14]+seiseki15
        
        self.score[15] = self.score[15]+seiseki16

        self.score[16] = self.score[16]+seiseki17

        self.score[17] = self.score[17]+seiseki18
        
        self.score[18] = self.score[18]+seiseki19

        self.score[19] = self.score[19]+seiseki20
        
        self.score[20] = self.score[20]+seiseki21

        self.score[21] = self.score[21]+seiseki22
        
        self.score[22] = self.score[22]+seiseki23

        self.score[23] = self.score[23]+seiseki24

        self.score[24] = self.score[24]+seiseki25
        
        self.score[25] = self.score[25]+seiseki26

        self.score[26] = self.score[26]+seiseki27

        self.score[27] = self.score[27]+seiseki28
        
        self.score[28] = self.score[28]+seiseki29

        self.score[29] = self.score[29]+seiseki30



    def encList(self):

        for i in range(len(self.score)):

            self.encScore[i] = self.pk.encrypt(self.score[i])



    def decList(self,list):

        for i in range(len(list)):

            self.resultScore[i] = self.sk.decrypt(list[i])
            self.resultScore[i] = round(self.resultScore[i],1)
            



    def recSub(self):

        self.entDec.insert(tk.END, self.resultScore)

        self.entJob.insert(tk.END, self.subList[np.argmax(self.resultScore)])







def main():



    win = tk.Tk()

    app = Application(win)

    app.mainloop()





if __name__ == '__main__':

    main()