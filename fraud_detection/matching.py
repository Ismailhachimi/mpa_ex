class MatchingEngine:
    fullname = None

    def __init__(self, fullname=None):
        self.fullname = fullname

    def get_matches(self):
        if not self.fullname:
            raise ValueError("Please provide fullname")

        # TODO matching
        results = []
        return results

    def compute_matches(self):
        # TODO compute matches
        status = True
        return status