import numpy as np
import datetime
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)


class NeuralNetwork:
	def __init__(self, Inputs, DesiredOutputs):
		self.inputs	   = Inputs
		self.yd = DesiredOutputs 
		self.weights1   = np.random.rand(2,2) 
		self.weights2 = np.random.rand(2,1)
		"""
		self.weights1[0][0] = 0.5
		self.weights1[0][1] = 0.9
		self.weights1[1][0] = 0.4
		self.weights1[1][1] = 1.0
		self.weights2[0][0] = -1.2
		self.weights2[1][0] = 1.1
		"""
	
		self.Deltaweights1   = np.random.rand(2,2) 
		self.Deltaweights2 = np.random.rand(2,1)
		self.output1     = np.zeros((1,2))
		self.output2 = np.zeros((1,1))
		self.theta = np.random.rand(1,3)
		"""
		self.theta[0][0]= 0.8
		self.theta[0][1]= -0.1
		self.theta[0][2]= 0.3
		"""
		
		self.Deltatheta = np.zeros((1,3))
		self.alpha = 17.9 
		self.error = 0.0
		self.quadraticError = 0.0
		self.yd = DesiredOutputs
		self.epochs = []
		self.qerror = []
		self.accuracy = 0.001


	def trainEpoch(self):
		self.quadraticError = 0.0
		for i in range(0,self.inputs.shape[1]):
			
			#print("Input pattern number = ", i)
			#print (self.inputs[:,i])
			#print(self.weights1)
			#print(self.weights1[:,0])
			#print("inputs[:,i] = ",self.inputs[:,i])

			self.feedforward(self.inputs[:,i])

			#print("yd = ", self.yd[i,0])
			self.error = self.yd[i,0] - self.output2[0,0]
			#print("error = ", self.error)

			self.quadraticError = self.quadraticError + (self.error * self.error)
			#weight adjustment
			#error gradient for the output layer
			gradient = sigmoid_derivative(self.output2[0,0]) * self.error
			#print("gradiante = ",gradient)
			self.Deltaweights2[0,0]= self.alpha * self.output1[0,0] * gradient
			self.Deltaweights2[1,0]= self.alpha * self.output1[0,1] * gradient
			self.Deltatheta[0,2] = self.alpha * (-1) * gradient
			"""
			print("weights2 = ",self.weights2)
			print("delta weights2 = ",self.Deltaweights2)
			print("delta thetha = ",self.Deltatheta)
			"""
		
			#for the hidden layer
			gradient2 = sigmoid_derivative(self.output1[0,0])* gradient * self.weights2[0,0]
			#print("gradiente 2 = ",gradient2)
			self.Deltaweights1[0,0]= self.alpha * self.inputs[0,i] * gradient2
			self.Deltaweights1[1,0]= self.alpha * self.inputs[1,i] * gradient2
			self.Deltatheta[0,0] = self.alpha * (-1) * gradient2

			#for the hidden layer
			gradient3 = sigmoid_derivative(self.output1[0,1]) * gradient * self.weights2[1,0]
			#print(gradient3)
			self.Deltaweights1[0,1]= self.alpha * self.inputs[0,i] * gradient3
			self.Deltaweights1[1,1]= self.alpha * self.inputs[1,i] * gradient3
			self.Deltatheta[0,1] = self.alpha * (-1) * gradient3

			"""
			print("weights1 = ",self.weights1)
			print("delta weights1 = ", self.Deltaweights1)
			print("delta thetha = ",self.Deltatheta)
			"""

			#weight update
			self.weights2 = self.weights2 + self.Deltaweights2
			self.weights1 = self.weights1 + self.Deltaweights1
			self.theta = self.theta + self.Deltatheta

			"""
			print("updated values")
			print(self.weights2)
			print(self.weights1)
			print(self.theta)
			"""

	def feedforward(self, pattern):
		"""
		print("weights1[0,:]= ", self.weights1[0,:])
		print("weights1[1,:]= ", self.weights1[1,:])
		print("pattern ", pattern)
		print("dot product = ",np.dot(pattern, self.weights1[:,0]))
		"""
		self.output1[0,0] = sigmoid(np.dot(pattern, self.weights1[:,0]) - self.theta[0,0])
		self.output1[0,1] = sigmoid(np.dot(pattern, self.weights1[:,1]) - self.theta[0,1]) 
		#print("output for the first layer = ",self.output1) #hidden layer output
		#print(self.output1[0,:]) 			 
		self.output2[0,0] = sigmoid(np.dot(self.output1[0,:], self.weights2[:,0]) - self.theta[0,2])	
		#print("output for the second layer = ", self.output2) #output layer


	def outputSimul(self, pattern):
		self.quadraticError = 0.0
		for i in range(0,pattern.shape[1]):
			print("simulation")
			self.feedforward(self.inputs[:,i])	
			print("Input pattern = ", self.inputs[:,i])
			print("Output = ", self.output2)
			self.error = self.yd[i,0] - self.output2[0,0]
			self.quadraticError = self.quadraticError + (self.error * self.error)

	def train(self,acc):
		self.epochs = []
		self.qerror = []
		self.accuracy = acc
		inic = datetime.datetime.now()
		print("Start trainning =================================== accuracy = ", self.accuracy)
		i = 0
		while True:
			#print("Epoch = ", i)
			nn.trainEpoch()
			#print("quadratic error",self.quadraticError)
			i = i + 1
			#for the plot
			self.epochs.append(i)
			self.qerror.append(self.quadraticError)

			#for the progress barr
			if i%500 == 0:
				print('.', end='', flush=True)
			#exit condition
			if self.quadraticError < self.accuracy:
				print("\nEnd of training ===================================")
				self.epochs = np.asarray(self.epochs)
				self.qerror = np.asarray(self.qerror)	
				break

		end = datetime.datetime.now()
		print ("Epoch trained = ", i)
		print("Elapsed time = ", end - inic)
		print("Quadratic error = ",self.quadraticError)
		print("Weights1 = ")
		print(self.weights1)
		print("Weights2 = ")
		print(self.weights2)
		print("Thresholds = ")
		print(self.theta)

	def plotError(self):
		#plot the error
		plt.plot(self.epochs,self.qerror)
		fig = plt.gcf()
		fig.canvas.set_window_title('Trainning Results')
		plt.xlabel('Epochs')
		plt.ylabel('Quadratic Error')
		plt.title('Feedforward Backpropagation NN Training Plot')
		plt.show()

	
#===============================================================================
#  main program
#===============================================================================

#inputs	
X = np.array([[1,1,0,0],
              [1,0,1,0]])
#desired outputs
Y = np.array([[0],[1],[1],[0]])

#creates a neural network
nn = NeuralNetwork(X,Y)

print("Untrained outputs===================================")
#simulate the NN with untrained weights
nn.outputSimul(X)

#train for a given accuracy
nn.train(0.01)

print("Trained outputs===================================")
#test after taining
nn.outputSimul(X)

#plot the error
nn.plotError()

