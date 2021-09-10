#mplot
import matplotlib.pyplot as plt

class Montgomery:
    def __init__(self):
        plt.plot()
    def show(self):
        plt.show()
    def add(self,plot):
        try:
            plt.plot(plot['x'],plot['y'],plot['marker'])
        except:
            plt.plot(plot['x'],plot['y'])
    def new(self,**plot):
        return self.Smithers(self,plot)
        
    class Smithers:
        def __init__(self,outer,plot):
            self.outer = outer
            self.plot = plot
            self.accessOuter()
        def accessOuter(self):
            self.outer.add(self.plot)
            
m = Montgomery()
m.new(x=[1, 2, 3, 4],y= [1, 4, 9, 16], marker='.')
m.show()

