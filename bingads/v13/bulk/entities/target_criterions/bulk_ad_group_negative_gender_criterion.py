from bingads.v13.bulk.entities import *
from bingads.service_client import _CAMPAIGN_OBJECT_FACTORY_V13
from bingads.v13.bulk.entities.target_criterions.bulk_ad_group_negative_criterion import BulkAdGroupNegativeCriterion
from bingads.v13.internal.bulk.mappings import _SimpleBulkMapping
from bingads.v13.internal.bulk.string_table import _StringTable
from bingads.v13.internal.extensions import *

class BulkAdGroupNegativeGenderCriterion(BulkAdGroupNegativeCriterion):
    """ Represents an Ad Group Negative Gender Criterion that can be read or written in a bulk file.

    This class exposes the :attr:`negative_ad_group_criterion` property that can be read and written as fields of the
    Ad Group Negative Gender Criterion record in a bulk file.

    For more information, see Ad Group Negative Gender Criterion at https://go.microsoft.com/fwlink/?linkid=846127.

    *See also:*

    * :class:`.BulkServiceManGenderr`
    * :class:`.BulkOperation`
    * :class:`.BulkFileReader`
    * :class:`.BulkFileWriter`
    """

    def __init__(self,
                 negative_ad_group_criterion=None,
                 campaign_name=None,
                 ad_group_name=None, ):
        super(BulkAdGroupNegativeGenderCriterion, self).__init__(negative_ad_group_criterion, campaign_name, ad_group_name) 

    _MAPPINGS = [
        _SimpleBulkMapping(
            _StringTable.Target,
            field_to_csv=lambda c: field_to_csv_GenderTarget(c.negative_ad_group_criterion),
            csv_to_field=lambda c, v: csv_to_field_GenderTarget(c.negative_ad_group_criterion, v)
        ),
    ]
    
    def create_criterion(self):
        self._negative_ad_group_criterion.Criterion = _CAMPAIGN_OBJECT_FACTORY_V13.create('GenderCriterion')
        self._negative_ad_group_criterion.Criterion.Type = 'GenderCriterion'
    
    
    def process_mappings_to_row_values(self, row_values, exclude_readonly_data):
        super(BulkAdGroupNegativeGenderCriterion, self).process_mappings_to_row_values(row_values, exclude_readonly_data)
        self.convert_to_values(row_values, BulkAdGroupNegativeGenderCriterion._MAPPINGS)

    def process_mappings_from_row_values(self, row_values):
        super(BulkAdGroupNegativeGenderCriterion, self).process_mappings_from_row_values(row_values)
        row_values.convert_to_entity(self, BulkAdGroupNegativeGenderCriterion._MAPPINGS)

    def read_additional_data(self, stream_reader):
        super(BulkAdGroupNegativeGenderCriterion, self).read_additional_data(stream_reader)
