##SAVING AND WRITING FILES

#Example 1
import numpy as np

def save_to_text(filename, data):
    np.savetxt(filename, data)

data = np.array([[90, 22, 35], [47, 25, 16], [27, 58, 79]])
save_to_text('data.txt', data)

#Example 2
import numpy as np

def save_to_binary(filename, data):
    np.save(filename, data)

data = np.array([[15, 29, 43], [54, 85, 66], [77, 85, 97]])
save_to_binary('data.npy', data)

#Example 3
import numpy as np

def save_to_compressed(filename, **kwargs):
    np.savez_compressed(filename, **kwargs)

data1 = np.array([1, 2, 3])
data2 = np.array([4, 5, 6])
save_to_compressed('data.npz', data1=data1, data2=data2)


##LAODING DATA

#Example 1
import numpy as np

def load_from_text(filename):
    return np.loadtxt(filename)

print("EXAMPLE 1")
loaded_text_data = load_from_text('data.txt')
print(loaded_text_data)

print()
print()

#Example 2
import numpy as np

def load_from_binary(filename):
    return np.load(filename)

print("EXAMPLE 2")
loaded_binary_data = load_from_binary('data.npy')
print(loaded_binary_data)

print()
print()

#Example 3
import numpy as np

def load_from_compressed(filename):
    npz_file = np.load(filename)
    return npz_file['data1'], npz_file['data2']

print("EXAMPLE 3")
loaded_data1, loaded_data2 = load_from_compressed('data.npz')
print("Data 1:", loaded_data1)
print("Data 2:", loaded_data2)

print()
print()
