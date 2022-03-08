from pymodm import MongoModel, fields


class Target(MongoModel):
    target_id = fields.CharField(primary_key=True)
    name = fields.CharField()
    town = fields.CharField()
    type = fields.CharField()
    x_coordinate = fields.FloatField()
    y_coordinate = fields.FloatField()
    location_method = fields.CharField(blank=True)
    location_accuracy = fields.CharField(blank=True)
    url = fields.URLField()
    created_at = fields.DateTimeField()
    is_ancient = fields.BooleanField(blank=True)
    source = fields.CharField()
    is_pending = fields.BooleanField(blank=True)

    class Meta:
        connection_alias = 'app'
        final = True

    @staticmethod
    def create(
        target_id,
        name,
        town,
        type,
        x_coordinate,
        y_coordinate,
        location_method,
        location_accuracy,
        url,
        created_at,
        is_ancient,
        source,
        is_pending
    ):
        target = Target(
            target_id=target_id,
            name=name,
            town=town,
            type=type,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            location_method=location_method,
            location_accuracy=location_accuracy,
            url=url,
            created_at=created_at,
            is_ancient=is_ancient,
            source=source,
            is_pending=is_pending
        )
        target.save()
        return target

    def to_json(self):
        return {
            'type': 'Feature',
            'properties': {
                'id': str(self.target_id),
                'name': self.name,
                'town': self.town,
                'type': self.type,
                'location_method': self.location_method,
                'location_accuracy': self.location_accuracy,
                'url': self.url,
                'created_at': str(self.created_at).split(' ')[0],
                'is_ancient': self.is_ancient,
                'source': self.source
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [self.x_coordinate, self.y_coordinate]
            }
        }
