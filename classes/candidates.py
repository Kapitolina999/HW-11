import json


class Candidates:
    """ класс Candidates с полем path - путь json файла, из которого
    выгружается необходимая информация о кандидатах.
    Методы: get_data_candidates, get_data_candidate,
    get_candidates_with_skill
    """

    def __init__(self, path):
        self.path = path

    def get_data_candidates(self):
        """
        :return: Возвращает вложенный список всех кандидатов.
        """
        with open(self.path, encoding='utf-8') as file:
            return json.load(file)

    def get_data_candidate(self, id):
        """
        :param id: идентификатор кандидата в списке кандидатов
        :return: словарь с данными о кандидате
        """
        candidates = self.get_data_candidates()
        for _ in candidates:
            if id == _["id"]:
                return _
        # return [_ for _ in candidates if id == _["id"]]

    def get_data_by_name(self, name):
        """
        :param name: имя кандидата
        :return: список с данными о кандидатах
        """
        candidates = self.get_data_candidates()
        return [_ for _ in candidates if name.title() in _["name"].title()]

    def get_data_by_skill(self, skill):
        """
        :param skill: навык, по котору ведется поиск кандидатов
        :return: список кандидатов, владеющих навыком
        """
        candidates = self.get_data_candidates()
        return [_ for _ in candidates
                if skill.lower() in _["skills"].lower().split(', ')]
