import requests

def test_case_1():
    print("\nRunning Test Case 1: Valid Resume and Relevant Job Description")
    url = 'http://localhost:5000/match'
    files = {'resume': open('sample_resume.pdf', 'rb')}
    data = {
        'job_description': """
        We are looking for a Data Scientist with experience in Python, machine learning, 
        scikit-learn, and cloud deployment platforms. Knowledge of Flask is a plus.
        """
    }
    response = requests.post(url, files=files, data=data)
    handle_response(response)


def test_case_2():
    print("\nRunning Test Case 2: Valid Resume with Unrelated Job Description")
    url = 'http://localhost:5000/match'
    files = {'resume': open('sample_resume.pdf', 'rb')}
    data = {
        'job_description': """
        Seeking a Marketing Manager with expertise in digital marketing, SEO, 
        social media strategy, and content creation.
        """
    }
    response = requests.post(url, files=files, data=data)
    handle_response(response)


def test_case_3():
    print("\nRunning Test Case 3: No Resume Provided")
    url = 'http://localhost:5000/match'
    data = {
        'job_description': """
        We are looking for a Software Engineer skilled in Python, Flask, and web development.
        """
    }
    response = requests.post(url, files=None, data=data)
    handle_response(response)


def test_case_4():
    print("\nRunning Test Case 4: No Job Description Provided")
    url = 'http://localhost:5000/match'
    files = {'resume': open('sample_resume.pdf', 'rb')}
    data = {'job_description': ""}
    response = requests.post(url, files=files, data=data)
    handle_response(response)


def test_case_5():
    print("\nRunning Test Case 5: Corrupted Resume File")
    url = 'http://localhost:5000/match'
    files = {'resume': open('corrupted_resume.pdf', 'rb')}
    data = {
        'job_description': """
        Looking for a Backend Developer proficient in Python, Django, and REST APIs.
        """
    }
    response = requests.post(url, files=files, data=data)
    handle_response(response)


def handle_response(response):
    """Utility function to handle and display the response."""
    if response.status_code == 200:
        result = response.json()
        print("Test Successful!")
        print("Category:", result.get('category', 'N/A'))
        print("Match Score:", result.get('score', 'N/A'), "%")
    else:
        print("Test Failed!")
        print("Error:", response.json().get('error', 'Unknown error'))


if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
