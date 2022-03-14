import sqlite3


def regis(nam,age,phn,mail,unam,pas):
    db=sqlite3.connect("melanoma.db")
    c=db.cursor()
    print (nam+" "+unam+" "+pas+" "+age+" "+phn+" "+mail)
    query="INSERT INTO regis (name,age,phone,email,username,password) VALUES ('%s','%s','%s','%s','%s','%s')"%(nam,age,phn,mail,unam,pas)
    try:
        c.execute(query)
        db.commit()
        val=c.fetchone
        return val
    except Exception as e:
        print ("In Exception",e)
        db.rollback()
    db.close()
    return 0
def logcheck(unam,pas):
    db=sqlite3.connect("melanoma.db")
    c=db.cursor()
    flag=0
    idd=0
    try:
        query="SELECT * FROM regis"
        c.execute(query)
        result=c.fetchall()
        for rows in result:
            una=rows[5]
            pa=rows[6]
            if una == unam and pa == pas :
                flag=1
        idd=rows[0]
        return flag,idd
    except:
        print ("Unable to fetch!!!")
    db.close()

    
