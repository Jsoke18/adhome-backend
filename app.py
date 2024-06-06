import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def load_jobs():
    """
    Load jobs data from JSON file.
    
    Returns:
        list: A list of job dictionaries.
    """
    with open('data/jobs.json', 'r') as file:
        return json.load(file)

def save_jobs(jobs):
    """
    Save jobs data to JSON file.
    
    Args:
        jobs (list): A list of job dictionaries.
    """
    with open('data/jobs.json', 'w') as file:
        json.dump(jobs, file, indent=4)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    """
    Retrieve all jobs.
    
    Returns:
        list: A list of job dictionaries.
    """
    jobs = load_jobs()
    return jsonify(jobs)

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """
    Retrieve a specific job by ID.
    
    Args:
        job_id (int): The ID of the job.
        
    Returns:
        dict: The job dictionary if found, empty dictionary otherwise.
        int: 404 status code if job is not found.
    """
    jobs = load_jobs()
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job:
        return job
    else:
        return {}, 404

@app.route('/jobs', methods=['POST'])
def add_job():
    """
    Add a new job record.
    
    Returns:
        dict: The newly added job dictionary.
        int: 201 status code for successful creation.
    """
    jobs = load_jobs()
    new_job = request.get_json()
    new_job['id'] = len(jobs) + 1
    jobs.append(new_job)
    save_jobs(jobs)
    return jsonify(new_job), 201

@app.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    """
    Update an existing job record.
    
    Args:
        job_id (int): The ID of the job to update.
        
    Returns:
        dict: The updated job dictionary if found.
        dict: Error message if job is not found.
        int: 404 status code if job is not found.
    """
    jobs = load_jobs()
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job:
        updated_job = request.get_json()
        job.update(updated_job)
        save_jobs(jobs)
        return jsonify(job)
    else:
        return jsonify({'error': 'Job not found'}), 404

@app.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    """
    Delete a job record.
    
    Args:
        job_id (int): The ID of the job to delete.
        
    Returns:
        str: Empty string for successful deletion.
        int: 204 status code for successful deletion.
    """
    jobs = load_jobs()
    updated_jobs = [job for job in jobs if job['id'] != job_id]
    save_jobs(updated_jobs)
    return '', 204

if __name__ == '__main__':
    app.run()