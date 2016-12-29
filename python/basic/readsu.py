import re
pattern=re.compile('CN')
s=[('CN=V630254,OU=Other,OU=Vendors,OU=Corporate,OU=TWCOrg,OU=TWC Divisions,DC=corp,DC=twcable,DC=com', {'displayName': ['Annavajhula, Kartik\xc2\xa0(contractor)']}), (None, ['ldap://DomainDnsZones.corp.twcable.com/DC=DomainDnsZones,DC=corp,DC=twcable,DC=com'])]
print s
if re.search(pattern,s):
    print s
else:
    print "no"
