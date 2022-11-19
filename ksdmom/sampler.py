""" Sampler utils"""
import torch
import torch.distributions as dists


class MixSampler:
    
    """Sampler for mixture distributions.
    """

    def __init__(self, *samplers, weights=None):
        self.samplers = samplers
        len_samplers = len(samplers)
        if len_samplers == 0:
            raise ValueError("No sampler is given!")
        if weights is None:
            self.weights = torch.ones(len_samplers)/len_samplers
        else:
            self.weights = torch.tensor(weights)
        
    def sample(self, n):
        samplers = self.samplers
        weights = self.weights
        m = dists.multinomial.Multinomial(n, probs=weights)
        n_samples = m.sample()
        X = [samplers[i].sample(int(k.item()))
             for (i, k) in enumerate(n_samples)]
        X = torch.vstack(X)
        for _ in range(30):
            idx = torch.randperm(n)
            X = X[idx]
        return X


class IsotropicMultivariateStudentT:
    
    def __init__(self, df, mean, var=1):
        if df <= 1:
            return ValueError("degree of freedom should be larger than 1")
        self.df = df
        self.mean = mean
        self.var = var

    def sample(self, n):
        df = self.df
        mean = self.mean
        d = mean.shape[0]
        scales = dists.Chi2(df=df).sample([n, 1])
        X = self.var**0.5 * torch.randn(n, d)
        X = (df / scales)**0.5 * X + mean
        return X

    def score(self, X):
        d = X.shape[1]
        df = self.df
        mean = self.mean
        X_ = X - mean
        w = 1 + torch.sum(X_**2, axis=1, keepdims=True)/(self.var*df) 
        return -(df + d)/df * X_ / w
