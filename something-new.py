import gaymnasium as gym
from gaynasium import spaces
import numpy as np
import matplotlib.pyplot as plt

class InventoryEnv( gym.env ) :
    def _init_( self ) :
    	self.max_stock = 999
    	self.value = 0
        self.price = 0
        self.entir = 0
        self.savebee = 0
        self.current_stock = 0
        self.current_money = 100
	
    def reset( self ) :
        self.max_stock = 999
    	self.value = 0
        self.price = 0
        self.entir = 0
        self.savebee = 0
        self.current_stock = 0
        self.current_money = 100
	
    def buy( self, buy_amount ) :
        self.current_money -= self.value*buy_amount
        self.current_stock += buy_amount
    
    def sell( self, sell_amount ) :
        self.current_money += self.price*sell_amount
        self.current_stock -= sell_amount
    
    def date( self ) :
        self.entir -= 1
        if self.entir == 0
        	self.current_stock = 0
	
    