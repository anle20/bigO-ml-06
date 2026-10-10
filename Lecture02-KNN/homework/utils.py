import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

def plot_data1(clf, X, y, X_test=np.array([])):
    assert X.shape[0] == y.shape[0], f'Number of data points and number of labels does not match'

    x_min, x_max = 0, 60
    y_min, y_max = 0, 60

    if X_test.shape[0] != 0:
        assert 0 < X_test[0] < 100, "Only supported for age in range (0, 100)" 
        assert 0 < X_test[1] < 100, "Only supported for time spent in range (0, 100)" 
        if X_test[0] >= 60 or X_test[1] >= 60:
            x_min, x_max = 0, 100
            y_min, y_max = 0, 100
    
    cmap_light = ListedColormap(['#AAFFAA', '#AAAAFF', '#FFAAAA'])
    params = clf.get_params()
    h = 1

    xx, yy = np.meshgrid(np.arange(x_min-1, x_max+1, h),
                         np.arange(y_min-1, y_max+1, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    fig, (ax, cax) = plt.subplots(ncols=2, figsize=(8,5), gridspec_kw={"width_ratios":[1, 0.05]})
    cax.axis('off')
    ax.pcolormesh(xx, yy, Z, cmap=cmap_light)
    
    idxes0 = y == 0
    idxes1 = y == 1
    idxes2 = y == 2
    ax.plot(X[idxes0, 0], X[idxes0, 1], 'go', markersize=5, label='Group 0')
    ax.plot(X[idxes1, 0], X[idxes1, 1], 'bo', markersize=5, label='Group 1')
    ax.plot(X[idxes2, 0], X[idxes2, 1], 'ro', markersize=5, label='Group 2')
    
    if X_test.shape[0] != 0:
        _, neighbors = clf.kneighbors(X_test.reshape(1, -1))
        neighbors = neighbors[0]
        for idx in neighbors:
            ax.plot([X_test[0], X[idx, 0]], [X_test[1], X[idx, 1]], 'k--', alpha=0.5)

        ax.plot(X_test[0], X_test[1], 'ko', markersize=5, label='X test')
        
    ax.legend()
    
    ax.set_xlabel('Age')
    ax.set_ylabel('Time spent (minute)')
    ax.set_title(f"n_neighbors : {params['n_neighbors']}; weights: {params['weights']}")
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    
    fig.show()

def plot_data2(clf, X, y, X_test=np.array([])):
    assert X.shape[0] == y.shape[0], f'Number of data points and number of labels does not match'

    x_min, x_max = 0, 60
    y_min, y_max = 0, 60

    if X_test.shape[0] != 0:
        assert 0 < X_test[0] < 100, "Only supported for age in range (0, 100)" 
        assert 0 < X_test[1] < 100, "Only supported for time spent in range (0, 100)" 
        if X_test[0] >= 60 or X_test[1] >= 60:
            x_min, x_max = 0, 100
            y_min, y_max = 0, 100
    
    TEXT_OFFSET = [-1.5, 1]
    params = clf.get_params()
    fig, (ax, cax) = plt.subplots(ncols=2, figsize=(8,5), gridspec_kw={"width_ratios":[1, 0.05]})

    pcm = ax.scatter(X[:, 0], X[:, 1], c=y, s=25)
    cbar = fig.colorbar(pcm, cax=cax)
    
    if X_test.shape[0] != 0:
        _, neighbors = clf.kneighbors(X_test.reshape(1, -1))
        neighbors = neighbors[0]
        for idx in neighbors:
            ax.plot([X_test[0], X[idx, 0]], [X_test[1], X[idx, 1]], 'k--', alpha=0.5)
            ax.text(X[idx, 0] + TEXT_OFFSET[0], X[idx, 1] + TEXT_OFFSET[1], round(y[idx], 2), fontsize=8)
            
        y_test = clf.predict(X_test.reshape(1, -1))[0]
        ax.text(X_test[0] + TEXT_OFFSET[0], X_test[1]+TEXT_OFFSET[1], round(y_test, 2), fontsize=8)
        ax.scatter(X_test[0], X_test[1], color='k', s=25, label='X test')

        ax.legend()
    
    ax.set_xlabel('Age')
    ax.set_ylabel('Time spent (minutes)')
    if X_test.shape[0] != 0:
        ax.set_title(f"n_neighbors : {params['n_neighbors']}; weights: {params['weights']}")
    cbar.set_label('Income (Million VND)')
    
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])

    fig.show()

def plot_data3(X, outlier_idxes=[]):

    outlier_idxes = np.array(outlier_idxes)

    x_min, x_max = 0, 60
    y_min, y_max = 0, 60

    fig, (ax, cax) = plt.subplots(ncols=2, figsize=(8,5), gridspec_kw={"width_ratios":[1, 0.05]})
    cax.axis('off')

    ax.scatter(X[:, 0], X[:, 1], c='g', s=25)
    ax.scatter(X[outlier_idxes, 0], X[outlier_idxes, 1], c='r', s=30, label='Outliers')

    ax.set_xlabel('Age')
    ax.set_ylabel('Time spent (minute)')
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    ax.legend()
    
    fig.show()    

def plot_data_p2(df):
    X = df.drop(['Group'], axis=1).values

    x_min, x_max = 0, 60
    y_min, y_max = 0, 60

    fig, (ax, cax) = plt.subplots(ncols=2, figsize=(8,5), gridspec_kw={"width_ratios":[1, 0.05]})
    cax.axis('off')

    ax.scatter(X[:, 0], X[:, 1], c='g', s=25)

    ax.set_xlabel('Age')
    ax.set_ylabel('Time spent (minute)')
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    # set title for the figure
    ax.set_title('Hình 1: Tập dữ liệu data1.csv', fontsize=12)
    plt.show()