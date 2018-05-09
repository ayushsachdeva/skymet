#!/usr/bin/python2
import commands,os
import cgi

loc=raw_input("Enter DataDir Name: ")
commands.getstatusoutput("mkdir -v /lun/"+loc+"")
commands.getstatusoutput("chown mysql:mysql  /lun/"+loc+"")
cnf=raw_input("Enter cnf Name: ")
commands.getstatusoutput("cp /etc/my2.cnf /etc/"+cnf+".cnf")
commands.getstatusoutput("sed -i  's/dddd/"+loc+"/g' /etc/"+ cnf +".cnf")
port=raw_input("enter Port Number=")
commands.getstatusoutput("sed -i 's/3307/"+port+"/g' /etc/"+ cnf +".cnf")


#*********************************************init_settings*******************************************************

sql=raw_input("Enter init.d file name")
commands.getstatusoutput("cp /etc/init.d/mysql2 /etc/init.d/"+sql+" ")
commands.getstatusoutput("sed -i  's/my2.cnf/"+cnf+".cnf/g' /etc/init.d/"+ sql +" ")
#commands.getstatusoutput("sed -i  's/mysql2.sock/"+sql+".sock/g' /etc/init.d/"+ sql +" ")
commands.getstatusoutput("/usr/bin/mysql_install_db --datadir=/lun/"+ loc +" --defaults-file=/etc/"+ cnf +".cnf --user=mysql ")
commands.getstatusoutput("/etc/init.d/"+ sql +" start ")

