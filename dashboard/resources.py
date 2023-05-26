
from import_export import resources
from dashboard.models import Data

class DataResource(data.ModelResource):

    class Meta:
        model = Data