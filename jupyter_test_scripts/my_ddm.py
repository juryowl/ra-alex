import numpy as np
import matplotlib.pyplot as plt


def ddm_sim(v = 0, a = 1, w = 0.5, n_samples = 2000, max_t = 4, dt = 0.01):
    data = np.zeros((n_samples, 2))
    
    for i in range(n_samples):
        y = -a +  (2 * w * a)
        t = 0
        while(y > -a and y < a and t < max_t):
            y += v*dt + np.sqrt(dt)*np.random.normal()
            t += dt
        data[i, :] = [np.sign(y), t]
        #print('sample generated :)')
    
    return data


    
if __name__ == "__main__":
    print('starting script')
    data = ddm_sim() 
    plt.hist(data[:, 0] * data[:, 1])
    plt.show()
    print('finished')

