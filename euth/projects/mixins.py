from django.views import generic


class PhaseDispatchMixin(generic.DetailView):
    def dispatch(self, request, *args, **kwargs):
        kwargs['project'] = self.get_object()
        return self._view_by_phase()(request, *args, **kwargs)

    def _view_by_phase(self):
        """
        Choose the appropriate view for the current active phase.
        """
        project = self.get_object()

        if project.active_phase:
            return project.active_phase.view.as_view()
        elif project.last_phase:
            return project.last_phase.view.as_view()
        else:
            return super().dispatch


class ProjectMixin(generic.base.ContextMixin):
    def dispatch(self, *args, **kwargs):
        self.project = kwargs['project']
        self.phase = self.project.active_phase or self.project.last_phase
        self.is_between_phases = not self.project.active_phase and self.\
            project.last_phase
        self.module = self.phase.module if self.phase else None
        return super(ProjectMixin, self).dispatch(*args, **kwargs)
