SCENARIO_DICTIONARY = {'1,1':  
                       'Captain $player_object.name uses extra fuel to '
                       'accelerate '
                       '$player_object.ship_name out of the way\nbefore the '
                       'asteroid storm hits.\nCaptain $player_object.name '
                       'makes the '
                       'hyperspace jump to Sector B.'}


def retrieve_scenario_text(player_object, scenario, conclusion_number):
    """Input text to be changed."""
    key = str(scenario) + ',' + str(conclusion_number)
    scenario_text = SCENARIO_DICTIONARY[key].replace('$player_object.name', 
                                                     player_object.name)
    scenario_text = scenario_text.replace('$player_object.ship_name', 
                                          player_object.ship_name)
    print(scenario_text)
    return
