mypymongo --> Package created to performs various operations on mangodb

This package contains 2 modules
1.datareader.
2.databaseoperations.

********* About data reader module***********

This module contains only one function -> read_csv(path)
	
	* This function will take path for csv file as input and
    returns list of dictionaries


********* About databaseoperations module *******

This module contains one class --> 
DatabaseOperations()
	
	* While creating object we have to pass connection string as a parameter to this  class.
	* This class contains 7 methods
		
		1.connect_to_database() 
			
			This method will returns status as type str

		2.create_database()

			This method will accept input database_name:type str
			and returns status as type str

		3.create_collection()

			This method will accept two parameters
        		database_name: type str,
        		collection_name: type str
        		and returns status type str

		4.insert_values()

			This method will accept input
        		database_name: type str
        		collection_name: type str
        		data: type dict or list of dict
        		flag: type str (Accepts two values 'one' or 'many')
        		and returns status as str

		5.find_values()

        		This method will accept 
        		database_name: as str, 
        		collection_name: as str,
       			command: as type dict , if no filter pass {}
        		and returns obj if no error else will return str 

        	6.update_values()

			This method will accept input
        		database_name: type str
        		collection_name: type str
        		filter: type dict ,if no condition pass empty dict ie {}
        		newvalues: type str
        		flag: type str accepts two values 'one','many'
        		and returns status as str

		7.delete_values()

			 This method will accept imput
        		 database_name: type str,
        		 collection_name: type str,
        		 command: type dict,
        		 flag: type str accepts two values 'one','many'


main.py --> by executing this with some customizations(giving inputs) we can perform
	    various operations on database

carbon_nanotubes.csv --> This file contains data which is imported into database.
