import py3Dmol

# Lookup a molecule using its CID (PubChem Compound Identification) code
p=py3Dmol.view(query='cid:8981')

# Set the render style
p.setStyle({'stick': {'radius': .1}, 'sphere': {'scale': 0.3}})
with open('test2.html', 'w') as file:
    file.write(p._make_html())