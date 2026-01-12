from FillForm import INFO_ACTIONS as infoActions
from FillForm import MEAL_ACTIONS as mealActions
from FillForm import fillForm

def testConstants(actions):
    for action in actions:
        assert "type" in action
        assert "by" in action
        assert "locator" in action
        if action["type"] == "input":
            assert "value" in action

# whitebox test
testConstants(infoActions)
testConstants(mealActions["breakfast"])
testConstants(mealActions["lunch"])
testConstants(mealActions["dinner"])
