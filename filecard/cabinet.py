from .filecard import FileCard
import itertools


class Cabinet:

    stored_files = set()

    def __init__(self):
        super().__init__()

    def _get_combinations(self):
        combinations = []
        for i in range(len(self.stored_files)):
            combinations.append(itertools.combinations(self.stored_files, i + 1))
        return combinations

    def _eval_comb_prob(self, comb: list, question: str):
        pass

    def add_file(self, file: FileCard):
        self.stored_files.add(file)

    def get_file(self, name: str):
        return self.get_files(name)

    def get_files(self, value: str, key="name"):
        matches = [file for file in self.stored_files if file.getattr(key) == value]
        for file in matches:
            file.touch()
        return matches

    def eval_combs_prob(self, question: str, singular: bool, gender: str):

        if singular:
            if gender:
                combs = [[file] for file in self.get_files(gender, "gender")]
            else:
                combs = [[file] for file in self.stored_files]
        else:
            combs = self._get_combinations()

        for combination in combs:
            self._eval_comb_prob(combination, question)
