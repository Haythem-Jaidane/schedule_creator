# -*- coding: utf-8 -*-
#jocker 2.0

from fpdf import FPDF 
from datetime import date,timedelta

class create_table:
    
    duration=0
    number=0
    start_hour=0
    end_hour=0
    start_date=""
    end_date=""
    week_day=0
    data=[]
    date_tuple=""
    file_name="sans_titre"
    Error=False
    
    def date_system(self,str_date):
        
        self.start_date=date(int(str_date[:4]),int(str_date[5:7]),int(str_date[8:]))
        self.week_day=self.start_date.weekday()
        self.end_date=self.start_date+timedelta(days=self.number)
        self.date_tuple=(str(self.start_date.day)+"/"+str(self.start_date.month),
                         str(self.end_date.day)+"/"+str(self.end_date.month))
        
        
    def create_data(self):
        
        date_str=[("Monday",1),("Tuesday",1),("Wednesday",1)
                ,("Thursday",1), ("Friday",1), ("Saturday",1),("Sunday",1)]
        
        date_data=[("    ",1)]
        for z in range(self.week_day,self.week_day+self.number):
            date_data.append(date_str[z%7])
        self.data.append(date_data)
        for i in range(self.start_hour,self.end_hour):
            row=[(str(i)+"h to "+str(i+1)+"h",1)]
            for g in range(self.number):
                row.append(["free",1])
            self.data.append(row)
    
    def web2pdf(self,to_say=""):
        
        pdf_object=FPDF()
        
        pdf_object.set_font("Arial",size=15)
        pdf_object.add_page(orientation ="L")
        
        pdf_object.ln(5)
        pdf_object.cell(pdf_object.w,txt="From "+self.date_tuple[0]+" to "+self.date_tuple[1],align="C")
        pdf_object.ln(10)
        
        widht = pdf_object.w / 10
        height = pdf_object.font_size*2
        
        i=0
        history=[[0,True] for l in range(self.number+1)]
        while(i<=self.duration):
            j=0
            while(j<=self.number):
                if(history[j][0]==0):
                    history[j][1]=True
                    history[j][0]=self.data[i][j][1]
                if(history[j][0]!=1):
                    if(j==self.duration and history[j][1]):
                        pdf_object.cell(widht,height*history[j][0],
                                txt=self.data[i][j][0],border='LRB',align="C")
                    elif(j!=self.duration and history[j][1]):
                        pdf_object.cell(widht,height*history[j][0],
                                txt=self.data[i][j][0],border='LR',align="C")
                    else:
                        pdf_object.cell(widht,height*1,
                                txt='',border='LR',align="C")
                    history[j][1]=False
                else:
                    if(history[j][1]):
                        pdf_object.cell(widht,height*history[j][0],
                                txt=self.data[i][j][0],border='LTRB',align="C")
                    else:
                        pdf_object.cell(widht,height*1,
                                txt="",border='LRB',align="C")
                history[j][0]-=1
                j=j+1
            i=i+1
            pdf_object.ln(height)
        
        pdf_object.ln(20)
        pdf_object.cell(pdf_object.w,txt=to_say)
            
        pdf_object.output("../uploads/"+self.file_name+".pdf")