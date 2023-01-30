import json

files=['1.json','2.json','3.json','4.json','5.json','6.json','7.json','8.json','9.json','10.json','11.json','12.json','13.json','14.json','15.json','16.json']

dwith open('merged_file_name.json', "w") as outfile:
   outfile.write('{}'.format('\n'.join([open(f, "r").read() for f in files])))
