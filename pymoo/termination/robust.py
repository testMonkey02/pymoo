from pymoo.core.termination import Termination
from pymoo.util.sliding_window import SlidingWindow


class RobustTermination(Termination):

    def __init__(self,
                 termination,
                 n=30,
                 **kwargs
                 ) -> None:
        """

        Parameters
        ----------

        termination : Termination
            The termination criterion that shall become robust

        n : int
            The number of last generations to be considered for termination.

        """
        super().__init__(**kwargs)

        # create a collection in case number of max generation or evaluations is used
        self.termination = termination

        # the history calculated also in a sliding window
        self.history = SlidingWindow(n)

    def _update(self, algorithm):
        perc = self.termination.update(algorithm)
        self.history.append(perc)
        return min(self.history)
