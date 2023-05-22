from gradio import Component
from gradio import JSONSerializable
import moleculelib
from pydantic import BaseModel


# The types accepted by our components are not 
# documented well.
# We should expose our existing datatypes better,
# e.g. ImageData, GalleryData, CodeData so that
# component authors can use them in their components.
# We should also let them define their own data models.
class MoleculeData(BaseModel):
    pass


# Component defines change events so all components
# have change events
class MoleculeViewer(Component, JSONSerializable):

    # This automatically adds .edit and .scroll methods?
    EVENTS = ["edit", "scroll"]

    # We should expose 
    def preprocess(self, data: MoleculeData):
        return moleculelib.generate(**data)

    # This is the default impl in Component
    def postprocess(self, data: dict):
        return data
    
    def update(self, *args, **kwargs):
        pass
