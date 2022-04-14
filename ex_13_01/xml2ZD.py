import xml.etree.ElementTree as ET

#under users is a list of children tags
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

#decodes the input to string
stuff = ET.fromstring(input)
#the dash between works like a path. Under User child find all users that are under child "user"
lst = stuff.findall('users/user')
#conts how many users are there.
print('User count:', len(lst))

#Prints out each user information
for item in lst:
    #prints text under the child "name"
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    #prints child's attribute info under the attribute 'x'
    print('Attribute', item.get('x'))
