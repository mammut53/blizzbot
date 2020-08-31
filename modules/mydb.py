#import discord
#import mysql.connector
#test
DBhost = zz_init.config().get_DBhost()
DBuser = zz_init.config().get_DBuser()
DBpasswd = zz_init.config().get_DBpasswd()
DBdatabase = zz_init.config().get_DBdatabase()

mydb = mysql.connector.connect(
    host=DBhost,
    user=DBuser,
    passwd=DBpasswd,
    database=DBdatabase,
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

#create database
mycursor.execute("CREATE DATABASE blizzbot")

#create table
mycursor.execute("CREATE TABLE mcnames (id INT AUTO_INCREMENT PRIMARY KEY, discord_id BIGINT, minecraft_name TINYTEXT, uuid TINYTEXT, isWhitelistedYoutube BOOLEAN, isWhitelistedYoutube BOOLEAN)")

mycursor.execute("CREATE TABLE ranking (id INT AUTO_INCREMENT PRIMARY KEY, discord_id BIGINT, points INT)")
