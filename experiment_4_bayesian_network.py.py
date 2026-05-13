from pgmpy.models import DiscreteBayesianNetwork 
from pgmpy.factors.discrete import TabularCPD 
from pgmpy.inference import VariableElimination 
import networkx as nx
import matplotlib.pyplot as plt

def main(): 
    model = DiscreteBayesianNetwork([ 
        ('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), 
        ('Alarm', 'JohnCalls'), ('Alarm', 'MaryCalls') 
    ]) 

    cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]]) 
    cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]]) 
    cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, values=[[0.999, 0.71, 0.06, 0.05], [0.001, 0.29, 0.94, 0.95]], evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2]) 
    cpd_john = TabularCPD(variable='JohnCalls', variable_card=2, values=[[0.9, 0.05], [0.1, 0.95]], evidence=['Alarm'], evidence_card=[2]) 
    cpd_mary = TabularCPD(variable='MaryCalls', variable_card=2, values=[[0.7, 0.01], [0.3, 0.99]], evidence=['Alarm'], evidence_card=[2]) 

    model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary) 
    print("Model valid?", model.check_model()) 

    infer = VariableElimination(model) 
    result = infer.query(variables=['Burglary'], evidence={'JohnCalls': 1, 'MaryCalls': 1}) 
    print("\nProbability of Burglary given John and Mary called:\n", result)

    G = nx.DiGraph(model.edges())
    nx.draw(G, with_labels=True, node_size=3000, node_color='skyblue', arrows=True)
    plt.title("Bayesian Network Structure")
    plt.show()

if __name__ == "__main__": 
    main()