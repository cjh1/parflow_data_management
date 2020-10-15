from django.contrib import admin
from .models import project, simulation

admin.site.register(project.Project)
admin.site.register(simulation.Simulation)