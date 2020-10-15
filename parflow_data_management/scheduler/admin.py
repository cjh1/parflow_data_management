from django.contrib import admin
from .models import project, simulation, mesh

admin.site.register(project.Project)
admin.site.register(simulation.Simulation)
admin.site.register(mesh.Mesh)