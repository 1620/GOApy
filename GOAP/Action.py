class Action:

    def __init__(self, name: str, pre_conditions: dict, effects: dict):
        self.name = name
        self.pre_conditions = pre_conditions
        self.effects = effects

    def __str__(self):
        return 'Action: {0}, Pre_Conditions: {1}, Effects: {2}'.format(self.name, self.pre_conditions, self.effects)

    def __repr__(self):
        return self.__str__()


class Actions:

    def __init__(self):
        self.actions = list()

    def add_action(self, name, pre_conditions, effects):
        # add action to self.actions
        self.actions.append(Action(name, pre_conditions, effects))

    def remove_action(self, name: str):
        # traverse self.actions and remove named action
        [self.actions.remove(action) for action in self.actions if action.name == name]

    def get(self, name):
        for action in self.actions:
            if action.name == name:
                return action

    def __str__(self):
        return '{}'.format(self.actions)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter(self.actions)

    def __len__(self):
        return len(self.actions)

if __name__ == '__main__':
    actions = Actions()
    actions.add_action(name='CreateVPC', pre_conditions={'vpc': False}, effects={'vpc': False})
    actions.add_action(name='CreateDB', pre_conditions={'db': False}, effects={'db': True})
    actions.add_action(name='CreateASG', pre_conditions={'asg': False}, effects={'asg': True})
    print('{0}\n{1}'.format(actions, actions.__len__()))
    actions.remove_action(name='CreateVPC')
    print('{0}\n{1}'.format(actions, actions.__len__()))
    print(actions.get(name='CreateDB'))
