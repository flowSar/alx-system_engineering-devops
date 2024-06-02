 Web infrastructure design
 task 0: 0. Simple web stack
        What is a server: server is remote computer system or a software that provides services to a client or to other computers
       like file storage , database managment, application running or web hosting in a netwrok. and this server can be in
       data center or a local sever.
       
       What is the role of the domain name: is to provide a human readable address that maps to ip adress that was used by
       computers on a network.
       
       What is the role of the web server: handle http request, return static web page and files from server file system, return dynamic content
       by interaction with app server monitoring of requests.
       
       What is the role of the application server. handel dynamic content and he can interact with databases and do busnisses logic
       
       What is the role of the database :store data in a table form.
       
       What is the server using to communicate with the computer of the user requesting the website: http protocol.

   task 1:
        What distribution algorithm your load balancer is configured with and how it works : Round-Robin algorithm is works on 
        distributing the request on     multiple webserver 
        in sequential cycle order , for example if we have 3 servers it will go like 1,2,3,1,2,3,1,2,3

       Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both :active-Passive setup:
       until something happen to the active one to take over.

       How a database Primary-Replica (Master-Slave) cluster works : primary database is the main source of data and 
       can accept insert,update,delte operation when 
       replica database (slave) is a copy of primary and it's read-only database.

       What is the difference between the Primary node and the Replica node in regard to the application :
       Replica node is a copy of primary node and each change happen to the primary node will aply to the replica node 
       but you can't make any change on replica node directly
       so if something happed to primary node the replica node will take over is like a back up.

   task 2:
      What are firewalls for : protecting our network from unauthorized access , from hackers or malware .
      Why is the traffic served over HTTPS : to ensure the data transmitted between the website and user browser secure and private.
      What monitoring is used for : it helps for track the health and performance of webserver. 
      How the monitoring tool is collecting data: by using monitoring toosl lis agent-based monitoring, API-based monitoring. log analysis.
      Explain what to do if you want to monitor your web server QPS:
      choose the monitoring tool , install monitoring agent configure the monitoring tool to collect QPS data from web server.
      set up a dashboard to visualize the QPS.

