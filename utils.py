import json
path = "C:\pythonProject\HW11\candidates.json"


def load_candidates_from_json(path):
    """
    возвращает список всех кандидатов после загрузки данных из файла json
    :param path: путь до данных
    :return:
    """

    with open(path, encoding="utf-8") as f:
        candidates = json.load(f)
    return candidates


# print(load_candidates_from_json(path))


def get_candidate(candidate_id):
    """
    возвращает одного кандидата по его id
    :param candidate_id:
    :return:
    """
    candidates = load_candidates_from_json(path)
    for candidate in candidates:
        if candidate["id"] == int(candidate_id):
            return candidate


# print(get_candidate(5))


def get_candidates_by_name(candidate_name):
    """
    возвращает кандидатов по имени
    :param candidate_name: 
    :return: 
    """
    candidates = load_candidates_from_json(path)
    candidates_selected = []
    for candidate in candidates:
        candidate_name_lower = candidate_name.lower()
        candidate_dict_lower = candidate["name"].lower()
        if candidate_name_lower in candidate_dict_lower:
            candidates_selected.append(candidate)
    return candidates_selected
    

# print(get_candidates_by_name("e"))


def get_candidates_by_skill(skill_name):
    """
    возвращает кандидатов по навыку
    :param skill_name:
    :return:
    """
    candidates = load_candidates_from_json(path)
    candidates_selected_by_skill = []
    for candidate in candidates:
        skill_lower = skill_name.lower()
        skills_purged = candidate["skills"].lower().split(", ")
        if skill_lower in skills_purged:
            candidates_selected_by_skill.append(candidate)
    return candidates_selected_by_skill
    

# print(get_candidates_by_skill("go"))
