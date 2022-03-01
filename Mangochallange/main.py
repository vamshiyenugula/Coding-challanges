from mypymongo.databaseoperations import DatabaseOperations
from mypymongo import datareader
import logging


logging.basicConfig(filename="assignmentlog.txt",level = logging.INFO,format ='%(asctime)s %(message)s')

logging.info('program execution started')

# Creating Object
logging.info('creating object for Databaseoperations class')
try:
    db_ops_obj = DatabaseOperations("mongodb+srv://mongodb:mongodb@cluster0.h9qxo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    logging.info('object created sucessfully')
except Exception as error:
    logging.error(error)



# Creating Connection
logging.info('Connecting to Database')
try:
    conn = db_ops_obj.connect_to_database()
    if conn == 'connected sucessfully':
        logging.info(conn)
    else:
        logging.error(conn)
except Exception as error:
    logging.error(error)



# Create Database
logging.info('Creating Database')
try:
    temp_db = db_ops_obj.create_database('database1')
    if temp_db == "Database Created Sucessfully":
        logging.info(temp_db)
    elif temp_db == "database not created or collection not created yet":
        logging.warning(temp_db)
    else:
        logging.error(temp_db)
except Exception as error:
    logging.error(error)



# Create Collection
logging.info('Creating Collection')
try:
    temp_c1 = db_ops_obj.create_collection('database1','collection1')
    if temp_c1 == "database and collection created sucessfully.":
        logging.info(temp_c1)
    elif temp_c1 == "dataabase not created,collection not created ,or no data is available in collection.":
        logging.warning(temp_c1)
    else:
        logging.error(temp_c1)
except Exception as error:
    logging.error(error)



# Insert values
logging.info('Inserting Values')

# Reading data from carbon_nanotubes.csv
logging.info('Reading data from carbon_nanotubes.csv')
try:
    data = datareader.read_csv('carbon_nanotubes.csv')
    if type(data) == list:
        logging.info('Reading data completed')
    else:
        logging.error(data)
except Exception as error:
    logging.error(error)

try:
    status_many = db_ops_obj.insert_values('database1','collection1',data,'many')
    if status_many == 'value inserted sucessfully':
        logging.info(status_many)
    else:
        logging.error(status_many)
except Exception as error:
    logging.error(error)




# Finding values
logging.info('Finding Values')

cmmd = {"Calculated atomic coordinates v'":'017014'}
#cmmd = {} -> no condition

try:
    find_status = db_ops_obj.find_values('database1','collection1',cmmd)
    for i in find_status:
        logging.debug(find_status)
except Exception as error:
    logging.error(error)



# Update values
logging.info('Updating Values')

filter = {'Chiral indice n':"3;1;0"}
#filter = {} -> no condition to filter

newvalues = { "$set": {'Chiral indice n':'00000'}}

try:
    stat_update = db_ops_obj.update_values('database1','collection1',filter,newvalues,'many')
    if stat_update == 'Value updated successfully':
        logging.info(stat_update)
    else:
        logging.error(stat_update)
except Exception as error:
    logging.error(error)




# delete values
logging.info('Deleting Values')

cmmd = {'Chiral indice n':'2;1;0'}
try:
    temp_remove = db_ops_obj.delete_values('database1','collection1',cmmd,'many')
    if temp_remove == 'values deleted sucesssfully':
        logging.info(temp_remove)
    else:
        logging.error(temp_remove)
except Exception as error:
    logging.error(error)

logging.info('program execution completed')