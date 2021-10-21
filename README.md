# ASSIGNMENT
In this assignment, you will develop a simple Web server in Python that is capable of processing only one request. Specifically, your Web server will 
1. create a connection socket when contacted by a client (browser); 
2. receive the HTTP request from this connection; 
3. parse the request to determine the specific file being requested; 
4. get the requested file from the server’s file system; 
5. create an HTTP response message consisting of the requested file preceded by header lines; and 
6. send the response over the TCP connection to the requesting browser. If a browser requests a file that is not present in your server, your server should return a “404 Not Found” error message.

