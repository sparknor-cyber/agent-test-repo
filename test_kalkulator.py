from kalkulator import legg_sammen

def test_positive_tall():
    assert legg_sammen(2, 3) == 5

def test_negative_tall():
    assert legg_sammen(-4, -6) == -10

def test_blanding():
    assert legg_sammen(-1, 1) == 0

if __name__ == "__main__":
    test_positive_tall()
    test_negative_tall()
    test_blanding()
    print("Alle 3 tester bestått ✅")
