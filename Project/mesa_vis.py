## Finished Visuals

import mesa

from main import MazeModel

width = 10
height = 10


def agent_portrayal(agent):
    # visualisation for nodes
    if agent.type == 0:
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "black",
            "w": 1,
            "h": 1,
        }
        if agent.is_goal:
            portrayal["Color"] = "Green"
        if agent.pos == (0,0):
            portrayal["Color"] = "Blue"

    # visualisation for agents
    elif agent.type == 1:
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "Layer": 2,
            "Color": "red",
            "r": 0.5
        }

    # visualisation for walls
    elif agent.type == 2:
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 1,
            "Color": "white",
        }
        # calculates width, height and alignment depending on direction of the wall
        if agent.direction == "E":
            portrayal["w"] = 0.1
            portrayal["h"] = 1
            portrayal["xAlign"] = 1
        elif agent.direction == "W":
            portrayal["w"] = 0.1
            portrayal["h"] = 1
            portrayal["xAlign"] = 0
        elif agent.direction == "N":
            portrayal["w"] = 1
            portrayal["h"] = 0.1
            portrayal["yAlign"] = 0
        elif agent.direction == "S":
            portrayal["w"] = 1
            portrayal["h"] = 0.1
            portrayal["yAlign"] = 1

    return portrayal



model_params = {
    "agent_number": mesa.visualization.Slider("agent_number", value = 100, step = 10, max_value = 500 , min_value = 10),
    "fitness_quotient": mesa.visualization.Slider("fitness_quotient", min_value = 1.0, value = 1.0,  step = 10.0, max_value = 1000.0),
    "length_dividend": mesa.visualization.Slider("length_dividend", value = 2, step = 0.25, max_value = 5, min_value = 0.25),
    "mutate_min": mesa.visualization.Slider("mutate_min", value = 2, step = 1, min_value = 0, max_value = 5),
    "mutate_max": mesa.visualization.Slider("mutate_max", value = 10, step = 1, min_value = 2, max_value = 20)

}

grid = mesa.visualization.CanvasGrid(agent_portrayal, width, height, 500, 500)

chart1 = mesa.visualization.ChartModule([{"Label": "Average fitness", "Color" : "Black"}])
chart2 = mesa.visualization.ChartModule([{"Label": "Max fitness", "Color" : "Black"}])

server = mesa.visualization.ModularServer(
    MazeModel, [grid, chart1 ,chart2], "MazeModel", model_params
)

server.port = 8521
server.launch()