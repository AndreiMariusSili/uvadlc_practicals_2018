"""
This module implements a multi-layer perceptron (MLP) in NumPy.
You should fill in code into indicated sections.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from typing import List, Union

from modules import *


class MLP(object):
    """
    This class implements a Multi-layer Perceptron in NumPy.
    It handles the different layers and parameters of the model.
    Once initialized an MLP object can perform forward and backward.
    """

    _layers: List[Union[LinearModule, ReLUModule, SoftMaxModule]]

    def __init__(self, n_inputs: int, n_hidden: List[int], n_classes: int):
        """
        Initializes MLP object.

        Args:
          n_inputs: number of inputs.
          n_hidden: list of ints, specifies the number of units
                    in each linear layer. If the list is empty, the MLP
                    will not have any linear layers, and the model
                    will simply perform a multinomial logistic regression.
          n_classes: number of classes of the classification problem.
                     This number is required in order to specify the
                     output dimensions of the MLP

        TODO:
        Implement initialization of the network.
        """

        ########################
        # PUT YOUR CODE HERE  #
        #######################
        self._layers = []
        if n_hidden:
            in_dim = n_inputs
            for i, out_dim in enumerate(n_hidden):
                self._layers.append(LinearModule(in_dim, out_dim))
                self._layers.append(ReLUModule())
                in_dim = out_dim
            self._layers.append(LinearModule(in_dim, n_classes))
            self._layers.append(SoftMaxModule())
        else:
            self._layers.append(LinearModule(n_inputs, n_classes))
            self._layers.append(SoftMaxModule())

        ########################
        # END OF YOUR CODE    #
        #######################

    def forward(self, x):
        """
        Performs forward pass of the input. Here an input tensor x is transformed through
        several layer transformations.

        Args:
          x: input to the network
        Returns:
          out: outputs of the network

        TODO:
        Implement forward pass of the network.
        """

        ########################
        # PUT YOUR CODE HERE  #
        #######################
        for layer in self._layers:
            out = layer.forward(x)
            x = out
        ########################
        # END OF YOUR CODE    #
        #######################

        return out

    def backward(self, dout):
        """
        Performs backward pass given the gradients of the loss.

        Args:
          dout: gradients of the loss

        TODO:
        Implement backward pass of the network.
        """

        ########################
        # PUT YOUR CODE HERE  #
        #######################
        for layer in reversed(self._layers):
            dout = layer.backward(dout)

        ########################
        # END OF YOUR CODE    #
        #######################

        return
