from flask import Flask,request,jsonify

api=Flask(__name__)
@api.route("/hitung",methods=["POST"])
def calc():
   print(request.data)
   return str(eval(request.data))

@api.route("/hai",methods=["POST"])
def hai():
   print(request.data)
   return "hai"
@api.route("/hai",methods=["POST"])
def hai2():
   print(request.data)
   return "hai2"
if __name__=="__main__":
   api.run(host="localhost",debug=False)
   
   
