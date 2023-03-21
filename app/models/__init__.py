import os
import importlib

# dynamic loading of models
def import_models():
    for filename in os.listdir('app/models'):
        # filter files and import modules dynamically
        if filename.endswith('.py') and filename != "__init__.py":
            module = importlib.import_module(f'.{filename[:-3]}', package='app.models')



# from .Test import Test

# from concurrent.futures import process
# from app import db
# import os, importlib
# from datetime import date


# # model classes are stored here
# models = {}

# # check value and typecast if it does not match the data type in the model
# def validate_datatype(model, column, value, allow_null=False):
#     # print(f'model: {model}')
#     # print(f'column: {column}')
#     # print(f'value: {value}')

#     # get database data type
#     d_type = model.__table__.columns[column].type.python_type

#     # skip value checking if value is None and allow_null is True
#     if allow_null and value is None:
#         return value

#     # validate if input and db data type are the same
#     # typecast if data type does not coincide with the database or if it is a date
#     elif (type(value) != d_type) and (d_type != date):
#         value = d_type(value)

#     return value

# # if process_session is True, this function will handle session adding
# def insert(model, auto_commit=True, allow_null=False, **kwargs):
#     # instantiate model
#     table = model()

#     # loop through the keyword arguments
#     for key, value in kwargs.items():
#         print(key)
#         print(value)

#         # check if attribute exists
#         if hasattr(table, key):
#             # assign attribute
#             setattr(table, key, validate_datatype(model, key, value, allow_null))
    
#     # add and commit changes into database
#     db.session.add(table)

#     # return table and session
#     # session is useful if you want to rollback after an error
#     if not auto_commit:
#         # print('returning table and session')
#         return (table, db.session)

#     # commit the transaction
#     db.session.commit()
#     # db.session.close()

#     print('insert done')

#     return table

# def delete(result_sets=[], auto_commit=True):
#     # delete and commit changes into database
#     for result_set in result_sets:
#         db.session.delete(result_set)

#     # return session
#     # session is useful if you want to rollback after an error
#     if not auto_commit:
#         print('returning session')
#         return db.session

#     # commit the transaction
#     db.session.commit()
#     # db.session.close()

#     print('delete done')

#     return

# # row_data format sample: [{'id' : 1, 'description' : 'qweqwe'}, {'id' : 2, 'description' : 'zxcxzc'}]
# # NOTE: row_data dictionary should follow the column names of the table where the data will be inserted to
# def bulk_insert(model, row_data=[], auto_commit=True, allow_null=False):
#     # list of model instances
#     model_data = []

#     # loop through each row data
#     for row in row_data:
#         # instantiate model
#         m = model()

#         # loop through the dictionary
#         for key, value in row.items():

#             # check if attribute exists
#             if hasattr(m, key):

#                 # assign attribute
#                 setattr(m, key, validate_datatype(model, key, value, allow_null))

#         # add table
#         # db.session.add(model_data)
#         model_data.append(m)

#     # bulk save
#     db.session.bulk_save_objects(model_data, return_defaults=True)

#     # return model_data and session
#     # session is useful if you want to rollback after an error
#     if not auto_commit:
#         print('returning table and session')
#         return (model_data, db.session)
    
#     # commit the transaction
#     db.session.commit()
#     # db.session.close()

#     print('bulk insert done')

#     return model_data

# # update a single row.
# # result_set is the result from sqlalchemy query. Should only accept an array as input
# # if there are multiple result sets, all of them will use the same value update in value_updates
# # value_updates is a dictionary which indicates which column should be updated; {column name:value} 
# # value_updates values should be in this format: {column name : value}
# def update(result_set=[], value_updates={}, auto_commit=True, process_session=True, allow_null=False):
#     # iterate through the sqlalchemy result set
#     for result in result_set:

#         # iterate through the dictionary for value updates
#         for key, value in value_updates.items():
#             # print (key)
#             # print (value)
#             # check if attribute exists
#             if hasattr(result, key):

#                 # assign attribute
#                 setattr(result, key, validate_datatype(result, key, value, allow_null))
        
#         # add session
#         db.session.add(result)

#     # return session
#     # session is useful if you want to rollback after an error
#     if not auto_commit:
#         print('returning session')
#         return (result_set, db.session)

#     # commit the transaction
#     db.session.commit()
#     # db.session.close()

#     print('update done')

#     return result_set

# # update an array of result set
# # NOTE: result_set index should correspond to the same index of value_updates. 
# #   - result_set[0] update values will be taken from value_updates[0]
# # result_set is an array of results sets that you want to update
# # value_updates format: [{column1 : new value, column2 : new value}]
# # NOTE: this bulk update is not recommended -- use multiple_updates()
# def bulk_update(result_set=[], value_updates=[], auto_commit=True, allow_null=False):
#     # sourcery skip: for-append-to-extend, inline-immediately-returned-variable, list-comprehension, raise-specific-error
#     # check if result set and value updates have corresponding values
#     if len(result_set) != len(value_updates):
#         raise Exception('BULK_UPDATE: result_set and value_updates do not have the same length.')

#     updated_result_set = []
#     sessions = []

#     # iterate through the sqlalchemy result set
#     for index, result in enumerate(result_set):

#         if auto_commit:
#             update_result = update([result], value_updates[index], auto_commit, allow_null)

#         else:
#             update_result, session = update([result], value_updates[index], auto_commit, allow_null)
#             sessions.append(session)
        
#         updated_result_set.extend(update_result)
    
#     return updated_result_set if auto_commit else [updated_result_set, sessions]

# # # NOTE: value_updates should contain the primary key of the table that you want to update
# # def multiple_updates(table, value_updates=[], auto_commit=True):
# #     session = db.session.bulk_update_mappings(table, value_updates)

# #     if not auto_commit:
# #         return session

# #     session.commit()
# #     return

# # update specific rows with specific values
# # value_updates is a dictionary which indicates which specific column w/ specific primary keys should be updated;
# # value_updates values should be in this format: {primary key : {column name : value}}
# # primary key column name should be specified in pk_column so this function knows which column to use as reference
# def specific_updates(result_set=[], value_updates={}, pk_column='id', auto_commit=True, allow_null=False):
#     # iterate through the sqlalchemy result set
#     for result in result_set:
        
#         # check if primary key column exists
#         if not hasattr(result, pk_column):
#             break

#         # get primary key
#         pk = getattr(result, pk_column, None)

#         # if primary key is not found
#         if pk is not None and pk in value_updates:

#             # iterate through the values of the update
#             for key, value in value_updates[pk].items():

#                 # check if attribute exists
#                 if hasattr(result, key):

#                     # assign attribute
#                     setattr(result, key, validate_datatype(result, key, value, allow_null))

#             # add session
#             db.session.add(result)

#     # return result set and session
#     # session is useful if you want to rollback after an error
#     if not auto_commit:
#         print('returning result set and session')
#         return (result_set, db.session)
    
#     # commit the transaction
#     db.session.commit()
#     # db.session.close()

#     print('specific updates done')

#     return result_set




# def get_modules():
#     # sourcery skip: inline-immediately-returned-variable, list-comprehension
#     modules = []

#     # get all files in this directory
#     for filename in os.listdir('app/models'):
        
#         # filter files and import modules dynamically
#         if filename.endswith('.py') and filename != "__init__.py":
#             modules.append(filename[:-3])

#     return modules


# # get class instance of models and store them in the dictionary
# for module in get_modules():
#     mod = __import__(f'app.models.{module}', fromlist=[module])
#     models[module] = getattr(mod, module)