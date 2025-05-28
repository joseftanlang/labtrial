import Lab2_soln.bmi as bmi

def test_bmi_normal_weight():
    expected_result = 0
    height = 1.75  # Example height in meters
    weight = 70.0  # Example weight in kg
    result = bmi.calculate_bmi(height,weight)# Example height in meters and weight in kg
    assert result == expected_result
    
def test_bmi_over_weight():
    height = 1.75  # Example height in meters
    weight = 85.0  # Example weight in kg
    expected_result = 1
    result = bmi.calculate_bmi(height, weight)  # Example height in meters and weight in kg
    assert result == expected_result
    
def test_bmi_under_weight():
    height = 1.75  # Example height in meters
    weight = 50.0  # Example weight in kg
    expected_result = -1
    result = bmi.calculate_bmi(height, weight)  # Example height in meters and weight in kg
    assert result == expected_result