class ItemMixin():
    def _feature_enabled(self, feature):
        active_phase = self.object.project.active_phase
        return (active_phase is not None
                and active_phase.has_feature(feature, self.model))

    def __getattr__(self, name):
        if name.endswith('_enabled'):
            feature = name[:-8]
            return self._feature_enabled(feature)
        else:
            super().__getattr__(name)
