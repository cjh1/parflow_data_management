from django.contrib import admin
from .models import project, simulation, mesh, conceptual_model, metadata

admin.site.register(project.Project)
admin.site.register(simulation.Simulation)
admin.site.register(mesh.Mesh)
admin.site.register(conceptual_model.ConceptualModel)
admin.site.register(metadata.Metadata)
