import numpy as np

class NeuralNetwork():

    def __init__(self, layer_sizes):

        # layer_sizes example: [4, 10, 2]
        self.input_neurons_num = layer_sizes[0]
        self.hidden_neurons_num = layer_sizes[1]
        self.output_neurons_num = layer_sizes[2]

        # Weights and biases matrices
        self.W_1 = np.random.randn(self.input_neurons_num, self.hidden_neurons_num)
        # self.b_1 = np.zeros((self.hidden_neurons_num, 1))
        self.b_1 = np.random.randn(self.hidden_neurons_num, 1)
        self.W_2 = np.random.randn(self.hidden_neurons_num, self.output_neurons_num)
        # self.b_2 = np.zeros((self.output_neurons_num, 1))
        self.b_2 = np.random.randn(self.output_neurons_num, 1)

    def activation(self, x, activation_type):    # Leaky ReLU activation function

        if activation_type == 'LRelu':
            x = np.where(x > 0, x, x * 0.01)
        elif activation_type == 'sigmoid':
            x = 1/(1 + np.exp(-x))
        return x

    def forward(self, x):
        
        # x example: np.array([[0.1], [0.2], [0.3]])
        x = x.reshape(x.shape[0], 1)
        z_1 = np.matmul(self.W_1.T, x) + self.b_1
        a_1 = self.activation(z_1, activation_type='LRelu')
        z_2 = np.matmul(self.W_2.T, a_1) + self.b_2
        output = self.activation(z_2, activation_type='sigmoid')
        return output