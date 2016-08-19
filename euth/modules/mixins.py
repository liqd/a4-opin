class ItemMixin():
    def _feature_enabled(self, feature):
        active_phase = self.object.project.active_phase
        return (active_phase is not None
                and active_phase.has_feature(feature, self.model))

    @property
    def comment_enabled(self):
        return self._feature_enabled('comment')

    @property
    def crud_enabled(self):
        return self._feature_enabled('crud')

    @property
    def rate_enabled(self):
        return self._feature_enabled('rate')
