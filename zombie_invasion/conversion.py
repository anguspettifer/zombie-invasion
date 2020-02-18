class Conversion:
    """ Knows how to convert source object to destination based on matching criteria """
    def __init__(self, source_items, destination_items, destination_object):
        self.source_items = source_items
        self.destination_items = destination_items
        self.destination_object = destination_object
        self.source_items_and_counters = {}
        self._matching_criteria_count()

    def _matching_criteria_count(self):
        """Given a source item, returns the number of destination items and other source items with the same criteria"""

        for source, criteria in self.source_items.items():
            number_source_objects = len([k for k in self.source_items if self.source_items[k] == criteria])
            number_destination_object = len([k for k in self.destination_items if self.destination_items[k] == criteria])
            self.source_items_and_counters[source] = (criteria, [number_source_objects, number_destination_object])

    def convert(self):
        # Create new zombies
        criteria_and_sources_to_delete = dict()
        for source_instance, value in self.source_items_and_counters.items():
            if tuple(value[0]) in criteria_and_sources_to_delete:
                continue
            number_of_sources_to_convert = min([value[1][0], value[1][1]])
            for i in range(number_of_sources_to_convert):
                self.destination_items[self.destination_object()] = value[0]
                # Convert dict key into a tuple. Lists are not hashable.
                criteria_and_sources_to_delete[tuple(value[0])] = number_of_sources_to_convert

        # Delete old humans
        sources_to_delete = []
        for criteria, number in criteria_and_sources_to_delete.items():
            for key, value in self.source_items.items():
                if criteria == tuple(value):
                    sources_to_delete.append(key)
                    number -= 1
                    if number == 0: break

        for source in sources_to_delete: del self.source_items[source]
