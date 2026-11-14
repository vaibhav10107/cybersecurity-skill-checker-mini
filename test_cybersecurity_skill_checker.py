from cybersecurity_skill_checker import check_skills

def test_check_skills():
    skills_to_check = ['T1234', 'S5678']
    expected_output = ['T1234', 'S5678']
    assert check_skills(skills_to_check) == expected_output
