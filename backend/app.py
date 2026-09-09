from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)
DB = "society.db"

def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    con = db()
    con.executescript('''
    CREATE TABLE IF NOT EXISTS residents(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL, flat TEXT NOT NULL, phone TEXT, email TEXT);
    CREATE TABLE IF NOT EXISTS notices(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL, message TEXT NOT NULL, date TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS complaints(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      resident TEXT NOT NULL, subject TEXT NOT NULL,
      description TEXT NOT NULL, status TEXT DEFAULT 'Pending');
    CREATE TABLE IF NOT EXISTS bills(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      resident TEXT NOT NULL, flat TEXT NOT NULL,
      amount REAL NOT NULL, status TEXT DEFAULT 'Unpaid');
    ''')
    if con.execute("SELECT COUNT(*) FROM notices").fetchone()[0] == 0:
        con.execute("INSERT INTO notices(title,message,date) VALUES(?,?,?)",
                    ("Water Supply Notice","Water maintenance will be carried out tomorrow.",datetime.now().strftime("%Y-%m-%d")))
    if con.execute("SELECT COUNT(*) FROM bills").fetchone()[0] == 0:
        con.execute("INSERT INTO bills(resident,flat,amount,status) VALUES(?,?,?,?)",
                    ("Demo Resident","A-101",1500,"Unpaid"))
    con.commit()
    con.close()

@app.get("/api/residents")
def residents():
    con=db(); rows=con.execute("SELECT * FROM residents ORDER BY id DESC").fetchall(); con.close()
    return jsonify([dict(r) for r in rows])

@app.post("/api/residents")
def add_resident():
    d=request.get_json()
    con=db()
    cur=con.execute("INSERT INTO residents(name,flat,phone,email) VALUES(?,?,?,?)",
                    (d["name"],d["flat"],d.get("phone",""),d.get("email","")))
    con.commit(); con.close()
    return jsonify({"message":"Resident added","id":cur.lastrowid}),201

@app.get("/api/notices")
def notices():
    con=db(); rows=con.execute("SELECT * FROM notices ORDER BY id DESC").fetchall(); con.close()
    return jsonify([dict(r) for r in rows])

@app.post("/api/notices")
def add_notice():
    d=request.get_json()
    con=db(); cur=con.execute("INSERT INTO notices(title,message,date) VALUES(?,?,?)",
                              (d["title"],d["message"],datetime.now().strftime("%Y-%m-%d %H:%M")))
    con.commit(); con.close()
    return jsonify({"message":"Notice added","id":cur.lastrowid}),201

@app.get("/api/complaints")
def complaints():
    con=db(); rows=con.execute("SELECT * FROM complaints ORDER BY id DESC").fetchall(); con.close()
    return jsonify([dict(r) for r in rows])

@app.post("/api/complaints")
def add_complaint():
    d=request.get_json()
    con=db(); cur=con.execute("INSERT INTO complaints(resident,subject,description) VALUES(?,?,?)",
                              (d["resident"],d["subject"],d["description"]))
    con.commit(); con.close()
    return jsonify({"message":"Complaint submitted","id":cur.lastrowid}),201

@app.get("/api/bills")
def bills():
    con=db(); rows=con.execute("SELECT * FROM bills ORDER BY id DESC").fetchall(); con.close()
    return jsonify([dict(r) for r in rows])

@app.get("/api/health")
def health():
    return jsonify({"status":"running","service":"Smart Society API"})

if __name__=="__main__":
    init_db()
    app.run(host="0.0.0.0",port=5000,debug=True)
