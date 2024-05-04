# make a dictionary of all subjects and teachers and print satya sir's subject

subject={
    'Python':'Satya Sir',
    'DSP':'Monalisa Mam',
    'DAA':'Sujit Sir',
    'COA':'Nibedita Mam',
    'Economics':'Surya Sir',
    'NPTEL':'Snigdha Mam',
    'Python(Lab)':'Satya Sir',
    'DAA(Lab)':'Sujit Sir',
    'COA(Lab)':'Nibedita Mam'
    }
print([x for x,y in subject.items() if y=='Satya Sir'])