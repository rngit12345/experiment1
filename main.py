import pickle
import os

savedir = './results/'
savefile = 'values.pkl'

a = [1,2,3,4]

print('a values are')
for val in a:
	print(val)

# Saving
print('Saving a values ...')
if not os.path.exists(savedir):
    os.makedirs(savedir)
with open(savedir+savefile, 'wb') as f:
    pickle.dump(a, f)

# Loading
print('Reading a values ...')
with open(savedir+savefile, 'rb') as f:
    b = pickle.load(f)

print('b values are')
for val in b:
	print(val)





