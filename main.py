import pickle

savedir = './results/'
savefile = 'values.pkl'

a = [1,2,3,4]

print('a values are')
for val in a:
	print(val)

# Saving
with open(savedir+savefile, 'wb') as f:
    pickle.dump(a, f)

# Loading
with open(savedir+savefile, 'rb') as f:
    b = pickle.load(f)

print('b values are')
for val in b:
	print(val)





