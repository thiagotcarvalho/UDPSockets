<strong><font size="30">UDP Sockets - Ping</font></strong>

Client sends a ping request to the Server. When the Server receives the request, it notifies the Client.
<br>The Server also notifies the Client when it does not receive a request, which causes the request to timeout.</br>
The Client then displays how many requests were sent, how many were received by the Server, and the percentage.
<br>In the case that the Server is offline, the Client still sends the ping requests, but then it times-out and closes.</br>

-------------------------------------------------
For both the clientPing.py and serverPing.py file, 
on the command line, write "python clientPing.py" OR
"python serverPing.py" to compile and run the programs. 
<br>(REMOVE THE QUOTATION MARKS WHEN ENTERING ONTO COMMAND LINE)</br>

**TO RUN BOTH THE CLIENT AND THE SERVER, OPEN TWO SEPARATE TERMINALS/COMMAND LINES.**
