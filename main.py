from flask import Flask, render_template
from classes.candidates import Candidates

app = Flask(__name__)
candidates = Candidates('json/candidates.json')


@app.route('/')
def page_index():
    return render_template('list.html',
                           candidates=candidates.get_data_candidates())


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    return render_template('card.html', id=uid,
                           candidate=candidates.get_data_candidate(uid))


@app.route('/search/<name>')
def page_by_name(name):
    return render_template('search.html', name=name,
                           candidates=candidates.get_data_by_name(name),
                           number=len(candidates.get_data_by_name(name)))


@app.route('/skill/<skill>')
def page_by_skill(skill):
    return render_template('skill.html', skill=skill,
                           candidates=candidates.get_data_by_skill(
                               skill),
                           number=len(candidates.get_data_by_skill(skill)
                                      ))


app.run()
