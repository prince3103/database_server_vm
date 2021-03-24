from flask import Flask, request
from skill_database import SkillDatabase
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def hello():
    job_role = request.args.get('job_role')
    skill_type = request.args.get('skill_type')
    # job_result = SkillDatabase.get_data(job_role=job_role, skill_type='both skill')
    job_result = SkillDatabase.get_data(job_role=job_role, skill_type=skill_type)
    if job_result == []:
        return {'skills': 'No skill found for given input.'}, 404
    return {'skills': job_result}, 200

if __name__ == '__main__':
    app.run(port = 8080)