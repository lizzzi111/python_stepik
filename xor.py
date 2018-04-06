X=np.array(((0,0),(0,1),(1,0),(1,1)))
y=np.array((0,1,0,0))
w = np.random.random((X.shape[1], 1))
neuron = Neuron(w, activation_function=sigmoid, activation_function_derivative=sigmoid_prime);
test=neuron.SGD(X, y, 4, learning_rate=0.1, eps=1e-6, max_steps=200)
print(test);
print(neuron.w)
