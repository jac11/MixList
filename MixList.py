#!/sur/bin/env python
import os
import sys
import json
import argparse
with  open ('Banner','r') as readbanner:
      banner = readbanner.read()
      print(banner)    
class Gen_List:
     def __init__(self):   
                         
         self.control()
         self.List_Gen()  
         self.JSON_FORMAT()       
     def List_Gen(self): 
          self.path = self.args.Outlist+'_Mix_pass'
          self.path2 = self.args.Outlist+'_Mix_UserName'         
          if os.path.exists(self.path) and os.path.exists(self.path2) :
             os.remove(self.path)
             os.remove(self.path2)
             with open (self.path,'w') as List :
                  with open (self.path2,'w') as List :
                       pass
          Count = 0                         
          for  i in range(int(self.args.Repete/3+1)):
               with open (self.path2,'a') as List :
                    if Count ==  int(self.args.Repete/3+1) :
                        break
                    else:   
                        MixUserName = List.write(self.args.MyUserName +'\n'+self.args.VactimUser +'\n'+self.args.VactimUser +'\n')                                         
          count = 0 
          Num1  = 1
          Num2  = 2
          try: 
              with open (self.args.passordlist,'r') as readpass :
                    PassowordList = readpass.readlines()
                    PassNumber = int(self.args.Repete/3)
              with open (self.path,'w') as finsh :
                   MixPassList = finsh.write(self.args.Mypassord+'\n'+str(PassowordList[0])+str(PassowordList[0]))    
              for Pass in  PassowordList :
                with open (self.path,'a') as finsh :
                   MixPassList = finsh.write(self.args.Mypassord+'\n'+str(PassowordList[Num1])+ str(PassowordList[Num2]) )
                   count +=1
                   Num1 = Num1+2 
                   Num2 = Num2+2 
                   if count == int(self.args.Repete/3) :
                     break   
          except FileNotFoundError  as A :  
                 print('[!] Error : ', A )
                 exit()                                  
          except IndexError :
              with open (self.path,'a') as finsh :
                 MixPassList = finsh.write(self.args.Mypassord+'\n'+str(PassowordList[-2])+str(PassowordList[-1] ) )                                       
          print('[+] MixList generate the Mix UserName Done ')
          print('[+] MixList generate the Mix Passoword List  Done ')
          if  not self.args.Json:
              exit()
     def JSON_FORMAT(self):
         try:
             if self.args.Json and self.args.File and\
             self.args.File == self.args.Outlist : 
                   with open (self.path2,'r')as readFile:
                        Json_F = str(readFile.readlines()).replace('\n','').replace('\\n','')
                        Json_format = json.dumps(Json_F)
                        with open(self.path2+".json" ,'w') as jwrite:
                             jwrite.write(Json_format)  
                   with open (self.path,'r')as readFile:
                        Json_F = str(readFile.readlines()).replace('\n','').replace('\\n','')
                        Json_format = json.dumps(Json_F)
                        with open(self.path+".json" ,'w') as jwrite:
                             jwrite.write(Json_format)
             elif  self.args.Json and self.args.File and\
             self.args.File != self.args.Outlist :
                   with open (self.args.File,'r')as readFile:
                        Json_F = str(readFile.readlines()).replace('\n','').replace('\\n','')
                        Json_format = json.dumps(Json_F)
                        with open(self.args.File+".json" ,'w') as jwrite:
                             jwrite.write(Json_format) 
         except FileNotFoundError  as A :  
                 print('[!] Error : ', A )
                 exit()                                                                                          
     def control(self):        
        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
        parser.add_argument("-VU  ",'--VactimUser'  , action=None    ,required=True          ,help =" add victim username to Create UserName List") 
        parser.add_argument("-MU  ","--MyUserName"  , action=None    ,required=True          ,help =" add your real  account UserName To mix with Victam UserName") 
        parser.add_argument("-W   ","--passordlist" , action=None    ,required=True          ,help =" self.path of the Oragnail Password List")
        parser.add_argument("-J   ","--Json"        , action='store_true',required=False     ,help =" self.path of the Oragnail Password List")
        parser.add_argument("-F   ","--File"        , action=None    ,required=False          ,help =" the file do you like to be jsoin format")
        parser.add_argument("-R   ","--Repete"      , action=None    ,required=True ,type=int,help =" Length Of the UserName List And Password List To generate")
        parser.add_argument("-MP  ","--Mypassord"   , action=None    ,required=True          ,help =" add Your real acount Password To can login after every two Time rowang Try ") 
        parser.add_argument("-O   ","--Outlist"     , action=None    ,required=True          ,help =" add the file name for New lists will generate ")
        self.args = parser.parse_args()
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()        
            exit()  
if __name__=='__main__':
          Gen_List()
