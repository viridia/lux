# Executes the pattern constructor and maintains references to the patter evaluation methods.
class Pattern:
    tracked = []

    def __init__(self, module, *args, **kwargs):
        self.module = module
        self.args = args
        self.kwargs = kwargs
        self.build();

    def build(self):
        saveTracked = Pattern.tracked
        Pattern.tracked = []
        self.update, self.eval = self.module.main(*self.args, **self.kwargs)
        self.tracked = Pattern.tracked
        Pattern.tracked = saveTracked

    def advance(self, ms):
        for t in self.tracked: t.advance(ms)
