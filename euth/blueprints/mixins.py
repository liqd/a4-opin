from .blueprints import blueprints


class BlueprintMixin():
    @property
    def blueprint(self):
        return dict(blueprints)[self.kwargs['blueprint_slug']]
