import os
import json

def run_os_route():
    
    routes = []
    command = os.popen("ip -json route show")
    output = command.read()

    data = json.loads(output)
    #print(json.dumps(data, indent=4))

    # each route in the list
    for route_info in data:
        route = {}
        # each key, val in the route
        for key, value in route_info.items():
            if key == "dst":
                route[key]=value
            if key == "gateway":
                route[key]=value
            if key == "dev":
                route[key]=value
        routes.append(route)

    #print(json.dumps(routes,indent=4))
    return routes 

run_os_route()
