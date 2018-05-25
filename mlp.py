from sklearn.neural_network import MLPClassifier

X = [[80., 70., 10., 80.], [10., 50., 80., 50.], [90., 60., 70., 90.],[0., 100., 0., 100.]]
y = ['siria', 'europa', 'africa','europa']
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
h = clf.fit(X, y)
prediction = clf.predict([[10., 50., 100., 50.]])
print(prediction)