from grit.common.model.version.item import Item


class LineageGraph(Item):

    def __init__(self, json_payload):
        super().__init__(json_payload)
        self._name = json_payload.get('name', '')
        self._source_key = json_payload.get('sourceKey', '')

    @classmethod
    def from_lineage_graph(cls, _id, other_lineage_graph):
        return cls({
            'id': _id,
            'tags': other_lineage_graph.get_tags(),
            'name': other_lineage_graph.get_name(),
            'sourceKey': other_lineage_graph.get_source_key(),
        })

    def get_name(self):
        return self._name

    def get_source_key(self):
        return self._source_key

    def __eq__(self, other):
        return (
            isinstance(other, LineageGraph)
            and self.get_name() == other.get_name()
            and self.get_id() == other.get_id()
            and self.get_source_key() == other.get_source_key()
            and self.get_tags() == other.get_tags()
        )
