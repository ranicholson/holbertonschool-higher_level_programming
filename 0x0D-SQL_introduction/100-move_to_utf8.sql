-- Script to convert database to UTF8
ALTER DATABASE hbtn_0c_0 charset=utf8;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8;
