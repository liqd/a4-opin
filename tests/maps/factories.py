import json

import factory

from adhocracy4.test.factories import ModuleFactory
from euth.maps import models as maps_models


class AreaSettingsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = maps_models.AreaSettings

    module = factory.SubFactory(ModuleFactory)
    polygon = json.dumps({
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                55.37109374999999,
                                61.438767493682825
                            ],
                            [
                                55.37109374999999,
                                66.08936427047088
                            ],
                            [
                                71.630859375,
                                66.08936427047088
                            ],
                            [
                                71.630859375,
                                61.438767493682825
                            ],
                            [
                                55.37109374999999,
                                61.438767493682825
                            ]
                        ]
                    ]
                },
                "properties":{}
            }
        ]
    })
