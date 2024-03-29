class Setup:
    def __init__(self):
        self._delta = 0.0
        self._alpha = 0.0
        self._dx = 0.0
        self._aType = 0

    def setVariables(self, parameters):
        self._delta = parameters['delta']
        self._alpha = parameters['alpha']
        self._dx = parameters['dx']
        self._aType = parameters['aType']
        
    def getAtype(self):
        return self._aType
