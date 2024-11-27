import csv
from typing import Dict, List, Tuple
from collections import namedtuple

# Define a namedtuple for storing subject data
Subject = namedtuple("Subject", ["assignment", "lab", "IA", "credit"])


# Utility Functions
def get_int(prompt: str) -> int:
    """Prompt user for an integer input with validation."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Input was not an integer. Try again.")


def read_marks(file_path: str) -> Dict[str, Dict[str, float]]:
    """Read marks from a CSV file and return a dictionary."""
    marks = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            marks[row[0]] = {"Lab": float(row[1]), "IA": float(row[2]), "credits": float(row[3])}
    return marks


# Input Marks
def get_mark(prompt: str, max_score: int) -> Tuple[int, int]:
    """Generic function to input marks for a specific type."""
    count = get_int(f"Enter number of {prompt}: ")
    total = count * max_score
    score = sum(get_int(f"Enter mark for {prompt} {i + 1} (scaled to {max_score}): ") for i in range(count))
    return total, score


def get_subject_marks(subjects: List[str]) -> Dict[str, Subject]:
    """Collect marks for all subjects."""
    marks = {}
    for subject in subjects:
        print(f"\nEntering marks for {subject}:")
        assignment = get_mark("assignments", 10)
        lab = get_mark("labs", 30)
        IA = get_mark("IAs", 50)
        credit = get_int("Enter course credit weight: ")
        marks[subject] = Subject(assignment, lab, IA, credit)
    return marks


def save_marks_to_csv(data: Dict[str, Subject], file_name: str) -> None:
    """Save marks to a CSV file."""
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for subject, marks in data.items():
            row = [subject]
            for category in ["assignment", "lab", "IA"]:
                row.extend(marks._asdict()[category])
            row.append(marks.credit)
            writer.writerow(row)


def load_marks_from_csv(file_name: str) -> Dict[str, Subject]:
    """Load marks from a CSV file and return as a dictionary."""
    marks = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            marks[row[0]] = Subject(
                assignment=(int(row[1]), int(row[2])),
                lab=(int(row[3]), int(row[4])),
                IA=(int(row[5]), int(row[6])),
                credit=int(row[7]),
            )
    return marks


# CGPA Calculation
def calculate_subject_cgpa(subject: Subject) -> float:
    """Calculate CGPA for a single subject."""
    assignment_weight = subject.assignment[1] / subject.assignment[0] if subject.assignment[0] else 0
    lab_weight = subject.lab[1] / subject.lab[0] if subject.lab[0] else 0
    IA_weight = subject.IA[1] / subject.IA[0] if subject.IA[0] else 0

    total_weight = subject.assignment[0] + subject.lab[0] / 25 + subject.IA[0] / 7.5
    if total_weight == 0:
        return 0
    return (assignment_weight * subject.assignment[0] +
            lab_weight * (subject.lab[0] / 25) +
            IA_weight * (subject.IA[0] / 7.5)) / total_weight


def calculate_semester_cgpa(marks: Dict[str, Subject]) -> float:
    """Calculate overall semester CGPA."""
    total_marks = total_credits = 0
    for subject, data in marks.items():
        subject_cgpa = calculate_subject_cgpa(data) * 10
        total_marks += subject_cgpa * data.credit
        total_credits += data.credit
    return total_marks / total_credits if total_credits else 0


# Predictions
def predict_required_marks(marks: Dict[str, Subject], target_cgpa: float, IA_left: int, external_expected: float) -> List[Tuple[str, float]]:
    """Predict marks required for achieving the target CGPA."""
    predictions = []
    for subject, data in marks.items():
        total_weight = data.assignment[0] + data.lab[0] / 25 + data.IA[0] / 7.5
        current_cgpa = calculate_subject_cgpa(data) * 10
        current_weight = (current_cgpa / 10) * total_weight

        required_weight = target_cgpa * (total_weight + 50 / 7.5 * IA_left + 50) / 10 - current_weight
        required_IA = (required_weight - 50 * external_expected) / IA_left
        predictions.append((subject, round(required_IA * 7.5, 2)))
    return predictions


# Main Execution
def main():
    subjects = ['math', 'chemistry', 'plc', 'caed', 'civil', 'english', 'sfh', 'kannada']
    marks = get_subject_marks(subjects)
    save_marks_to_csv(marks, "marks.csv")
    loaded_marks = load_marks_from_csv("marks.csv")

    semester_cgpa = calculate_semester_cgpa(loaded_marks)
    print(f"Semester CGPA: {semester_cgpa:.2f}")

    target_cgpa = float(input("Enter the target CGPA: "))
    IA_left = get_int("Enter number of IAs left: ")
    external_expected = float(input("Enter expected external marks (0-50): "))

    predictions = predict_required_marks(loaded_marks, target_cgpa, IA_left, external_expected)
    print("\nMarks required per subject to achieve the target CGPA:")
    for subject, marks_needed in predictions:
        print(f"{subject}: {marks_needed:.2f}")


if __name__ == "__main__":
    main()
