from com.ziclix.python.sql import zxJDBC

jdbc_url = "jdbc:ucanaccess:///Users/01017387/Downloads/JDBC/UCanAccess/loader/ucanload.jar
username = ""
password = ""
driver = "net.ucanaccess.jdbc.UcanloadDriver"

db = zxJDBC.connect(jdbc_url, username, password, driver)
crsr = db.cursor()
#crsr.execute("SELECT AgentName FROM Agents")
crsr.execute("SELECT AgentName FROM Agents")
crsr.fetchall()

#for row in crsr.fetchall():
#    print row[0]
crsr.close()
db.close()
