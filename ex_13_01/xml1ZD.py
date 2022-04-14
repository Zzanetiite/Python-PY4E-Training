import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
#Find child name and extract text of it.
print('Name:', tree.find('name').text)
#Get looks for the attribute in child "email" in the tree that it fins with the find function
print('Attr:', tree.find('email').get('hide'))
