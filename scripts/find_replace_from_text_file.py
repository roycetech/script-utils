import os
import string

map_file_path =  os.path.expanduser('~') + '/Desktop/MT-222-New_Product_ID-MAP.txt'
source_file_path =  os.path.expanduser('~') + '/Desktop/config.cfc'

with open(map_file_path, 'r') as map_file, \
        open(source_file_path, 'r') as source_file:

    id_map = {}

    for line in map_file:
        array = line.strip().split(' ')
        old_id = array[0]
        new_id = array[1]
        id_map[old_id] = new_id

    for line in source_file:
        updated_string = line.rstrip()
        for k, v in id_map.items():
            updated_string = string.replace(updated_string, k, v)

        print(updated_string)

import sys
print sys.version