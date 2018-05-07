from sklearn import linear_model, neural_network
from sklearn.svm import LinearSVC
from sklearn.metrics import log_loss, mean_squared_error, hinge_loss
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
import numpy as np

## 10fold splitting
kf = KFold(n_splits=10, shuffle=True)

def logistic_regression(x,y,p):

    ##Default parameters
    default_parameters=[0.001,1.0,'lbfgs',100] ##Parameters with order: Tolerance, C, solver, maximum iteration 

    ##set custom parameters
    for i in range(len(p)):
        if p[i]!=None:
            default_parameters[i] = p[i]
    
    ##create model
    model = linear_model.LogisticRegression(tol = default_parameters[0],
                                            C = default_parameters[1],
                                            solver=default_parameters[2],
                                            max_iter=default_parameters[3])
    
    ##Train and test
    accuracy = [model.fit(x[train], y[train]).score(x[test],y[test]) for train, test in kf.split(x)]
    res = np.array(accuracy) ##get accuracy array as numpy array

    print("\nLogistic Regression\n-----------------\nAccuracy: %.2f" % res.mean())
    print("Loss: %.2f" % log_loss(y, model.predict_proba(x)))

    info=['%.2f'%res.mean(),'%.2f'%log_loss(y, model.predict_proba(x))]
    
    return model, info, default_parameters

def linear_regression(x,y,p):
    ##create model
    model = linear_model.LinearRegression()

    model.fit(x,y)

    print("\nLinear Regression\n-----------------\nAccuracy: %.2f" % model.score(x,y))
    print("Loss: %.2f" % mean_squared_error(y, model.predict(x)))

    info=['%.2f'%model.score(x,y),'%.2f'%mean_squared_error(y, model.predict(x))]

    
    
    return model, info

def svm(x,y,p):

    ##Default parameters
    default_parameters=[True,0.001,1.0,1000] ##Parameters with order: Dual, Tolerance, C, maximum iteration

    ##set custom parameters
    for i in range(len(p)):
        if p[i]!=None:
            default_parameters[i] = p[i]
    
    ##create model
    model = LinearSVC(dual = default_parameters[0],
                      tol = default_parameters[1],
                      C = default_parameters[2],
                      max_iter = default_parameters[3])
    
    ##Train and test
    accuracy = [model.fit(x[train], y[train]).score(x[test],y[test]) for train, test in kf.split(x)]
    res = np.array(accuracy)

    print("\nSupport Vector Machine\n----------------------\nAccuracy: %.2f" % res.mean())
    print("Loss: %.2f"%hinge_loss(y,model.decision_function(x)))

    info=['%.2f'%res.mean(),'%.2f'%hinge_loss(y,model.decision_function(x))]
    
    return model, info, default_parameters

def mlp(x,y,p):

    ##Default parameters
    default_parameters=[(100,),'relu','adam',0.0001,'auto',0.001,200,0.0001] ##Parameters with order: hidden layer sizes, activation, solver, alpha, batch_size, learning rate, maximum iteration, tolerance

    ##set custom parameters
    for i in range(len(p)):
        if p[i]!=None:
            default_parameters[i] = p[i]
            
    ##create model
    model = neural_network.MLPClassifier(hidden_layer_sizes=default_parameters[0],
                                         activation = default_parameters[1],
                                         solver = default_parameters[2],
                                         alpha = default_parameters[3],
                                         batch_size = default_parameters[4],
                                         learning_rate_init = default_parameters[5],
                                         max_iter = default_parameters[6],
                                         tol = default_parameters[7])
    
    ##Train and test
    accuracy = [model.fit(x[train], y[train]).score(x[test],y[test]) for train, test in kf.split(x)]
    res = np.array(accuracy)
    
    print("\nMultilayer Perceptron\n-----------------\nAccuracy: %.2f" % res.mean())
    print("Loss: %.2f" % model.loss_)

    info=['%.2f'%res.mean(),'%.2f'%model.loss_]
    
    return model, info, default_parameters


def mlp_regressor(x,y,p):
    model = neural_network.MLPRegressor(max_iter=10000)

    ##Train and test
    accuracy = [model.fit(x[train], y[train]).score(x[test],y[test]) for train, test in kf.split(x)]
    res = np.array(accuracy)
    
    print("\nMultilayer Perceptron\n-----------------\nAccuracy: %.2f" % res.mean())
    print("Loss: %.2f" % model.loss_)

    info=['%.2f'%res.mean(),'%.2f'%model.loss_]

    return model, info
