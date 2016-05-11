from xml.etree import ElementTree as ET

tree = ET.parse('GraphML-2272.xml')
root = tree.getroot()

target = open("tweets.txt", 'a')

for child in root:
	if child.tag == '{http://graphml.graphdrawing.org/xmlns}graph':
		for sub_child in child:
			if sub_child.tag == '{http://graphml.graphdrawing.org/xmlns}node':
				data = sub_child[5].text
				data = data[data.index('\n\n')+len('\n\n'):]
				data = data.replace('\n','').encode('utf-8')
				target.write(data+'\n')
				