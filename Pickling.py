import pickle

# Input Data
my_data = { 'chenai', 'covai', 'Trichy', 'madhurai'}

# Pickle the input
with open("demo.pickle","wb") as file_handle:
   pickle.dump(my_data, file_handle, pickle.HIGHEST_PROTOCOL)

# Unpickle the above pickled file
with open("demo.pickle","rb") as file_handle:
   res = pickle.load(file_handle)
   print(my_data)