import pickle

# Pickiling the python variable which is the user unique id
uinqueid  = 0

file = 'useruniqu.pkl'
fileobj = open(file, 'wb')
pickle.dump(uinqueid, fileobj)
fileobj.close()