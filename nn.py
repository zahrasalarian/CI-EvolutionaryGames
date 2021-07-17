import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):

        # TODO
        # layer_sizes example: [4, 10, 2]
        self.inp_llen = layer_sizes[0]
        self.hidden_llen = layer_sizes[1]
        self.outp_llen = layer_sizes[2]
        self.b = [np.zeros(self.hidden_llen), np.zeros(self.outp_llen)] 
        self.w = [np.random.normal(0, 1, size=(self.hidden_llen, self.inp_llen)), np.random.normal(0, 1, size=(self.outp_llen, self.hidden_llen))]

    def activation(self, x):
        
        # TODO
        s = 1/(1+np.exp(-x))
        return s

    def forward(self, x):
        
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        w_layer_2 = self.w[0]
        b_2 = self.b[0]
        
        w_layer_3 = self.w[1]
        b_3 = self.b[1]

        a_s = []
        # hidden layer
        a_2 = np.zeros((self.hidden_llen, 1))
        a_2 = self.activation((w_layer_2 @ x + b_2))
        #print('********************')
        #print(np.transpose(a_2))
        #print('********************')

        a_s.append(np.transpose(a_2)[0].reshape(self.hidden_llen,1))
        #print(a_s[0])

        # output layer 
        a_3 = np.zeros((self.outp_llen, 1))
        a_3 = self.activation(w_layer_3 @ a_s[0] + b_3)
        a_s.append(np.transpose(a_3)[0].reshape(self.outp_llen,1))

        return a_s[-1]
