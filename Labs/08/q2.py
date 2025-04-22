from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = BayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# Define the CPDs (Conditional Probability Distributions)

cpd_intelligence = TabularCPD(
    variable='Intelligence',
    variable_card=2,
    values=[[0.7], [0.3]],
    state_names={'Intelligence': ['High', 'Low']}
)

cpd_study = TabularCPD(
    variable='StudyHours',
    variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'StudyHours': ['Sufficient', 'Insufficient']}
)

cpd_difficulty = TabularCPD(
    variable='Difficulty',
    variable_card=2,
    values=[[0.4], [0.6]],
    state_names={'Difficulty': ['Hard', 'Easy']}
)

cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.8, 0.7, 0.6, 0.7, 0.5, 0.4, 0.6, 0.4],  # A
        [0.15, 0.2, 0.3, 0.2, 0.3, 0.3, 0.3, 0.4],  # B
        [0.05, 0.1, 0.1, 0.1, 0.2, 0.3, 0.1, 0.2]   # C
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    state_names={
        'Grade': ['A', 'B', 'C'],
        'Intelligence': ['High', 'Low'],
        'StudyHours': ['Sufficient', 'Insufficient'],
        'Difficulty': ['Hard', 'Easy']
    }
)

cpd_pass = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.50],  # Yes
        [0.05, 0.20, 0.50]   # No
    ],
    evidence=['Grade'],
    evidence_card=[3],
    state_names={
        'Pass': ['Yes', 'No'],
        'Grade': ['A', 'B', 'C']
    }
)

# Add CPDs to the model
model.add_cpds(cpd_intelligence, cpd_study, cpd_difficulty, cpd_grade, cpd_pass)

# Check if the model is valid
assert model.check_model()

# Perform inference
infer = VariableElimination(model)

# Query 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)
result_1 = infer.query(
    variables=['Pass'],
    evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'}
)
print("P(Pass | StudyHours=Sufficient, Difficulty=Hard):")
print(result_1)

# Query 2: P(Intelligence=High | Pass=Yes)
result_2 = infer.query(
    variables=['Intelligence'],
    evidence={'Pass': 'Yes'}
)
print("\nP(Intelligence=High | Pass=Yes):")
print(result_2)
