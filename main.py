import pickle

savedir = './results/'
savefile = 'values.pkl'

a = [1,2,3,4]
for val in a:
	print(val)

# Saving

with open(savedir+savefile, 'wb') as f:
    pickle.dump(a, f)

