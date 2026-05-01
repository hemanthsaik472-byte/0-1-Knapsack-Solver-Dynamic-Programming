import sys
from algorithms.knapsack_dp import solve_01_knapsack
from algorithms.fractional_knapsack import solve_fractional_knapsack

def get_integer_input(prompt):
    """Helper to ensure valid integer input."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("❌ Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

def main_menu():
    print("\n" + "="*50)
    print("      🌟 SMART BUDGET OPTIMIZATION SYSTEM 🌟")
    print("="*50)
    print("1. Start New Budget Calculation")
    print("2. Exit System")
    print("-"*50)
    
    choice = input("Select an option (1/2): ")
    return choice

def run_optimization():
    print("\n--- 📝 Input Phase ---")
    num_items = get_integer_input("Enter the number of items: ")
    
    if num_items == 0:
        print("⚠️ No items to process.")
        return

    weights = []
    values = []
    
    for i in range(num_items):
        print(f"\nItem {i+1}:")
        v = get_integer_input(f"  Value (Profit): ")
        w = get_integer_input(f"  Weight (Cost): ")
        values.append(v)
        weights.append(w)
        
    budget = get_integer_input("\nEnter total Budget (Capacity): ")

    print("\n" + "="*50)
    print("🔍 PROCESSING OPTIMIZATION MODELS...")
    print("="*50)

    # 1. 0/1 Knapsack Calculation
    dp_val, dp_items = solve_01_knapsack(budget, weights, values)
    
    # 2. Fractional Knapsack Calculation
    fr_val, fr_items = solve_fractional_knapsack(budget, weights, values)

    # Display Results for 0/1 Knapsack
    print("\n[METHOD 1: 0/1 Knapsack (Dynamic Programming)]")
    print(f"👉 Maximum Value possible: {dp_val}")
    print("✅ Items Selected (Complete):", end=" ")
    if not dp_items:
        print("None (Budget too low)")
    else:
        # Sort and display item indices (1-based for users)
        display_items = sorted([idx + 1 for idx in dp_items])
        print(", ".join(map(str, display_items)))
    print("💡 Explanation: This model assumes you can only buy whole units. No fractions allowed.")

    # Display Results for Fractional Knapsack
    print("\n[METHOD 2: Fractional Knapsack (Greedy Approach)]")
    print(f"👉 Maximum Value possible: {fr_val:.2f}")
    print("✅ Allocation strategy:")
    if not fr_items:
        print("   None")
    for item in fr_items:
        perc = item['fraction'] * 100
        print(f"   - Item {item['id']+1}: Took {item['weight_taken']} units ({perc:.1f}% of item)")
    print("💡 Explanation: This model allows buying partial units to maximize the budget utilization.")

    # Comparison Summary
    print("\n" + "="*50)
    print("📊 COMPARISON SUMMARY")
    print("="*50)
    print(f"0/1 Knapsack Total Value: {dp_val}")
    print(f"Fractional Knapsack Total Value: {fr_val:.2f}")
    difference = fr_val - dp_val
    if difference > 0:
        print(f"📈 Insight: Fractional approach gained {difference:.2f} more value by using partial items.")
    else:
        print("📈 Insight: Both approaches yielded the same value for this specific input.")
    print("="*50)

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == '1':
            run_optimization()
        elif choice == '2':
            print("\n👋 Thank you for using the Smart Budget Optimization System! Goodbye.")
            sys.exit()
        else:
            print("❌ Invalid selection. Please try again.")
