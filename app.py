from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    n1,n2,n3=input().split(" ")
    n1=int(n1)
    n2=str(n2)
    n3=int(n3)
    if n2 == "+":
        return f"{n1}+{n3}={n1+n3}"
    elif n2 == "-" :
        return f"{n1}-{n3}={n1-n3}"  
    elif n2 == "*":
        return f"{n1}*{n3}={n1*n3}"
    else : 
        return f"{n1}/{n3}={n1/n3}"

if __name__ == "__main__":
    app.run()