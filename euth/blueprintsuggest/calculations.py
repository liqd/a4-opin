from euth.dashboard.blueprints import blueprints as blueprints_tuple

blueprints_dict = dict(blueprints_tuple)

# the order maps to the values in the form
aim_to_blueprints_mapping = {
    'collect_ideas': [
        blueprints_dict['ideas-collection-1'],
        blueprints_dict['ideas-collection-2'],
        blueprints_dict['agenda-setting']
    ],
    'discuss_topic': [
        blueprints_dict['ideas-collection-1'],
        blueprints_dict['ideas-collection-2'],
        blueprints_dict['agenda-setting']
    ],
    'design_place': [
        blueprints_dict['MapIdeas'],
        blueprints_dict['map-ideas-challenge']
    ],
    'run_survey': [
        blueprints_dict['flashpoll'],
        blueprints_dict['ideas-collection-2'],
        blueprints_dict['agenda-setting']
    ],
    'run_competition': [
        blueprints_dict['ideas-collection-2'],
        blueprints_dict['agenda-setting']
    ],
    'work_document': [
        blueprints_dict['commenting-text']
    ]
}


class BlueprintSuggester:
    def __init__(self, values):
        self.aim = values['aim']
        self.result = values['result']
        self.experience = values['experience']
        self.dedication = values['dedication']

    def get_blueprints(self):
        blueprints = self.blueprints_from_aim()
        return blueprints

    def blueprints_from_aim(self):
        return aim_to_blueprints_mapping[self.aim]
