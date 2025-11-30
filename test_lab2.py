import lab2

def test_cal_average_temperature():
    input = [10,90,100,20,1]
    result = lab2.cal_average_temperature(input)
    assert result == 44.2

def test_find_min_max_temperature():
    input = [10,90,100,20,1]
    result = lab2.find_min_max_temperature(input)
    assert result == (1,100)
