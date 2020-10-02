from flask import Flask,render_template,request,send_file,redirect
import program_manger as pm
import os,time


app=Flask(__name__,template_folder="../web_page",static_folder="../style")
obj=pm.create_table()

@app.route('/')

def settings():
    for i in os.listdir("../uploads"):
        if time.time()-os.path.getmtime("../uploads/"+i)>900:
            os.remove("../uploads/"+i)
    return render_template("first.html",error={"er_bool":obj.Error})

@app.route('/create',methods=['POST'])

def create():
    try:
        start=request.form["start"]
        obj.file_name=request.form["name"]
        obj.number=int(request.form["day_number"])
        obj.start_hour=int(request.form["wakeup"])
        obj.end_hour=int(request.form["sleep"])
        obj.duration=int(request.form["sleep"])-int(request.form["wakeup"])
        obj.date_system(start)
        obj.create_data()
        data_table={"table":obj.data,"num":obj.number,"duration":obj.duration}
        obj.Error=False
        return render_template("index.html",table=data_table)
    except:
        obj.Error=True
        return redirect('/')
    start=request.form["start"]
    obj.file_name=request.form["name"]
    obj.number=int(request.form["day_number"])
    obj.start_hour=int(request.form["wakeup"])
    obj.end_hour=int(request.form["sleep"])
    obj.duration=int(request.form["sleep"])-int(request.form["wakeup"])
    obj.date_system(start)
    obj.create_data()
    data_table={"table":obj.data,"num":obj.number,"duration":obj.duration}
    obj.Error=False
    return render_template("index.html",table=data_table)

@app.route('/pdf_create',methods=['POST'])

def made():
    for i in range(1,obj.number+1):
        for l in range(1,obj.duration+1):
            obj.data[l][i][0]=request.form[str(l)+str(i)+"time"]
            obj.data[l][i][1]=int(request.form[str(l)+str(i)+"duration"])
    obj.web2pdf()
    return render_template("final_page.html")

@app.route("/download",methods=["POST","GET"])

def download():
    return send_file('../uploads/'+obj.file_name+".pdf",as_attachment=True)

if __name__=="__main__":
    app.run(debug=True,port=4000)