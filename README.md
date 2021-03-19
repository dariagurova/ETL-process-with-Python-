In order to perform a basic ETL for the downloaded CSV file I first set up a virtual machine in Google Cloud Platform. 
The documentation on how to do it canbe found here : https://cloud.google.com/compute/docs/instances/create-start-instance
Please note in order to connect to your instance please change the password and database name in the code to your VM corresponding credentials. 
The code is serving a purpose of creating database and tables, cleaning the dataset downloaded from URL and inserting it into those tables on for further analysis. 
