# POLLING WEBSITE
A simple polling website built using Html,Css and Flask which is a amazing micro web framework written in Python.
But a non-responsive one :(

<strong>INSTRUCTIONS :</strong> 

1. Create a local mysql database using :<br><pre>CREATE DATABASE polling;</pre>
2. Create a table in the database using the following command : <br><pre>CREATE TABLE register(id int AUTO_INCREMENT PRIMARY KEY,name varchar (50) NOT NULL,username varchar (60) NOT NULL UNIQUE KEY,age int (3) NOT NULL,votes int (11) NOT NULL DEFAULT 0);</pre>
3. Once the table has been created , go back to the polling.py file and make the following changes: <br><br>![Screenshot from 2019-12-12 22-44-19](https://user-images.githubusercontent.com/53977614/70733807-0d2edf00-1d31-11ea-94eb-46f5d7f49c56.png)
<ul>
<li>Set your localhost in line 12 (default : localhost) </li>
<li>Set your username in line 13 (default : root) </li>
<li>Set the password of your mysql database in line 14 </li><br>
You can get all the information about your mysql by running the following command :
<pre>
status
</pre>
<br>
<li>Install all the necessary modules (given below) before executing the polling.py file.
<pre>
pip install flask
</pre>
<pre>
pip install flask-wtf
</pre>
<pre>
pip install flask-mysqldb
</pre>
</li>
</ul>
<br>

4.Thats ' it <br> 
You are ready ! 
