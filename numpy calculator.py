import numpy as np
class NpCalc:
    def __init__(self):
        self.A=np.arange(-20,20)
        self.B=np.arange(-40,0)
        self.matrix=""
        self.dime=0
        self.mode=""
        self.inc=0
        self.n_col=7
        self.n_row=5
        
    def assigning(self):
        self.a=np.array(self.A)
        self.b=np.array(self.B)
        self.ranging=[int(self.dime[i]) for i in range(len(self.dime))]
        
    def reshaping(self):
        self.a_r=np.reshape(self.a,self.ranging)
        self.b_r=np.reshape(self.b,self.ranging)
        return self.a_r
        
    def add(self):
        self.adding = np.add(self.a,self.b)
        return np.reshape(self.adding,self.ranging)
    
    def subtract(self):
        self.subtracting = np.subtract(self.a,self.b)
        return np.reshape(self.subtracting,self.ranging)
    
    def multiply(self,mode):
        if mode==str("element_wise"):
            self.multiplying = np.multiply(self.a,self.b)
            return np.reshape(self.multiplying,self.ranging)
        
        elif mode==str("dot"):
            #self.multiplying=np.dot(self.a,self.b)
            self.multiplying = np.dot(np.reshape(self.a,self.ranging),np.reshape(self.b,self.ranging))
            return self.multiplying#[int(self.dime[i]) for i in range(len(self.dime))])
        
    def divide(self):
        self.dividing = np.divide(self.a,self.b)
        return np.reshape(self.dividing,self.ranging)
    
    def transpose(self,prefer):
        if prefer==1:
            return np.reshape(self.a,self.ranging).T
        elif prefer==2:
            return np.reshape(self.b,self.ranging).T
    
    def sort(self,list_num):
        self.soorting=sorted(list_num,key=lambda x:x[0])
        return self.soorting
    
    def np_abs(self,prefer):
        if prefer==1:
            self.absolutee=np.array(list(map(lambda x:np.absolute(x),self.A)))
            return np.reshape(self.absolutee,self.ranging)
        elif prefer==2:
            self.absolutee=np.array(list(map(lambda x:np.absolute(x),self.B)))
            return np.reshape(self.absolutee,self.ranging)
        
    def negative_out(self,prefer):
        if prefer==1:
            self.negativea=np.array(list(filter(lambda x:x>=0,self.A)))
            return self.negativea
        elif prefer==2:
            self.negativeb=np.array(list(filter(lambda x:x>=0,self.B)))
            return self.negativeb
        
    def negative_out_a(self,prefer):
        if prefer==1:
            return np.reshape(self.a.clip(0),self.ranging)
        elif prefer==2:
            return np.reshape(self.b.clip(0),self.ranging)
    
    def increment(self,incre,prefer):
        if prefer==1:
            self.increa=np.array(list(map(lambda x:x+int(incre),self.A)))
            return np.reshape(self.increa,self.ranging)
        elif prefer==1:
            self.increb=np.array(list(map(lambda x:x+int(incre),self.B)))
            return np.reshape(self.increb,self.ranging)
        
    def get_slice(self,prefer):
        self.reshaping()
        self.row=int(input("enter which row you want:"))
        self.column=int(input("enter which column you want:"))
        if prefer==1:
            return self.a_r[self.row,self.column]
        elif prefer==2:
            return self.a_r[self.row,self.column]
        
    def modify(self):
        ask=str(input("do you really want to change the array A and B,if yes then type 'yes' an if not type 'exit':"))
        print ("NOTE:/nIf you want to keep the array same the write 'same'" )
        if ask=="yes":
            self.A=input("enter the array of A here,separated by commas")
            self.B=input("enter the array of B here,separated by commas")
        if ask=="exit":
            exit
        else:
            print ("wrong input")
        NC.assigning()
        
    def Input(self):
        self.A=[int(i) for i in input("enter the array of A here,separated by commas:").split(' ')]
        self.B=[int(i) for i in input("enter the array of B here,separated by commas:").split(' ')]
        self.dime=input("enter the values of parameters in which you want to reshape array,separated by spaces:").split()
        NC.assigning()
        
NC=NpCalc()
NC.Input()
        
        
        