
import pymongo

# creating class
class DatabaseOperations(): 

    def __init__(self,connection_string):
        self.connection_string = connection_string
    

    def connect_to_database(self):
        """
        This method will returns status as type str
        """
        try:
            self.connection = pymongo.MongoClient(self.connection_string)
            databases = self.connection.list_database_names()
            if type(databases) == list:
                return 'connected sucessfully'
        except Exception as error:
            return error



    def create_database(self,database_name):

        """ 
        This method will accept input database_name:type str
        and returns status as type str
        """
        try:
            temp_string = self.connect_to_database()
            if temp_string == "connected sucessfully":
                if type(database_name == str):
                    self.connection[database_name]
                    temp_list = self.connection.list_database_names()
                    if database_name in temp_list:
                        return "Database Created Sucessfully"
                    else:
                        return "database not created or collection not created yet"
                else:
                    return f'{TypeError}: This method only accepts input type str'
            else:
                return "you are not connected to database"
        except Exception as error:
            return error
                


    def create_collection(self,database_name,collection_name):
        """ 
        This method will accept two parameters
        database_name: type str,
        collection_name: type str
        and returns status type str
        """
        try:
            temp_string = self.connect_to_database()
            if temp_string == "connected sucessfully":
                if type(database_name) == str and type(collection_name)==str:
                    temp_database = self.connection[database_name]
                    temp_database[collection_name]
                    temp_list = self.connection.list_database_names()
                    if database_name in temp_list:
                        return "database and collection created sucessfully."
                    else:
                        return "dataabase not created,collection not created ,or no data is available in collection."
                else:
                    return f'{TypeError}: This method only accepts input type str'
            else:
                return 'you are not connected to database'
        except Exception as error:
            return error
        

    
    def insert_values(self,database_name,collection_name,data,flag):

        """
        This method will accept input
        database_name: type str
        collection_name: type str
        data: type dict or list of dict
        flag: type str accepts two values 'one','many'
        and returns status as str
        """
        try:
            temp_string = self.connect_to_database()
            if temp_string == "connected sucessfully":
                inner_cond = type(data) == dict or type(data) == list
                cond = (type(database_name) == str and type(collection_name) == str and inner_cond and type(flag) == str)
                if cond:
                    temp_database = self.connection[database_name]
                    temp_collection = temp_database[collection_name]
                    if flag in ['one','many']:
                        if flag.lower() == 'one':
                            try:
                                temp_collection.insert_one(data)
                                return 'value inserted sucessfully'
                            except Exception as error:
                                return error
                        else:
                            try:
                                temp_collection.insert_many(data)
                                return 'value inserted sucessfully'
                            except Exception as error:
                                return error
                    else:
                        return 
                else:
                    return f"{TypeError}"
            else:
                return 'you are not connected to database'
        except Exception as error:
            return error

    def find_values(self,database_name,collection_name,command):

        """ 
        This method will accept 
        database_name as str, 
        collection_name as str,
        command as type dict , if no filter pass {}
        and returns obj if no error else will return str 
        """
        try:
            temp_string = self.connect_to_database()
            if temp_string == "connected sucessfully":
                cond = (type(database_name) == str and type(collection_name) == str and type(command) == dict)
                if cond:
                    temp_database = self.connection[database_name]
                    temp_collection = temp_database[collection_name]
                    try:
                        temp_obj = temp_collection.find(command)
                        return temp_obj
                    except Exception as error:
                        return error
                else:
                    return f"{TypeError}"
            else:
                return 'you are not connected to database'
        except Exception as error:
            return error


    def update_values(self,database_name,collection_name,filter,newvalues,flag):
        
        """
        This method will accept input
        database_name: type str
        collection_name: type str
        filter: type dict ,if no condition pass empty dict ie {}
        newvalues: type str
        flag: type str accepts two values 'one','many'
        and returns status as str
        """
        
        try:
            temp_string = self.connect_to_database()
            if temp_string == "connected sucessfully":
                cond = (type(database_name) == str and type(collection_name) == str and type(filter) == dict and type(newvalues) == dict and type(flag) == str)
                if cond:
                    temp_database = self.connection[database_name]
                    temp_collection = temp_database[collection_name]
                    try:
                        if flag in ['one','many']:
                            if flag.lower() == 'one':
                                temp_collection.update_one(filter,newvalues)
                                return 'Value updated successfully'
                            else:
                                temp_collection.update_many(filter,newvalues)
                                return 'Value updated successfully'
                    except Exception as error:
                        return error
                else:
                    return f"{TypeError}"
            else:
                return 'you are not connected to database'
        except Exception as error:
            return error

    def delete_values(self,database_name,collection_name,command,flag):

        """
         This method will accept imput
        database_name: type str,
        collection_name: type str,
        command: type dict,
        flag: type str accepts two values 'one','many'
        """
        try:
            temp_string = self.connect_to_database()
            if temp_string == "connected sucessfully":
                cond = type(database_name) == str and type(collection_name) == str and type(command) == dict and type(flag) == str
                if cond:
                    temp_database = self.connection[database_name]
                    temp_collection = temp_database[collection_name]
                    try:
                        if flag in ['one','many']:
                            if flag == 'one':
                                temp_obj = temp_collection.delete_one(command)
                                return 'values deleted sucesssfully'
                            else:
                                temp_obj = temp_collection.delete_many(command)
                                return 'values deleted sucesssfully'
                        return temp_obj
                    except Exception as error:
                        return error
                else:
                    return f"{TypeError}"
            else:
                return 'You are not connected to database'
        except Exception as error:
            return error   
