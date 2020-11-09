from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CharField
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from guardian.shortcuts import assign_perm


class Project(TimeStampedModel, models.Model):
    name = CharField(_("Name of Project"), blank=True, max_length=255)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="projects"
    )
    # TODO: more fields

    class Meta:
        permissions = [
            ("can_give_admin", "Can give others full access"),
            ("can_remove_admin", "Can revoke full access"),
            ("can_give_transferable_admin", "Can give others transferable full access"),
            ("can_remove_transferable_admin", "Can revoke transferable full access"),
        ]


@receiver(models.signals.post_save, sender=Project)
def _project_post_save(sender, instance, created, *args, **kwargs):
    if created:
        # Modifying a project
        assign_perm("scheduler.change_project", instance.owner, instance)
        assign_perm("scheduler.delete_project", instance.owner, instance)
        assign_perm("scheduler.view_project", instance.owner, instance)

        # Giving / revoking admin
        assign_perm("project.can_give_admin", instance.owner, instance)
        assign_perm("project.can_remove_admin", instance.owner, instance)
        assign_perm("project.can_give_transferable_admin", instance.owner, instance)
        assign_perm("project.can_remove_transferable_admin", instance.owner, instance)