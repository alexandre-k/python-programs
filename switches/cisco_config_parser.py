from pyparsing import Word, Regex, OneOrMore, Or, SkipTo, Literal, alphas, nums
startblock = 'interface'
intfType = Regex(r'[a-zA-Z]+').setResultsName('interface_type')
intf_id = Word(nums + '/').setResultsName('interface_number')
desc = 'description'
desc_details = Regex(r'[a-zA-Z\(\)0-9\. ]+').setResultsName('description')
vlan_number = "switchport access allow vlan" + Word(nums).setResultsName('vlan')
duplex = SkipTo(Literal('duplex')) + Literal('duplex') + Or(Literal('full'), Literal('half')).setResultsName('duplex')
speed = 'speed' + Word( nums  ).setResultsName('speed')
endblock = SkipTo(Literal('end')) + Literal('end')
settings = intfType + intf_id + desc + desc_details + vlan_number + duplex + speed
body = startblock + settings + endblock
grammar = body
# result = grammar.parseFile('runconfig.txt')
#with open('runconfig.txt') as file:
#    result = grammar.searchString(file.read(),)
for result in grammar.scanString(open('runconfig.txt').read()):
        print(result)

