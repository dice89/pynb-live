

def cells():

    '''
    # Demo

    This bastard is causing the caching to disable
    '''
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic("matplotlib inline")
    print('Test2')
    del ipython
    '''
    # Small Iris experiment
    '''
    import matplotlib.pyplot as plt
    from sklearn import datasets
    from sklearn.decomposition import PCA
    '''
    ## Import some data to play with
    ### Test
    '''

    iris = datasets.load_iris()
    X = iris.data[:, :2]  # we only take the first two features.
    y = iris.target

    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

    plt.figure(2, figsize=(8, 6))
    plt.clf()



    # Plot the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
                edgecolor='k')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')


    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)


    '''
    ## Let us train a simple classifier
    '''

    from sklearn.ensemble import RandomForestClassifier

    cls = RandomForestClassifier()

    cls.fit(X,y)

    y_pred= cls.predict(X)
    '''
    ### Quick validation
    
    This is bullshit, since I'm training and testing on the same data but anyhow
    '''

    from sklearn.metrics import classification_report

    print(classification_report(y,y_pred))

    '''
    It has some potential
    '''

    '''
    1000
    '''

    '''
    Is the cache now working?
    '''

    '''
    Not really
    '''

    '''
    Now it is?
    '''

    '''
    Still
    '''

    '''
    Improve it maybe with achors
    '''

    '''
    Test 123
    '''
    a = 1000
    b = 100000
    a+b

    '''
    Test 1235
    '''

    for i in range(5,100):
        print(i)




    '''
    
    stuff
    It takes so long because the ipython container will be restarted all the time, maybe we can reuse existing containers
    '''

    print('Hello Lukasz')

    '''
    # This is a new tool for Data Science
    '''

    for i in range(1,100):
        print(i)


    '''
    Code change
    '''

    plt.figure(2, figsize=(8, 6))
    plt.clf()



    # Plot the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
                edgecolor='k')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')


    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)



    '''
    This is it
    '''

    print('Hello #Dev')
