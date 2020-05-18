# -*- coding: utf-8 -*-
#jocker 2.0

from fpdf import FPDF 


class create_table:
    
    duration=0
    number=0
    
    def create_data(self,from_,to,num_day):
        num_day=int(num_day)
        self.duration=int(to)-int(from_)
        self.number=num_day
        data=[
                [("    ",1),("Monday",1),("Tuesday",1),("Wednesday",1)
                ,("Thursday",1), ("Friday",1), ("Saturday",1),("Sunday",1)]
            ]
        data=data[:num_day]
        for i in range(int(from_),int(to)):
            row=[(str(i)+"h to "+str(i+1)+"h",1)]
            for g in range(num_day):
                row.append(["free",1])
            data.append(row)
        return data
    
    def web2pdf(self,data,date,name="sanstitre",to_say=""):
        
        pdf_object=FPDF()
        
        pdf_object.set_font("Arial",size=20)
        pdf_object.add_page(orientation ="L")
        
        pdf_object.ln(5)
        pdf_object.cell(pdf_object.w,txt="From "+date[0]+" to "+date[1],align="C")
        pdf_object.ln(10)
        
        widht = pdf_object.w / 7.5
        height = pdf_object.font_size*2
        
        for row in data:
            for col in row:
                k='LTRB'
                l=col[1]
                if l>1:
                    k='LTR'
                elif l==0:
                    k='LR'
                pdf_object.cell(widht,height*l,
                                txt=col[0],border=k,align="C")
            pdf_object.ln(height*l)
        
        pdf_object.ln(20)
        pdf_object.cell(pdf_object.w,txt=to_say)
            
        pdf_object.output(name+".pdf")