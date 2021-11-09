import numpy as np
from math import log, e
import scipy.stats as stat
from calcbsimpvol import calcbsimpvol

class BSM:   
    def __init__(self):
        print('__init__')
        #self.mkt_prc = float(args[0])   #옵션 시장가격
        #self.Type = int(args[1])        #기초자산 가격
        #self.S = float(args[2])         #기초자산 가격
        #self.K = float(args[3])         #행사가
        #self.r = float(args[4])         #이자율
        #self.q = float(args[5])         #배당율
        #self.T = float(args[6]) / 365.0 #만기일

        #self.sigma = self.imp_vol()     #
        #self.sigmaT = self.sigma * self.T ** 0.5
        #self.d1 = (log(self.S / self.K) + (self.r - self.q - 0.5 * (self.sigma **2)) * self.T) / self.sigmaT
        #self.d2 = self.d1 - self.sigmaT
    
    #옵션가격
    def option_value(S, K, T, r, sigma, option_type):
        d1 = (np.log(S / K) + (r + 0.5 * (sigma **2)) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        if option_type == 1:
            V = S * stat.norm.cdf(d1) - K * np.exp(-r * T) * stat.norm.cdf(d2)
        else:
            V = K * np.exp(-r * T) * stat.norm.cdf(-d2) - S * stat.norm.cdf(-d1)

        return V

    #델타
    def delta(S, K, T, r, sigma, option_type):
        d1 = (np.log(S / K) + (r + 0.5 * (sigma **2)) * T) / (sigma * np.sqrt(T))

        if option_type == 1:
            return stat.norm.cdf(d1)
        else:
            return stat.norm.cdf(d1) - 1
    
    #감마
    def gamma(S, K, T, r, sigma, option_type):
        d1 = (np.log(S / K) + (r + 0.5 * (sigma **2)) * T) / (sigma * np.sqrt(T))
        
        return stat.norm.pdf(d1) / (sigma * S * np.sqrt(T))

    #세타
    def theta(S, K, T, r, sigma, option_type):
        d1 = (np.log(S / K) + (r + 0.5 * (sigma **2)) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * T ** 0.5
        return (-sigma * S * stat.norm.pdf(d1)) / (2 * np.sqrt(T)) - option_type * (r * K * np.exp(-r * T) * stat.norm.cdf(option_type * d2))

    #베가
    def vega(S, K, T, r, sigma, option_type):
        d1 = (np.log(S / K) + (r + 0.5 * (sigma **2)) * T) / (sigma * np.sqrt(T))
        
        return S * np.sqrt(T) * stat.norm.pdf(d1)
    
    
    
    #로
    def rho():
        return "rho"


    '''
    def imp_vol(self):
        cp = np.asarray(self.Type)          #옵션타입(콜/풋)
        P = np.asarray([self.mkt_prc])      #옵션 시장가격
        S = np.asarray(self.S)              #기초자산 가격
        K = np.asarray([self.S])            #행사가
        tau = np.asarray([self.T])          #만기일
        r = np.asarray(self.r)              #이자율
        q = np.asarray(self.q)              #배당율

        imvol = calcbsimpvol(dict(cp=cp, P=P, S=S, K=K, tau=tau, r=r, q=q))
        imvol = np.ndarray.item(imvol)
        return imvol
    '''
    
    
        