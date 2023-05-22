from gradio import Component
from gradio import JSONSerializable
import moleculelib


# Component defines change events so all components
# have change events
class MoleculeViewer(Component, JSONSerializable):

    # This automatically adds .edit and .scroll methods?
    EVENTS = ["edit", "scroll"]

    def preprocess(self, data: dict):
        return moleculelib.generate(**data)

    # This is the default impl in Component
    def postprocess(self, data: dict):
        return data
    
    # This
    def update(self, *args, **kwargs):
        pass
