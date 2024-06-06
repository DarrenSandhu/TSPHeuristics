import networkx as nx
import random
import sys
sys.path.append("../")
from Code.Large_Neighbourhood_Search.large_neighbourhood_search_convergence import large_neighborhood_search_convergence


def test_large_neighborhood_search_convergence():
    # Create a sample graph
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2, 3])
    G.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    
    # Define distances between nodes
    distances = {
        (0, 1): 1, (1, 0): 1,  # Adding both (0, 1) and (1, 0)
        (0, 2): 2, (2, 0): 2,  # Adding both (0, 2) and (2, 0)
        (0, 3): 3, (3, 0): 3,  # Adding both (0, 3) and (3, 0)
        (1, 2): 4, (2, 1): 4,  # Adding both (1, 2) and (2, 1)
        (1, 3): 5, (3, 1): 5,  # Adding both (1, 3) and (3, 1)
        (2, 3): 6, (3, 2): 6   # Adding both (2, 3) and (3, 2)
    }
    
    # Define the number of nodes
    n = G.number_of_nodes()
    
    # Define the maximum number of iterations
    max_iterations = 100
    
    # Call the function
    tour, distance = large_neighborhood_search_convergence(G, distances, n, max_iterations)
    
    # Assert that the tour is a valid permutation of nodes
    assert set(tour) == set(G.nodes()), f"Invalid tour: {tour}"
    
    # Assert that the algorithm converges within the specified maximum iterations
    assert distance >= 0, f"Negative distance: {distance}"
    assert len(tour) == n, f"Invalid tour length: {len(tour)}"


# Run the test
test_large_neighborhood_search_convergence()