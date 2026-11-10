import pytest
from diet_app.recommendation import (
    food_matches_rules,
    recommend_foods,
    load_foods,
    load_conditions,
    evaluate_food,
)


def test_food_passes_all_rules():
    food = {"name": "Apple", "sugar": 10, "fiber": 4}
    rules = [
        {"field": "fiber", "operator": ">=", "value": 3},
        {"field": "sugar", "operator": "<=", "value": 12},
    ]
    assert food_matches_rules(food, rules) is True


def test_unknown_operator_raises_error():
    food = {"name": "Apple", "sugar": 10}
    rules = [{"field": "sugar", "operator": "=>", "value": 3}]
    with pytest.raises(ValueError):
        food_matches_rules(food, rules)

def test_missing_field_is_not_allowed():
    food = {"name": "Mystery Food", "fiber": 5}
    rules = [{"field": "sugar", "operator": "<=", "value": 10}]
    assert food_matches_rules(food, rules) is False


def test_unknown_condition_raises_error():
    foods = [{"name": "Apple", "sugar": 10}]
    conditions = [
        {"name": "Diabetes",
         "rules": [{"field": "sugar", "operator": "<=", "value": 12}]}
    ]
    with pytest.raises(ValueError):
        recommend_foods(foods, conditions, ["Not A Condition"])


def test_recommend_foods_returns_matching_foods():
    foods = [
        {"name": "Apple", "sugar": 10},
        {"name": "Cake", "sugar": 40},
    ]
    conditions = [
        {"name": "Diabetes",
         "rules": [{"field": "sugar", "operator": "<=", "value": 12}]}
    ]
    result = recommend_foods(foods, conditions, ["Diabetes"])
    names = [f["name"] for f in result[0]["foods"]]
    assert names == ["Apple"]


def test_data_files_load_from_any_folder():
    assert len(load_foods()) > 0
    assert len(load_conditions()) > 0


def test_fails_greater_equal_rule():
    food = {"name": "White Rice", "fiber": 1}
    rules = [{"field": "fiber", "operator": ">=", "value": 3}]
    assert food_matches_rules(food, rules) is False


def test_fails_less_equal_rule():
    food = {"name": "Cake", "sugar": 40}
    rules = [{"field": "sugar", "operator": "<=", "value": 12}]
    assert food_matches_rules(food, rules) is False


def test_fails_equal_rule():
    food = {"name": "Milk", "type": "dairy"}
    rules = [{"field": "type", "operator": "==", "value": "vegan"}]
    assert food_matches_rules(food, rules) is False


def test_one_rule_fails_so_food_is_rejected():
    food = {"name": "Banana", "fiber": 4, "sugar": 30}
    rules = [
        {"field": "fiber", "operator": ">=", "value": 3},
        {"field": "sugar", "operator": "<=", "value": 12},
    ]
    assert food_matches_rules(food, rules) is False

from diet_app.recommendation import evaluate_food


def test_evaluate_food_allowed():
    food = {"name": "Apple", "sugar": 10}
    rules = [{"field": "sugar", "operator": "<=", "value": 12}]
    result = evaluate_food(food, rules)
    assert result["allowed"] is True
    assert result["failed"] == []


def test_evaluate_food_reports_failed_rule():
    food = {"name": "Cake", "sugar": 40}
    rules = [{"field": "sugar", "operator": "<=", "value": 12}]
    result = evaluate_food(food, rules)
    assert result["allowed"] is False
    assert result["failed"] == [
        {"field": "sugar", "operator": "<=", "value": 12, "actual": 40}
    ]


def test_evaluate_food_reports_all_failures():
    food = {"name": "Banana", "fiber": 1, "sugar": 30}
    rules = [
        {"field": "fiber", "operator": ">=", "value": 3},
        {"field": "sugar", "operator": "<=", "value": 12},
    ]
    result = evaluate_food(food, rules)
    assert len(result["failed"]) == 2


def test_evaluate_food_missing_field():
    food = {"name": "Mystery", "fiber": 5}
    rules = [{"field": "sugar", "operator": "<=", "value": 12}]
    result = evaluate_food(food, rules)
    assert result["allowed"] is False
    assert result["failed"][0]["actual"] is None