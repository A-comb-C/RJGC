import argparse
import random
import fractions
import itertools


class MathQuizGenerator:
    def __init__(self, num_questions, value_range):
        self.num_questions = num_questions
        self.value_range = value_range
        self.questions = set()
        self.answers = []

    def generate_fraction(self):
        numerator = random.randint(1, self.value_range - 1)
        denominator = random.randint(2, self.value_range - 1)
        return fractions.Fraction(numerator, denominator)

    def generate_number(self):
        return random.choice([random.randint(0, self.value_range - 1), self.generate_fraction()])

    def generate_expression(self, depth=0):
        if depth >= 2 or random.random() < 0.5:
            return str(self.generate_number())

        op = random.choice(['+', '-', '*', '/'])
        left = self.generate_expression(depth + 1)
        right = self.generate_expression(depth + 1)

        if op == '-' and eval(left) < eval(right):
            left, right = right, left
        elif op == '/' and eval(right) == 0:
            return self.generate_expression(depth)

        expr = f'({left} {op} {right})'
        return expr

    def generate_unique_questions(self):
        while len(self.questions) < self.num_questions:
            expr = self.generate_expression()
            try:
                answer = eval(expr)
                if answer >= 0 and expr not in self.questions:
                    self.questions.add(expr)
                    self.answers.append(str(answer))
            except:
                continue

    def save_to_files(self):
        with open("Exercises.txt", "w") as f:
            f.writelines(f"{q} =\n" for q in self.questions)
        with open("Answers.txt", "w") as f:
            f.writelines(f"{a}\n" for a in self.answers)

    def run(self):
        self.generate_unique_questions()
        self.save_to_files()


class AnswerChecker:
    def __init__(self, exercise_file, answer_file):
        self.exercise_file = exercise_file
        self.answer_file = answer_file
        self.correct = []
        self.wrong = []

    def load_files(self):
        with open(self.exercise_file, 'r') as f:
            questions = [line.split('=')[0].strip() for line in f.readlines()]
        with open(self.answer_file, 'r') as f:
            answers = [line.strip() for line in f.readlines()]
        return questions, answers

    def check_answers(self):
        questions, answers = self.load_files()
        for idx, (q, a) in enumerate(zip(questions, answers), 1):
            try:
                if eval(q) == eval(a):
                    self.correct.append(idx)
                else:
                    self.wrong.append(idx)
            except:
                self.wrong.append(idx)

    def save_results(self):
        with open("Grade.txt", "w") as f:
            f.write(f"Correct: {len(self.correct)} ({', '.join(map(str, self.correct))})\n")
            f.write(f"Wrong: {len(self.wrong)} ({', '.join(map(str, self.wrong))})\n")

    def run(self):
        self.check_answers()
        self.save_results()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate math problems or check answers.")
    parser.add_argument("-n", type=int, help="Number of questions to generate")
    parser.add_argument("-r", type=int, help="Max range of numbers")
    parser.add_argument("-e", type=str, help="Exercise file for grading")
    parser.add_argument("-a", type=str, help="Answer file for grading")
    args = parser.parse_args()

    if args.n and args.r:
        generator = MathQuizGenerator(args.n, args.r)
        generator.run()
    elif args.e and args.a:
        checker = AnswerChecker(args.e, args.a)
        checker.run()
    else:
        print("Usage: Myapp.exe -n <number> -r <range> OR Myapp.exe -e <exercise_file> -a <answer_file>")
