from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
path = "C:\pythonProject\HW11\candidates.json"

app = Flask(__name__)


@app.route("/",)
def page_all_candidates():
    candidates = load_candidates_from_json(path)
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<uid>",)
def page_candidate(uid):
    candidate = get_candidate(uid)
    if not candidate:
        return "Кандидат не существует, скорректируйте ваш запрос"
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>",)
def page_search_candidate(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    candidates_number = len(candidates)
    return render_template("search.html", candidates=candidates, candidates_number=candidates_number)


@app.route("/skill/<skill_name>",)
def page_search_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    candidates_number = len(candidates)
    return render_template("skill.html", candidates=candidates, candidates_number=candidates_number)


app.run()

