import re
import sys
#u'id': u'603688059744596', u'name': u'Motiafi Jok'
def main():
    the_file = open(sys.argv[1],'r')
    id_string = ''
    for line in the_file.readlines():
        id_list = re.findall(r'u\'id\': u\'\d{15}\', u\'name\': u\'[\w ]+',line)
    the_file.close()
    regexp = re.compile(r'id\': u\'(?P<id>\d{15})\', u\'name\': u\'(?P<name>[\w ]+)')
    file = open('name_id_list.txt','w')
    for line in id_list:
        result = regexp.search(line)
        file.write('id: ' + result.group('id') + ' name: ' + result.group('name') + '\n')
    file.close()

main()
