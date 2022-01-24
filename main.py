import argparse
from operations.db_operations import DBOperations
from operations.file_operations import FileOperations

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-json_path', '--file', required=True, help='File required')
    parser.add_argument('-db', '--db', required=True, help='Database required')
    args = parser.parse_args()
    
    db_name = args.db
    json_path = args.file
    
    db = DBOperations(db_name)
    db.createTable()

    f = FileOperations(json_path)
    recordList = f.extractFromJson()

    db.insertData(recordList)
