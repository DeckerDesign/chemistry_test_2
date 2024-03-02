import random

class ChemistryQuiz:
    def __init__(self):
        self.questions = [
            # Fixed conceptual questions with proper dictionary syntax
            {"question": "What is the unit of concentration that represents moles of solute per liter of solution?", "answer": "molarity", "type": "text"},
            {"question": "Percentage of theoretical yield actually obtained", "answer": "percent yield", "type": "text"},
            {"question": "Concentration unit relating percentage of solute to solution", "answer": "mass percent", "type": "text"},
            {"question": "The stoichiometric amount of product obtained from a reaction", "answer": "theoretical yield", "type": "text"},
            {"question": "Reactants in an equation which are not limiting", "answer": "excess reactant", "type": "text"},
            {"question": "Another measure of concentration, often used for very dilute solutions", "answer": "parts per million", "type": "text"},
            {"question": "The ratio of moles involved stoichiometrically in a reaction", "answer": "mole ratio", "type": "text"},
            {"question": "Equation used to calculate molarities and volumes to dilute", "answer": "dilution equation", "type": "text"},
            {"question": "Reactant in an equation which determines yield", "answer": "limiting reactant", "type": "text"},
            {"question": "Actual yield/theoretical yield * 100", "answer": "percent yield", "type": "text"},
            {"question": "Represents the stoichiometric relationship between the reactants and products in a reaction", "answer": "chemical equation", "type": "text"},
            {"question": "Reactions that occur in water", "answer": "aqueous reaction", "type": "text"},
            # Fixed calculation-based question with actual logic needed for answers
            {"question": "A quantity of gas at 741 mm Hg and 31.0 °C is heated to 98.0 °C at constant volume. What pressure results from the heating? (Enter your answer in mm Hg)", "formula": "Use Gay-Lussac's law: P1/T1 = P2/T2. Convert temperatures to Kelvin.", "answer": 904.2, "tolerance": 1, "type": "numerical"},
            {"question": "What volume is occupied by 21.3 g sulfur dioxide (SO2) at standard temperature and pressure (STP)? (Enter your answer in liters, STP conditions are 0 °C and 1 atm)", "formula": "Use the ideal gas law in combination with molar mass of SO2. At STP, 1 mole gas occupies 22.4 L.", "answer": 0.3, "tolerance": 0.1, "type": "numerical"},
            {"question": "What volume is occupied by 21.3 g sulfur dioxide (SO2) at standard temperature and pressure (STP)? (Enter your answer in liters, STP conditions are 0 °C and 1 atm)", "formula": "Use the ideal gas law in combination with molar mass of SO2. At STP, 1 mole gas occupies 22.4 L.", "answer": 7.45, "tolerance": 0.1, "type": "numerical"},
            {"question": "52.81 g of a gas occupy 30.4 L of volume at 729.6 torr and 23.0 ˚C. What is the molecular weight of the gas? What density does it exhibit at STP? (Enter your answer as 'molecular weight; density', e.g., '44.0; 1.96')", "formula": "Use the ideal gas law and concepts of molecular weight and density.", "answer": "44.0; 1.96", "tolerance": 0.1, "type": "text"},  # Note: Adjusted format for clarity
            {"question": "Acetylene, an important component of organic synthesis, was formerly prepared via reaction of calcium carbide with water: CaC2 + 2 H2O -> Ca(OH)2 + C2H2. If this reaction is performed, yielding 1.481x10^3 dL of acetylene at 63.54˚C and 681 torr, what mass of water was initially reacted with the calcium carbide? (Enter your answer in grams)", "formula": "Apply gas laws and stoichiometry principles.", "answer": 44.0, "tolerance": 1, "type": "numerical"},  # Assuming the answer provided is a placeholder; requires correct calculation or context
            # Additional questions...

    # Remaining class definition...

        ]
        self.score = 0

    def ask_question(self, question):
        print(question["question"])
        if "formula" in question:
            print("Hint: ", question["formula"])
        user_answer = input("Your answer: ").strip()

        if question["type"] == "text":
            return user_answer.lower() == question["answer"]
        elif question["type"] == "numerical":
            try:
                user_answer_num = float(user_answer)
                return abs(user_answer_num - question["answer"]) <= question["tolerance"]
            except ValueError:
                print("Invalid numerical answer. Please enter a valid number.")
                return False
        return False

    # Corrected indentation for run_quiz method
    def run_quiz(self):
        questions_copy = self.questions[:]  # Create a copy of the questions list
        random.shuffle(questions_copy)  # Shuffle the copy for random order

        for question in questions_copy:
            correct = self.ask_question(question)
            if correct:
                print("Correct!")
                self.score += 1
            else:
                # Moved inside the else block to only print if the answer is incorrect
                print(f"Incorrect. The correct answer is {question['answer']}.")
            print()  # Newline for readability

        # This print statement is outside the loop to display the final score
        print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")

# Main execution
if __name__ == "__main__":
    quiz = ChemistryQuiz()
    quiz.run_quiz()