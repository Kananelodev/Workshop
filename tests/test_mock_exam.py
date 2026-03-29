"""
Unit Tests for Mock Summative Assessment

Run all tests:
    python3 -m pytest tests/test_mock_exam.py -v

Run specific test:
    python3 -m pytest tests/test_mock_exam.py::TestMockExam::test_even_odd_tracker -v
"""

import pytest
from mock_exam import (
    even_odd_tracker,
    temperature_filter,
    calculate_order_total,
    process_scores,
    organize_products,
    sequence_growth,
)


class TestMockExam:
    """Test suite for all coding questions."""

    # ========================================================================
    # QUESTION 1 TESTS: even_odd_tracker
    # ========================================================================

    def test_even_odd_tracker_basic(self):
        """Test basic even/odd tracking with mixed numbers."""
        assert even_odd_tracker([1, 2, 3, 4]) == ["Odd", "Even", "Odd", "Even"]

    def test_even_odd_tracker_all_even(self):
        """Test with all even numbers."""
        assert even_odd_tracker([2, 4, 6, 8]) == ["Even", "Even", "Even", "Even"]

    def test_even_odd_tracker_all_odd(self):
        """Test with all odd numbers."""
        assert even_odd_tracker([1, 3, 5, 7]) == ["Odd", "Odd", "Odd", "Odd"]

    def test_even_odd_tracker_empty(self):
        """Test with empty list."""
        assert even_odd_tracker([]) == []

    def test_even_odd_tracker_single_even(self):
        """Test with single even number."""
        assert even_odd_tracker([42]) == ["Even"]

    def test_even_odd_tracker_single_odd(self):
        """Test with single odd number."""
        assert even_odd_tracker([99]) == ["Odd"]

    def test_even_odd_tracker_with_zero(self):
        """Test with zero (which is even)."""
        assert even_odd_tracker([0, 1]) == ["Even", "Odd"]

    def test_even_odd_tracker_negative_numbers(self):
        """Test with negative numbers."""
        assert even_odd_tracker([-2, -1, -4, -3]) == ["Even", "Odd", "Even", "Odd"]

    def test_even_odd_tracker_large_numbers(self):
        """Test with large numbers."""
        assert even_odd_tracker([1000, 1001]) == ["Even", "Odd"]

    # ========================================================================
    # QUESTION 2 TESTS: temperature_filter
    # ========================================================================

    def test_temperature_filter_basic(self):
        """Test basic temperature filtering."""
        assert temperature_filter([10, 18, 22, 30, 61, -100]) == [18, 22]

    def test_temperature_filter_all_valid(self):
        """Test when all temperatures are valid."""
        assert temperature_filter([18, 19, 20, 25]) == [18, 19, 20, 25]

    def test_temperature_filter_all_invalid(self):
        """Test when all temperatures are invalid."""
        assert temperature_filter([10, 30, 100, -100]) == []

    def test_temperature_filter_empty(self):
        """Test with empty list."""
        assert temperature_filter([]) == []

    def test_temperature_filter_boundaries(self):
        """Test boundary conditions (18 and 25 should be included)."""
        assert temperature_filter([17, 18, 25, 26]) == [18, 25]

    def test_temperature_filter_below_negative_50(self):
        """Test that temperatures below -50 are ignored."""
        assert temperature_filter([-51, -100, 20, 25]) == [20, 25]

    def test_temperature_filter_above_60(self):
        """Test that temperatures above 60 are ignored."""
        assert temperature_filter([20, 61, 100, 22]) == [20, 22]

    def test_temperature_filter_edge_case_minus_50(self):
        """Test edge case at -50 (should be ignored)."""
        assert temperature_filter([-50, 20, 60]) == [20]

    def test_temperature_filter_edge_case_60(self):
        """Test edge case at 60 (should be ignored)."""
        assert temperature_filter([20, 60]) == [20]

    def test_temperature_filter_single_valid(self):
        """Test with single valid temperature."""
        assert temperature_filter([20]) == [20]

    # ========================================================================
    # QUESTION 3 TESTS: calculate_order_total
    # ========================================================================

    def test_calculate_order_total_basic(self):
        """Test basic order calculation: 10 + (100 * 1) = 110."""
        assert calculate_order_total(100, 1) == 110

    def test_calculate_order_total_with_multiplier_bonus(self):
        """Test with quantity > 5 bonus: 10 + (10 * 5) + 20 = 100."""
        assert calculate_order_total(10, 5) == 100

    def test_calculate_order_total_minimum(self):
        """Test minimum total enforcement: 10 + (5 * 2) = 20 → 50 (min)."""
        assert calculate_order_total(5, 2) == 50

    def test_calculate_order_total_zero_price(self):
        """Test with zero price: 10 + 0 = 10 → 50 (min)."""
        assert calculate_order_total(0, 1) == 50

    def test_calculate_order_total_quantity_exactly_5(self):
        """Test with quantity exactly 5 (>= 5 should apply bonus)."""
        assert calculate_order_total(20, 5) == 10 + (20 * 5) + 20  # 130

    def test_calculate_order_total_quantity_6(self):
        """Test with quantity 6: 10 + (15 * 6) + 20 = 120."""
        assert calculate_order_total(15, 6) == 120

    def test_calculate_order_total_large_order(self):
        """Test with large order: 10 + (100 * 10) + 20 = 1030."""
        assert calculate_order_total(100, 10) == 1030

    def test_calculate_order_total_exactly_50(self):
        """Test where total is exactly 50 (no change)."""
        assert calculate_order_total(20, 2) == 50  # 10 + (20 * 2) = 50

    # ========================================================================
    # QUESTION 4 TESTS: process_scores
    # ========================================================================

    def test_process_scores_stops_early(self):
        """Test stopping when score below 40 is found."""
        assert process_scores([60, 70, 35, 80]) == "Stopped early at score 35"

    def test_process_scores_completes(self):
        """Test when all scores are valid (>= 40)."""
        assert process_scores([45, 50, 55]) == "All scores processed"

    def test_process_scores_first_score_invalid(self):
        """Test stopping immediately at first score."""
        assert process_scores([30, 50, 60]) == "Stopped early at score 30"

    def test_process_scores_last_score_invalid(self):
        """Test stopping at last score."""
        assert process_scores([45, 50, 35]) == "Stopped early at score 35"

    def test_process_scores_empty(self):
        """Test with empty list."""
        assert process_scores([]) == "All scores processed"

    def test_process_scores_single_valid(self):
        """Test with single valid score."""
        assert process_scores([50]) == "All scores processed"

    def test_process_scores_single_invalid(self):
        """Test with single invalid score."""
        assert process_scores([30]) == "Stopped early at score 30"

    def test_process_scores_boundary_40(self):
        """Test boundary at 40 (should be valid)."""
        assert process_scores([40, 50]) == "All scores processed"

    def test_process_scores_boundary_39(self):
        """Test boundary at 39 (should be invalid)."""
        assert process_scores([39, 50]) == "Stopped early at score 39"

    def test_process_scores_multiple_below_40(self):
        """Test stopping at first score below 40."""
        assert process_scores([50, 60, 30, 25]) == "Stopped early at score 30"

    # ========================================================================
    # QUESTION 5 TESTS: organize_products
    # ========================================================================

    def test_organize_products_basic(self):
        """Test basic product organization by category."""
        items = [
            {"name": "Milk", "category": "Dairy"},
            {"name": "Cheese", "category": "Dairy"},
            {"name": "Bread", "category": "Bakery"},
        ]
        expected = {"Dairy": ["Milk", "Cheese"], "Bakery": ["Bread"]}
        assert organize_products(items) == expected

    def test_organize_products_empty(self):
        """Test with empty list."""
        assert organize_products([]) == {}

    def test_organize_products_single_item(self):
        """Test with single item."""
        items = [{"name": "Apple", "category": "Fruits"}]
        expected = {"Fruits": ["Apple"]}
        assert organize_products(items) == expected

    def test_organize_products_different_categories(self):
        """Test with all different categories."""
        items = [
            {"name": "Milk", "category": "Dairy"},
            {"name": "Carrot", "category": "Vegetables"},
            {"name": "Chicken", "category": "Meat"},
        ]
        expected = {
            "Dairy": ["Milk"],
            "Vegetables": ["Carrot"],
            "Meat": ["Chicken"],
        }
        assert organize_products(items) == expected

    def test_organize_products_same_category_multiple(self):
        """Test multiple items in same category."""
        items = [
            {"name": "Milk", "category": "Dairy"},
            {"name": "Cheese", "category": "Dairy"},
            {"name": "Yogurt", "category": "Dairy"},
        ]
        expected = {"Dairy": ["Milk", "Cheese", "Yogurt"]}
        assert organize_products(items) == expected

    def test_organize_products_mixed_categories(self):
        """Test complex scenario with mixed categories."""
        items = [
            {"name": "Milk", "category": "Dairy"},
            {"name": "Bread", "category": "Bakery"},
            {"name": "Butter", "category": "Dairy"},
            {"name": "Bagel", "category": "Bakery"},
            {"name": "Carrot", "category": "Vegetables"},
        ]
        expected = {
            "Dairy": ["Milk", "Butter"],
            "Bakery": ["Bread", "Bagel"],
            "Vegetables": ["Carrot"],
        }
        assert organize_products(items) == expected

    def test_organize_products_order_preserved(self):
        """Test that order of items within category is preserved."""
        items = [
            {"name": "A", "category": "X"},
            {"name": "B", "category": "X"},
            {"name": "C", "category": "X"},
        ]
        result = organize_products(items)
        assert result["X"] == ["A", "B", "C"]

    # ========================================================================
    # QUESTION 6 TESTS: sequence_growth
    # ========================================================================

    def test_sequence_growth_basic(self):
        """Test basic sequence growth: [3, 4, 5] = 3."""
        assert sequence_growth([3, 4, 5, 1, 2]) == 3

    def test_sequence_growth_entire_list(self):
        """Test when entire list is increasing."""
        assert sequence_growth([1, 2, 3, 4, 5]) == 5

    def test_sequence_growth_no_growth(self):
        """Test when no increasing sequence (all decreasing)."""
        assert sequence_growth([5, 4, 3, 2, 1]) == 1

    def test_sequence_growth_single_element(self):
        """Test with single element."""
        assert sequence_growth([42]) == 1

    def test_sequence_growth_empty(self):
        """Test with empty list."""
        assert sequence_growth([]) == 0

    def test_sequence_growth_two_elements_increasing(self):
        """Test with two increasing elements."""
        assert sequence_growth([1, 2]) == 2

    def test_sequence_growth_two_elements_decreasing(self):
        """Test with two decreasing elements."""
        assert sequence_growth([2, 1]) == 1

    def test_sequence_growth_multiple_sequences(self):
        """Test with multiple increasing sequences."""
        # [1,2,3] and [5,6,7] -> longest is 3
        assert sequence_growth([1, 2, 3, 4, 0, 5, 6, 7]) == 4

    def test_sequence_growth_duplicates(self):
        """Test with duplicate values (not strictly increasing)."""
        # [1,2] [2] [3,4,5] -> longest is [3,4,5] = 3
        assert sequence_growth([1, 2, 2, 3, 4, 5]) == 3

    def test_sequence_growth_sequences_equal_length(self):
        """Test when multiple sequences have equal length."""
        # [1,2,3] and [5,6,7]
        result = sequence_growth([1, 2, 3, 4, 5, 6, 7])
        assert result == 7  # Entire sequence

    def test_sequence_growth_negative_numbers(self):
        """Test with negative numbers."""
        assert sequence_growth([-3, -2, -1, 0, 1]) == 5

    def test_sequence_growth_mixed_positive_negative(self):
        """Test with mixed positive and negative."""
        assert sequence_growth([1, 2, -5, -4, -3]) == 3

    def test_sequence_growth_large_gaps(self):
        """Test with large gaps between numbers."""
        assert sequence_growth([1, 100, 0, 50, 51, 52]) == 3

    def test_sequence_growth_single_long_sequence(self):
        """Test single long increasing sequence."""
        assert sequence_growth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10

    def test_sequence_growth_sawtooth_pattern(self):
        """Test sawtooth pattern (up then down repeatedly)."""
        assert sequence_growth([1, 2, 1, 2, 1, 2]) == 2  # [1,2] appears repeatedly

    def test_sequence_growth_zero_in_sequence(self):
        """Test with zero as part of sequence."""
        assert sequence_growth([-2, -1, 0, 1, 2]) == 5


# ==============================================================================
# Summary Report
# ==============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
